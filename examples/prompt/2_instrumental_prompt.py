from riff_api import RiffAPIClient

client = RiffAPIClient()

response = client.prompt(
    prompt="Aggressive hip-hop instrumental, low brass, 808s, high synth lines",
    instrumental=True,
    save_to="2_instrumental_prompt.m4a",
)

print("Saved song to 2_instrumental_prompt.m4a")
