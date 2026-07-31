# AI Agent

A production-style conversational AI agent built using Python, LangChain and Ollama.

The project focuses on software engineering principles while implementing an AI assistant with memory and tool calling.

---

## Features

- Tool Calling
- Conversation Memory
- Summary Memory
- Persistent JSON Memory
- Session-based Memory
- Repository Pattern
- Dependency Injection
- Tool Registry
- Modular Prompt Management

---

## Technologies

- Python
- LangChain
- Ollama
- JSON Storage

---

## Project Structure

```

01-ai-agent/
│
├── memory/
├── prompts/
├── tools/
│
├── agent.py
├── config.py
├── interfaces.py
├── main.py
├── memory.py
├── repository.py
├── tool_registry.py

```

---

## Architecture

```

User
│
▼
Agent
│
├───────────────┐
▼               ▼
Memory      Tool Registry
│               │
▼               ▼
Repository     Tools
│
▼
JSON Storage

```

---

## Current Features

- Multi-turn conversation
- Tool execution
- Session-based memory
- Incremental conversation summary
- Modular architecture

---

## Future Improvements

- RAG Integration
- Vector Database
- Streaming Responses
- FastAPI API
- PostgreSQL Memory
- Redis Cache

---

## Run Locally

### Clone the repository

```bash
git clone <your-repo-url>
```

### Navigate to the project

```bash
cd building-ai-agents/01-ai-agent
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Start Ollama

```bash
ollama serve
```

Pull the model

```bash
ollama pull qwen3:4b
```

### Run

```bash
python main.py
```

---

## Learning Objectives

This project was created to understand:

- AI Agent Architecture
- Memory Systems
- LangChain
- Tool Calling
- Software Design Patterns
- Prompt Engineering