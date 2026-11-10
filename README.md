# LLMs Practice

A collection of small projects and experiments with large language models, APIs, fine-tuning, and retrieval-augmented generation. Each folder is a standalone example; there is no single application or shared dependency environment.

## Projects

| Folder | What it contains |
| --- | --- |
| `Gemini/` | Gemini File Search example: uploads `sample.txt` to a File Search store and asks a question grounded in the file. |
| `Google-ADK/` | Google Agent Development Kit agent that answers questions about the current time in a city. |
| `SarvamAI_ChatBot/` | Streamlit chat interface powered by Sarvam AI. |
| `Sarvam_AI/` | Minimal command-line example for calling the Sarvam AI chat API. |
| `Llama/` | Groq-hosted Llama chat completion example with streamed output. |
| `Gemma/` | Python fine-tuning example using Gemma 2B, 4-bit quantization, and LoRA on a quotes dataset. |
| `Qwen/` | Notebook experiment for visual-model fine-tuning. |
| `ChatGpt/` | Google Colab notebook for QLoRA fine-tuning of `gpt-oss-20b`. |

The Gemini example uses the repository-level `sample.txt` file as its input. The Gemini File Search results screenshot is retained below.

## Requirements

- Python 3.9 or newer for the Python examples (some ML libraries may require a newer version).
- API credentials for the hosted model services you use.
- GPU/CUDA support and substantial memory for the Gemma and Qwen fine-tuning workflows. The ChatGPT-named notebook is designed for Google Colab.

Dependencies are currently project-specific. The only checked-in requirements file is for the Streamlit chatbot.

## Run an example

Run commands from the repository root unless otherwise noted. Create a virtual environment for each project to keep its dependencies separate.

### Sarvam AI Streamlit chatbot

```bash
python -m venv .venv
# Activate the environment, then:
pip install -r SarvamAI_ChatBot/requirements.txt
```

Create `SarvamAI_ChatBot/.env` with your key:

```dotenv
SarvamAI_API_KEY=your_api_key
```

Start the app:

```bash
streamlit run SarvamAI_ChatBot/app.py
```

### Gemini File Search

Install the `google-genai` and `python-dotenv` packages, then create `Gemini/.env`:

```dotenv
GOOGLE_API_KEY=your_api_key
```

Run from the repository root so the script can find `sample.txt`:

```bash
python Gemini/File_search.py
```

### Other examples

- `Sarvam_AI/main.py` expects `SarvamAI_API_KEY` in a `.env` file at the repository root. Install `sarvamai` and `python-dotenv`, then run `python Sarvam_AI/main.py`.
- `Google-ADK/my_agent/` is an ADK agent package. Install the Google ADK and configure its Google model credentials, then launch it with the ADK CLI from `Google-ADK/` (for example, `adk web`).
- `Llama/Groq_LLM.py` requires the `groq` Python package and a Groq API key. Replace the `API_KEY` placeholder in the script with your key before running it.
- `Gemma/gemma_finetuning_notebook.py` expects a Hugging Face token, access to `google/gemma-2b`, a CUDA GPU, and the Transformers, PyTorch, Datasets, TRL, and PEFT packages. It also uses a Colab `userdata` helper, so adapt that token setup when running outside Colab.
- Open the notebooks in `Qwen/` and `ChatGpt/` in a compatible notebook environment and follow their setup cells. Their model and hardware requirements can be significant.

## Credentials

Keep API keys and access tokens private. Store them in local `.env` files or the notebook platform's secret manager, and never commit credentials. The repository ignores `.env` files.

## Gemini File Search results

<img width="1262" height="218" alt="Gemini File Search results" src="https://github.com/user-attachments/assets/77f6820d-a296-4c6f-b73a-c27370be2578" />
