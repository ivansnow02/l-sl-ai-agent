FROM langchain/langgraph-api:3.12



ADD . /deps/react-agent-2

RUN PYTHONDONTWRITEBYTECODE=1 pip install --no-cache-dir -c /api/constraints.txt -e /deps/*

ENV LANGSERVE_GRAPHS='{"agent": "/deps/react-agent-2/src/react_agent/graph.py:graph"}'

WORKDIR /deps/react-agent-2
