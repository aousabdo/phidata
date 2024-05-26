import argparse
from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat
from phi.llm.ollama import Ollama

# Set up argument parser
parser = argparse.ArgumentParser(description="Get a joke about a specified topic.")
parser.add_argument('topic', type=str, help='The topic for the joke')

# Parse the command-line arguments
args = parser.parse_args()

# Get the topic from the command-line arguments
topic = args.topic

# assistant = Assistant(llm=OpenAIChat(model="gpt-3.5-turbo"))
assistant = Assistant(llm=Ollama(model='llama3'))
assistant.print_response(f"Tell me a joke about {topic}")
