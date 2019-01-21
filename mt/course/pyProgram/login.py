# coding=utf-8
"""
创建好数据库以及表：
create table userinfos(
id int primary key auto_increment,
uname varchar(20),
upwd char(40),
isdelete bit default 0
);
加入数据:
insert into userinfos values(0,'123','40bd001563085fc35165329ea1ff5c5ecbdbbeef',0);

加入的密码值是123的sha1加密后的值，因为存入密码是肯定要加密的！
之后我们就可以写python的实际操作代码，来对数据库test01进行操作。
要引入哈希算法的模块进行数据加密，加密之后用加密的数据与数据库里的数据进行对比，
如果相同，则证明登陆成功。
注册的操作便是利用insert方法对数据库插入数据。总体理解较为简单。

"""
from mylib.mysqlhelp import MysqlHelper
from hashlib import sha1

# 注册
uname = input("请输入用户名:")
upwd = input("请输入用户名:")

# 初始化sha1对象
s1 = sha1()
# 对s1进行更新
s1.update(upwd.encode('utf-8'))
# 加密
upwd2 = s1.hexdigest()

# sql语句
sql = 'insert into userinfos(username, upwd) values(%s,%s)'

# 将插入的值存入列表中
params = [uname,upwd2]
# 将sql语句以及值传给对象中的方法
helper = MysqlHelper()
# 返回的是受到改变的行
row = helper.insert(sql,params)
print(row)

# 登录
uname = input("请输入用户名：")
upwd = input("请输入密码：")


s1 = sha1()
s1.update(upwd.encode())
upwd2 = s1.hexdigest()

sql = "SELECT upwd from userinfos where username = %s "
#大写也可以
params = [uname]

helper = MysqlHelper()
result = helper.fetchone(sql, params)

if result == None:
    print ('用户名错误')
elif result[0] == upwd2:
    print ('登录成功')
else:
    print ('密码错误')

    'https: // blog.csdn.net / wangbowj123 / article / details / 77943988'




