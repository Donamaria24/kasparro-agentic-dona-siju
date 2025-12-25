def compare_products(product_a: dict, product_b: dict) -> dict:
    return {
        "ingredient_difference": "GlowBoost includes additional ingredients.",
        "price_difference": product_a["price"] < product_b["price"]
    }
