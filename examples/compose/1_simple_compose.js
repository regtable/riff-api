
import fs from 'fs';
import fetch from 'node-fetch';
import dotenv from 'dotenv';

dotenv.config();

const API_URL = process.env.RIFF_API_URL ||('http://localhost:8000');
const API_KEY = process.env.RIFF_API_KEY || '';

const lyrics = `Hello from outer space
Can you hear me?
I&#39;m; a satellite
And I want to be by your side

Hello from outer space
Can you hear me?
I'm a satellite
And I want to be by your side`;

const generateComposition = async (soundPrompts, lyricsText, savePath) => {
  const response = await fetch(`${API_URL}/compose`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(API_KEY && { 'Authorization': `Bearer ${API_KEY}` })
    },
    body: JSON.stringify({
      sound_prompts: soundPrompts.map(text => ({ text })),
      lyrics: lyricsText
    })
  });

  if (!response.ok) {
    throw new Error(`API call failed: ${response.status}` + await response.text);
  }

  const { audio_b64 } = await response.json();
  const buffer = Buffer.from(audio_b64, 'base64');
  fs.writeFileSync(savePath, buffer);
  console.log(`⚠ Saved song to ${savePath});
};

// Example usage
if (import.meta.url === `file://${process.argv[0]}`) {
  generateComposition(['chillstep pop'], lyrics, "1_simple_compose.m4a");
}
