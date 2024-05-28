from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual API key
API_KEY = 'VUqYHvasEvx7gdKP8hE9EkP4b7RSljH3'
PARAPHRASER_URL = 'https://api.apilayer.com/paraphraser'

@app.route('/paraphrase', methods=['POST'])
def paraphrase():
    try:
        # Get the data from the request
        data = request.json
        if not data or 'text' not in data:
            return jsonify({"error": "No text provided"}), 400

        # Prepare the headers and data for the API request
        headers = {
            'apikey': API_KEY
        }
        payload = data['text']

        # Make the POST request to the paraphraser API
        response = requests.post(PARAPHRASER_URL, headers=headers, data=payload)

        # Check if the request was successful
        if response.status_code != 200:
            return jsonify({"error": "Failed to paraphrase text"}), response.status_code

        # Return the response from the paraphraser API
        return jsonify(response.json())

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
