from dotenv import load_dotenv
load_dotenv()

from agents.graph import app
from data.product_input import PRODUCT_DATA
import json
import os

initial_state = {
    "product": PRODUCT_DATA,
    "faqs": [],
    "product_page": {},
    "comparison_page": {}
}

final_state = app.invoke(initial_state)

os.makedirs("output", exist_ok=True)

with open("output/faq.json", "w") as f:
    json.dump(final_state["faqs"], f, indent=2)

with open("output/product_page.json", "w") as f:
    json.dump(final_state["product_page"], f, indent=2)

with open("output/comparison_page.json", "w") as f:
    json.dump(final_state["comparison_page"], f, indent=2)
