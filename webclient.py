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
    import time
    SERVER_URL = input("Enter server URL or press Enter to use default: ")
    if  SERVER_URL == "":
        SERVER_URL = "http://gregglesthegreat.pythonanywhere.com/"
    start = time.time()
    var_value = str(get_variable(SERVER_URL,"d_pgp_LOGIN"))
    end = time.time()
    timed = (end-start)*1000
    print("Currently: " + var_value)
    print(f"Took {timed} milliseconds")
    # new_value = input("Enter a new value for example_variable: ")
    new_value = {'muffin' : 'lolz', 'foo' : 'kitty'}
    start = time.time()
    update_variable(SERVER_URL,"d_pgp_LOGIN", new_value)
    end = time.time()
    timed = (end-start)*1000
    print(f"Took {timed} milliseconds")


