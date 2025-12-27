from agents.state import AgentState
from langchain_google_genai import ChatGoogleGenerativeAI
import json

def product_agent(state: AgentState) -> AgentState:
    prompt = f"""
    Create a structured PRODUCT PAGE in JSON format using ONLY the data below.
    Do not add external information.

    Product data:
    {state['product']}

    Output ONLY valid JSON.
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
        product_page = {
            "product_name": state["product"].get("name", "Unknown Product"),
            "description": "This product page was generated using fallback logic due to LLM unavailability.",
            "benefits": [
                "Improves skin appearance",
                "Easy to use",
                "Suitable for daily use"
            ],
            "usage": "Apply as directed on the product label.",
            "safety": "For external use only."
        }

    return {
        **state,
        "product_page": product_page
    }
