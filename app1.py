## create url dynamically

from flask import Flask, redirect, url_for

#initiate flask ( create the WSGI app)
app = Flask(__name__) # WSGI App that will be communicating with server

# create a decorator (take a rule ( specific url you are going), and options)
@app.route('/') # right now , the url is the root hompage
def welcome():
    return "Welcome to the city of Los Angeles: The city of the warriors"

@app.route('/success/<int:score>')
def success(score):
    return 'The person has passed and the marks is: ' + str(score)

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




# to automatically append changes to the wabsite without needing to run the file
#again set debug = True
if __name__ == '__main__':
    app.run(debug = True)


