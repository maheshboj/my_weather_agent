# test_local.py
from agent import graph

# Test the agent
result = graph.invoke({
    "messages": [
        {"role": "user", "content": "What's the weather in New York?"}
    ]
})

print(result)