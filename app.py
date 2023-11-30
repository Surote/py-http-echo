from flask import Flask,request,render_template
import os
import json

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/')
def home():
    re_dict = {'headers': {},'remote_addr': str(request.remote_addr),'pod_name': str(os.getenv("HOSTNAME","N/A"))}
    background_color = os.environ.get("BACKGROUND_COLOR", "blue")
    print(request.headers,request.query_string,request.remote_addr)
    for i in request.headers:
        if i[0] not in re_dict.keys():
            re_dict['headers'][i[0]] = i[1]

    # Render an HTML template with the background color
    return render_template('home.html', json_data=json.dumps(re_dict, indent=4), background_color=background_color)
    #return re_dict

@app.route('/api/v1')
def json_return():
    print(request.headers, request.query_string,request.remote_addr)
    re_dict = {'headers': {},'remote_addr': str(request.remote_addr),'pod_name': str(os.getenv("HOSTNAME","N/A")),
            'http_method':str(request.method), 'http_req_url':str(request.url) }
    
    print("test")
    print(request.method,request.url)
    for i in request.headers:
        if i[0] not in re_dict.keys():
            re_dict['headers'][i[0]] = i[1]
        
    return re_dict

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)