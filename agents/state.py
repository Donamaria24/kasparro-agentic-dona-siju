from typing import TypedDict, List, Dict, Any


class AgentState(TypedDict):
    product: Dict[str, Any]
    faqs: List[Dict[str, Any]]
    product_page: Dict[str, Any]
    comparison_page: Dict[str, Any]
    config: Dict[str, Any]   # ✅ REQUIRED
