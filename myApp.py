from flask import Flask

def check_name(my_name):
    return True

def check_name_len(my_name):
    return True

def check_sid_len(my_id):
    return True    

# imagine these data is from db
myName = "YI Jiaci"
myId = "1155160267" 
### end of data

app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"<p> Hello, my name is {myName}, my sid is {myId}</p>"

if __name__ == "__main__":
    app.run(debug=True)