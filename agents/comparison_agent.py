from agents.state import AgentState
from langchain_google_genai import ChatGoogleGenerativeAI
import json

def comparison_agent(state: AgentState) -> AgentState:
    prompt = f"""
    Compare the following product with a fictional competitor (Product B).
    Output a structured JSON comparison.

    Product A:
    {state['product']}

    Output ONLY valid JSON.
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
        comparison_page = {
            "product_a": state["product"].get("name", "Product A"),
            "product_b": "Fictional Product B",
            "comparison": {
                "ingredients": "Product A uses cleaner ingredients",
                "effectiveness": "Product A shows faster visible results",
                "price": "Product A offers better value for money",
                "suitability": "Product A is suitable for sensitive skin"
            }
        }

    return {
        **state,
        "comparison_page": comparison_page
    }
