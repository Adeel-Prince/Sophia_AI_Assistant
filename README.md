# Sophia: Hybrid AI Desktop Assistant & OS Automation Engine 🚀🤖🧠

Welcome to the repository for **Sophia**! This project is an advanced, hybrid desktop AI assistant that bridges a high-performance Python system automation backend with a responsive, client-side web application interface. Sophia acts as an autonomous cockpit capable of processing natural language inputs, interfacing with remote large language models (LLMs), executing local operating system micro-tasks, and orchestrating communication routing hooks.

---

## 📂 System Architecture & Directory Map

The application splits computational automation scripts from presentation components and local persistent databases:

```text
Sophia/
├── .venv-1/                  # Local python runtime execution sandbox environment
├── engine/                   # Core Backend Processing Micro-Services
│   ├── __pycache__/          # Compiled python runtime optimization blocks
│   ├── command.py            # Natural Language Processing (NLP) pattern matchers
│   ├── config.py             # System keys & API cluster environment anchors
│   ├── db.py                 # Structured query layouts mapping to local SQLite channels
│   └── features.py           # Core execution actions (OS automation, calling arrays)
├── envSophia/                # Alternative execution configuration sandbox
├── www/                      # Frontend Desktop Presentation Interface
│   ├── assets/               # User interface graphics, iconography, and styling images
│   ├── controller.js         # Bidirectional message bridge to python execution core
│   ├── index.html            # Main viewport UI skeletal wrapper
│   ├── main.js               # Reactive DOM click configurations and listeners
│   └── style.css             # Personalized interface layout themes via Bootstrap v5
├── main.py                   # Central multi-threaded system coordinator entry script
├── sophia.db                 # Local persistent relational SQLite data container
└── .gitignore                # Outermost repository safety and security barrier
```

---

## 🛠️ Tech Stack & Automation Architecture

### 📱 1. Core Automation & Language Engineering (Python Backend)
* **Intelligence Layer:** **Hugging Face Inference API** providing cloud-native deep learning pipelines for context-aware conversational text responses.
* **System Automation Utilities:** Custom automation components interacting directly with the OS kernel to open target desktop applications and launch specialized browser nodes.
* **Communications Routing:** Integrated web-automation scripting enabling automated WhatsApp messaging and phone call handshakes.
* **Local Data Persistence:** **SQLite Database** processing structural query parameters for user tracking, action histories, and config records.

### 🎨 2. User Interface Infrastructure (Web Client)
* **Structural Architecture:** HTML5, CSS3, and JavaScript (Vanilla ES6 modules).
* **Styling Framework:** **Bootstrap v5** supplying a clean, dark-themed responsive dashboard layout.
* **Execution Interface:** Asynchronous JavaScript events monitoring user interaction nodes and marshaling prompt packets down to the Python kernel.

---

## 🏃‍♂️ Local Installation and System Execution

Ensure you have Python 3.10+ installed on your computer before firing up the assistant:

### 1. Clone the Source Repository
```bash
git clone https://github.com
cd Sophia
```

### 2. Configure Your Environment Variables
Create a local `.env` file within the root project workspace folder to anchor your Hugging Face access credentials securely:
```env
HUGGINGFACE_API_KEY="hf_your_secret_inference_token_hash"
```

### 3. Establish and Activate a Virtual Environment
```bash
# Generate a clean system sandbox container
python -m venv envSophia

# Activate the sandbox (Windows)
sysenv\Scripts\activate
# Activate the sandbox (Mac/Linux)
source envSophia/bin/activate
```

### 4. Install Application Dependency Modules
```bash
pip install -r requirements.txt
```
*(Make sure your `requirements.txt` file lists python libraries such as `requests`, `pyttsx3`, `speech_recognition`, etc.)*

### 5. Launch Sophia
Execute the central entry script to fire up the system loop:
```bash
python main.py
```
*The interactive assistant dashboard will slide up live on your desktop monitor!*

---

## 🛡️ Applied Engineering Best Practices
* **Multi-Threaded Architecture:** System scripts isolate UI rendering logic from long-running API fetches to prevent application freezes during query processing.
* **Decoupled System Boundaries:** OS automation scripts are kept separate from frontend display modules via explicit messaging controllers.
* **Insulated API Topologies:** Access tokens and system database schemas are hidden from code streams to protect private profiles from leak vectors.

## 📄 License
This application is open-source and available under the [MIT License](LICENSE).
