from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def main():
    hostname = request.host_url
    message = 'Thanks for visiting have a wonderful day!'
    return render_template('index.html', host=hostname, msg=message)

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/volunteering', methods=['GET'])
def artist():
    return render_template('volunteering.html')
