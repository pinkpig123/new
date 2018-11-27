from flask import Flask, signals


app = Flask(__name__)

@app.before_request
def www():
    print("wwwwww")

def xxx(arg):
    print("12345")
signals.request_started.connect(xxx)

@app.route("/login")
def login():
    return "1"

if __name__ == '__main__':
    app.run()
    #app.__call__