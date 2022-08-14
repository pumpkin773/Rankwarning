import cmd_tool as ct
import os

if __name__ == '__main__':
    project_name = 'commons-lang'
    project_path = 'D://data//repos//repos-a//{}//'.format(project_name)
    git_tag_command = 'git tag'
    git_show_command = 'git show {}'
    output_file = 'D://graduated_design//data_preprocess//Exp//commons-lang//' + project_name + '_tag.list'
    master_commit_file = 'D://graduated_design//data_preprocess//Exp//commons-lang//result//commons-lang_commit.list'
    revision_file = 'D://graduated_design//data_preprocess//Exp//commons-lang//result//commons-lang_revision.list'
    tag_list = []
    master_commit_list = []
    tag_commit_list = {}
    final_commit_list = []
    ct.change_path_to_target(project_path)
    res = ct.run_command(git_tag_command)
    for i in res:
        if i != '':
            tag_list.append(i)

    with open(master_commit_file, 'r') as f:
        lines = f.readlines()
    f.close()
    for line in lines:
        master_commit_list.append(line.strip())

    for i in tag_list:
        ct.change_path_to_target(project_path)
        command = git_show_command.format(i)
        res = ct.run_command(command)
        for j in res:
            if j.startswith('commit'):
                commit_id = j.split(' ')[1]
                tag_commit_list[i] = commit_id
        print(i)

    if not os.path.exists(output_file):
        with open(output_file, 'w') as f:
            for i in tag_commit_list.keys():
                f.write(tag_commit_list.get(i) + ' ' + i + '\n')
        f.close()

    for i in tag_commit_list.values():
        if i in master_commit_list:
            final_commit_list.append(tag_commit_list.get(i) + ' ' + i)

    with open(revision_file, 'w') as f:
        for i in final_commit_list:
            f.write(i + '\n')
    f.close()