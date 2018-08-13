"""setting.py"""
import subprocess
from time import sleep

def execute(cmd: str, print_cmd=False) -> None:
    """
    Execute the command at the command prompt.

    Parameters
    ----------
    cmd : str
        The command you want to execute
    print_cmd : bool
        Whether to print cmd.
    """
    if print_cmd:
        print(cmd)

    subprocess.run(cmd, shell="True")
    print("-" * 30)

if __name__ == '__main__':
    print("Start initial setting.")
    print("-" * 30)
    print("install required package.")
    print("-" * 30)
    execute("pip install bottle", True)
    execute("pip install gevent", True)
    execute("pip install gevent-websocket", True)
    execute("pip install mypy", True)
    execute("pip install requests", True)
    print("pip install was completed.")
    print("-" * 30)
    execute("python bottler.py")
    