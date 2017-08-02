#!/usr/bin/python
import subprocess
import socket

port = 8888
host = "0.0.0.0"


def execute(cmd, process_input=None, addl_env=None,
            return_stderr=False, run_as_root=False):
    obj, cmd = create_process(cmd, run_as_root=run_as_root,
                              addl_env=addl_env)
    _stdout, _stderr = obj.communicate(process_input)
    obj.stdin.close()

    return (_stdout, _stderr) if return_stderr else _stdout


def create_process(cmd, run_as_root=False, addl_env=None):
    """Create a process object for the given command.
    """
    if addl_env is None:
        addl_env = []
    else:
        addl_env = ['env'] + ['%s=%s' % pair for pair in addl_env.items()]
    cmd = list(map(str, addl_env + cmd))
    if run_as_root:
        cmd = ['sudo'] + cmd
    obj = subprocess.Popen(cmd, shell=False,
                           stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)

    return obj, cmd


def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(1)
    while True:
        cli_sock, addr = sock.accept()
        recv_data = cli_sock.recv(1024).strip()
        if not recv_data:
            cli_sock.close()
            continue
        return_data = ""
        try:
            return_data = execute(["./example1", recv_data])
        finally:
            if return_data:
                cli_sock.send(return_data)
            cli_sock.close()


if __name__ == "__main__":
    server()

