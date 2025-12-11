# agent.py
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.tools import tool
from langgraph.graph.state import CompiledStateGraph

# Define a simple tool the agent can use
@tool
def get_weather(city: str) -> str:
    """Get weather information for a city.
    
    Args:
        city: The name of the city (e.g., 'New York', 'London')
    """
    # In production, call a real weather API
    # For now, return mock data
    return f"Weather in {city}: Sunny, 72°F (22°C), light winds"

@tool
def get_time(timezone: str) -> str:
    """Get current time for a timezone.
    
    Args:
        timezone: Timezone name (e.g., 'EST', 'PST', 'UTC')
    """
    return f"Current time in {timezone}: 2:30 PM"

# Create the agent
model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

graph: CompiledStateGraph = create_agent(
    model,
    tools=[get_weather, get_time],
    system_prompt="You are a helpful weather assistant. Answer questions about weather and time in different cities."
)