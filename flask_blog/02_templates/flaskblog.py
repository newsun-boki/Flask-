from flask import Flask, render_template, url_for
#如果这样运行那么__name__==__main__
app = Flask(__name__)

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    #通过posts可以进行传参
    return render_template("home.html",posts=posts)


@app.route("/about")
def about():
    return render_template("about.html",title='About')

#运行时通过在命令行设定环境变量set FLASK_APP=flaskblog.py(Windows)或export FLASK_APP=flaskblog.py
#便可以使用flask run来运行
#在127.0.0.1:5000或localhost:5000中查看
if __name__ == '__main__':
    app.run(debug=True)

#app.run(debug=True)或者设定环境变量FLASK_DEBUG=1来进入调试模式，可以不暂停python程序而随时改变html内容