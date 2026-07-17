<div align="center">

# 🤖 PocketAI

### A lightweight, private, and beautiful local AI assistant powered by Ollama.

[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg?logo=python&logoColor=white)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-v0.6-orange.svg)](#)
[![Ollama](https://img.shields.io/badge/Ollama-Compatible-black?logo=ollama)](#)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20Android-blue)](#)

[![GitHub Repo](https://img.shields.io/badge/GitHub-PocketAI-black?logo=github)](https://github.com/kongogaming/PocketAI)
[![GitHub release](https://img.shields.io/github/v/release/kongogaming/PocketAI?color=blue)](https://github.com/kongogaming/PocketAI/releases)
[![GitHub stars](https://img.shields.io/github/stars/kongogaming/PocketAI?style=social)](https://github.com/kongogaming/PocketAI/stargazers)

**PocketAI** is an elegant terminal-based AI assistant that connects to your local **Ollama** server.

Unlike cloud AI assistants, PocketAI keeps everything **offline**, **private**, and **under your control**. 

Whether your AI model runs on your desktop computer or on your Android phone through Termux, PocketAI provides the exact same seamless experience over your local network.

> ⚡ Fast • 🔒 Private • 🎨 Beautiful • 💻 Terminal First 

</div>

---

## ✨ Features

- 🤖 **Local AI chat** powered by Ollama
- 🚀 **First-Run Setup Wizard**
- 🤖 **Automatic Ollama Detection**
- 📦 **Automatic Model Detection**
- ⚙️ **Automatic Configuration Creation**
- 🖥️ **EXE Ready** (No manual config required)
- 🛡️ **Graceful Ctrl+C Exit Confirmation**
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
- 📤 **Export** conversations to Markdown, Plain Text, or PDF
- 🔄 **Built-in update checker**
- 📦 **Model browser** & quick model switching
- 📖 **Rich help menu**
- 🔒 **100% Local & Private**
- 📱 **Windows • Linux • Android Hybrid Support**

---

## 🏆 Feature Comparison

| Feature | PocketAI | ChatGPT Web | Local AI Web UIs |
|---------|:---:|:---:|:---:|
| **Offline processing** | ✅ | ❌ | ✅ |
| **Rich Terminal UI** | ✅ | ❌ | ❌ |
| **Zero Setup (EXE)** | ✅ | ✅ | ❌ |
| **Android (Termux) Ready**| ✅ | ❌ | ❌ |
| **Open Source** | ✅ | ❌ | ✅ |
| **Document Chat (RAG)** | *v0.6* | ✅ | ⚠️ *(Varies)* |

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

> 📸 Screenshots and demo GIFs will be added soon.

**Current UI includes:**
- 🚀 First-Run Setup Wizard
- 🎨 Rich Dashboard
- 📦 Model Manager
- 🔍 Conversation Search
- 📤 Export Manager
- 📚 Conversation History
- ⚙️ Theme System

---

## 🏗️ Architecture

PocketAI acts as a lightweight, blazing-fast bridge between your terminal and your local LLMs.

```text
       You (Terminal)
             │
             ▼
       PocketAI CLI
             │
             ├──────────────────┐ (Hybrid Mode)
             ▼                  ▼
      Local PC Ollama    Android (Termux) Ollama
             │                  │
             └────────┬─────────┘
                      ▼
               Local AI Models

```

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
│   ├── setup.py
│   ├── setup_ui.py
│   ├── storage.py
│   ├── theme.py
│   ├── ui.py
│   ├── updater.py
│   └── main.py
│
├── chats/
├── exports/
├── PocketAI.spec
├── requirements.txt
├── README.md
└── LICENSE

```

---

## ⚙️ Requirements & Tested Platforms

### 💻 Desktop

* **Tested On:** Windows 11 ✅ | Ubuntu 24.04 ✅
* **Python 3.13+**
* **Git**
* **Requests & Rich Libraries**
* **Ollama** (Installed locally on your computer)

### 📱 Android (Hybrid Mode)

* **Tested On:** Android 13/14 (Termux) ✅
* **Android Device**
* **Termux** (via F-Droid or GitHub — *Do not use Google Play version*)
* **Ollama for Android** (Running inside Termux)

---

## 📥 Download

The easiest way to get started with PocketAI is by downloading the latest release from the [GitHub Releases](https://www.google.com/url?sa=E&source=gmail&q=https://github.com/kongogaming/PocketAI/releases) page.

### 🪟 Windows

#### Option 1 — Standalone EXE (Recommended)

1. Download `PocketAI.exe` from the latest release.
2. Double-click `PocketAI.exe`.
3. Complete the first-run setup wizard.
4. Start chatting with your local AI.

#### Option 2 — ZIP Package

1. Download the Windows ZIP package.
2. Extract it to any folder.
3. Run `PocketAI.exe`.
4. Complete the first-run setup wizard.

> **Note:** Ollama must already be installed and running with at least one model.

---

## 🛠️ Build from Source

Developers who want to build PocketAI from source can clone the repository and install the required dependencies:

```bash
git clone [https://github.com/kongogaming/PocketAI.git](https://github.com/kongogaming/PocketAI.git)
cd PocketAI
pip install -r requirements.txt

```

Next, choose **one of the two** methods below to host your AI model.

---

### 💻 Method 1 — Run on Your Computer (Recommended)

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



---

### 📱 Method 2 — Android Hybrid Mode (Termux)

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


5. **Find your Phone's IP Address:** Take note of your phone's local IP (e.g., `192.168.29.142`).

---

## 🏁 Run PocketAI

If you built from source, launch the app on your PC from the PocketAI folder:

```bash
python pocketai/main.py

```

### 🚀 First Launch

PocketAI automatically detects whether a configuration exists. **No manual config editing is required.**

On first launch, the interactive setup wizard will:

1. Connect to your Ollama server (or prompt for your phone's IP if using Hybrid Mode).
2. Detect installed models.
3. Recommend the best model.
4. Generate your configuration file automatically.
5. Launch the PocketAI dashboard.

### ⚙️ Configuration Example

If you ever need to manually inspect the `config.json` that the wizard generates, it looks like this:

```json
{
  "url": "[http://127.0.0.1:11434/api/chat](http://127.0.0.1:11434/api/chat)",
  "model": "qwen2.5:1.5b",
  "theme": "monokai",
  "stats": true
}

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

## 🛠️ Troubleshooting

### Ollama isn't detected

Make sure the server is actively running. Open a new terminal window and run:

```bash
ollama serve

```

### No models found during Setup

You need to pull at least one model before PocketAI can use it. Run:

```bash
ollama pull qwen2.5:1.5b

```

### Connection Refused (Hybrid Mode)

If connecting from your PC to your Android phone fails, ensure your phone is broadcasting on `0.0.0.0` by running `export OLLAMA_HOST=0.0.0.0:11434` inside Termux before starting the server.

---

## ❓ FAQ

**Does PocketAI require the Internet?**
No, 100% of the processing happens locally on your machine once your models are downloaded.

**Can I use it with any Ollama model?**
Yes. As long as Ollama supports it, PocketAI can chat with it.

**Does it work on Android?**
Yes, using the Termux method outlined in the installation instructions.

---

## ⚠️ Known Limitations

* Internet web search is not currently supported.
* Requires an active Ollama server to function.
* Document RAG functionality is not yet available (Planned for v0.6).

---

## 🗺️ Roadmap

### ✅ v0.1 - v0.4

* Local AI Chat & Streaming Responses
* Configuration & Theme Systems
* Rich Terminal UI & Statistics
* Conversation Memory, Save & Load
* History Management & Dashboard Improvements

### ✅ v0.5.1

* Search Conversations
* Markdown, TXT, and PDF Export
* Update Checker
* Model Manager Improvements
* UI Polish & Better Help System

### ✅ v0.5.2

* [x] First-Run Setup Wizard
* [x] Automatic Ollama Detection
* [x] Automatic Model Detection
* [x] Automatic Configuration Creation
* [x] Better EXE Distribution
* [x] Graceful Ctrl+C Exit Confirmation
* [x] Setup Wizard UI Polish

### 🚀 Planned for v0.6

* [ ] Automatic Self-Updater
* [ ] GitHub Release Installer
* [ ] Voice Input
* [ ] Text-to-Speech
* [ ] Chat With Documents (RAG)
* [ ] Image Understanding
* [ ] Plugin System
* [ ] Performance Improvements

---

## ❤️ Acknowledgements & Built With

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