from flask import Flask
from flask import json
import logging

app = Flask(__name__)

@app.route('/status')
def healthcheck():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )

    app.logger.info('Status request successfull')
    return response

@app.route('/metrics')
def metrics():
    response = app.response_class(
            response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
            status=200,
            mimetype='application/json'
    )

    app.logger.info('Metrics request successfull')
    return response

@app.route("/")
def hello():
    app.logger.info('Hala AWS Dubai UG!')
    app.logger.info('Main request successfull')

    return '<div> Update 1.0</div><br><center> <H1> Hala AWS Dubai UG! </H1> </center> <p style="text-align:center;"> <img src="https://www.arabianbusiness.com/public/images/2019/04/18/AWS-SUMMIT_Dr-Werner-Vogels-CTO-Amazon.jpg" width="800" height="500" alt="AWS Dubai Summit"> </p> '
if __name__ == "__main__":
    ## stream logs to a file
    logging.basicConfig(filename='app.log',level=logging.DEBUG)
    
    app.run(host='0.0.0.0',port=8080)
