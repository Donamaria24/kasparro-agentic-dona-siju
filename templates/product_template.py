def product_template(product: dict) -> dict:
    return {
        "page_type": "Product Page",
        "name": product["name"],
        "concentration": product["concentration"],
        "skin_type": product["skin_type"],
        "ingredients": product["ingredients"],
        "benefits": product["benefits"],
        "usage": product["usage"],
        "price": product["price"]
    }
