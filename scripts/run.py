import subprocess

def run(*args):
  subprocess.run(["poetry", "run", *args], check=True)

def dev():
  run("uvicorn", "mjw_server.main:app", "--reload")
