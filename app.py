from flask_bootstrap import Bootstrap5
from flask import Flask, render_template, request, jsonify
from prompts import INITIAL_PROMPT, RESPONSE
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

bootstrap = Bootstrap5(app)

def analyze_prompt(prompt):
    response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are CLEARBOT, an expert on large language model and AI chatbot prompting."},
        {"role": "user", "content": INITIAL_PROMPT},
        {"role": "assistant", "content": RESPONSE},
        {"role": "user", "content": prompt}
    ]
)
    return response.choices[0]['message']['content']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prompt = request.form.get('prompt')
        result = analyze_prompt(prompt)
        return jsonify(result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
