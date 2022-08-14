import os
import configure as c

if __name__ == "__main__":
    workings = os.listdir(c.working_dir)
    for i in workings:
        print('Now process ' + i)
        print('--------------------------------------------')
        working_path = os.path.join(c.working_dir, i)
        shell_dir_path = os.path.join(working_path, 'shell')
        shells = os.listdir(shell_dir_path)
        for j in shells:
            print('process ' + j)
            shell_path = os.path.join(shell_dir_path, j)
            os.popen('bash ' + shell_path)
        print('--------------------------------------------')
