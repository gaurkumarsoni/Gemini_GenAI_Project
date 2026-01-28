

# 📌 GemTalk – All-in-One Generative AI Streamlit App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://gemtalk.streamlit.app/)

**GemTalk** is a Next-Gen AI web app built with **Streamlit** and powered by **Google Gemini models**. It brings together multiple AI capabilities — conversational chatbot, image captioning, semantic text embeddings, and an ask-anything assistant — into a simple, interactive interface.

👉 Try it live: **[https://gemtalk.streamlit.app/](https://gemtalk.streamlit.app/)**

---

## 🧠 🚀 Features

GemTalk combines powerful AI features in one interface:

* **🤖 Chatbot Conversation** – Chat naturally with Gemini-powered AI
* **🖼️ Image Captioning** – Upload images and generate contextual captions
* **📌 Text Embedding** – Generate semantic embeddings for text
* **❓ Ask Me Anything (Q&A)** – Ask questions and get accurate AI responses
* **💬 Multi-modal Support** – Works on both text and image inputs

This makes the app useful for demos, exploration, prototyping, or learning generative AI workflows.

---

## ⚙️ Technology Stack

| Part               | Technology                                          |
| ------------------ | --------------------------------------------------- |
| UI/Frontend        | **Streamlit**                                       |
| AI Backend         | **Google Gemini models (Gemini API)**               |
| Deployment         | **Streamlit Community Cloud**                       |
| API Key Management | **Environment Variables / `.env` and `st.secrets`** |

---

## 🛠️ Getting Started (Run Locally)

### 1. Clone the Repository

```bash
git clone https://github.com/gaurkumarsoni/Gemini_GenAI_Project.git
cd Gemini_GenAI_Project
```

---

### 2. Create Virtual Environment (Optional)

```bash
python -m venv venv
# Activate on macOS/Linux:
source venv/bin/activate
# Or on Windows:
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_google_gemini_api_key_here
```

⚠️ Make sure `.env` is in `.gitignore` so your key does **not** get committed.

---

### 5. Run the App

```bash
streamlit run main.py
```

This will start the app on `localhost:8501`.

---

## 🧩 Usage

Once running:

* Enter text in the Chat interface to talk with the AI.
* Upload images to get auto-generated captions.
* Use the “Ask Anything” tab to get instant, generative answers.
* Generate text embeddings for semantic search or analysis.

---

## 🚀 Deployment

The app is deployed on **Streamlit Community Cloud**.
To get a similar deployment:

1. Push your commits to GitHub.
2. Connect your GitHub repository to **Streamlit Community Cloud**.
3. Add your `GEMINI_API_KEY` in **Streamlit Secrets**.
4. Streamlit will auto-deploy every push to the `main` branch. ([Streamlit Docs][1])

---

## 📁 Project Structure

```
Gemini_GenAI_Project/
├── main.py
├── gemini_utility.py
├── requirements.txt
├── .gitignore
├── README.md
└── .env.example
```

---

## 🛡️ Secure API Key Handling

* Use `st.secrets` for deployment.
* Use `.env` and **python-dotenv** locally.
* Never commit API keys to GitHub.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to fork the project and submit a pull request.

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for details.

---

## 🔗 Links

* Live App: [https://gemtalk.streamlit.app/](https://gemtalk.streamlit.app/)
* Repo: [https://github.com/gaurkumarsoni/Gemini_GenAI_Project.git](https://github.com/gaurkumarsoni/Gemini_GenAI_Project.git)

---

## 🌟 Support / Star & Fork

If you like **GemTalk**, please give it a ⭐ on GitHub and feel free to **fork** the repository to experiment, improve, or add new features.  

Your support helps keep the project growing! 🙌

- ⭐ Star: [https://github.com/gaurkumarsoni/Gemini_GenAI_Project](https://github.com/gaurkumarsoni/Gemini_GenAI_Project)  
- 🍴 Fork: [https://github.com/gaurkumarsoni/Gemini_GenAI_Project/fork](https://github.com/gaurkumarsoni/Gemini_GenAI_Project/fork)
