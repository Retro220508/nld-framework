from nld.api import solve

def mock_llm(prompt):
    return "The total cost is $1782"

problem = """
A company sells products in bundles...
What is the total cost?
"""

result = solve(problem, mock_llm)
print(result)
