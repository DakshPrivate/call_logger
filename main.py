from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return '''
    <h2>Upload Call Logs</h2>
    <form method="POST" action="/upload" enctype="multipart/form-data">
        <input type="file" name="file"><br><br>
        <input type="submit" value="Upload">
    </form>
    '''

@app.route('/upload', methods=['POST'])
def upload_file():
    uploaded_file = request.files.get('file')
    if uploaded_file:
        filepath = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
        uploaded_file.save(filepath)
        return f"File uploaded as <a href='/download/{uploaded_file.filename}'>{uploaded_file.filename}</a>"
    return "No file uploaded", 400

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
