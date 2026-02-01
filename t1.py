from smolagents import CodeAgent, DuckDuckGoSearchTool,  LiteLLMModel

lmodel = LiteLLMModel(
        model_id="ollama_chat/qwen2:7b",  # Or try other Ollama-supported models
        api_base="http://127.0.0.1:11434",  # Default Ollama local server
        num_ctx=8192,
    )
agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=lmodel)

agent.run("Search for the best music recommendations for a party at the Wayne's mansion.")

