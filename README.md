<div align="center">

# 🤖 PocketAI

### A lightweight, private, and beautiful local AI assistant powered by Ollama.

[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg?logo=python&logoColor=white)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-v0.5.1-orange.svg)](#)
[![Ollama](https://img.shields.io/badge/Ollama-Compatible-black?logo=ollama)](#)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20Android-blue)](#)
[![GitHub Repo](https://img.shields.io/badge/GitHub-PocketAI-black?logo=github)](https://github.com/kongogaming/PocketAI)

**PocketAI** is an elegant terminal-based AI assistant that connects to your local **Ollama** server.

Unlike cloud AI assistants, PocketAI keeps everything **offline**, **private**, and **under your control**. 

Whether your AI model runs on your desktop computer or on your Android phone through Termux, PocketAI provides the exact same seamless experience over your local network.

> ⚡ Fast • 🔒 Private • 🎨 Beautiful • 💻 Terminal First 

</div>

---

## ✨ Features

- 🤖 **Local AI chat** powered by Ollama
- ⚡ **Real-time streaming** responses
- 🧠 **Conversation memory**
- 💾 **Save** conversations
- 📚 **Browse** saved chat history
- 📂 **Load** previous conversations
- ✏️ **Rename** saved conversations
- 🗑️ **Delete** saved conversations
- 🎨 **Multiple beautiful themes**
- 📊 **Built-in response statistics**
- 🔍 **Search** within the current conversation
- 📤 **Export** conversations to Markdown
- 📄 **Export** conversations to Plain Text
- 📕 **Export** conversations to PDF
- 🔄 **Built-in update checker**
- 📦 **Model browser** & quick model switching
- ⚙️ **Interactive configuration** panel
- 📖 **Rich help menu**
- 🔒 **100% Local & Private**
- 📱 **Windows • Linux • Android Hybrid Support**

---

## 🌟 Why PocketAI?

PocketAI was built for developers, students, Linux users, and AI enthusiasts who love working inside the terminal. Instead of providing another heavy browser interface, PocketAI focuses on simplicity.

**Why choose PocketAI?**
- 🚀 Starts instantly
- 💻 Terminal-first workflow
- 🪶 Lightweight architecture
- 🔒 Completely offline
- 🎨 Beautiful Rich-powered UI
- 📂 Persistent conversation management
- ⚡ Extremely fast
- ❤️ Open Source

If you spend most of your time in the terminal, PocketAI feels like a natural AI companion.

---

## 📸 Preview

> 📸 Screenshots and demo GIFs will be added after the v0.5.2 release.

**Current UI includes:**
- Beautiful Rich dashboard
- Live streaming responses
- Theme system
- Model manager
- Statistics panel
- Search panel
- Export manager
- Conversation history

---

## 📂 Project Structure

```text
PocketAI/
│
├── pocketai/
│   ├── ai.py
│   ├── config.py
│   ├── exporter.py
│   ├── markdown.py
│   ├── models.py
│   ├── search.py
│   ├── storage.py
│   ├── theme.py
│   ├── ui.py
│   ├── updater.py
│   └── main.py
│
├── chats/
├── exports/
├── config.json
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore

```

---

## ⚙️ Requirements

### 💻 Desktop

* **Python 3.13+**
* **Git**
* **Requests & Rich Libraries**
* **Ollama** (Installed locally on your computer)

### 📱 Android (Hybrid Mode)

* **Android Device**
* **Termux** (via F-Droid or GitHub — *Do not use Google Play version*)
* **Ollama for Android** (Running inside Termux)

---

## 🚀 Installation

First, clone the repository and install the required Python dependencies on the machine where you will run the PocketAI interface:

```bash
git clone [https://github.com/kongogaming/PocketAI.git](https://github.com/kongogaming/PocketAI.git)
cd PocketAI
pip install -r requirements.txt

```

Next, choose **one of the two** methods below to host your AI model.

---

## 💻 Method 1 — Run on Your Computer (Recommended)

*Use this method if you want your PC's hardware to handle the AI processing.*

1. **Install Ollama:** Download from [ollama.com/download](https://ollama.com/download).
2. **Download a Model:**
```bash
ollama pull qwen2.5:1.5b

```


3. **Start Ollama:**
```bash
ollama serve

```


4. **Run PocketAI:** Open a new terminal in the PocketAI folder and launch:
```bash
python pocketai/main.py

```



---

## 📱 Method 2 — Android Hybrid Mode (Termux)

*Use this method if you want your phone to run the AI, and connect to it from your PC over Wi-Fi.*

1. **Install Termux:** Download the latest APK from [F-Droid (Recommended)](https://f-droid.org/en/packages/com.termux/) or the [Termux GitHub Releases](https://www.google.com/search?q=https://github.com/termux/termux-app/releases/latest).
> ⚠️ **Important:** Do *not* download Termux from the Google Play Store, as that version is deprecated and broken.


2. **Update Packages:**
```bash
pkg update && pkg upgrade

```


3. **Install Ollama & Download a Model:** Follow standard Termux instructions for Ollama, then run:
```bash
ollama pull gemma3:270m

```


4. **Expose Ollama to your Local Network:**
```bash
export OLLAMA_HOST=0.0.0.0:11434
ollama serve

```


> ⚠️ *Leave this Termux session running!*


5. **Find your Phone's IP Address:** (e.g., `192.168.29.142`)
6. **Update `config.json`:** On your PC, open the config file in the PocketAI folder and point it to your phone's IP:
```json
{
    "url": "[http://192.168.29.142:11434/api/chat](http://192.168.29.142:11434/api/chat)",
    "model": "gemma3:270m"
}

```


7. **Run PocketAI:** Launch the app on your PC:
```bash
python pocketai/main.py

```



---

## 🎮 Commands

PocketAI comes with a rich set of built-in commands to manage your experience directly from the chat prompt.

| Command | Description |
| --- | --- |
| `/help` | Show help menu |
| `/about` | About PocketAI |
| `/config` | View current configuration |
| `/theme` | Browse available themes |
| `/theme <name>` | Change theme |
| `/models` | List installed Ollama models |
| `/model` | Show current model |
| `/model <name>` | Switch model |
| `/save` | Save conversation |
| `/history` | Browse saved chats |
| `/load <id>` | Load conversation |
| `/rename <id> <title>` | Rename conversation |
| `/delete <id>` | Delete conversation |
| `/search <text>` | Search current conversation |
| `/export md` | Export as Markdown |
| `/export txt` | Export as Text |
| `/export pdf` | Export as PDF |
| `/update` | Check for updates |
| `/stats` | Show statistics status |
| `/stats on` | Enable statistics |
| `/stats off` | Disable statistics |
| `/reset` | Clear conversation |
| `/clear` | Clear terminal |
| `/version` | Show PocketAI version |
| `/bye` | Exit PocketAI |

---

## 🧩 Supported Models

PocketAI works with any Ollama-compatible model.

**Recommended:**

* ⭐ `qwen2.5:1.5b`
* ⭐ `qwen2.5:3b`
* ⭐ `qwen3:4b`
* ⭐ `gemma3:1b`
* `gemma3:270m`
* `llama3.2`
* `phi4-mini`
* `deepseek-r1`
* `mistral`
* `tinyllama`

---

## 🗺️ Roadmap

### ✅ v0.1

* [x] Local AI Chat
* [x] Streaming Responses

### ✅ v0.2

* [x] Configuration System
* [x] Rich Terminal UI
* [x] Statistics

### ✅ v0.3

* [x] Conversation Memory
* [x] Better CLI Experience

### ✅ v0.4

* [x] Theme System
* [x] Save & Load Conversations
* [x] History Management
* [x] Dashboard Improvements

### ✅ v0.5.1

* [x] Search Conversations
* [x] Markdown Export
* [x] TXT Export
* [x] PDF Export
* [x] Update Checker
* [x] Model Manager Improvements
* [x] UI Polish
* [x] Better Help System
* [x] Better Search UI

### 🚀 Planned for v0.5.2

* [ ] First Launch Setup Wizard
* [ ] Automatic Configuration Creation
* [ ] Automatic Ollama Detection
* [ ] Automatic Model Detection
* [ ] Better EXE Distribution

### 🌟 Planned for v0.6

* [ ] GitHub Release Checker
* [ ] Automatic Updater
* [ ] Voice Input
* [ ] Text-to-Speech
* [ ] Chat With Documents (RAG)
* [ ] Plugin System
* [ ] Image Generation Support
* [ ] Better Markdown Renderer

---

## ❤️ Built With

PocketAI is powered by amazing open-source projects. Huge thanks to their maintainers:

* [Python](https://www.python.org/)
* [Ollama](https://ollama.com/)
* [Rich](https://github.com/Textualize/rich)
* [Requests](https://requests.readthedocs.io/)

---

## 🤝 Contributing

Contributions are always welcome! Feel free to:

* Fork the repository
* Improve the code
* Suggest features
* Report bugs
* Open Pull Requests

---

## 📄 License

Licensed under the **MIT License**. See the `LICENSE` file for details.

---

## 👨‍💻 Author

**Somya Ranjan Pal**

* **GitHub:** [@kongogaming](https://github.com/kongogaming)
* **Repository:** [PocketAI](https://github.com/kongogaming/PocketAI)

---

### ⭐ If you like PocketAI, consider giving the repository a star!

Made with ❤️ using Python, Rich, and Ollama.