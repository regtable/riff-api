curl -X POST \
  -H "Content-Type: application/json" \
  -H "Api-Key: ${RIFFUSION_API_KEY}" \
  -d '{"prompt": "Rap fun facts about Alaskan history"}' \
  https://wb.riffusion.com/api/v1/prompt \
  | jq -r .audio_b64 | base64 -d > 4_curl.m4a
