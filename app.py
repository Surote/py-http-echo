from flask import Flask,request
import os

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/')
def home():
    re_dict = {'headers': {},'remote_addr': str(request.remote_addr),'pod_name': str(os.getenv("HOSTNAME","N/A"))}

    print(request.headers, request.json,request.query_string,request.remote_addr)
    for i in request.headers:
        if i[0] not in re_dict.keys():
            re_dict['headers'][i[0]] = i[1]
    return re_dict

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)