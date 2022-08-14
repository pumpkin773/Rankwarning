import cmd_tool as ct

if __name__ == '__main__':
    #获取master的list
    project_name = 'commons-math'
    project_path = 'D:/app/IDEAworkspace/Exp_data/repos/repo-a//{}//'.format(project_name)
    git_command = 'git log master'
    # output_file = 'D://graduated_design//data_preprocess//Exp//' + project_name + '_master_commit.txt'
    output_file = 'D:\\app\\IDEAworkspace\\findbugs-violations-master\\violation-collection\\'+ project_name + '_commit.list'
    commit_list = []
    ct.change_path_to_target(project_path)
    res = ct.run_command(git_command)
    for i in res:
        if i.startswith('commit'):
            commit_id = i.split(' ')[1]
            commit_list.append(commit_id)
        print(i)
    with open(output_file, 'w') as f:
        for i in commit_list:
            f.write(i + '\n')
    f.close()

