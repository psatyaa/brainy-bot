# Copilot Instructions for **brainy-bot**

This small repository is a single‑module Streamlit app that hosts a **tool‑enabled AI agent**.  The goal of the project is educational: students run a web UI where the agent can calculate math and look up Wikipedia.  An AI coding assistant should keep the following in mind when navigating or modifying the code.

---

## 📁 Project Layout

```
agent_app.py        # the only Python module, contains entire application logic
instructions.md     # workshop instructions for humans
README.md           # high-level overview & lab steps
requirements.txt    # pip deps: openai, streamlit, wikipedia, dotenv
assets/             # image(s) used by the Streamlit background
``` 

There are no tests, packages or sub‑modules; everything lives in `agent_app.py`.  Treat that file as the canonical place for behaviour changes.

---

## 🧠 Big‑picture Architecture

* A Streamlit web page configured at the top of `agent_app.py` (`st.set_page_config` and inline CSS).  The background watermark is loaded from `assets/stem_watermark.png` if present.
* The ``calculate`` and ``search_wikipedia`` functions are the **tools** the agent can invoke.  They are pure Python helpers with simple error handling and are registered in two structures:
  * `available_functions` maps the tool name to the Python callable.
  * `tools` is a list of JSON‑serialisable function descriptions passed to the LM via the OpenAI client.
* A single OpenAI client instance is stored in `st.session_state.client`.  It is created lazily using the GitHub Models endpoint (`https://models.inference.ai.azure.com`) and the API key found in the `MY_GITHUB_MODELS_TOKEN` environment variable or a local `.env` file.
* Conversation history is held in `st.session_state.messages` with the initial system prompt defined as a large multiline string.  Editing that string is the way to change the agent's persona or guardrails.
* The main interaction loop lives under `if prompt := st.chat_input(...)`: user message → send to `client.chat.completions.create` along with `tools` → inspect `response_message.tool_calls` → execute any tool and append its result → request a second completion for the final answer.

This is the **think‑act‑observe** pattern implemented directly in Streamlit: the agent thinks (first completion), acts (tool call), and observes its own action before answering.

---

## 🔧 Developer Workflows

1. **Setup**
   ```bash
   python -m venv .venv          # create a venv (optional)
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. **Environment variable**
   - Define `MY_GITHUB_MODELS_TOKEN` with a GitHub PAT that has `Models: Read-only` permissions.
   - In Codespaces the secret is defined under *Settings ➔ Secrets and variables ➔ Codespaces*.
   - A local `.env` file is also read via `dotenv`.
3. **Run the app**
   ```bash
   streamlit run agent_app.py
   ```
   The local URL printed by Streamlit opens the chat UI.
4. **Editing or extending tools**
   - Add a Python function and update both `available_functions` and `tools` entries.
   - Keep the JSON schema in `tools` consistent with the callable’s parameters.
   - Use the same pattern for tool results (append a `tool`‑role message) so the second completion has the data.

There are no build scripts, tests, or CI pipelines to worry about; simply modify `agent_app.py` and rerun.

---

## 🧩 Conventions & Patterns

* All logic lives in the Streamlit script—no hidden modules.  Don't create new packages unless the project outgrows one file.
* Guardrails are encoded in the system prompt string.  Use explicit refusal messages (see examples in the prompt) to keep the agent on‑topic.
* The agent **must always try to use a tool** for factual or mathematical queries.  If you add new tools, update the system prompt accordingly so the model knows they exist.
* `calculate` uses a very simple `eval` with `{'__builtins__': None}`; this is for demonstration only and not intended for production.
* The environment variable name is **exact** (`MY_GITHUB_MODELS_TOKEN`).  The app fails early with a `st.error` if it is missing.
* For background images, the script checks `os.path.exists` and falls back gracefully to a solid color.

---

## 🚨 Integration Points

* **OpenAI/GitHub Models API:**  All network calls go through `st.session_state.client.chat.completions.create`.  The default `model` is `gpt-4o` and `tool_choice` is set to `auto`.
* **Wikipedia package:**  Used by `search_wikipedia`; handles disambiguation and page errors.
* **Streamlit session state:**  Used to persist both the chat history and the client across reruns.

No other external services are used.

---

If anything is unclear or you spot missing details, let me know and we can refine these notes further.