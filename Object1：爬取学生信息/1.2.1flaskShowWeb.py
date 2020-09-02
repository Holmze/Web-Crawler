import flask
app = flask.Flask(__name__)

@app.route("/")
def index():
    try:
        fobj=open("Object1：爬取学生信息\index.htm","rb")
        data = fobj.read()
        fobj.close()
        return data
    except Exception as err:
        return str(err)

if __name__=="__main__":
    app.run()