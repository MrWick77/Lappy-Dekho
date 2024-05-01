from flask import Flask, render_template, request, jsonify
from joblib import load

app = Flask(__name__)
model = load('model_lpp.joblib')

gp_dict = {'nil': 0, 'gtx-1650': 4.38, 'rtx-3050': 4.55}

pr_dict = {'i3': 3, 'i5': 5, 'i7': 7}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    storage = int(request.form['storage'])
    if storage is None:
        return jsonify({'error': 'Enter the valid storage!'})
    ram = int(request.form['ram'])
    if ram is None:
        return jsonify({'error': 'Enter the valid RAM!'})
    g_size = int(request.form['g_size'])
    if g_size is None:
        return jsonify({'error': 'Enter the valid Graphics size!'})
    gp_card = request.form['gp_card']
    gc = gp_dict.get(gp_card, None)
    if gc is None:
        return jsonify({'error': 'Invalid graphics card type!'})
    processor_input = request.form['processor']
    processor = pr_dict.get(processor_input, None)
    if processor is None:
        return jsonify({'error': 'Invalid processor type!'})

    predicted_price = model.predict([[storage, ram, processor, g_size, gc]])
    return jsonify({'predicted_price': predicted_price[0]})

if __name__ == '__main__':
    app.run(debug=True)
