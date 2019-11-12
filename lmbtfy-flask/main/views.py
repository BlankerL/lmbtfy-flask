from . import main
from flask import render_template, request, Response
import json
import requests


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/api', methods=['GET', 'POST'])
def api():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
    }
    r = requests.get(url='http://sa.sogou.com/gettiny?url=' + request.values.get('url'), headers=headers)
    response = dict()
    if r.content:
        response['code'] = 200
        response['msg'] = 'success'
        response['result'] = r.content.decode()
        return Response(response=json.dumps(response), content_type='json')
    else:
        response['code'] = 403
        response['msg'] = 'API Error!'
        return Response(response=json.dumps(response), content_type='json')
