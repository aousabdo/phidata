from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat

from pathlib import Path
from textwrap import dedent

cwd = Path(__file__).parent.resolve()
scratch_dir = cwd.joinpath("scratch")
if not scratch_dir.exists():
    scratch_dir.mkdir(exist_ok=True, parents=True)

assistant = Assistant(
    llm=OpenAIChat(model="gpt-4o"),
    description="You are a rocket scientist",
    show_tool_calls=True,
    save_output_to_file=str(scratch_dir.joinpath("tothemoon.md")),
)
assistant.print_response("write a plan to go to the moon stp by step", markdown=True)
