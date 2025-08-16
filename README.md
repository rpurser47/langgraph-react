# Reason-Act (ReAct) Agent exercise

I'm learning to use [LangGraph](https://www.langchain.com/langgraph) by taking a [Udemy class](https://www.udemy.com/course/langgraph)

# Using the Reason-Act pattern
The [ReAct pattern](https://en.wikipedia.org/wiki/Large_language_model#Agency), which stands for Reason + Act, is a framework that enhances AI agents' ability to solve complex problems by combining reasoning and action-taking. It involves an iterative cycle where an agent reasons about the situation, takes an action, observes the result, and then uses that observation to refine its reasoning for the next step. This approach allows agents to adapt to new information, handle ambiguity, and solve problems that require dynamic decision-making. 

This is a simple example where the agent has access to two tools:  A search engine, Tavily, and a custom calculator that triples / multiplies numbers by 3

## Example
``` text
"What is the weather in Tokyo? List it, and then triple the windspeed."
```
**Thinking**
``` text
LLM called tool tavily_search with arguments  {'query': 'Tokyo weather', 'search_depth': 'basic'}
LLM called tool triple with arguments  {'num': 16.1}
``` 
**Response**
``` text
The current weather in Tokyo is as follows:

- **Temperature**: 28.3°C (82.9°F)
- **Condition**: Partly cloudy
- **Wind Speed**: 16.1 mph (25.9 kph)
- **Wind Direction**: South
- **Humidity**: 84%
- **Pressure**: 1013.0 mb
- **Visibility**: 10 km

The tripled wind speed is approximately **48.3 mph**.
```

## LangGraph Graph

``` mermaid
---
config:
  flowchart:
    curve: linear
---
graph TD;
        __start__([<p>__start__</p>]):::first
        agent_reason(agent_reason)
        act(act)
        __end__([<p>__end__</p>]):::last
        __start__ --> agent_reason;
        act --> agent_reason;
        agent_reason -.-> __end__;
        agent_reason -.-> act;
        classDef default fill:#f2f0ff,line-height:1.2
        classDef first fill-opacity:0
        classDef last fill:#bfb6fc
```

## Notes
Note that you'll need an `.env` file like this:

``` text
OPENAI_API_KEY=<MY_OPENAI_API_KEY>
TAVILY_API_KEY=<MY_TAVILY_API_KEY>
LANGCHAIN_API_KEY=<MY_LANGSMITH_API_KEY>
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=ReAct LangGraph
PYTHONPATH=C:\localprojects\langgraph-react
```
