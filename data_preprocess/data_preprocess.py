import os
import clone
import configure as c
import math


def create_repos(working_root, repo_root, repo_num):
    index = ord('a')

    for i in range(repo_num):
        repo_path = os.path.join(repo_root, 'repos-' + chr(index + i))
        working_path = os.path.join(working_root, 'working-' + chr(index + i))
        if os.path.exists(repo_path) and os.path.isdir(repo_path):
            print(repo_path + ' exists!')
        else:
            os.makedirs(repo_path)
        if os.path.exists(working_path) and os.path.isdir(working_path):
            print(working_path + ' exists!')
        else:
            os.makedirs(working_path)


# 使用ssh方式git项目
def clone_pros(repo_path, repo_pros):
    if os.path.exists(repo_path):
        for i in repo_pros:
            pro_name = i.split('/')[1].split('.git')[0]
            clone.git_clone(repo_path, pro_name, i)
    else:
        print(repo_path + ' not exists!')


if __name__ == '__main__':
    with open(c.repo_list_path) as f:
        pro_list = f.readlines()
    f.close()

    # 用来将http的git url转化为ssh的git url
    # for i in range(len(pro_list)):
    #     tokens = pro_list[i].split('https://github.com/')
    #     pro_list[i] = 'git@github.com:' + tokens[1]
    #     print(pro_list[i])
    #
    # with open('repos.list', 'w') as f:
    #     for i in pro_list:
    #         f.write(i)
    # f.close()

    size = len(pro_list)
    repo_num = math.ceil(size / c.pro_num_per_repo)

    create_repos(c.working_dir, c.repo_dir, repo_num)

    for i in range(repo_num):
        start = i * c.pro_num_per_repo
        end = start + c.pro_num_per_repo if start + c.pro_num_per_repo <= size else size
        repo_pros = pro_list[start: end]
        clone_pros(os.path.join(c.repo_dir, 'repos-' + chr(ord('a') + i)), repo_pros)
