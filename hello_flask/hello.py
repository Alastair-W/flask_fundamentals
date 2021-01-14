from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template('index.html')  # Return the string 'Hello World!' as a response

@app.route('/dojo')          # The "@" decorator associates this route with the function immediately following
def hello_dojo():
    return 'Hello Dojo!' 

@app.route('/success')
def success():
    return "success"

@app.route('/say/<name>')
def hello(name):
    if type(name) == str:
        print(name)
        return f"Hi {name.capitalize()}"

@app.route('/repeat/<num>/<string>')
def repeat(num, string):
    if type(string) == str and num.isdigit():
        return string * int(num)
        
@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    print(username)
    print(id)
    return f"username: {username}, id: {id}"

@app.route('/play')
def play():
    return render_template('play.html')

@app.route('/play/<num>')
def playX(num):
    return render_template('play.html', num_times=int(num))

@app.route('/play/<num>/<color>')
def playColor(num, color):
    return render_template('play.html', num_times=int(num), my_color=color)

@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    users = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template("lists.html", users_list = users)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.