try:
    import os
    destination_path = "Game/"
    clone_command = "git clone https://github.com/Greggles182/Assesment-Y7.git"
    clone_with_path = clone_command + " " + destination_path
    os.system(clone_with_path)
    os.chdir(destination_path)
    with open("requirements.txt", "w") as f:
        f.write("""""")
except Exception as e:
    print(e)