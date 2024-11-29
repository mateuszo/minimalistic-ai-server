# Minimalistic AI Server

This is a minimalistic AI server built using Flask and GPT4All. The server provides an endpoint to generate responses based on prompts sent to it.

## Requirements

- Python 3.12
- Virtual environment (venv)
- 4.66 GB of free space

## Installation

1. Clone the repository.

2. Create and activate a virtual environment:

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask server.

    ```sh
    flask run
    ```

    On the first startup this will download the Meta Llama model (4,66 GB) to `~/.cache/gpt4all/`. ([Check GPT4All docs](https://docs.gpt4all.io/gpt4all_python/ref.html) for more details)

2. The server will start on `http://127.0.0.1:5000/`.

3. To generate a response, send a POST request to `http://127.0.0.1:5000/prompt` with a JSON body containing the prompt:

    ```json
    {
        "prompt": "Your prompt here"
    }
    ```

## Endpoints

- `POST /prompt` - Accepts a JSON body with a `prompt` field and returns a generated response.

## Example

```sh
curl -X POST http://127.0.0.1:5000/prompt -H "Content-Type: application/json" -d '{"prompt": "Tell me a joke."}'
```
