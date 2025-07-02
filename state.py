import operator
from typing import Annotated, TypedDict, Union
from langchain_core.agents import AgentAction, AgentFinish

# from langgraph.graph import StateGraph
# from langgraph.graph.message import add_messages

class AgentState(TypedDict):
    input: str
    agent_outcome: Union[AgentAction, AgentFinish, None]
    intermediate_steps: Annotated[list[tuple[AgentAction, str]], operator.add]


