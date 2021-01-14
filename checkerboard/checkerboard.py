from flask import Flask, render_template  
app = Flask(__name__)  

@app.route('/')          
def checker():
    return render_template('index.html', num_rows=int(8), num_cols=int(8))

@app.route('/<num>')
def flexCheckOne(num):
    return render_template('index.html', num_rows=int(num), num_cols=int(num))

@app.route('/<num_y>/<num_x>')
def flexCheckTwo(num_y, num_x):
    return render_template('index.html', num_rows=int(num_y), num_cols=int(num_x))

@app.route('/<num_y>/<num_x>')
def flexCheckThree(num_y, num_x):
    return render_template('index.html', num_rows=int(num_y), num_cols=int(num_x))

@app.route('/<num_y>/<num_x>/<color_y>/<color_x>')
def flexCheckColor(num_y, num_x, color_y, color_x):
    return render_template('index.html', num_rows=int(num_y), num_cols=int(num_x), color1=color_y, color2=color_x)


if __name__=="__main__":  
    app.run(debug=True)   