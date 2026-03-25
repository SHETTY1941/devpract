from flask import Flask, request, render_template

app = Flask(__name__)

# ✅ Home route
@app.route('/')
def home():
    return "Go to /register to use the form"

@app.route('/regis', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        print(name, email, password)

        return render_template('success.html')

    return render_template('regis.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)