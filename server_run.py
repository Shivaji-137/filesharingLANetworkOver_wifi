from flask import Flask, request, redirect, url_for, send_from_directory, render_template_string, abort

import os

app = Flask(__name__)


UPLOAD_FOLDER = os.getcwd()  # Use the current working directory
ALLOWED_EXTENSIONS = {
    'zip', 'tar', 'gz', 'rar', '7z',                # Compressed files
    'mp3', 'wav', 'aac', 'flac', 'ogg',             # Audio files
    'mp4', 'mkv', 'avi', 'mov', 'wmv', 'flv',       # Video files
    'jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff',     # Image files
    'pdf'                                           # PDF files
}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    items = os.listdir(app.config['UPLOAD_FOLDER'])
    files = [f for f in items if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], f))]
    directories = [d for d in items if os.path.isdir(os.path.join(app.config['UPLOAD_FOLDER'], d))]
    return render_template_string('''
    <!doctype html>
    <title>File Directory</title>
    <h1>File Directory</h1>
    <ul>
      {% for directory in directories %}
        <li>
          <a href="{{ url_for('browse_directory', path=directory) }}">{{ directory }}/</a>
        </li>
      {% endfor %}
      {% for file in files %}
        <li>
          <a href="{{ url_for('uploaded_file', filename=file) }}">{{ file }}</a> - 
          <a href="{{ url_for('download_file', filename=file) }}">Download</a>
        </li>
      {% endfor %}
    </ul>
    <h2>Upload new Files</h2>
    <form method=post enctype=multipart/form-data>
      <input type=file name=files multiple>
      <input type=submit value=Upload>
    </form>
    ''', files=files, directories=directories)

@app.route('/', methods=['POST'])
def upload_file():
    if 'files' not in request.files:
        return 'No file part', 400
    files = request.files.getlist('files')
    if not files:
        return 'No selected files', 400

    for file in files:
        if file.filename == '':
            return 'No selected file', 400
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    return redirect(url_for('index'))

@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    try:
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    except FileNotFoundError:
        abort(404)

@app.route('/download/<path:filename>')
def download_file(filename):
    try:
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)
    except FileNotFoundError:
        abort(404)

@app.route('/browse/<path:path>/')
def browse_directory(path):
    full_path = os.path.join(app.config['UPLOAD_FOLDER'], path)
    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        abort(404)

    items = os.listdir(full_path)
    files = [f for f in items if os.path.isfile(os.path.join(full_path, f))]
    directories = [d for d in items if os.path.isdir(os.path.join(full_path, d))]
    return render_template_string('''
    <!doctype html>
    <title>File Directory - {{ path }}</title>
    <h1>File Directory - {{ path }}</h1>
    <ul>
      <li><a href="{{ url_for('index') }}">.. (root)</a></li>
      {% for directory in directories %}
        <li>
          <a href="{{ url_for('browse_directory', path=path + '/' + directory) }}">{{ directory }}/</a>
        </li>
      {% endfor %}
      {% for file in files %}
        <li>
          <a href="{{ url_for('uploaded_file', filename=path + '/' + file) }}">{{ file }}</a> - 
          <a href="{{ url_for('download_file', filename=path + '/' + file) }}">Download</a>
        </li>
      {% endfor %}
    </ul>
    <h2>Upload new Files</h2>
    <form method=post enctype=multipart/form-data action="{{ url_for('upload_file_to_directory', path=path) }}">
      <input type=file name=files multiple>
      <input type=submit value=Upload>
    </form>
    ''', path=path, files=files, directories=directories)

@app.route('/upload/<path:path>', methods=['POST'])
def upload_file_to_directory(path):
    full_path = os.path.join(app.config['UPLOAD_FOLDER'], path)
    if 'files' not in request.files:
        return 'No file part', 400
    files = request.files.getlist('files')
    if not files:
        return 'No selected files', 400

    for file in files:
        if file.filename == '':
            return 'No selected file', 400
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(full_path, filename))

    return redirect(url_for('browse_directory', path=path))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

