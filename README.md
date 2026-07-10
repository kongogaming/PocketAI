<div align="center">

# 📱 PocketAI

**A lightweight, private, and fast local AI assistant powered by Ollama.**

[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg?logo=python&logoColor=white)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/Version-v0.3.0-orange.svg)](#)
[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/kongogaming/PocketAI.git)

**PocketAI** is a lightweight Python CLI that connects to a local Ollama server. Unlike cloud AI assistants, PocketAI keeps everything **private, offline, and 100% under your control.** *The best part? It's Hybrid.* Whether you want to run your AI model directly on your Windows PC or offload it to your Android phone via Termux, PocketAI connects seamlessly over your local network.

</div>

---

## ✨ Features

- 🤖 **Local AI Chat:** Converse with LLMs completely offline.
- 🔄 **Hybrid Ecosystem:** Run models on your PC (Windows/Linux/Mac) OR your phone (Android/Termux).
- ⚡ **Real-time Streaming:** Fast, typewriter-style responses.
- 🧠 **Conversation Memory:** Maintains chat context naturally via the Ollama Chat API.
- 📊 **Response Statistics:** Track prompt evaluation and token generation speeds.
- 🎨 **Beautiful CLI:** A clean, minimal, and responsive terminal UI.
- 🔒 **100% Private:** Your data never leaves your device or local network.

---

## 📸 Media & Demos

> **Note:** Screenshots and video demonstrations will be added after the **v1.0** release! Stay tuned. 🚀

---

## 📂 Project Structure

```text
PocketAI/
│
├── pocketai/
│   ├── ai.py
│   ├── config.py
│   └── main.py
│
├── config.json
├── README.md
├── LICENSE
├── requirements.txt
└── .gitignore

```

---

## ⚙️ Requirements

### 💻 For PC Setup

* **Python 3.13+**
* **Git**
* **Requests Library** (`pip install -r requirements.txt`)
* **Ollama** (Installed locally on your computer)

### 📱 For Android Setup (Hybrid)

* **Android Device**
* **Termux** (via F-Droid or GitHub)
* **Ollama for Android** (via Termux)

---

## 🚀 Installation & Setup

First, clone the repository and install the required Python dependencies on the machine where you will run the CLI:

```bash
git clone [https://github.com/kongogaming/PocketAI.git](https://github.com/kongogaming/PocketAI.git)
cd PocketAI
pip install -r requirements.txt

```

Next, choose **one of the two** methods below to host your AI model.

### Method 1: Run Entirely on Windows / PC (Recommended)

*Use this method if you want your PC's hardware to handle the AI processing.*

1. **Install Ollama:** Download and install Ollama from [ollama.com/download](https://ollama.com/download).
2. **Pull a Model:** Open your terminal and download a model (e.g., Qwen 2.5):
```bash
ollama pull qwen2.5:1.5b

```


3. **Start the Server:** ```bash
ollama serve
```
*(By default, Ollama connects to `http://localhost:11434`)*

```


4. **Run PocketAI:** Open a new terminal in the PocketAI folder and run:
```bash
python pocketai/main.py

```



### Method 2: Run via Android / Termux (Hybrid Mode)

*Use this method if you want your phone to run the AI, and connect to it from your PC (or run it straight on the phone).*

1. **Install Termux:** Download from [F-Droid](https://f-droid.org/) or [GitHub Releases](https://github.com/termux/termux-app/releases) (Do not use the Google Play Store version).
2. **Update Packages:**
```bash
pkg update && pkg upgrade

```


3. **Install Ollama:** Follow the official Ollama Termux installation instructions.
4. **Pull a Model:**
```bash
ollama pull gemma3:270m

```


5. **Allow LAN Connections & Start Server:**
This step exposes Ollama so your PC can connect to your phone over Wi-Fi.
```bash
export OLLAMA_HOST=0.0.0.0:11434
ollama serve

```


> ⚠️ **Note:** Leave this Termux session running!


6. **Find your Phone's IP Address:** (e.g., `192.168.29.142`)
7. **Update Configuration:** Open `config.json` in your PocketAI folder and update the URL:
```json
{
    "url": "[http://192.168.29.142:11434/api/chat](http://192.168.29.142:11434/api/chat)",
    "model": "gemma3:270m"
}

```


8. **Run PocketAI:** On your PC, launch the CLI:
```bash
python pocketai/main.py

```



---

## 🎮 Commands

Once you are in the PocketAI interface, you can use the following commands:

| Command | Description |
| --- | --- |
| `/help` | Show available commands and help menu |
| `/about` | View details about PocketAI |
| `/config` | View your current configuration settings |
| `/stats on` | Enable response statistics (speed, tokens) |
| `/stats off` | Disable response statistics |
| `/clear` | Clear the terminal screen |
| `/reset` | Reset the conversation memory |
| `/bye` | Exit the PocketAI CLI |

---

## 🧩 Supported Models

PocketAI works with **any** Ollama-compatible model. Just ensure you update your `config.json` to match the model you pulled.

**Popular Choices:**

* `qwen2.5:1.5b` ⭐ *(Great balance of speed and logic)*
* `gemma3:270m` *(Ultra-lightweight, perfect for older phones)*
* `llama3.2`
* `phi4-mini`
* `deepseek-r1`

---

## 🗺️ Roadmap

**✅ Completed**

* [x] Local AI Chat & Streaming responses
* [x] Conversation memory via Chat API
* [x] Configuration system (`config.json`)
* [x] Response statistics & Help system
* [x] Beautiful CLI interface

**🚧 Coming Soon**

* [ ] Theme support
* [ ] Chat history viewer & Save conversations
* [ ] Export chats to file
* [ ] Model switching directly in CLI
* [ ] Plugin support
* [ ] Voice interaction

---

## 🤝 Contributing

Contributions, ideas, and feature requests are always welcome!
Feel free to fork the repository and submit a Pull Request.

---

## 📄 License

This project is licensed under the **MIT License**. See the `LICENSE` file for more details.

---

## 👨‍💻 Author

**Somya Ranjan Pal**

* GitHub: [@kongogaming](https://www.google.com/search?q=https://github.com/kongogaming)
* Repository: [PocketAI](https://github.com/kongogaming/PocketAI.git)