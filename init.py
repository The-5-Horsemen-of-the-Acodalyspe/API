import subprocess

subprocess.run("rm app.db", shell=True)
subprocess.run("rm -r migrations", shell=True)
subprocess.run("pip3 install -r requirement.txt", shell=True)
subprocess.run("python3.7 -m flask db init", shell=True)
subprocess.run("python3.7 -m flask db migrate", shell=True)
subprocess.run("python3.7 -m flask db upgrade", shell=True)
subprocess.run("python3.7 -m flask run", shell=True)
