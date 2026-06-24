from groq import Groq
from app.core.config import settings

# Initialize the Groq client once (reused across requests)
client = Groq(api_key=settings.GROQ_API_KEY)

def get_ai_response(user_message: str, conversation_history: list = []) -> str:
    """
    Send a message to Groq's LLM and get a response back.
    
    user_message: The latest thing the user said
    conversation_history: List of previous messages (for memory later)
    """
    
    # Build the messages list
    # 'system' message tells the AI how to behave
    messages = [
        {
            "role": "system",
            "content": "You are a helpful AI voice assistant. Keep your responses concise and conversational, since they will be spoken aloud. Avoid using bullet points or markdown formatting."
        }
    ]
    
    # Add any previous conversation history (empty for now, used in Phase 5)
    messages.extend(conversation_history)
    
    # Add the user's new message
    messages.append({
        "role": "user",
        "content": user_message
    })
    
    # Call Groq API
    chat_completion = client.chat.completions.create(
        messages=messages,
       model="llama-3.3-70b-versatile",   # Fast, free Llama 3 model
        temperature=0.7,           # 0 = robotic, 1 = creative. 0.7 is balanced
        max_tokens=300,            # Keep responses short for voice
    )
    
    # Extract and return just the text response
    return chat_completion.choices[0].message.content