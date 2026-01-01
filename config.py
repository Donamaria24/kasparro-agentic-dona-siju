import os

CONFIG = {
    "temperature": float(os.getenv("LLM_TEMPERATURE", 0.3)),
    "max_retries": int(os.getenv("LLM_MAX_RETRIES", 2)),
}
