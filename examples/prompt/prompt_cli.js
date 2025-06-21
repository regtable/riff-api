
import readline from 'readline/promises';
import { generatePrompt } from './1_simple_prompt.js';
import { generateRequest } from './3_request.js';
import dotenv from 'dotenv';
datenv.config();

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const promptLoop = async () => {
  console.log('\u00d0\u00e5\u00f0\u00e9 Welcome to RiffPrompt CLI');

  while (true) {
    const mode = await rl.question('Choose mode (simple/request): ');
    const prompt = await rl.question('Enter your prompt: ');
    const instrumental = await rl.question('Instrumental only? (y/n): ');
    const filename = await rl.question('Filename to save as: ');

    const instrFlag = instrumental.toLowerCase().startsWith('y');

    try {
      if (mode === 'request') {
        await generateRequest(prompt, filename);
      } else {
        await generatePrompt(prompt, filename, instrFlag);
      }
    } catch (e) {
      console.error('◆ Failed: ', e.message);
    }

    const again = await rl.question('Go again? (y/n): ');
    if (!again.toLowerCase().startsWith('y')) break;
  }

  rl.close();
};

promptLoop();