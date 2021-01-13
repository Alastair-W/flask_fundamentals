from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

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

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.