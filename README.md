# PicoAgents Multi-Agent Collaboration (Paico Multi Agent)

This project demonstrates a multi-agent collaboration system built using the [picoagents](https://github.com/microsoft/picoagents) library. It establishes a round-robin communication channel between a **Poet Agent** and a **Critic Agent** to collaboratively write and refine haikus.

## Project Structure

```
├── README.md              # Project documentation
├── pyproject.toml         # Python dependency configuration
├── uv.lock                # UV lockfile for deterministic dependencies
├── .env.example           # Example environment variables file
├── main.py                # Entrypoint to run the Web UI
├── client.py              # LLM client setup using PicoAgents and OpenRouter/OpenAI API
├── orchestrator.py        # Multi-agent round-robin orchestrator setup
└── agents/
    ├── poet_agent.py      # Poet Agent definition (writes haikus)
    └── critic_agent.py    # Critic Agent definition (provides critique & approves)
```

## How It Works

1. **Poet Agent**: Generates a haiku on a given prompt.
2. **Critic Agent**: Reviews the haiku, provides constructive feedback, or responds with `"Approved"` once the haiku is satisfactory.
3. **Orchestrator**: Coordinates the conversation loop using a round-robin layout. The orchestration terminates when:
   - The Critic Agent mentions `"Approved"`.
   - The conversation reaches the maximum limit of 8 messages.

---

## Getting Started

### Prerequisites

- Python `>= 3.13`
- [uv](https://github.com/astral-sh/uv) (recommended Python package manager)

### Installation

1. Clone the repository and navigate to the project directory:
   ```bash
   git clone <repository-url>
   cd paico_mlti_agent
   ```

2. Setup your virtual environment and install dependencies:
   ```bash
   # Using uv (Recommended)
   uv sync

   # Or using standard pip
   python -m venv .venv
   source .venv/bin/activate
   pip install -r pyproject.toml
   ```

### Configuration

Copy the example environment file and configure your API key and base URL:
```bash
cp .env.example .env
```

Open `.env` and fill in the values:
```env
OPENAI_BASE_URL="https://openrouter.ai/api/v1" # or your preferred OpenAI-compatible base URL
OPENAI_API_KEY="your_api_key_here"
OPENAI_MODEL="nvidia/nemotron-3-nano-30b-a3b:free" # or your target model
```

---

## Running the Project

### Running the Web UI
To launch the interactive PicoAgents Web UI:

```bash
# Using uv (Recommended)
uv run python main.py

# Or within your activated virtual environment
python main.py
```

The Web UI will automatically open in your default browser at `http://localhost:8070`. You can interact with the orchestrator directly from the browser.

### Running via Script (Terminal)
If you want to run the orchestrator synchronously inside the terminal, you can uncomment line 6 in [main.py](file:///Users/raihan/ML_Workspace/personal_prjects/paico_mlti_agent/main.py):

```python
# main.py
def main():
    asyncio.run(run_orcherstrator())  # Uncomment this to run in terminal
    # serve(entities=[orchestrator], port=8070, auto_open=True)
```
