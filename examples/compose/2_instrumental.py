"""
Pass no lyrics to create instrumental music.
"""

from riff_api import RiffAPIClient, SoundPrompt

client = RiffAPIClient()

response = client.compose(
    sound_prompts=[
        SoundPrompt(text="lo-fi cozy christmas jazz"),
    ],
)

client.save_audio(response.audio_b64, "2_instrumental.m4a")
