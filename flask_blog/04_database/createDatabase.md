# create Database in terminal

+ 打开终端进入虚拟环境以及当前路径

+ 终端输入python进入交互式命令行

+ 创建空表

```python
>>> from flaskblog import db,app
>>> with app.app_context():
...     db.create_all()
```
这会在`instance`文件夹中创建site.db数据库.

+ 添加数据
  
```python
from flaskblog import db,app
from flaskblog.models import User, Post
app.app_context().push()
user_1 = User(username='lby',email='C@demo.com',password='password')
db.session.add(user_1)
db.session.commit()#似乎add和commit必须在一个context中
```

+ 查询表
```python
with app.app_context():#app.app_context().push()
    User.query.all()#查询全部
    User.query.first()#查询第一个
    User.query.filter_by(username='lby').all()
    user = User.query.filter_by(username='lby').first()
    user.id#输出lby的id
    user = User.query.get(1)#获取id为1的记录
with app.app_context():
    post_1= Post(title = 'Blog1',content = 'First one!', user_id=user.id)
    post_2= Post(title = 'Blog2',content = 'Second two!', user_id=user.id)
    db.session.add(post_1)
    db.session.add(post_2)
    db.session.commit()
    print(user.posts)
```

+ 删除表

```python
with app.app_context():
    db.drop_all()
```