from .verifier import simple_verify

def solve(problem, llm_call):
    """
    Main entry point for NLD framework

    Parameters:
    - problem: str
    - llm_call: function that takes prompt and returns response
    """

    response = llm_call(problem)

    if simple_verify(problem, response):
        return f"✅ Verified Answer: {response}"
    else:
        return f"❌ Verification Failed: {response}"
