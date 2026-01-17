import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Setup the AI Client using GitHub's free model endpoint
# NOTE: In Codespaces, GITHUB_TOKEN is provided automatically!
client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.environ.get("MY_GITHUB_MODELS_TOKEN") 
)

def junior_agent():
    print("🚀 Agent Online! Type 'exit' to stop.")
    
    # The 'System Message' defines the AI's persona
    messages = [
        {"role": "system", "content": "You are a helpful STEM Lab Assistant for middle schoolers. Use emojis and be encouraging!"}
    ]

    while True:
        user_input = input("\nStudent: ")
        if user_input.lower() == 'exit': break

        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            temperature=0.7
        )

        reply = response.choices[0].message.content
        print(f"\n🤖 Agent: {reply}")
        messages.append({"role": "assistant", "content": reply})

if __name__ == "__main__":
    junior_agent()
