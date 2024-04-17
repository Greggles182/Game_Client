try:
    import subprocess
    process = subprocess.Popen(['git', 'fetch'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode == 0:
        print('Git status output:')
        print(stdout.decode())
    else:
        print('Error:')
        print(stderr.decode())
except Exception as e:
    print(e)