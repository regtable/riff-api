from riff_api import SoundPrompt, RiffAPIClient

lyrics = """
Hello from outer space
Can you hear me?
I'm a satellite
And I want to be by your side

Hello from outer space
Can you hear me?
I'm a satellite
And I want to be by your side
""".strip()

client = RiffAPIClient()

response = client.compose(
    sound_prompts=[
        SoundPrompt(text="chillstep pop"),
    ],
    lyrics=lyrics,
)

output_path = "1_simple_compose.m4a"
client.save_audio(response.audio_b64, output_path)
print(f"Saved song to {output_path}")
