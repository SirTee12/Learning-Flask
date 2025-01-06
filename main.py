## Integrate HTML with Flask
## create url dynamically

from flask import Flask, redirect, url_for, render_template, request

#initiate flask ( create the WSGI app)
app = Flask(__name__) # WSGI App that will be communicating with server

# create a decorator (take a rule ( specific url you are going), and options)
@app.route('/') # right now , the url is the root hompage
def welcome():
    return render_template('index_main.html')
@app.route('/success/<int:score>')
def success(score):
    res = ''
    if score >= 50:
        res = 'PASS'
    else:
        res = 'FAIL'
        
    return render_template('result.html', result = res)
@app.route('/fail/<int:score>')
def fail(score):
    return 'The person has failed and the marks is: ' + str(score)

@app.route('/results/<int:marks>')
def result(marks):
    result = ''
    if marks < 50:
        result = 'fail'
    else:
        result = 'success'
    return redirect(url_for(result, score = marks))
    #return result
    
@app.route('/submit', methods = ['GET', 'POST'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        datascience = float(request.form['datascience'])
        total_score = (science + maths + c + datascience)/4
        
    res = ''
    return redirect(url_for('success', score = total_score))
        




# to automatically append changes to the wabsite without needing to run the file
#again set debug = True
if __name__ == '__main__':
    app.run(debug = True)


