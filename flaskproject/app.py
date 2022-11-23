from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        userName = request.form['username']
    resp = make_response(render_template("base.html"))
    resp.set_cookie('username', userName)
    return resp

@app.route('/profile')
def profile():
    userName = request.cookies.get('username')  
    return render_template('profile.html', name=userName)

@app.route('/')
def login():
   return render_template('login.html')

@app.route("/brenden")
def Brenden():
	return render_template("brenden.html")

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=2224)

