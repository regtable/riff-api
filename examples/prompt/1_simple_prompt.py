from riff_api import RiffAPIClient

client = RiffAPIClient()

response = client.prompt(
    "Explain the concept of time in French, piano chill",
    save_to="1_simple_prompt.m4a",
)

print("Saved song to 1_simple_prompt.m4a")
