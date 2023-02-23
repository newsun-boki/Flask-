from flask import Flask
#如果这样运行那么__name__==__main__
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return "<h1>Home 1Page</h1>"


@app.route("/about")
def about():
    return "<h1>About Page</h1>"

#运行时通过在命令行设定环境变量set FLASK_APP=flaskblog.py(Windows)或export FLASK_APP=flaskblog.py
#便可以使用flask run来运行
#在127.0.0.1:5000或localhost:5000中查看
if __name__ == '__main__':
    app.run(debug=True)

#app.run(debug=True)或者设定环境变量FLASK_DEBUG=1来进入调试模式，可以不暂停python程序而随时改变html内容