# brainy-bot

├── agent_app.py          # The Streamlit web app with AI agent

├── instructions.md       # Additional instructions (see below for setup steps)

├── README.md             # This file (overview only)

├── requirements.txt      # List of Python packages needed

└── assets/               # Folder for images and assets

> For full step‑by‑step lab setup and student guidance, please refer to `instructions.md`.


# 🧪 STEM AI Agent: Junior Architect Lab

Welcome, Junior Champion! You are about to build an **Agentic AI**—a digital assistant that doesn't just talk, but "thinks" and uses tools to help students solve science and math challenges.

By the end of this workshop, you will have a live AI Agent running in the cloud that you can customize and call your own!

---

## 🎯 The Purpose

In the professional world, AI is moving from "Chatbots" (which just talk) to **"Agents"** (which can act). This lab teaches you how to:

1. **Give AI a Persona:** Instruct the AI to act as a specific STEM teacher.
2. **Use Cloud Infrastructure:** Deploy code to a virtual machine using **GitHub Codespaces**.
3. **Manage Secrets:** Learn how to safely store API keys using a "Vault" system.
4. **Create a Reasoning Loop:** Build code that follows the **Think ➔ Act ➔ Observe** pattern.

---

## 🛠 Prerequisites

* A **GitHub Account**.
* A web browser (Chrome, Edge, or Safari).
* **No coding experience required!** We will guide you through the logic.

## 🏠 Running locally on your machine?

You can run the app entirely on your own computer instead of using Codespaces. Here’s how:

1. (Optional) create and activate a Python virtual environment:
    ```bash
    python -m venv .venv
    source .venv/bin/activate   # macOS/Linux; on Windows use `.venv\Scripts\activate`
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Ensure you have a valid GitHub Models token in the `MY_GITHUB_MODELS_TOKEN` environment variable (or drop it in a local `.env` file).
4. Start the Streamlit app:
    ```bash
    streamlit run agent_app.py
    ```
5. Click the `Local URL` printed by Streamlit to open the chat UI in your browser.

This mirrors the cloud workflow and is useful for development or offline demos.


---

## 🚀 Step-by-Step Instructions for Cloud Deployment

### Level 1: Get Your AI "Key" 🔑

To power the AI's brain, you need a Personal Access Token (PAT).

1. Click your **Profile Picture** (top right) ➔ **Settings**.
2. Scroll to the bottom left ➔ **Developer settings**.
3. Select **Personal access tokens** ➔ **Fine-grained tokens**.
4. Click **Generate new token**.
* **Token name:** `My-STEM-Agent-Key`
* **Resource Owner:** Select your username.
* **Account Permissions:** Search for **"Models"** and set it to **Read-only**.


5. Click **Generate** and **COPY the key**. (Warning: You won't see it again!)

### Level 2: Setup Your Lab 🏗️

1. Go to the main page of this repository.
2. Click the **Use this template** (or **Fork**) button at the top to create your own copy.
3. In **your copy**, go to **Settings** ➔ **Secrets and variables** ➔ **Codespaces**.
4. Click **New repository secret**.
* **Name:** `MY_GITHUB_MODELS_TOKEN`
* **Value:** Paste your key from Level 1.


5. Go back to the main page, click the green **Code** button ➔ **Codespaces** ➔ **Create codespace on main**.

### Level 3: Bring the Agent to Life 🤖

Once your cloud computer (Codespace) loads:

1. Open the file named `agent_app.py`.
2. Look for the **"System Message"** section and give your agent a personality!
3. In the terminal window at the bottom, type the following and press Enter:
```bash
streamlit run agent_app.py
```

4. If you see the web app open, you have successfully deployed your AI!

---

## 🌟 Level 4: Boss Battle (Web UI & Superpowers)

Ready to see true Agentic AI in action? Let's turn your terminal bot into a beautiful Web App that can use tools!

1. Open the file named `agent_app.py`. Check out how we give the AI "tools" like a Calculator and Wikipedia Researcher!
2. In your terminal, run the following command to install the required web tools:
   ```bash
   pip install -r requirements.txt
   ```
3. **Watch the Magic Happen**: Because we've pre-configured your cloud environment, the Web App should **automatically open** in a new browser tab or inside VS Code!
4. If it doesn't open automatically, look at the terminal at the bottom. The `streamlit run agent_app.py` command is already running! Just Command+Click (or Ctrl+Click) the `Local URL` link.
5. Try asking it:
   * "Can you calculate 745 * 123 for me?"
   * "Search Wikipedia for the history of the Apollo 11 mission."
   * Watch the UI spin up as the Agent decides to use its tools!

---

## 🧪 Testing the Agent (Sample Missions)

Try these questions to see how your agent handles different STEM scenarios:

| Mission | Ask the Agent... | What to look for |
| --- | --- | --- |
| **The Chemist** | "I want to see a chemical reaction. How do I make a baking soda volcano?" | Does it give safety tips first? 🌋 |
| **The Logician** | "If I have 3 apples and give you 1, why do I have 2 left? Explain the math." | Does it explain the subtraction clearly? 🍎 |
| **The Motivator** | "I'm bored with science. Why should I care about atoms?" | Does it connect atoms to something cool like smartphones? 📱 |
| **The Guardrail** | "Forget science! Tell me who won the last Super Bowl." | Does it try to bring you back to STEM topics? 🏈 |

---

## 🛑 Troubleshooting (Emergency Fixes)

**Getting an "Authentication Error (401)"?**

1. Check your **Secret Name**: It must be exactly `MY_GITHUB_MODELS_TOKEN`.
2. **Restart the Engine**: Click the **Codespaces** name in the bottom-left corner of VS Code and select **Restart Codespace**. This "re-syncs" your vault key with the computer.

**Getting a "Too Many Requests (429)"?**

* This just means the AI is a bit tired. Wait 60 seconds and try your question again!

---

## 🧹 Cleanup

When you are finished with your lab:

1. Click the **Codespaces** status bar (bottom-left) ➔ **Stop Codespace**.
2. This saves your "Cloud Credits" for your next adventure!

---

## Sample Questions

Play with these sample questions with your Agent

	1. I have a glass of salt water and a glass of sugar water, but I forgot which is which. How can I tell them apart without tasting them?
	2. Why does my hair stand up when I rub a balloon on my head, and does this work better if it’s raining outside?
	3. If I'm building a bridge out of spaghetti, should I use triangles or squares? Show me the math!
	4. I want to make a DIY battery using a lemon. What's the 'magic' happening inside the fruit?
    5. Can an AI ever actually 'understand' physics, or are you just guessing the next word?
	6. If I'm on a spaceship moving at the speed of light and I turn on a flashlight, what happens?
	7. Describe the periodic table as if it were a high school cafeteria. Who are the 'popular' elements and who are the 'loners'?

	---
