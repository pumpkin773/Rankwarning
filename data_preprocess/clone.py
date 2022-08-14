import cmd_tool
import os


def git_clone(repo_path, pro_name, git_url):
    pro_path = os.path.join(repo_path, pro_name)
    # 从远程仓库将代码下载到上面创建的目录中
    if not os.path.exists(pro_path):
        git_clone_command = 'git clone ' + git_url
        cmd_tool.change_path_to_target(repo_path)
        cmd_tool.run_command(git_clone_command)
    else:
        print(pro_name + " exists!")