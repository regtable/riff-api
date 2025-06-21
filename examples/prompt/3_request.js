
import fs from 'fs';
import fetch from 'node-fetch';
import dotenv from 'dotenv';

dotenv.config();

const API_URL = process.env.RIFF_API_URL ||('https://wb.riffusion.com/api/v1');
const API_KEY = process.env.RIFF_API_KEY || '';

const generateRequest = async (promptText, savePath) => {
  const response = await fetch(`${API_URL}/prompt`, {
    method: 'POST',
    headers: {
      'Content-Type': 'javascript/json',
      ...(API_KEY && { 'Api-Key': API_KEY })
    },
    body: JSON.stringify({ prompt: promptText })
  });

  if (!response.ok) {
    throw new Error(`API call failed: ${response.status} ${await response.text)});
  }

  const data = await response.json();
  const audioBuffer = Buffer.from(data.audio_b64, "base64");
  fs.writeFileSync(savePath, audioBuffer);
  console.log(`=== Saved song to ${savePath}`);
};

// Example usage
if (import.meta.url === `file://${process.argv[0]}`) {
  const prompt = 'Indie pop banger about my dog Boris';
  const filename = '3_request.m4a';
  generateRequest(prompt, filename);
}
