from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

app = Flask(__name__)

# Initialize the models (adjust paths accordingly)
tokenizer_1 = AutoTokenizer.from_pretrained("google/flan-t5-xxl")
model_1 = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-xxl")

@app.route("/generate", methods=["POST"])
def generate_response():
    data = request.json
    prompt = data["prompt"]
    inputs = tokenizer_1(prompt, return_tensors='pt')
    outputs = model_1.generate(inputs["input_ids"])
    response = tokenizer_1.decode(outputs[0], skip_special_tokens=True)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
