from pydantic import BaseModel
from typing import List


class ProductPage(BaseModel):
    product_name: str
    description: str
    benefits: List[str]
    usage: str
    safety: str
