from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langgraph.graph import END, MessagesState, StateGraph
from nodes import tool_node, run_agent_reasoning
from rich.console import Console
from rich.markdown import Markdown

load_dotenv()

AGENT_REASON = "agent_reason"
ACT = "act"
LAST = -1

def should_continue(state: dict) -> str:
    latestMessage = state["messages"][LAST]
    if latestMessage.tool_calls:
        print("LLM called tool",
              latestMessage.tool_calls[0]['name'],
              "with arguments ",
              latestMessage.tool_calls[0]['args'])
        return ACT
    return END

flow = StateGraph(MessagesState)

flow.add_node(AGENT_REASON, run_agent_reasoning)
flow.set_entry_point(AGENT_REASON)
flow.add_node(ACT, tool_node)

flow.add_conditional_edges(AGENT_REASON, should_continue, {
    END:END,
    ACT:ACT})

flow.add_edge(ACT, AGENT_REASON)

app = flow.compile()

if __name__ == "__main__":
    console = Console()
    console.print(Markdown("# Hello ReAct with LangGraph"))
    console.print(app.get_graph().draw_ascii())
    #print(app.get_graph().draw_mermaid())
    result = app.invoke(
        input = {
            "messages": [
                HumanMessage(
                    content="What is the weather in Tokyo? List it, including the name of source of information, and then triple the windspeed."
                )
            ]
        }
    )
    console.print(Markdown(result["messages"][LAST].content))
