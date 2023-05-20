from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/writefile', methods=['POST'])
def write_file():
    content = request.json['content']
    
    try:
        with open('file.txt', 'w') as file:
            file.truncate(0)
            file.write(content)
        return jsonify({'message': 'CIAO'}), 200
    except Exception as e:
        print(str(e))
        return jsonify({'message': 'Error writing file'}), 500

if __name__ == '__main__':
    app.run(port=3000)


#Linux disable cors
#google-chrome --disable-web-security

#Mac disable cors
#open -n -a /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --args --user-data-dir="/tmp/chrome_dev_test" --disable-web-security

#Run server
#python3 server.py 
