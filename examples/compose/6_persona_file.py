"""Compose a song using sound prompts parsed from a persona file."""

from pathlib import Path
from riff_api import RiffAPIClient, SoundPrompt


def load_persona_prompts(path: Path) -> list[SoundPrompt]:
    """Read `key: value` lines from a persona file as individual sound prompts."""
    prompts: list[SoundPrompt] = []
    with path.open() as f:
        for line in f:
            line = line.strip()
            if not line or ":" not in line:
                continue
            _, desc = line.split(":", 1)
            desc = desc.strip()
            if desc:
                prompts.append(SoundPrompt(text=desc))
    return prompts


persona_file = Path(__file__).resolve().parents[1] / "personas" / "elias_driftborn.ai"

sound_prompts = load_persona_prompts(persona_file)

lyrics = """\
Wandering through echoes of the unknown,
voices intertwine in sacred tone.
""".strip()

client = RiffAPIClient()
response = client.compose(
    sound_prompts=sound_prompts,
    lyrics=lyrics,
)

output_path = "6_persona_file.m4a"
client.save_audio(response.audio_b64, output_path)
print(f"Saved song to {output_path}")
