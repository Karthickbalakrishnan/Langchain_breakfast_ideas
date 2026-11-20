# LangChain Breakfast Ideas

A lightweight Python command-line example that uses LangChain and OpenAI's `gpt-4o-mini` model to generate five healthy, vegetarian South Indian breakfast ideas.

The application loads environment variables with `python-dotenv`, invokes the language model with a strictly formatted prompt, and prints the model's response to the terminal.

## Features

- Generates exactly five breakfast suggestions
- Requests healthy and purely vegetarian South Indian ideas
- Uses a numbered-list, one-item-per-line output format
- Uses `gpt-4o-mini` through LangChain's OpenAI integration
- Loads the API key securely from a local `.env` file
- Uses a temperature of `0.7` for varied creative responses

## How It Works

The script follows a short, direct execution flow:

1. Loads environment variables from a local `.env` file.
2. Creates a `ChatOpenAI` model instance using `gpt-4o-mini`.
3. Sends a prompt requesting five breakfast ideas.
4. Calls `llm.invoke(prompt)` to obtain a message response.
5. Prints `reply.content`, keeping only the generated text.

The main implementation is in [`breakfast.py`](breakfast.py).

## Requirements

- Python 3.9 or newer
- An OpenAI API key
- The following Python packages:
  - `langchain-openai`
  - `python-dotenv`

## Installation

Clone the repository:

```bash
git clone https://github.com/Karthickbalakrishnan/Langchain_breakfast_ideas.git
cd Langchain_breakfast_ideas
```

Create and activate a virtual environment:

**Linux/macOS:**

```bash
python -m venv .venv
source .venv/bin/activate
```

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install the required packages:

```bash
pip install langchain-openai python-dotenv
```

## Configuration

Create a `.env` file in the project root:

```dotenv
OPENAI_API_KEY=your_openai_api_key
```

The script uses `load_dotenv()` to read this value into the process environment. Do not commit your `.env` file or API key to source control.

## Usage

Run the script from the repository root:

```bash
python breakfast.py
```

Example output:

```text
1. Idli with sambar and coconut chutney
2. Medu vada with vegetable sambar
3. Rava dosa with tomato chutney
4. Adai with avial
5. Pesarattu with ginger chutney
```

Generated suggestions may vary because `temperature=0.7` allows for more creative and varied responses.

## Model Settings

| Setting | Value | Purpose |
|---|---|---|
| Model | `gpt-4o-mini` | Efficient OpenAI chat model |
| Temperature | `0.7` | Produces varied, creative suggestions |
| Prompt | Strictly numbered list | Requests concise, consistently formatted results |

To make output more deterministic, change the temperature to `0.0`:

```python
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.0)
```

## Project Structure

```text
Langchain_breakfast_ideas/
├── breakfast.py       # LangChain and OpenAI execution entry point
├── breakfast1.jpeg    # Supporting image asset
├── breakfast2.jpeg    # Supporting image asset
└── README.md          # Project documentation
```

## Example Prompts

You can customize the prompt in `breakfast.py`. For example:

```python
prompt = (
    "Provide exactly 5 low-calorie vegetarian breakfast ideas from South India. "
    "Format them strictly as a numbered list, exactly one line per idea, with no preamble."
)
```

## Troubleshooting

### `OPENAI_API_KEY` is missing

Make sure:

- A `.env` file exists in the project root.
- It contains `OPENAI_API_KEY=your_api_key`.
- `python-dotenv` is installed.
- The script is started from the correct project directory.

### Authentication or quota error

Verify that:

- The API key is valid and active.
- The OpenAI account has available quota or billing configured.
- The key has permission to access the selected model.

### Import errors

Install both dependencies in the active virtual environment:

```bash
pip install --upgrade langchain-openai python-dotenv
```

## Limitations

- Requires internet access and a valid OpenAI API key.
- Usage may incur provider charges.
- Model output is not guaranteed to be exact or consistently structured.
- The script does not validate dietary claims or ingredient safety.
- The script has no command-line arguments or interactive input.
- There is currently no automated test suite.

## Potential Improvements

- Add retry and timeout handling.
- Validate and parse model output into a Python list.
- Add CLI arguments for dietary preferences and number of ideas.
- Support alternative LangChain chat models.
- Store the prompt in a reusable prompt template.
- Add tests with mocked chat-model responses.
- Add a `requirements.txt` or `pyproject.toml` file for dependency management.
- Use structured output with Pydantic for reliable response formatting.

## Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new feature branch.
3. Make and test your changes.
4. Submit a pull request with a clear description.
