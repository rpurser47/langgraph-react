from dotenv import load_dotenv
load_dotenv()

from langchain_core.agents import AgentFinish
from langgraph.graph import END, StateGraph

from nodes import execute_tools, run_agent_reasoning_engine
from state import AgentState

AGENT_REASON = "agent_reason"
ACT = "act"

def should_continue(state: AgentState) -> str:
    if isinstance(state["agent_outcome"], AgentFinish):
        return END
    else:
        return ACT
    
flow = StateGraph(AgentState)

flow.add_node(AGENT_REASON, run_agent_reasoning_engine)
flow.set_entry_point(AGENT_REASON)
flow.add_node(ACT, execute_tools)

flow.add_conditional_edges(
    AGENT_REASON,
    should_continue
)

flow.add_edge(ACT, AGENT_REASON)

app = flow.compile()
print(app.get_graph().draw_mermaid())

if __name__ == "__main__":
    print("Hello ReAct with LangGraph")
    app.invoke(
        input = {
            "input": "What is the weather in San Francisco? Write it, and then triple it.",
        }
    )

