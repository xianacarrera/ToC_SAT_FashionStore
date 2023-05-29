from flask import Flask, request, jsonify
import sys
sys.path.append('../')
import main


app = Flask(__name__)

def check_validity(file_path):
    file_path = file_path
    garments, colors = main.read_input_from_file(file_path)
    solution = main.encode_fashion_store_problem(garments, colors)

    print("\n\n")
    if solution:
        print("SATISFIABLE:")
        for garment, color in zip(garments, colors):
            print(f"Garment: {garment}, Color: {color}")
        return ("SATISFIABLE")
    else:
        print("UNSATISFIABLE")
        return ("UNSATISFIABLE")
    
@app.route('/writefile', methods=['POST'])
def write_file():
    content = request.json['content']
    
    try:
        with open('file.txt', 'w') as file:
            file.truncate(0)
            file.write(content)
        # solution = main.run()
        solution = check_validity("file.txt")
        return jsonify({'message': solution}), 200
    

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
