from flask import Flask, render_template, request, jsonify
from prompts import INITIAL_PROMPT, RESPONSE
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

def format_response(response_text):
    if response_text[0] == '"' and response_text[-1] == '"':
        response_text = response_text[1:-1]
    with_title = f"<h2 class='subtitle is-3'>Your Prompt Report</h2><p>{response_text}</p>"
    return with_title.replace("\n", "<br />")

def analyze_prompt_with_chatgpt(prompt):
    response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are CLEARBOT, an expert on large language model and AI chatbot prompting."},
        {"role": "user", "content": INITIAL_PROMPT},
        {"role": "assistant", "content": RESPONSE},
        {"role": "user", "content": prompt}
    ]
)
    response_text = response.choices[0]['message']['content']
    return format_response(response_text)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prompt = request.form.get('prompt')
        result = analyze_prompt_with_chatgpt(prompt)
        return jsonify(result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
