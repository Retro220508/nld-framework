from nld.api import solve

def mock_llm(prompt):
    return """
    w1_new = -15.1
    w2_new = -0.4
    """

problem = """
Neural network with 2 layers:
x = 4
w1 = 0.5, w2 = -3
Compute updated weights.
"""

result = solve(problem, mock_llm)
print(result)
