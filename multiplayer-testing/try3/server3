from flask import Flask, request, jsonify

app = Flask(__name__)

variables = {}

@app.route('/get_variable', methods=['GET'])
def get_variable():
    variable_name = request.args.get('name')
    return jsonify({variable_name: variables.get(variable_name, None)})

@app.route('/update_variable', methods=['POST'])
def update_variable():
    data = request.json
    variable_name = data['name']
    value = data['value']
    variables[variable_name] = value
    return 'Variable updated successfully'

if __name__ == '__main__':
    app.run(debug=True)
