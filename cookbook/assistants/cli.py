from phi.assistant import Assistant
from phi.tools.duckduckgo import DuckDuckGo
from phi.llm.openai import OpenAIChat
from phi.llm.ollama import Ollama

# llm = OpenAIChat(model="gpt-4o")
llm = Ollama(model="llama3")

assistant = Assistant(
    llm=llm,
    tools=[DuckDuckGo()], 
    instructions=["respond to user messages given the tools you have access to"],
    show_tool_calls=True, 
    read_chat_history=True)

assistant.cli_app(markdown=True)
