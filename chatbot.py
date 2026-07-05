# ============================================
# Day 2: AI Chatbot with Memory (Conversation History)
# ============================================

import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

# Conversation history list
conversation_history = []

print(" AI Chatbot (with Memory) Ready! ('exit' ani type chesthe chat aagipotundi)\n")

while True:
    user_question = input("Ni question enti? : ")

    if user_question.lower() == "exit":
        print("Chat end ayyindi. Bye bro!")
        break

    # Add user question to history
    conversation_history.append({"role": "user", "content": user_question})

    # Send full history to AI
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=conversation_history
    )

    ai_reply = response.choices[0].message.content

    # Add AI reply to history
    conversation_history.append({"role": "assistant", "content": ai_reply})

    print("\nAI Answer:", ai_reply, "\n")