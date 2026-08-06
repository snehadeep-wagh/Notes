from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI

# Load env variables/api keys
load_dotenv()


v_model = "gemini-2.0-flash"
v_temperature = 1.0


llm_model = GoogleGenerativeAI(
    model=v_model,
    temperature=v_temperature
)

# Chat message
msg = "What is the langchain."

res = llm_model.invoke(msg)

print(res)
