from agents.state import AgentState
from langchain_google_genai import ChatGoogleGenerativeAI
import json

def comparison_agent(state: AgentState) -> AgentState:
    prompt = f"""
    Compare the following product with a fictional competitor (Product B).
    Output structured JSON only.

    Product A:
    {state['product']}
    """

    try:
        llm = ChatGoogleGenerativeAI(
            model="gemini-pro",
            temperature=0.3
        )
        response = llm.invoke(prompt)
        comparison_page = json.loads(response.content)

    except Exception:
        # Graceful fallback
        product_a = (
            state["product"].get("product_name")
            or "Product A"
        )

        comparison_page = {
            "product_a": product_a,
            "product_b": "Fictional Vitamin C Serum",
            "comparison": {
                "ingredients": "Product A uses cleaner and more effective ingredients.",
                "effectiveness": "Product A shows faster visible results.",
                "skin_suitability": "Product A is suitable for oily and combination skin.",
                "price": "Product A offers better value for money."
            }
        }

    return {
        **state,
        "comparison_page": comparison_page
    }
