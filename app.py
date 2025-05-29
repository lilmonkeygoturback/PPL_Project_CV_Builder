from flask import Flask, request, jsonify, send_from_directory
from antlr4 import *
from flask_cors import CORS

import os
import sys
from CVToDictVisitor import CVToDictVisitor

# Add CompiledFiles to sys.path for ANTLR generated files
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'CompiledFiles'))
from CVLexer import CVLexer
from CVParser import CVParser

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)  # Enable CORS for all routes

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/parse', methods=['POST'])
def parse_cv():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    file = request.files['file']
    content = file.read().decode('utf-8')
    input_stream = InputStream(content)
    lexer = CVLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CVParser(stream)
    tree = parser.cv()
    visitor = CVToDictVisitor()
    result = visitor.visit(tree)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
