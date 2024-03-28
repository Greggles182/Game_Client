import subprocess, pygame, os  #, game

print("Game starting")
# Run git status
process = subprocess.Popen(['git', 'status'],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
stdout, stderr = process.communicate()

if process.returncode == 0:
    print('Git status output:')
    print(stdout.decode())
else:
    print('Error:')
    print(stderr.decode())
process = subprocess.Popen(['git', 'fetch'],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
stdout, stderr = process.communicate()

if process.returncode == 0:
    print('Git fetch output:')
    print(stdout.decode())
else:
    print('Error:')
    print(stderr.decode())
