from tenacity import retry, stop_after_attempt, wait_exponential

@retry(stop=stop_after_attempt(3), wait=wait_exponential(min=1, max=4))
def safe_llm_call(llm, prompt):
    return llm.invoke(prompt)
