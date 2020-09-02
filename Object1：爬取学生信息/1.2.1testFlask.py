import flask
app = flask.Flask(__name__)

@app.route("/")
# app.route(rule,options)
## rule:表示与该函数的URL绑定
## options：要转发给基础Rule对象的参数列表
def hello():
    return "你好"

@app.route("/hi")
def hi():
    return "Hi,你好"

if __name__=="__main__":
    app.run()
# app.run(host,port,debug,options)
## host:要监听的主机名。默认为127.0.0.1(localhost)
## port:默认为5000
## debug:默认为false
## options:要转发到底层的Werkzeug服务器