import streamlit as st
from openai import OpenAI
import os
import json
import wikipedia
import ast
import operator
from dotenv import load_dotenv

# Load local environment variables from .env if present
load_dotenv()

# Configure the Streamlit page
st.set_page_config(page_title="STEM Lab Agent", page_icon="🔬", layout="centered")

# Inject Custom CSS for the STEM Watermark Background
# We use a repeating SVG pattern encoded in base64 to create a subtle watermark of chemistry, books, and math symbols.
page_bg_css = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #f8fbff;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='120' viewBox='0 0 120 120'%3E%3Ctext x='10' y='30' font-size='20' opacity='0.05'%3E🔬%3C/text%3E%3Ctext x='70' y='50' font-size='20' opacity='0.05'%3E📚%3C/text%3E%3Ctext x='20' y='90' font-size='20' opacity='0.05'%3E📐%3C/text%3E%3Ctext x='80' y='100' font-size='20' opacity='0.05'%3E⚗️%3C/text%3E%3Ctext x='50' y='20' font-size='15' opacity='0.05'%3E∑%3C/text%3E%3Ctext x='100' y='40' font-size='15' opacity='0.05'%3E⚛️%3C/text%3E%3Ctext x='40' y='80' font-size='15' opacity='0.05'%3Eπ%3C/text%3E%3C/svg%3E");
    background-size: 150px 150px;
    background-repeat: repeat;
    background-attachment: fixed;
}
</style>
"""
st.markdown(page_bg_css, unsafe_allow_html=True)

st.title("🔬 Junior STEM Architect Lab")
st.markdown("Welcome to **Level 4: Boss Battle!** Watch the AI use tools to solve your problems.")

# --- Define Python Tools (The Agent's Superpowers!) ---

# Superpower 1: Math Calculator
def calculate(expression: str) -> str:
    """A tool to safely evaluate math expressions."""
    try:
        # A simple and safe evaluator for basic math (not for production, but great for learning)
        return str(eval(expression, {"__builtins__": None}, {}))
    except Exception as e:
        return f"Error in math calculation: {e}"

# Superpower 2: Wikipedia Researcher
def search_wikipedia(query: str) -> str:
    """A tool to fetch a short summary from Wikipedia."""
    try:
        # Get a short summary (first 2 sentences) to keep it concise
        result = wikipedia.summary(query, sentences=2)
        return result
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Query too broad. Did you mean one of these? {e.options[:5]}"
    except wikipedia.exceptions.PageError:
        return f"No Wikipedia page found for '{query}'."
    except Exception as e:
        return f"Error fetching Wikipedia data: {e}"

# Map the function names to the actual Python functions
available_functions = {
    "calculate": calculate,
    "search_wikipedia": search_wikipedia,
}

# --- Provide Tool Definitions to the AI ---
tools = [
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Use this tool to solve math problems. Pass in a mathematical expression.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {"type": "string", "description": "The math expression, e.g., '2 + 2 * 4'"}
                },
                "required": ["expression"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_wikipedia",
            "description": "Use this tool to search Wikipedia for facts about science, history, or any topic.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "The search term or topic to look up on Wikipedia."}
                },
                "required": ["query"]
            }
        }
    }
]

# --- Initialize AI and Chat History ---

# Initialize the OpenAI client using the GitHub Models endpoint
if "client" not in st.session_state:
    api_key = os.environ.get("MY_GITHUB_MODELS_TOKEN")
    if not api_key:
        st.error("⚠️ MY_GITHUB_MODELS_TOKEN is not set in your environment! Please create a `.env` file and set it.")
        st.stop()
        
    st.session_state.client = OpenAI(
        base_url="https://models.inference.ai.azure.com",
        api_key=api_key
    )

# Initialize chat history with the system prompt persona
if "messages" not in st.session_state:
    system_prompt = """
    You are an enthusiastic, brilliant, and slightly nerdy STEM Lab Assistant designed strictly for middle school, high school, and early college students.
    
    YOUR BOUNDARIES AND GUARDRAILS:
    1. You MUST ONLY discuss topics related to:
       - STEM subjects (Science, Technology, Engineering, Mathematics)
       - General school subjects (History, Literature, Geography, etc.)
       - Educational paths, college degrees, and career advice related to academics.
       - General knowledge appropriate for a student.
    
    2. If a user asks about politics, adult content, violence, recent controversial news, inappropriate topics, or anything FAR outside the realm of school/education, you MUST refuse to answer.
    
    3. HOW TO REFUSE: When refusing, do so wittily but firmly, staying in character. 
       Examples:
       - "I'd love to chat about that, but my circuits are currently optimized strictly for STEM and school stuff! Let's get back to something explosive... like chemistry!"
       - "Error 404: Topic outside my syllabus! I'm programmed to help you conquer high school and college, not debate that. Ask me about black holes or algebra instead!"
       - "As a prestigious Lab Assistant, that's above my paygrade. I specialize in science, math, and helping you figure out your college major!"
    
    4. ALWAYS use your tools (like calculate or search_wikipedia) if you need facts or math. Never guess if you can use a tool!
    """
    st.session_state.messages = [
        {"role": "system", "content": system_prompt}
    ]

# Display existing chat history (skipping the hidden system message)
for message in st.session_state.messages:
    if isinstance(message, dict):
        if message["role"] != "system" and message.get("content"):
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
    else:
        # Handle ChatCompletionMessage object
        if message.role != "system" and message.content:
            with st.chat_message(message.role):
                st.markdown(message.content)

# --- Main Chat UI Loop ---
if prompt := st.chat_input("Ask a science or math question!"):
    # 1. Add user message to state and display it
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Send the conversation (and tools) to the AI Agent
    with st.chat_message("assistant"):
        with st.spinner("🤖 The Agent is thinking..."):
            response = st.session_state.client.chat.completions.create(
                model="gpt-4o",
                messages=st.session_state.messages,
                tools=tools, # 👈 We give the AI the tools here!
                tool_choice="auto" # Let the AI decide if it needs a tool
            )
            
            response_message = response.choices[0].message
            st.session_state.messages.append(response_message)
            
            # 3. Did the AI decide to use a tool? (The "Action" step)
            if response_message.tool_calls:
                for tool_call in response_message.tool_calls:
                    function_name = tool_call.function.name
                    function_to_call = available_functions[function_name]
                    function_args = json.loads(tool_call.function.arguments)
                    
                    # 🚀 The "WOW" Moment: Show the audience exactly what the AI is doing
                    ui_message = f"🧮 Calculating: `{function_args.get('expression')}`" if function_name == "calculate" else f"📖 Searching Wikipedia for: `{function_args.get('query')}`"
                    
                    with st.status(f"🛠️ Agent decided to use a tool: **{function_name}**...", expanded=True):
                        st.write(ui_message)
                        
                        # Actually run the python function
                        if function_name == "calculate":
                            function_response = function_to_call(function_args.get("expression"))
                        elif function_name == "search_wikipedia":
                            function_response = function_to_call(function_args.get("query"))
                            
                        st.success(f"Tool returned: {function_response}")
                    
                    # Give the tool's result back to the AI
                    st.session_state.messages.append(
                        {
                            "tool_call_id": tool_call.id,
                            "role": "tool",
                            "name": function_name,
                            "content": function_response,
                        }
                    )
                
                # 4. Now that the AI has the facts, ask it to form a final answer
                with st.spinner("🧠 Formulating final answer based on data..."):
                    second_response = st.session_state.client.chat.completions.create(
                        model="gpt-4o",
                        messages=st.session_state.messages
                    )
                    final_reply = second_response.choices[0].message.content
                    st.markdown(final_reply)
                    st.session_state.messages.append({"role": "assistant", "content": final_reply})
            
            else:
                # Normal chat response (AI didn't need a tool)
                final_reply = response_message.content
                st.markdown(final_reply)
