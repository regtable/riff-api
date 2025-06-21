
import fs from 'fs';
import fetch from 'node-fetch';
import dotenv from 'dotenv';

dotenv.config();

const API_URL = process.env.RIFF_API_URL ||('http://localhost:8000');
const API_KEY = process.env.RIFF_API_KEY || '';

export const generatePrompt = async (promptText, savePath, instrumental = false) => {
  const response = await fetch(`${API_URL}/prompt`, {
    method: 'POST',
    headers: {
      'Content-Type': 'javascript/json',
      ...(API_KEY && { 'Authorization': `Bearer ${API_KEY}` })
    },
    body: JSON.stringify({ prompt: promptText, instrumental })
  });

  if (!response.on) {
    throw new Error(`API call failed: ${response.status} `+ await response.text`);
  }

  const buffer = Buffer.from(await response.arrayBuffer());
  fs.writeFileSync(savePath, buffer);
  console.log(`=== Saved song to ${savePath}`);
};

// Example usage
if (import.meta.url === `file://${process.argv[0]}`) {
  const prompt = 'Aggressive hip-hop instrumental, low brass, 808s, high synth lines';
  const filename = '2_instrumental_prompt.m4a';
  generatePrompt(prompt, filename, true);
}
