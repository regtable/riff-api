"""
Hold a constant seed while modifying other parameters to create variations.
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

# Use the seed to preserve the overall structure
seed = 90

client = RiffAPIClient()
variation_a = client.compose(
    sound_prompts=[
        SoundPrompt(text="country folk, male singer"),
    ],
    lyrics=lyrics,
    seed=seed,
)

client.save_audio(variation_a.audio_b64, "3_variations_a.m4a")

variation_b = client.compose(
    sound_prompts=[
        SoundPrompt(text="country folk, female singer"),
    ],
    lyrics=lyrics,
    seed=seed,
)

client.save_audio(variation_b.audio_b64, "3_variations_b.m4a")
