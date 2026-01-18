# brainy-bot

├── .devcontainer/

│   └── devcontainer.json    # The "Magic" that sets up the environment

├── junior_agent.py          # The core AI Agent code

├── requirements.txt         # List of tools the code needs

└── .env                     # (DO NOT PUSH THIS) Your API Keys


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

---

## 🚀 Step-by-Step Instructions

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

1. Open the file named `junior_agent.py`.
2. Look for the **"System Message"** section and give your agent a personality!
3. In the terminal window at the bottom, type the following and press Enter:
```bash
python junior_agent.py

```


4. If you see `🚀 Agent Online!`, you have successfully deployed your AI!

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

Would you like me to help you create a **"Completion Certificate"** (a Markdown badge) that students can add to their profile once they finish the workshop?
