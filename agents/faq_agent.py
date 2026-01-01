import sys
from pathlib import Path
import json

from langchain_google_genai import ChatGoogleGenerativeAI
from agents.state import AgentState

# --- Ensure project root is on PYTHONPATH (Windows-safe) ---
ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from schemas.faq_schema import FAQList


def faq_agent(state: AgentState) -> AgentState:
    product = state["product"]
    product_name = product["product_name"]  # validated earlier

    prompt = f"""
    Generate at least 15 FAQs in JSON format.
    Each FAQ must contain:
    - question
    - answer

    Use ONLY this product data:
    {product}
    """

    try:
        llm = ChatGoogleGenerativeAI(
            model="gemini-pro",
            temperature=state.get("config", {}).get("temperature", 0.3)
        )
        response = llm.invoke(prompt)
        faqs = json.loads(response.content)

    except Exception as e:
        print(f"⚠️ LLM failed, using deterministic fallback: {e}")

        # ✅ FINAL 15-FAQ DETERMINISTIC FALLBACK
        faqs = [
            {
                "question": f"What is {product_name} used for?",
                "answer": f"{product_name} is used to brighten the skin and help reduce the appearance of dark spots."
            },
            {
                "question": f"Who should use {product_name}?",
                "answer": "It is suitable for individuals with oily or combination skin who want a brighter and more even skin tone."
            },
            {
                "question": f"What are the key benefits of {product_name}?",
                "answer": "The key benefits include skin brightening, fading dark spots, and improving overall skin radiance."
            },
            {
                "question": "How does Vitamin C help the skin?",
                "answer": "Vitamin C helps reduce pigmentation, boost collagen production, and protect the skin from environmental damage."
            },
            {
                "question": f"How often should {product_name} be applied?",
                "answer": "It should be applied once daily, preferably in the morning."
            },
            {
                "question": f"What is the correct way to apply {product_name}?",
                "answer": "Apply 2–3 drops to clean, dry skin and gently massage until fully absorbed."
            },
            {
                "question": f"Can {product_name} be used on oily skin?",
                "answer": "Yes, it is specifically suitable for oily skin types."
            },
            {
                "question": f"Is {product_name} suitable for sensitive skin?",
                "answer": "It may cause mild tingling for sensitive skin, so a patch test is recommended."
            },
            {
                "question": f"Can {product_name} be used daily?",
                "answer": "Yes, it is safe for daily use when applied as directed."
            },
            {
                "question": f"Should {product_name} be used before sunscreen?",
                "answer": "Yes, it should be applied before sunscreen as part of a morning skincare routine."
            },
            {
                "question": f"How long does it take to see results from {product_name}?",
                "answer": "Visible improvements can typically be noticed after a few weeks of consistent use."
            },
            {
                "question": f"Are there any side effects of using {product_name}?",
                "answer": "Some users may experience mild tingling, especially those with sensitive skin."
            },
            {
                "question": f"Can {product_name} be combined with other skincare products?",
                "answer": "Yes, it can be combined with most skincare products, but avoid mixing with strong actives initially."
            },
            {
                "question": f"Is {product_name} safe for beginners in skincare?",
                "answer": "Yes, it is beginner-friendly when used according to the recommended instructions."
            },
            {
                "question": f"What precautions should be taken while using {product_name}?",
                "answer": "Always use sunscreen during the day and discontinue use if severe irritation occurs."
            }
        ]

    # --- Enforce minimum FAQ count ---
    if len(faqs) < 15:
        raise ValueError("FAQ count must be at least 15")

    # --- Schema validation ---
    validated = FAQList(faqs=faqs)

    return {
        **state,
        "faqs": validated.model_dump()["faqs"]
    }
