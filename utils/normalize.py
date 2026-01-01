def normalize_product(product: dict) -> dict:
    return {
        "name": product.get("product_name"),
        **product
    }
