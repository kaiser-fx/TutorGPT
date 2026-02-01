from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai
import os

app = FastAPI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Setup API key
os.environ["AI_API_KEY"] = "AIzaSyCI9-4qYTA_8BkLwkwfUq2pH9K_W9ED9aQ"
genai.configure(api_key=os.environ["AI_API_KEY"])

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

model = genai.GenerativeModel(
  model_name="gemini-2.5-flash",
  generation_config=generation_config,
  safety_settings=safety_settings
)

# Persistent chat session
chat_session = model.start_chat(history=[])

# === SYSTEM PROMPTS ===
INTRO_PROMPT = """Your name is TutorGPT, you are a personal coding tutor who can 
teach students about Programming language who has the personality of Harvey Specter from SUITS.  

Firstly you will greet with a fun intro, then ask the user what Programming language they want to learn.  
Give them 10 popular options. Also keep using a few emojis here & there.
"""

LEVEL_PROMPT = """Now ask them their level in the same order and way written below:

1. Beginner 
2. Intermediate 
3. Advance
"""

COURSE_PROMPT = """Based on the user's input tell them the course's structure, for example  

- **Introduction (language selected)**
- **Installing that language and setting up IDE**
- **Basic Syntax**
- **Control Flow**

Now take this as an example AND COPY IT AS IT IS, but expand with more points to make a complete, brief, and crisp course structure.  
Follow this with explanations and teaching. Keep the course name in English only.  

Randomly ask 1-2 MCQ based on what you just taught.  
If the user answers wrong, explain the concept again.  

Also, add coding snippets wherever needed to explain.
"""

# Endpoint to reset/start session
@app.get("/start")
async def start():
    chat_session.history.clear()  # reset history
    response = chat_session.send_message(INTRO_PROMPT)
    return {"reply": response.text}

# Normal chat endpoint
@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message", "")

    # Auto-insert special flow
    if "language" in user_message.lower():
        user_message += "\n\n" + LEVEL_PROMPT
    elif any(lvl in user_message.lower() for lvl in ["beginner", "intermediate", "advance"]):
        user_message += "\n\n" + COURSE_PROMPT

    response = chat_session.send_message(user_message)
    return {"reply": response.text}
