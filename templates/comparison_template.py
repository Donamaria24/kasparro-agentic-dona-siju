def comparison_template(product: dict) -> dict:
    product_b = {
        "name": "RadiantDrop Serum",
        "ingredients": ["Vitamin C"],
        "benefits": ["Basic brightening"],
        "price": 849
    }

    return {
        "page_type": "Comparison",
        "products": [
            {
                "name": product["name"],
                "ingredients": product["ingredients"],
                "benefits": product["benefits"],
                "price": product["price"]
            },
            product_b
        ]
    }
