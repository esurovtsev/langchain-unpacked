from langchain.agents.middleware import HumanInTheLoopMiddleware
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from tools import lookup_stock_symbol, fetch_stock_data_raw, place_order

system_prompt = """
You are a financial advisor assistant. Use the provided tools to ground your answers
in up-to-date market data. Be concise, factual, and risk-aware.

Be decisive: when you have sufficient information to act, proceed with tool calls without
asking for confirmation. Only if information is missing or uncertain, ask a concise 
clarifying question.

When preparing or describing actions, include appropriate parameters (e.g., symbol, shares,
limit price, budgets) based on available data. Do not fabricate numbers or facts.
"""

graph = create_agent(
    model="gpt-4o-mini",
    tools=[lookup_stock_symbol, fetch_stock_data_raw, place_order],
    system_prompt=system_prompt,

    middleware=[
        HumanInTheLoopMiddleware(
            interrupt_on={
                "place_order": { "allowed_decisions": ["approve", "edit", "reject"]}
            }
        ),
    ],
)