import re

def simple_verify(problem, response):
    """
    Basic verification:
    Extract numbers and check if they are reasonable.
    (Simple placeholder — real logic is private)
    """

    numbers = re.findall(r"[-+]?\d*\.\d+|\d+", response)

    if not numbers:
        return False

    # Simple sanity check: number exists
    return True
