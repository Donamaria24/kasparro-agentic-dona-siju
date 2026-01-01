import json
from pathlib import Path

from agents.graph import app
from data.product_input import PRODUCT_DATA


def main():
    # --- Initial LangGraph state ---
    initial_state = {
        "product": PRODUCT_DATA,
        "config": {
            "temperature": 0.3
        }
    }

    final_state = app.invoke(initial_state)

    # --- Ensure output directory exists ---
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    # --- Write outputs explicitly ---
    if "product_page" in final_state:
        (output_dir / "product_page.json").write_text(
            json.dumps(final_state["product_page"], indent=2)
        )

    if "faqs" in final_state:
        (output_dir / "faq.json").write_text(
            json.dumps(final_state["faqs"], indent=2)
        )

    if "comparison_page" in final_state:
        (output_dir / "comparison_page.json").write_text(
            json.dumps(final_state["comparison_page"], indent=2)
        )

    print("📁 Output written to /output")
    print("✅ Content generation completed successfully")


if __name__ == "__main__":
    main()
