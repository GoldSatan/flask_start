from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'SADIM!#(DH(sadas0d)___!@)E)d0192'

def update_session():
    if 'calc' not in session:
        session['calc'] = 100

def is_login():
    if 'login' in session:  return True
    else:   return False

def update_login():
    if not is_login():
        session['login'] = True


@app.route('/login')
def loginView():
    update_login()
    
    return redirect('/')

@app.route('/')
def indexView():
    update_session()
    
    return render_template('index.html', data = 0, number=session['calc'])

@app.route('/new1')
def new1View():
    update_session()
    
    return render_template('index.html', data = 1, number=session['calc'])

@app.route('/new2')
def new2View():
    update_session()
    
    return render_template('index.html', data = 2, number=session['calc'])

@app.route('/new3')
def new3View():
    update_session()
    
    return render_template('index.html', data = 3, number=session['calc'])

@app.route('/new4')
def new4View():
    update_session()
    
    return render_template('index.html', data = 4, number=session['calc'])



'''~~~~~~~~functions~~~~~~~~~'''



@app.route('/new1/function')
def new1FunctionView():
    update_session()
    session['calc'] += 10
    
    return redirect('/new1')

@app.route('/new2/function')
def new2FunctionView():
    update_session()
    session['calc'] -= 10
    
    return redirect(url_for('new2View'))

@app.route('/new3/function')
def new3FunctionView():
    if is_login():
        update_session()
        session['calc'] /= 2        
        
        return render_template('index.html', data = 3, number=session['calc'])
    else:
        return redirect('/') 

@app.route('/new4/function')
def new4FunctionView():
    if is_login():
        update_session()
        session['calc'] *= 3

        return render_template('index.html', data = 4, number=session['calc'])
    else:
        return redirect('/') 


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port='8080')