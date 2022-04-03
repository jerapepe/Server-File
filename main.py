from flask import Flask, render_template, request
from flask_cors import CORS
from models import create_post, get_post

Upload = 'static/upload'
app = Flask(__name__)
app.config['uploadFolder'] = Upload
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        pass

    if request.method == 'POST':
        name = request.form['name']
        pos = request.form['post']
        cont = request.files['uploadedfile'].read()
        if name == "":
            return "Error: Debe escribir el nombre"
        else:
            create_post(name, pos, cont)

    posts = get_post()
    return render_template('index.html', posts=posts)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)