from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja', methods=['POST'])
def create_user():
    name=request.form['name']
    location=request.form['location']
    language=request.form['language']
    course=request.form['course']
    comment=request.form['comment']
    OS=request.form.getlist('OS')
    return render_template('show.html', userName=name, userLocation=location, userLanguage=language, userCourse=course, userComment=comment, userOS=OS)


if __name__ == '__main__':
    app.run(debug=True)