from flask import Flask, request, jsonify, render_template
#from threading import Thread

app = Flask(__name__)
variables = {}


@app.route('/')
def home():
    return render_template('index.html')
    # return """Hello. I am alive! I am a Discord bot!</br>I am cool.</br>
    # <iframe src="https://discord.com/widget?id=1081525939726462986&theme=dark" width="350" height="500" allowtransparency="true" frameborder="0" sandbox="allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts"></iframe>"""
    # <link rel="shortcut icon" href="{{ url_for('static', filename='favicon.ico') }}">

# def run():
#     app.run(debug=True)
#     #app.run()


# def keep_alive():
#     print("Hello World!")
#     run()
#     #t = Thread(target=run)
#     #t.start
@app.route('/list_variables', methods=['GET'])
def list_variables():
    return variables

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
