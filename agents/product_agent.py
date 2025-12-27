from agents.state import AgentState
from langchain_google_genai import ChatGoogleGenerativeAI
import json

def product_agent(state: AgentState) -> AgentState:
    prompt = f"""
    Create a structured PRODUCT PAGE in JSON format using only the data below.
    Do not add external information.

    Product data:
    {state['product']}
    """

    try:
        llm = ChatGoogleGenerativeAI(
            model="gemini-pro",
            temperature=0.3
        )
        response = llm.invoke(prompt)
        product_page = json.loads(response.content)

    except Exception:
        # Graceful fallback
        product_name = (
            state["product"].get("product_name")
            or "the product"
        )

        product_page = {
            "product_name": product_name,
            "description": "This product page was generated using fallback logic due to LLM unavailability.",
            "concentration": state["product"].get("concentration"),
            "skin_type": state["product"].get("skin_type"),
            "key_ingredients": state["product"].get("key_ingredients"),
            "benefits": state["product"].get("benefits"),
            "how_to_use": state["product"].get("how_to_use"),
            "side_effects": state["product"].get("side_effects"),
            "price": state["product"].get("price")
        }

    return {
        **state,
        "product_page": product_page
    }
