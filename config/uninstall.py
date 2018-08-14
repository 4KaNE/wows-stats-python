"""install.pyでインストールしたpipライブラリを削除します"""
import subprocess
from time import sleep

def execute(cmd: str, print_cmd=True) -> None:
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
    execute("pip uninstall bottle")
    execute("pip uninstall gevent")
    execute("pip uninstall gevent-websocket")
    execute("pip uninstall bottle-websocket")
    execute("pip uninstall karellen-geventws")
    execute("pip uninstall mypy")
    execute("pip uninstall requests")
    print("pip uninstallation completed")
    print("This window will close automatically after 20 seconds")
    sleep(20)