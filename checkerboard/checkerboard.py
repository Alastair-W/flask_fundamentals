from flask import Flask, render_template  
app = Flask(__name__)  

@app.route('/')          
def checker():
    return render_template('index.html')

@app.route('/<num>')
def flexCheck(num):
    return render_template('flex.html', boardSize = int(num))


if __name__=="__main__":  
    app.run(debug=True)   