## 目的

方便flask app链路追踪集成

与[flask-opentracing](https://github.com/opentracing-contrib/python-flask)的不同之处：

> flask-opentracing只支持视图前后进行trace，此插件支持任何地方trace


### 初始化

```python

app = Flask(__name__)
app.config['SERVICE_NAME'] = "test_flask_jaeger"
app.config['JAEGER_HOST'] = '192.168.0.220'
tracer = FlaskJaeger(app)

```

### 打log

> 方式1

```python

@tracer.log_decorator(trace_info={"route": "root api"})

```

> 方式2

```python

    tracer.trace_info(func_name=<your func name>, info={"trace_info": "测试测试"})

```

### 跨多个请求的时候


例如:

requ1返回一个jaeger_trace_id为123321
requ2返回一个jaeger_trace_id为456654

但是requ1和requ2都是hello_a() function下发出来的，那么就不会形成一个堆栈，解决方法:


```python

response = requests.post("http://127.0.0.1:5000/", json={CUSTOM_TRACE_ID: trace_id})
jaeger_trace_id = response.headers.get(JAEGER_TRACE_ID)
print(jaeger_trace_id) 
response = requests.post("http://127.0.0.1:5000/more", json={CUSTOM_TRACE_ID: trace_id}, headers={JAEGER_TRACE_ID: jaeger_trace_id}) # 使用上一个请求返回的jaeger_trace_id
print(response.headers.get(JAEGER_TRACE_ID))


```

> 可以看到，这两个请求返回的jaeger_trace_id都是一样的。

















