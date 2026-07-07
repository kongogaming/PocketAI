
# 📱 PocketAI

**A lightweight Python CLI that connects to a local Ollama server running on an Android phone (Termux) or a computer.**

[![Python](https://img.shields.io/badge/Python-3.13+-blue.svg?logo=python&logoColor=white)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/Version-v0.1.0-orange.svg)](#)

</div>

PocketAI lets you use a local Large Language Model (LLM) running on your own device without relying on cloud services. It communicates with Ollama through its REST API and provides a simple, clean command-line chat interface.

---

## ✨ Features

- 🤖 **Local AI Chat:** Converse with LLMs completely offline.
- 📱 **Termux Ready:** Works seamlessly with Ollama running on Android.
- 💻 **Clean Interface:** A minimal and easy-to-use command-line interface.
- 🔒 **Fully Private:** 100% local processing; your data never leaves your network.
- ⚡ **API Powered:** Communicates efficiently via the Ollama REST API.
- 🛠️ **Built-in Commands:** Use `/help` for guidance and `/bye` to exit securely.

---

## 📂 Project Structure

```text
PocketAI/
│
├── pocketai/
│   ├── ai.py
│   └── main.py
│
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
└── .gitattributes

```
## ⚙️ Requirements
### 💻 PC
 * **Python 3.13+**
 * **Git**
 * **Requests Library** (pip install requests)
### 📱 Phone
 * **Android Device**
 * **Termux**
 * **Ollama for Android** (via Termux)
## 🚀 Installing PocketAI (PC)
**1. Clone the repository**
```bash
git clone [https://github.com/kongogaming/PocketAI.git](https://github.com/kongogaming/PocketAI.git)
cd PocketAI

```
**2. Create a virtual environment**
```bash
python -m venv .venv

```
**3. Activate the virtual environment**
 * **Windows:**
   ```bash
   .venv\Scripts\activate
   
   ```
 * **Linux / macOS:**
   ```bash
   source .venv/bin/activate
   
   ```
**4. Install dependencies**
```bash
pip install -r requirements.txt

```
## 📱 Setting up Ollama on Android (Termux)
### 1. Install Termux
Download the latest version from the official GitHub release page or F-Droid.
### 2. Update packages
```bash
pkg update && pkg upgrade

```
### 3. Install Ollama
Follow the official Ollama Android/Termux installation instructions.
### 4. Download a model
For PocketAI v0.1.0, this project uses gemma3:270m by default:
```bash
ollama pull gemma3:270m

```
*(You can replace this with any Ollama-compatible model later).*
### 5. Allow network access
Start Ollama so other devices on your local Wi-Fi can connect to it.
```bash
export OLLAMA_HOST=0.0.0.0:11434
ollama serve

```
> ⚠️ **Note:** Leave this terminal running while you use PocketAI!
> 
### 6. Verify the Connection
**On the phone:**
```bash
curl [http://127.0.0.1:11434](http://127.0.0.1:11434)

```
**From your PC (Browser):**
Navigate to your phone's IP address on port 11434:
```text
http://PHONE_IP:11434
# Example: [http://192.168.29.142:11434](http://192.168.29.142:11434)

```
**Expected Output:** Ollama is running
## 🛠️ Configure PocketAI
Open the pocketai/ai.py file in your code editor and set your Ollama server URL to match your phone's IP address:
```python
# pocketai/ai.py
url = "http://YOUR_PHONE_IP:11434/api/generate"

# Example:
# url = "[http://192.168.29.142:11434/api/generate](http://192.168.29.142:11434/api/generate)"

```
## 🎮 Run PocketAI
Start the CLI application:
```bash
python pocketai/main.py

```
### 🖥️ Example Output
```text
=============================================
               POCKET AI
=============================================

Type /help for commands.

You > Hello
AI  > Hello! How can I help you today?

You > /help

Commands:
/help - Show available commands
/bye  - Exit PocketAI

You > /bye
AI  > Goodbye!

```
## ⌨️ Commands
| Command | Description |
|---|---|
| /help | Show available commands and help menu |
| /bye | Exit the PocketAI CLI |
## 🧠 Models
PocketAI works with **any** Ollama model.
 * **Current Default:** gemma3:270m
 * **Popular Alternatives:**
   * qwen2.5:3b
   * llama3.2
   * phi4-mini
Browse the Official Ollama Model Library for more options.
## 🔗 Ollama API
PocketAI communicates using the standard Ollama REST API.
 * **Example Endpoint:** POST /api/generate
 * **Documentation:** Ollama API Docs
## 🗺️ Roadmap
 * [x] Local AI chat
 * [x] Modular architecture
 * [x] GitHub release
 * [ ] Configuration file support
 * [ ] Streaming responses
 * [ ] Chat history memory
 * [ ] Model switching in CLI
 * [ ] Voice support
## 📄 License
This project is licensed under the **MIT License**. See the LICENSE file for more details.
## 👨‍💻 Author
**Somya Ranjan Pal (kongogaming)**
 * GitHub: @kongogaming
```

```
