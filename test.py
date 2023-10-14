from decouple import config
import locale
config.encoding = locale.getpreferredencoding(False)

# Retrieve the OpenAI API key using decouple
openai_api_key = config("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file")

print(f"OPENAI_API_KEY: {openai_api_key}")