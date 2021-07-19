# -*- coding: utf8 -*-

import requests
import threading

from flask_jaeger import CUSTOM_TRACE_ID, JAEGER_TRACE_ID


def send(trace_id):
    response = requests.post("http://127.0.0.1:5000/", json={CUSTOM_TRACE_ID: trace_id})
    jaeger_trace_id = response.headers.get(JAEGER_TRACE_ID)
    print(jaeger_trace_id)
    response = requests.post("http://127.0.0.1:5000/more", json={CUSTOM_TRACE_ID: trace_id},
                             headers={JAEGER_TRACE_ID: jaeger_trace_id})
    print(response.headers.get(JAEGER_TRACE_ID))


if __name__ == '__main__':
    # a_th = threading.Thread(target=send, args=("new-thread1-trace-id",))
    # b_th = threading.Thread(target=send, args=("new-thread2-trace-id", ))
    # a_th.start()
    # b_th.start()
    # a_th.join()
    # b_th.join()
    send('909090')
