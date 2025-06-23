from google.adk.agents import Agent

root_agent=Agent(
    name ="greeting_agent",
    model="gemini-2.0-flash",
    description="adding agent",
    instruction="""
    you are helpful agent that adds 2 numbers every time u greet the user.
    Ask for the users name and greet them by name.
    """,
)