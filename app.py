from flask import Flask, redirect, url_for, render_template, request
from forms import RegForm, Login
from flask_bootstrap import Bootstrap

app=Flask(__name__)
app.config.from_mapping(SECRET_KEY=b'dsdhcusd048474jdodd0')
Bootstrap(app)

@app.route("/")
def index():
    return render_template('index.html', title='Home')

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegForm(request.form)
    if request.method=='POST' and form.validate_on_submit():
        return 'Registration Complete'
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Login(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        return 'Login Successful'
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(port=5000,debug=True)
