# -*- coding: utf8 -*-
import time
from flask import Flask, jsonify

from flask_jaeger import FlaskJaeger, get_custom_trace_id

app = Flask(__name__)
app.config['SERVICE_NAME'] = "test_flask_jaeger"
app.config['JAEGER_HOST'] = '192.168.0.220'
tracer = FlaskJaeger(app)


@app.route('/', methods=["POST"])
@tracer.log_decorator(trace_info={"route": "root api"})
def trace_api():
    tracer.trace_info(func_name='test', info={"trace_info": "哈哈哈" + get_custom_trace_id()},
                      trace_start_time=time.time(), trace_end_time=time.time())
    return jsonify({"code": 200})


@app.route("/more", methods=['POST'])
@tracer.log_decorator(trace_info={"route": "more api"})
def trace_api2():
    return jsonify({"code": 200})


if __name__ == '__main__':
    app.run()
