import sys
from pathlib import Path
import json

from langchain_google_genai import ChatGoogleGenerativeAI
from agents.state import AgentState

# --- Ensure project root is on PYTHONPATH (Windows-safe) ---
ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from schemas.product_schema import ProductPage


def product_agent(state: AgentState) -> AgentState:
    """
    Generates a structured product page.
    Uses LLM if available, otherwise deterministic fallback.
    Enforces schema via Pydantic.
    """

    product = state["product"]

    # --- Input validation (IMPORTANT) ---
    if "product_name" not in product or not product["product_name"]:
        raise ValueError("product_name is required in product input")

    prompt = f"""
    Create a structured PRODUCT PAGE in JSON format using ONLY the data below.
    Do NOT add external information.

    Required JSON fields:
    - product_name
    - description
    - benefits
    - usage
    - safety

    Product data:
    {product}
    """

    try:
        llm = ChatGoogleGenerativeAI(
            model="gemini-pro",
            temperature=state.get("config", {}).get("temperature", 0.3)
        )
        response = llm.invoke(prompt)
        product_page = json.loads(response.content)

    except Exception as e:
        print(f"⚠️ LLM failed, using deterministic fallback: {e}")

        product_page = {
            "product_name": product["product_name"],  # NEVER unknown
            "description": "This product page was generated using fallback logic due to LLM unavailability.",
            "benefits": product.get("benefits", []),
            "usage": product.get("how_to_use", ""),
            "safety": product.get("side_effects", "")
        }

    # --- Schema validation (MANDATORY) ---
    validated = ProductPage(**product_page)

    return {
        **state,
        "product_page": validated.model_dump()
    }
