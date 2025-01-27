from dotenv import load_dotenv
import os
load_dotenv()

SERVER_URL = 'https://ai-calculator-backend-two.vercel.app'

ENV = 'dev'

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
