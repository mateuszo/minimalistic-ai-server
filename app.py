from flask import Flask, request, jsonify

from gpt4all import GPT4All
model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/prompt", methods=["POST"])
def handle_prompt():
    data = request.get_json()
    response = model.generate(data['prompt'], max_tokens=1024)
    return {"message": response}
