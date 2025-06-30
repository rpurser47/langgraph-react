# ReAct Agent exercise

I'm learning to use [LangGraph](https://www.langchain.com/langgraph) by taking a [Udemy class](https://www.udemy.com/course/langgraph)

<!-- Agent architecture using CRAG built with LangGraph that does [Corrective Retrieval-Augmented Generation (RAG)](https://medium.com/@sahin.samia/crag-corrective-retrieval-augmented-generation-in-llm-what-it-is-and-how-it-works-ce24db3343a7) with RAG from blog posts from [https://lilianweng.github.io/posts](https://lilianweng.github.io/posts). The results are scored for relevance to the question, and then augmented with a web search, if not enough information is found.  Then, these results are used to generate a response. -->


### Example 1 -- RAG is relevant
<!-- ``` text
"what is agent memory?"
```

**Thinking**
``` text
---CHECK DOCUMENT RELEVANCE TO QUESTION---
---GRADE: DOCUMENT RELEVANT---
---GRADE: DOCUMENT RELEVANT---
---GRADE: DOCUMENT RELEVANT---
---GRADE: DOCUMENT RELEVANT---
---ASSESS GRADED DOCUMENTS---
---DECISION: GENERATE---
```
**Answer**

Agent memory is the component in an LLM-powered agent that stores and retrieves information across interactions. Short-term memory is handled via in-context inputs and prompt history, while long-term memory uses an external vector store for persistent storage and fast retrieval. Together they let the agent recall past experiences, plan future steps, and refine its behavior.

-->
### Example 2 -- RAG not relevant
<!-- ``` text
"how do i make a pizza?"
```

**Thinking**
``` text
---RETRIEVE---
---CHECK DOCUMENT RELEVANCE TO QUESTION---
---ASSESS GRADED DOCUMENTS---
---DECISION: NOT ALL DOCUMENTS ARE NOT RELEVANT TO QUESTION---
---WEB SEARCH---
---GENERATE---
```

**Answer**

1. Preheat your oven to 500 °F (260 °C) and prepare a 12-inch pizza crust (homemade or store-bought).
2. Spread ¾–1 cup of pizza sauce evenly over the dough, then add your choice of cheese and toppings.
3. Bake on a pizza stone or sheet for 8–12 minutes, or until the crust is golden and the cheese is bubbly.
-->
### LangGraph Graph

``` mermaid
```

### Notes
Note that you'll need an `.env` file like this:

``` text
OPENAI_API_KEY=<MY_OPENAI_API_KEY>
TAVILY_API_KEY=<MY_TAVILY_API_KEY>
LANGCHAIN_API_KEY=<MY_LANGSMITH_API_KEY>
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=CRAG
PYTHONPATH=C:\localprojects\agentic_rag
```
