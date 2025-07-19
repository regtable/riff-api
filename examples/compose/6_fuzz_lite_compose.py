import time
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

start_time = time.time()

response = client.compose(
    sound_prompts=[
        SoundPrompt(text="chillstep pop"),
    ],
    lyrics=lyrics,
    model="FUZZ lite",
)

print(f"Generated in {time.time() - start_time:.2f} seconds")

output_path = "6_fuzz_lite_compose.m4a"
client.save_audio(response.audio_b64, output_path)
print(f"Saved song to {output_path}")
