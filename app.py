from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "DevOps 流水线运行成功！Hello from Flask & Docker!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
