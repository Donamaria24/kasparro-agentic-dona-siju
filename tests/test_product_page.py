import json
from pathlib import Path

OUTPUT_FILE = Path("output/product_page.json")

def test_product_page_exists():
    assert OUTPUT_FILE.exists(), "product_page.json was not generated"

def test_product_page_schema():
    data = json.loads(OUTPUT_FILE.read_text())

    required_fields = [
        "product_name",
        "description",
        "benefits",
        "usage",
        "safety"
    ]

    for field in required_fields:
        assert field in data, f"Missing field: {field}"

def test_product_name_not_unknown():
    data = json.loads(OUTPUT_FILE.read_text())
    assert data["product_name"] != "Unknown Product"
