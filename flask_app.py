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

@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')

@app.route('/gallery', methods=['GET'])
def gallery():
    return render_template('gallery.html')

@app.route('/resources', methods=['GET'])
def resources():
    return render_template('resources.html')


