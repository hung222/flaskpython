from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return 'thủ da6ml là lấy tay xoa bóp cu xịt ra tinh trùng'
 
if __name__ == '__main__':
    app.run()