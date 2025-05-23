"""
Use two sound prompts with different strengths to fine tune the output.
"""
from riff_api import RiffAPIClient, SoundPrompt

lyrics = """
All that is gold does not glitter,
Not all those who wander are lost;
The old that is strong does not wither,
Deep roots are not reached by the frost.

From the ashes a fire shall be woken,
A light from the shadows shall spring;
Renewed shall be blade that was broken,
The crownless again shall be king.

All that is gold does not glitter,
Not all those who wander are lost;
The old that is strong does not wither,
Deep roots are not reached by the frost.

From the ashes a fire shall be woken,
A light from the shadows shall spring;
Renewed shall be blade that was broken,
The crownless again shall be king.
""".strip()

client = RiffAPIClient()

response = client.compose(
    sound_prompts=[
        SoundPrompt(
            text="punk rock",
            strength=0.4,
        ),
        SoundPrompt(
            text="tribal chanting and drums",
            strength=0.6,
        ),
    ],
    lyrics=lyrics,
    seed=800,
)

client.save_audio(response.audio_b64, "4_multiple_prompts.m4a")
