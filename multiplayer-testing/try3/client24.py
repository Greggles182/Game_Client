import requests

SERVER_URL = 'http://localhost:5000'

def get_variable(variable_name):
    response = requests.get(f'{SERVER_URL}/get_variable?name={variable_name}')
    return response.json().get(variable_name)

def update_variable(variable_name, value):
    data = {'name': variable_name, 'value': value}
    response = requests.post(f'{SERVER_URL}/update_variable', json=data)
    if response.ok:
        print('Variable updated successfully')
    else:
        print('Failed to update variable')

# Example usage:
new_value = 203
var_value = get_variable('example_variable')
update_variable('example_variable', new_value)
