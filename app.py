from flask import Flask

#initiate flask ( create the WSGI app)
app = Flask(__name__) # WSGI App that will be communicating with server

# create a decorator (take a rule ( specific url you are going), and options)
@app.route('/') # right now , the url is the root hompage
def welcome():
    return "Welcome to the city of Los Angeles: The city of the warriors"

# to automatically append changes to the wabsite without needing to run the file
#again set debug = True
if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 5000)