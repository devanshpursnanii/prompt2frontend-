# 🎨 Prompt2Frontend - AI-Powered Web App Generator

Transform your ideas into complete, production-ready web applications with just a simple text prompt! **Prompt2Frontend** is an intelligent multi-agent system built with [LangGraph](https://github.com/langchain-ai/langgraph) that acts as your personal development team, generating fully functional web apps with HTML, CSS, and JavaScript.

---

## ✨ Features

- 🤖 **Multi-Agent Architecture** - Three specialized AI agents work together to plan, architect, and code your project
- 🎯 **Complete Code Generation** - Generates ALL necessary files (HTML, CSS, JavaScript) with no placeholders
- 💾 **Automatic File Management** - Creates project structure and writes files automatically
- 🎨 **Modern, Beautiful Design** - Generates polished, colorful, production-ready interfaces
- 🔄 **Iterative Development** - Each agent passes context to the next for coherent implementation

---

## 🏗️ Architecture

### Three-Agent System:

1. **Planner Agent** 📋
   - Analyzes your natural language request
   - Creates a complete project specification
   - Lists ALL required files with their purposes

2. **Architect Agent** 🏛️
   - Breaks down the plan into implementation tasks
   - Specifies exact functionality for each file
   - Ensures proper integration between components

3. **Coder Agent** 👨‍💻
   - Implements each file with complete code
   - Uses tools to read/write files like a real developer
   - Produces production-ready, fully functional code

<div style="text-align: center;">
    <img src="resources/coder_buddy_diagram.mmd" alt="Agent Architecture" width="90%"/>
</div>

---

## 🛠️ Tech Stack

### Core Technologies:
- **Python 3.11+** - Main programming language
- **LangChain** - LLM framework for agent orchestration
- **LangGraph** - State machine and workflow management
- **Groq API** - Fast LLM inference (using openai/gpt-oss-120b model)
- **Pydantic** - Data validation and structured outputs

### Dependencies:
- `langchain` - LLM application framework
- `langchain-groq` - Groq integration for LangChain
- `langgraph` - Graph-based agent workflows
- `python-dotenv` - Environment variable management
- `pydantic` - Type-safe data structures

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.11 or higher**
- **Groq API Key** - Get yours at [Groq Console](https://console.groq.com/keys)
- **pip or uv** package manager

### 📦 Installation

#### Option 1: Using pip (Recommended)

```bash
# Clone the repository
git clone https://github.com/devanshpursnanii/prompt2frontend.git
cd prompt2frontend

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .sample_env .env
# Edit .env and add your GROQ_API_KEY
```

#### Option 2: Using uv

```bash
# Clone the repository
git clone https://github.com/devanshpursnanii/prompt2frontend.git
cd prompt2frontend

# Create virtual environment
uv venv
source .venv/bin/activate

# Install dependencies
uv pip install -r pyproject.toml

# Set up environment variables
cp .sample_env .env
# Edit .env and add your GROQ_API_KEY
```

### 🔑 Environment Setup

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

## 🎮 Usage

### Running the Generator

```bash
python3 main.py
```

You'll be prompted to enter your project description. The system will then:
1. 📋 Plan the complete project structure
2. 🏛️ Break it down into implementation tasks
3. 👨‍💻 Generate all files with complete code
4. 💾 Save everything to `generated_project/` directory

### 💡 Example Prompts

**Web Applications:**
```
"Build a colorful modern todo app in HTML, CSS, and JavaScript"
"Create a simple calculator web application with a modern design"
"Make a weather dashboard with dark mode"
"Build a pomodoro timer with notifications"
```

**Interactive Features:**
```
"Create a quiz app with multiple choice questions and score tracking"
"Build an expense tracker with charts"
"Make a markdown previewer"
```

### 📂 Output Structure

```
generated_project/
├── index.html      # Main HTML structure
├── style.css       # Complete styling
└── app.js          # Full JavaScript functionality
```

---

## 🎯 Key Improvements

This version includes critical enhancements:

✅ **Complete File Generation** - Ensures ALL files (especially JavaScript) are created  
✅ **No Placeholders** - Generates fully implemented, production-ready code  
✅ **Better Prompts** - Enhanced instructions for each agent  
✅ **Context Flow** - Agents share project details for coherent implementation  
✅ **Explicit Requirements** - Forces generation of HTML + CSS + JavaScript for web apps  

---

## 📁 Project Structure

```
prompt2frontend/
├── main.py                 # Entry point
├── requirements.txt        # Python dependencies
├── pyproject.toml          # Alternative dependency file
├── .env                    # Environment variables (create this)
├── .sample_env             # Environment template
├── agent/
│   ├── __init__.py
│   ├── graph.py           # Agent workflow orchestration
│   ├── prompts.py         # Enhanced agent prompts
│   ├── states.py          # Pydantic state models
│   └── tools.py           # File I/O tools
├── demo_todo/             # Example generated app
├── resources/             # Documentation assets
└── generated_project/     # Your generated apps appear here
```

---

## 🐛 Troubleshooting

**Issue: Python command not found**
```bash
# Use python3 instead
python3 main.py
```

**Issue: Missing GROQ_API_KEY**
```bash
# Make sure .env file exists with your API key
echo "GROQ_API_KEY=your_key_here" > .env
```

**Issue: Module not found errors**
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

---

## 📄 License

This project is open source and available under the MIT License.

---

## 🙏 Acknowledgments

- Built with [LangChain](https://github.com/langchain-ai/langchain) and [LangGraph](https://github.com/langchain-ai/langgraph)
- Powered by [Groq](https://groq.com/) for fast LLM inference
- Inspired by modern AI-assisted development workflows

---

## 📧 Contact

**Devansh Pursnani**  
GitHub: [@devanshpursnanii](https://github.com/devanshpursnanii)

---

**⭐ Star this repo if you find it helpful!**
