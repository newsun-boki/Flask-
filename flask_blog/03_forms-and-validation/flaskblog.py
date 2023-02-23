from flask import Flask, render_template, url_for,flash,redirect
from forms import RegistrationForm,LoginForm

#如果这样运行那么__name__==__main__
app = Flask(__name__)

app.config['SECRET_KEY'] = '4a4de39465bd06260237dafc09f81c56'

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

@app.route("/register", methods=['GET','POST'])
def register():
    #所以当用户第一次点击该url时，由于表单没有完成，所以会直接获取页面
    # 而当用户在该页面提交表单时，该路由会收到POST请求并重新调用该函数，进入if
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))#url_for中可以直接填入路由处理函数的名字，从而生成URL地址
    return render_template('register.html',title='Register',form = form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful, please check username and password','danger')
    return render_template('login.html',title='Login',form = form)

#运行时通过在命令行设定环境变量set FLASK_APP=flaskblog.py(Windows)或export FLASK_APP=flaskblog.py
#便可以使用flask run来运行
#在127.0.0.1:5000或localhost:5000中查看
if __name__ == '__main__':
    app.run(debug=True)

#app.run(debug=True)或者设定环境变量FLASK_DEBUG=1来进入调试模式，可以不暂停python程序而随时改变html内容