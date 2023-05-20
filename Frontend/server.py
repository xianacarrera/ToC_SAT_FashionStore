from flask import Flask, request

app = Flask(__name__)

@app.route('/writefile', methods=['POST'])
def write_file():
    content = request.json['content']
    
    try:
        with open('file.txt', 'w') as file:
            file.truncate(0)
            file.write(content)
        return '', 200
    except Exception as e:
        print(str(e))
        return 'Error writing file', 500

if __name__ == '__main__':
    app.run(port=3000)





#open -n -a /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --args --user-data-dir="/tmp/chrome_dev_test" --disable-web-security
#python3 server.py 
