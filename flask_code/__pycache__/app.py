from flask import Flask,jsonify

app=Flask(__name__)

#创造路由，路由‘访问的地址// //’
@app.route("/")  #装饰器
def index():
    hhml='''<!DOCTYPE html>
<html>
<head>
  <title>Bootstrap 实例</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://cdn.staticfile.org/twitter-bootstrap/4.3.1/css/bootstrap.min.css">
  <script src="https://cdn.staticfile.org/jquery/3.2.1/jquery.min.js"></script>
  <script src="https://cdn.staticfile.org/popper.js/1.15.0/umd/popper.min.js"></script>
  <script src="https://cdn.staticfile.org/twitter-bootstrap/4.3.1/js/bootstrap.min.js"></script>
</head>
<body>

<div class="jumbotron text-center">
  <h1>这是陈思维的第一个copy代码的html</h1>
  <p>重置浏览器大小查看效果!</p> 
</div>
 
<div class="container">
  <div class="row">
    <div class="col-sm-4">
      <h3>第一列</h3>
      <p>菜鸟教程</p>
      <p>学的不仅是技术，更是梦想！！！</p>
    </div>
    <div class="col-sm-4">
      <h3>第二列</h3>
      <p>菜鸟教程..</p>
      <p>学的不仅是技术，更是梦想！！！</p>
    </div>
    <div class="col-sm-4">
      <h3>第三列</h3> 
      <p>菜鸟教程..</p>
      <p>学的不仅是技术，更是梦想！！！</p>
    </div>
  </div>
</div>

</body>
</html>'''
    return hhml  #html

@app.route("/user")
def getuser():
  hdict={'name':'csw','phone':114,'high':170}

  return  jsonify(hdict)

if __name__ == "__main__":
    app.run(debug=True)
