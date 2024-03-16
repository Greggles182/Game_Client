import requests

#SERVER_URL = "http://localhost:5000"
#SERVER_URL = "http://gregglesthegreat.pythonanywhere.com/"

def get_variable(SERVER_URL,variable_name):
    response = requests.get(f"{SERVER_URL}/get_variable?name={variable_name}")
    return response.json().get(variable_name)

def update_variable(SERVER_URL,variable_name, value):
    data = {"name": variable_name, "value": value}
    response = requests.post(f"{SERVER_URL}/update_variable", json=data)
    if response.ok:
        print("Variable updated successfully")
    else:
        print("Failed to update variable")

# Example usage:
if __name__ == "__main__":
    var_value = str(get_variable("http://gregglesthegreat.pythonanywhere.com/","l_pgp_Player2"))
    print("Currently: " + var_value)
    new_value = input("Enter a new value for example_variable: ")
    update_variable("http://gregglesthegreat.pythonanywhere.com/","l_pgp_Player2", new_value)
