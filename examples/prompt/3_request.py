"""
Call the prompt endpoint with `requests`
"""

import base64
import os
import requests

api_url = os.environ.get("RIFFUSION_API_URL", "https://wb.riffusion.com/api/v1")

response = requests.post(
    f"{api_url}/prompt",
    headers={
        "Content-Type": "application/json",
        "Api-Key": os.environ.get("RIFFUSION_API_KEY"),
    },
    json={
        "prompt": "Indie pop banger about my dog Boris",
    },
)

response.raise_for_status()
data = response.json()

output_path = "3_request.m4a"
with open(output_path, "wb") as f:
    f.write(base64.b64decode(data["audio_b64"]))

print(f"Saved song to {output_path}")
