# 🚀 Junior STEM Architect Lab: The Ultimate Guide

Welcome, future engineer! Today, you are going to build your very own AI Assistant that lives in the cloud. It will act like a STEM teacher, solve math problems, and browse the internet for facts!

Don't worry if you've never coded before. Follow these exact steps, and you'll be a pro in no time!

---

## Part 1: Your Developer Passport

Before we build, we need a place to store our code. We are going to use **GitHub**, which is like Google Drive but for programmers!

### Step 1: Create a GitHub Account
1. Go to [https://github.com/](https://github.com/)
2. Click the **Sign Up** button in the top right corner.
3. Follow the space-themed prompts to enter your email, create a password, and pick a cool username!
4. Check your email to verify your account. 

*(If you already have a GitHub account, just click **Sign In**!)*

![GitHub Sign Up Page Placeholder](https://docs.github.com/assets/cb-103133/mw-1440/images/help/homepage/login-or-signup.webp)
*(Teacher: Insert screenshot of GitHub homepage Sign Up button)*

---

## Part 2: Copying the Blueprint (Forking)

We already wrote the base code for you. You just need to copy it to your new account!

1. Open this link: **[Link to Your Repository Here]**
2. In the top right corner of the page, click the button that says **Fork**. 
3. Click the green **Create Fork** button. 

🎉 Boom! You now have your very own copy of the code!

![Fork Button Placeholder](https://docs.github.com/assets/cb-68641/mw-1440/images/help/repository/fork_button.webp)
*(Teacher: Insert screenshot highlighting the Fork button)*

---

## Part 3: Giving Your AI a "Brain Key"

To make the AI smart, we need to rent a mini-brain from the cloud. We do this using a secret "Token" (which is basically a super-long password).

### Step 1: Generate the Key
1. Click on your **Profile Picture** in the very top right corner of GitHub.
2. Click **Settings**.
3. Scroll all the way down the left menu and click **Developer settings**.
4. Click **Personal access tokens**, then click **Fine-grained tokens**.
5. Click the **Generate new token** button.
   * **Token name:** Name it `My-AI-Brain`
   * **Expiration:** Leave it alone (usually 30 days is fine).
   * **Resource owner:** Select your username!
6. Scroll down to **Account Permissions**. Click it to open the list.
7. Find **Models** in the list, click the dropdown, and change it to **Read-only**.
8. Scroll to the very bottom and click the green **Generate token** button.

🛑 **STOP!** You will see a long code that looks like `github_pat_xxxxxxx`. **Copy this code right now.** Once you leave this page, it disappears forever!

![Copying PAT Placeholder](https://docs.github.com/assets/cb-103133/mw-1440/images/help/settings/personal_access_tokens_fine_grained_copy.webp)
*(Teacher: Insert screenshot showing the copy button for the new PAT)*

### Step 2: Hide the Key in the Vault
We need to hide this key in your project so only your cloud computer can see it.

1. Go back to your copy of the project (click your profile picture > Your repositories > click your project).
2. Click the **Settings** tab near the top right (it looks like a gear ⚙️).
3. On the left menu, click **Secrets and variables**, then click **Codespaces**.
4. Click the green **New repository secret** button.
5. In the **Name** box, type EXACTLY this: `MY_GITHUB_MODELS_TOKEN`
6. In the **Secret** box, paste your long key that you copied earlier.
7. Click **Add secret**.

![Adding Secret Placeholder](https://docs.github.com/assets/cb-103133/mw-1440/images/help/settings/secrets-add.webp)
*(Teacher: Insert screenshot showing the New Repository Secret form)*

---

## Part 4: Building the Cloud Computer

Now we press the magic button that builds a computer for you in the cloud.

1. Go back to the main page of your project (click the `< > Code` tab at the top left).
2. Click the big green **<> Code** button.
3. Switch to the **Codespaces** tab in the dropdown menu.
4. Click **Create codespace on main**.

A new tab will open in your browser, and you will see a computer screen starting up. Wait about 30-60 seconds for it to finish loading!

![Create Codespace Placeholder](https://docs.github.com/assets/cb-103133/mw-1440/images/help/codespaces/new-codespace-button.webp)
*(Teacher: Insert screenshot highlighting the Create Codespace button)*

---

## Part 5: The Boss Battle (Running your App!)

Because you set everything up perfectly, the magic happens automatically. 

1. Once the Codespace screen loads, look at the bottom window (the **Terminal**).
2. It is already doing work for you! It will download the tools and automatically start your Web App!
3. You will see a blue link that says something like `Local URL: http://localhost:8501`. 
4. **Hover your mouse** over that link, hold down the `Ctrl` key (or `Command` on Mac), and **click on it!**

![Clicking Local URL Placeholder](https://docs.github.com/assets/cb-102148/mw-1440/images/help/codespaces/forwarded-ports-link.webp)
*(Teacher: Insert screenshot showing the Streamlit running message and hovering over the link)*

A new tab will open, and you will see your Beautiful STEM Lab web app with a cool science watermark in the background!

### Test the Superpowers!

Your AI has special tools it can use! Try typing these into the chat:
* "Can you calculate 745 * 123 for me?" *(Watch it pull up the calculator!)*
* "Search Wikipedia for the history of the Apollo 11 mission." *(Watch it search the internet!)*
* "Who is the President?" *(Watch it wittily refuse because it's only allowed to talk about Science and Math!)*

**Congratulations! You are officially an AI Architect! 🎉**
