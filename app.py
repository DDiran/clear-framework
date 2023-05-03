from flask import Flask, render_template, request, jsonify
# from transformers import GPT2LMHeadModel, GPT2Tokenizer
from prompts import INITIAL_PROMPT, GPT_2_PROMPT, RESPONSE
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

# model_name = "gpt2"
# tokenizer = GPT2Tokenizer.from_pretrained(model_name)
# model = GPT2LMHeadModel.from_pretrained(model_name)

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

# def analyze_prompt_with_gpt2(prompt, max_length=1000, num_return_sequences=1):
#     combined_prompt = f"{GPT_2_PROMPT} {prompt}\n\nEVALUATION:"
#     inputs = tokenizer.encode(combined_prompt, return_tensors="pt")
#     outputs = model.generate(
#         inputs,
#         max_length=max_length,
#         num_return_sequences=num_return_sequences,
#         no_repeat_ngram_size=2,
#         temperature=0.7,
#         top_k=50,
#         top_p=0.95,
#         do_sample=True,
#     )
#     generated_text = [
#         tokenizer.decode(output, skip_special_tokens=True) for output in outputs
#     ]
#     return generated_text



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prompt = request.form.get('prompt')
        result = analyze_prompt_with_chatgpt(prompt)
        return jsonify(result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
