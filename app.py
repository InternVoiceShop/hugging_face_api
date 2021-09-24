from flask import Flask, jsonify, request, render_template
import requests

def create_app():
    app = Flask(__name__)


    @app.route('/')
    def index():
        return render_template('index.html')


    @app.route('/3b', methods=['POST', 'GET'])
    def query3b():
        '''API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-3B"
        headers = {"Authorization": "Bearer api_ndcDIXuwmRamNdauOoVpurzjzkaMvFszlq"}
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()['conversation']['generated_responses'][0]'''
        custom_response = ''
        if request.method == 'POST':
            payload = request.form.get("payload")
            API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-3B"
            headers = {"Authorization": "Bearer api_ndcDIXuwmRamNdauOoVpurzjzkaMvFszlq"}
            response = requests.post(API_URL, headers=headers, json=payload)
            custom_response = response.json()['conversation']['generated_responses'][0]
        
        return render_template('3b.html', response=custom_response)


    @app.route('/9b', methods=['POST', 'GET'])
    def query9b(payload="How are you?"):
        '''API_URL = "https://api-inference.huggingface.co/models/hyunwoongko/blenderbot-9B"
        headers = {"Authorization": "Bearer api_ndcDIXuwmRamNdauOoVpurzjzkaMvFszlq"}
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()['conversation']['generated_responses'][0]'''
        custom_response = ''
        if request.method == 'POST':
            payload = request.form.get("payload")
            API_URL = "https://api-inference.huggingface.co/models/hyunwoongko/blenderbot-9B"
            headers = {"Authorization": "Bearer api_ndcDIXuwmRamNdauOoVpurzjzkaMvFszlq"}
            response = requests.post(API_URL, headers=headers, json=payload)
            custom_response = response.json()['conversation']['generated_responses'][0]
        
        return render_template('9b.html', response=custom_response)


    return app 


#app.run(port=5000)