from flask import Flask

def check_name(my_name):
    # name must be a string
    if my_name == None or (not isinstance(my_name, str)):
        return False
    # name length must not exceed 20 bytes
    if not check_name_len(my_name):
        return False
    # name must only contain characters in printable characters in unicode and space
    if not my_name.isprintable():
        return False
    # name must end with a non-space character
    if my_name[-1] == ' ':
        return False
    return True

def check_name_len(my_name):
    if my_name == None or len(my_name.encode()) > 20:
        return False
    return True

def check_sid_len(my_id):
    if my_id == None:
        return False
    if isinstance(my_id, int) and (my_id < 10**9 or 10**10 <= my_id):
        return False
    if isinstance(my_id, str) and (len(my_id) != 10 or (not my_id.isdigit())):
        return False
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