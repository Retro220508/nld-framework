# NLD (No Look Down)

> A lightweight verification framework for LLM reasoning

LLMs are powerful — but they can be confidently wrong.

NLD adds a verification layer that checks outputs before accepting them.

---

## How it works

LLM → Answer  
        ↓  
     NLD verifies  
        ↓  
 Accept / Reject  

---

## Features

- Plug-and-play verification layer  
- Works with math, ML, and reasoning tasks  
- Helps detect incorrect outputs  
- Lightweight and simple  

---

## Example

```python
from nld.api import solve

def dummy_llm(prompt):
    return "The answer is 42"

problem = "What is 6 * 7?"

print(solve(problem, dummy_llm))
