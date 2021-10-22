#!/usr/bin/env python3

from flask import Flask, render_template
import os, sys, subprocess, re, requests, argparse

app = Flask(__name__)

# arguments
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--listen-port", dest = "listen_port", default=8888, type=int)
parser.add_argument("-d", "--directory", dest = "directory", default="/home/coder")
parser.add_argument("-a", "--app", dest = "application", default="jetbrains", choices=['vscode', 'jetbrains'])
parser.add_argument("-s", "--start-command", dest = "start_command", default="false")

args = parser.parse_args()

# start the application, if passed through
if args.start_command != "false":
    import subprocess
    subprocess.Popen(args.start_command.split ( ), close_fds=False)

@app.route('/health')
def health():
    return 'OK'

@app.route('/')
def instructions():

    if args.application == "jetbrains":

        # get the URL
        result = subprocess.run(["/bin/bash", "/coder/apps/jetbrains-gateway/find_url.sh"], capture_output=True, text=True)
    
        if not result.stdout:
            return render_template(
                'jetbrains_loading.html',
                description=result.stderr,
            ),{"Refresh": "1; url=."}


        return render_template(
            'jetbrains.html',
            title=("How to open \"% s\" in JetBrains Gateway" % (os.environ.get('CODER_ENVIRONMENT_NAME'))),
            url=result.stdout
        )
    
    elif args.application == "vscode":

        url = ("vscode://vscode-remote/ssh-remote+coder.% s% s" % (os.environ.get('CODER_ENVIRONMENT_NAME'), args.directory))

        return render_template(
            'vscode.html',
            title=("How to open \"% s\" in VS Code - Remote SSH" % (os.environ.get('CODER_ENVIRONMENT_NAME'))),
            url=url
        )

if __name__ == '__main__':
    app.run(debug=True, port=args.listen_port)