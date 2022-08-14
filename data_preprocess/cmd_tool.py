import os
import sys

def change_path_to_target(path):
    commendline = path
    os.chdir(commendline)

def run_command(command):
    com_res = os.popen(command)
    com_res = com_res.buffer.read().decode(encoding = 'utf-8',errors = 'ignore')
    return com_res.split('\n')

if __name__ == '__main__':
    cmd = sys.argv[1]
    run_command(cmd)
    # run_command("md D:\\data\\temp\\git")
    # run_command("Xcopy D:\\data\\repos\\repos-a\\AndroidFT D:\\data\\temp\\git\\ /E/H/C/I")
    # run_command("md D:\\data\\temp\\mvn")