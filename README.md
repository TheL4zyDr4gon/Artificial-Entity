## 🧠 Ollama Requirements

Artificial Entity uses [Ollama](https://ollama.com/) to run AI models locally on your computer. This allows your artificial entity to generate conversations without relying on a paid cloud AI service.

### Prerequisites

Before running Artificial Entity, you'll need:

- **Python 3.10 or newer**
- **Ollama** installed and running
- An Ollama-compatible language model
- Enough available RAM and storage for your chosen model

### Installation

**Step 1: Install Ollama**

Download and install Ollama from:

https://ollama.com/download

**Step 2: Download the AI model**

Open your terminal or PowerShell and run:

```bash
ollama pull llama3.2:3b
```

This downloads the default AI model used by Artificial Entity.

**Step 3: Verify Ollama**

Run:

```bash
ollama list
```

You should see `llama3.2:3b` listed among your installed models.

**Step 4: Start Artificial Entity**

Follow the project's installation instructions and launch Artificial Entity.

On your first launch, the setup wizard will guide you through naming your AI, customizing its personality, choosing a communication style, and enabling memory.

### Privacy

Artificial Entity is designed to run locally using Ollama. Conversations and memories can remain on your computer without being sent to a cloud AI provider.

Internet access may be required to download Ollama, AI models, and project updates.
