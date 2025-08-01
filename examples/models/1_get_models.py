from riff_api import RiffAPIClient

client = RiffAPIClient()

models = client.models()
print(models)
