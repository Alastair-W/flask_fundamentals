from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.config.from_pyfile('config.py')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja', methods=['POST'])
def create_user():
    session['name']=request.form['name']
    session['location']=request.form['location']
    session['language']=request.form['language']
    session['course']=request.form['course']
    session['comment']=request.form['comment']
    session['OS']=request.form.getlist('OS')
    return redirect('/show_user')

@app.route('/show_user')
def show_user():
    return render_template('show.html', userName=session['name'], userLocation=session['location'], userLanguage=session['language'], userCourse=session['course'], userComment=session['comment'], userOS=session['OS'])


if __name__ == '__main__':
    app.run(debug=True)