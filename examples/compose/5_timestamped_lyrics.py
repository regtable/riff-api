"""
Print the timestamp of each lyric from the generation response.
"""

from riff_api import RiffAPIClient, SoundPrompt

lyrics = """
[Intro]
Yeah, uh, Corner Store Chronicles
Back in the D, y'all know how it be
(Woo-ooh)

[Verse 1]
Quarter in my pocket, sun up in the sky
Meet up with my crew around half past five
Same routine daily, ain't nothing new
Gas station run with my day-one crew
Quick check the time, mama said be back soon
Walking down the block, humming out a tune
(La-la-di-da)
Simple life living, that's all we need
Hi-C and Capri's all we trying to seek

[Chorus]
Every day we hit the block (Yeah)
Same time, same spot (You know)
With my people, never stop (Never)
This the life we got
(Every day we hit the block)
Same time, same spot (Uh-huh)
With my people, never stop
This the life we got (That's right)

[Verse 2 - Spanish]
Cada día en la tienda local
Con mis amigos, momento especial
Capri Sun helado, Hi-C también
En las calles de Detroit, todo está bien
Memorias simples pero son real
Con mi gente leal, nunca va mal
(Así es)
En el barrio siempre juntos
Estos momentos valen mucho

[Verse 3]
Looking back now at those simple days
When all we needed was a sugar craze
Gas station owner knows us all by name
"Y'all back again?" (Yeah) it's all the same
These memories stick like juice to my brain
Summer heat but we don't complain
(Oh-oh-yeah)
Simple pleasures with my day one crew
This is how we do, that's nothing new

[Chorus]
Every day we hit the block (Yeah)
Same time, same spot (You know)
With my people, never stop (Never)
This the life we got
(Every day we hit the block)
Same time, same spot (Uh-huh)
With my people, never stop
This the life we got (For real)

[Outro]
That's how we living in the D
Simple life is all we need
(La-la-di-da-da)
[Fade out]
""".strip()

client = RiffAPIClient()

response = client.compose(
    sound_prompts=[
        SoundPrompt(text="chillstep pop"),
    ],
    lyrics=lyrics,
    save_to="5_timestamped_lyrics.m4a",
)

# Print each word's start time
assert response.timestamped_lyrics is not None
for word in response.timestamped_lyrics:
    print(f"{word.text:<12s} -> {word.start:6.1f}s")
