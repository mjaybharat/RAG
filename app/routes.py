from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    file = request.files['file']
    file.save(f"data/uploads/{file.filename}")
    return jsonify({'message': 'File uploaded successfully'}), 200
