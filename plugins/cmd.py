import subprocess

def run(value, params):
    command = [params["cmd"]]
    for arg in args:
        command.append(arg)
    subprocess.call(command)
