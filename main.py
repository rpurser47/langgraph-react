from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langgraph.graph import END, MessagesState, StateGraph
from nodes import tool_node, run_agent_reasoning

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
    print("Hello ReAct with LangGraph")
    #print(app.get_graph().draw_mermaid())
    print(app.get_graph().draw_ascii())
    result = app.invoke(
        input = {
            "messages": [
                HumanMessage(
                    content="What is the weather in Tokyo? List it, including the name of source of information, and then triple the windspeed."
                )
            ]
        }
    )
    print(result["messages"][LAST].content)
