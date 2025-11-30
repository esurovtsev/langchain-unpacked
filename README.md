# LangChain Unpacked

This repository accompanies the LangChain Unpacked series, a fresh learning journey through the LangChain and LangGraph ecosystem following the October 2025 release of LangChain 1.0 and LangGraph 1.0. These updates introduced significant API changes, new abstractions like middlewares, and modernized patterns for building agentic applications. Rather than continuing with outdated syntax, this series provides a clean restart that reflects current best practices. It builds on insights from previous LangGraph work while embracing the updated framework architecture. Designed for developers seeking production-ready AI workflows, this series covers agents, tools, memory, human oversight, and scalable system design.

## Why This Series Exists

In October 2025, LangChain introduced breaking changes across their ecosystem:

- LangChain 1.0 and LangGraph 1.0 releases
- Updated APIs and syntax
- New abstractions (e.g., middlewares, runtime context)
- Revised patterns for agent architectures

Previous content using older syntax remains useful for historical reference, but building modern applications requires alignment with the updated framework. This series addresses that need by starting fresh with current APIs and patterns.

## Getting Started

### 1. Clone the Repository

```bash
git clone git@github.com:esurovtsev/langchain-unpacked.git
cd langchain-unpacked
```

### 2. Set Up Your Python Environment

It is recommended to use a virtual environment to manage dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory with your API keys:

```bash
# Required: OpenAI API key for LLM access
OPENAI_API_KEY=your_openai_api_key_here

# Optional: LangSmith for tracing and debugging
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_api_key_here
LANGCHAIN_PROJECT=langchain-unpacked
```

If you plan to use LangGraph Studio, also create a `.env` file in the `studio/` directory with the same keys.

**Note**: Never commit `.env` files to version control. The `.gitignore` file should already exclude them.

## Usage

- Follow the lessons in order (scripts or notebooks).
- Each lesson will have an accompanying video tutorial.
- Explanations and code comments will help you understand each concept.

## Video Tutorials

 Each lesson will have a dedicated video tutorial. Links will be provided as lessons are released.

## Contents

1. **LangChain 1.0 Middleware & Human-in-the-Loop Agents** ([01_langchain_middleware.ipynb](01_langchain_middleware.ipynb))
   - Understand why the classic ReAct agent loop is fine for toy problems but risky once your agent can trigger real-world side effects like trades or API calls.
   - Learn what middleware means in LangChain 1.0, and where `HumanInTheLoopMiddleware` fits among the many built-in middleware components as a safety layer wrapped around the agent loop.
   - Use `HumanInTheLoopMiddleware` as your first concrete example of human-in-the-loop design: when the agent must pause, what it asks a human to decide, and how that decision shapes the rest of the run.
   - Build a mental model of interruptions and resumes as part of the control flow, using checkpoints and thread IDs to keep long-running conversations consistent, auditable, and debuggable.
   - Connect these ideas to a realistic scenario (approving a stock order via a high-stakes tool) and learn how LangGraph Studio helps you visualize, test, and explain these flows to others.
   - [LangChain 1.0 Unpacked – Build AI Agents with the New Middleware and and Human-in-the-Loop Controls](https://www.youtube.com/watch?v=fJ9o0EPXdHk)

*Additional lessons will be added as the series progresses. Topics will cover memory systems, human oversight patterns, multi-agent architectures, production deployment strategies, and advanced optimization techniques.*

## Running Agents in `studio` Using LangGraph Studio (Web Interface)

To run agents (such as those found in the `studio` directory) using the LangGraph Studio web interface for local development, follow these steps:

1. **Install Required Dependencies**
   Make sure all dependencies for your agent are installed:
   ```bash
   pip install -r studio/requirements.txt
   ```

2. **Install the LangGraph CLI**
   ```bash
   pip install -U "langgraph-cli[inmem]"
   ```

3. **Start the Local LangGraph Development Server**
   From the `studio` directory, run:
   ```bash
   langgraph dev
   ```
   This will start the local LangGraph server in watch mode.

4. **Open LangGraph Studio in Your Browser**
   Once the server is running, you can access the Studio UI at:
   [https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024](https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024)
   (If your server is running at a different host/port, update the `baseUrl` accordingly.)

For more details and troubleshooting, see the [official LangGraph Studio Quickstart](https://langchain-ai.github.io/langgraph/cloud/how-tos/studio/quick_start/).

## Contributing

Feedback and contributions are welcome! Please open issues or submit pull requests for suggestions and improvements.

## License

[Specify your license here, e.g., MIT]

---

*This README will be updated as the series progresses. Stay tuned for new lessons and videos!*
