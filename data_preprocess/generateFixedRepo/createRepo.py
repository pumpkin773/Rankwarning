import os
import conf
import shutil


def create_dir():
    if not os.path.exists(conf.fixed_dir):
        os.makedirs(conf.fixed_dir)

    type_list = os.listdir(conf.old_fixed_data_dir)
    for t in type_list:
        if os.path.exists(conf.fixed_dir + t):
            shutil.rmtree(conf.fixed_dir + t)
        os.mkdir(conf.fixed_dir + t)


# def data_prepare_cluster():
#     type_list = os.listdir(conf.old_fixed_data_dir)
#     for t in type_list:
#         type_dir = conf.old_fixed_data_dir + t
#
#         cluster_file = os.path.join(type_dir, 'clusterOutput.list')
#         with open(cluster_file, 'r') as f:
#             cluster_list = f.readlines()
#         f.close()
#         token_file = os.path.join(type_dir, 'Tokens.list')
#         with open(token_file, 'r') as f:
#             token_list = f.readlines()
#         f.close()
#         feature_file = os.path.join(type_dir, 'LearnedFeatures', '1_CNNoutput.csv')
#         with open(feature_file, 'r') as f:
#             feature_list = f.readlines()
#         f.close()
#         vectorized_token_file = os.path.join(type_dir, 'vectorizedTokens.csv')
#         with open(vectorized_token_file, 'r') as f:
#             vectorized_token_list = f.readlines()
#         f.close()
#
#         size = len(cluster_list)
#         cluster_dic = {}
#         for i in range(size):
#             temp_cluster = cluster_list[i].strip()
#             if temp_cluster not in cluster_dic.keys():
#                 cluster_dir = os.path.join(conf.fixed_dir, t, 'Cluster_' + temp_cluster)
#                 os.mkdir(cluster_dir)
#                 cluster_dic[temp_cluster] = ([token_list[i]], [feature_list[i]], [vectorized_token_list[i]])
#             else:
#                 cluster_dic[temp_cluster][0].append(token_list[i])
#                 cluster_dic[temp_cluster][1].append(feature_list[i])
#                 cluster_dic[temp_cluster][2].append(vectorized_token_list[i])
#
#         for i in cluster_dic.keys():
#             tokens = cluster_dic[i][0]
#             features = cluster_dic[i][1]
#             vectorized_tokens = cluster_dic[i][2]
#             tokens_file = os.path.join(conf.fixed_dir, t, 'Cluster_' + i, 'Tokens.list')
#             features_file = os.path.join(conf.fixed_dir, t, 'Cluster_' + i, 'Features.list')
#             vectorized_tokens_file = os.path.join(conf.fixed_dir, t, 'Cluster_' + i, 'VectorizedTokens.list')
#             with open(tokens_file, 'w') as f:
#                 for j in tokens:
#                     f.write(j)
#             f.close()
#             with open(features_file, 'w') as f:
#                 for j in features:
#                     f.write(j)
#             f.close()
#             with open(vectorized_tokens_file, 'w') as f:
#                 for j in vectorized_tokens:
#                     f.write(j)
#             f.close()


def data_prepare():
    type_list = os.listdir(conf.old_fixed_data_dir)
    print('--------------------------------------')
    for t in type_list:
        type_dir = os.path.join(conf.old_fixed_data_dir, t)
        target_dir = os.path.join(conf.fixed_dir, t)

        token_file = os.path.join(type_dir, 'Tokens.list')
        simplify_token_file = os.path.join(type_dir, 'NewTokens.list')
        vectorized_token_file = os.path.join(type_dir, 'vectorizedTokens.csv')
        vectorized_new_token_file = os.path.join(type_dir, 'vectorizedNewTokens.csv')

        target_token_file = os.path.join(target_dir, 'Tokens.list')
        target_simplify_token_file = os.path.join(target_dir, 'NewTokens.list')
        target_vectorized_token_file = os.path.join(target_dir, 'vectorizedTokens.csv')
        target_vectorized_new_token_file = os.path.join(target_dir, 'vectorizedNewTokens.csv')

        command1 = 'copy {} {}'.format(token_file, target_token_file)
        command2 = 'copy {} {}'.format(simplify_token_file, target_simplify_token_file)
        command3 = 'copy {} {}'.format(vectorized_token_file, target_vectorized_token_file)
        command4 = 'copy {} {}'.format(vectorized_new_token_file, target_vectorized_new_token_file)
        os.system(command1)
        os.system(command2)
        os.system(command3)
        os.system(command4)


def generate_new_tokens():
    type_list = os.listdir(conf.fixed_dir)
    for t in type_list:
        type_dir = os.path.join(conf.fixed_dir, t)
        token_file = os.path.join(type_dir, 'Tokens.list')
        with open(token_file, 'r') as f:
            tokens = f.readlines()
        f.close()
        new_tokens = []
        for token in tokens:
            token = token.strip()
            words = token.split(' ')
            new_words = []
            for i in range(len(words)):
                if i % 2 == 0:
                    new_words.append(words[i])
            new_token = ''
            for i in range(len(new_words) - 1):
                new_token = new_token + new_words[i] + ' '
            new_token = new_token + new_words[len(new_words) - 1] + '\n'
            new_tokens.append(new_token)
        new_token_file = os.path.join(type_dir, 'NewTokens.list')
        with open(new_token_file, 'w') as f:
            for i in new_tokens:
                f.write(i)
        f.close()

def generate_fixed_sql_script():
    sql_template = 'CREATE DATABASE IF NOT EXISTS data_repo;\n' + \
                   'USE data_repo;\n' + \
                   'DROP TABLE IF EXISTS `FixedPattern`;\n' + \
                   'CREATE TABLE `FixedPattern` (\n' + \
                   '`id` INT(20) NOT NULL PRIMARY KEY AUTO_INCREMENT,\n' + \
                   '`vtype` TEXT NOT NULL,\n' + \
                   '`token` TEXT NOT NULL,\n' + \
                   '`simplify_token` TEXT NOT NULL,\n' + \
                   '`vectorized_token` LONGTEXT NOT NULL,\n' + \
                   '`vectorized_new_token` LONGTEXT NOT NULL\n' + \
                   ')ENGINE=INNODB DEFAULT CHARSET=utf8;\n' + \
                   'INSERT INTO `FixedPattern` (vtype, token, simplify_token, vectorized_token, vectorized_new_token) VALUES\n'

    insert_template = "('{}', '{}', '{}', '{}', '{}'),\n"

    inserts = []
    type_list = os.listdir(conf.fixed_dir)
    for t in type_list:
        if os.path.isdir(os.path.join(conf.fixed_dir, t)):
            vtype = t
            token_file = os.path.join(conf.fixed_dir, t, 'Tokens.list')
            new_token_file = os.path.join(conf.fixed_dir, t, 'NewTokens.list')
            vectorized_token_file = os.path.join(conf.fixed_dir, t, 'vectorizedTokens.csv')
            vectorized_new_token_file = os.path.join(conf.fixed_dir, t, 'vectorizedNewTokens.csv')

            with open(token_file, 'r') as f:
                tokens = f.readlines()
            f.close()
            with open(new_token_file, 'r') as f:
                new_tokens = f.readlines()
            f.close()
            with open(vectorized_token_file, 'r') as f:
                vectorized_tokens = f.readlines()
            f.close()
            with open(vectorized_new_token_file, 'r') as f:
                vectorized_new_tokens = f.readlines()
            f.close()

            for i in range(len(tokens)):
                token = tokens[i].strip()
                new_token = new_tokens[i].strip()
                vectorized_token = vectorized_tokens[i].strip()
                vectorized_new_token = vectorized_new_tokens[i].strip()
                insert_statement = insert_template.format(vtype, token, new_token, vectorized_token, vectorized_new_token)
                inserts.append(insert_statement)

    for i in range(len(inserts) - 1):
        sql_template = sql_template + inserts[i]
    sql_template = sql_template + inserts[len(inserts) - 1][:-2]

    sql_script = os.path.join(conf.fixed_dir, 'data_repo.sql')
    with open(sql_script, 'w') as f:
        f.write(sql_template)
    f.close()



if __name__ == '__main__':
    create_dir()
    #
    data_prepare()

    # generate_new_tokens()

    generate_fixed_sql_script()

    sql_template = 'CREATE DATABASE IF NOT EXISTS data_repo;\n' + \
                   'USE data_repo;\n' + \
                   'DROP TABLE IF EXISTS `PatchPattern`;\n' + \
                   'CREATE TABLE `PatchPattern` (\n' + \
                   '`id` INT(20) NOT NULL PRIMARY KEY AUTO_INCREMENT,\n' + \
                   '`vtype` TEXT NOT NULL,\n' + \
                   '`token` TEXT NOT NULL,\n' + \
                   '`editScript` TEXT NOT NULL,\n' + \
                   '`patchAST` TEXT NOT NULL\n' + \
                   ')ENGINE=INNODB DEFAULT CHARSET=utf8;\n' + \
                   'INSERT INTO `PatchPattern` (vtype, token, editScript, patchAST) VALUES\n'

    insert_template = "('{}', '{}', '{}', '{}'),\n"

    inserts = []
    token_file = os.path.join(conf.patch_dir, 'tokens.list')
    edit_script_file = os.path.join(conf.patch_dir, 'editScripts.list')
    type_file = os.path.join(conf.patch_dir, 'alarmTypes.list')
    patch_source_code_file = os.path.join(conf.patch_dir, 'patchSourceCode.list')

    with open(token_file, 'r') as f:
         tokens = f.readlines()
    f.close()
    with open(edit_script_file, 'r') as f:
         edit_scripts = f.readlines()
    f.close()
    with open(type_file, 'r') as f:
        types = f.readlines()
    f.close()
    with open(patch_source_code_file, 'r') as f:
        patch_source_codes = f.readlines()
    f.close()

    typelist = []
    patches = []
    patchAST = ''
    flag = False
    flag1 = False
    counter = 0
    for line in patch_source_codes:
        if line == 'AST Diff###:\n':
            flag = True
            counter += 1
            continue
        if line == '\n':
            if len(patchAST) != 0:
                patches.append(patchAST)
                patchAST = ''
                flag = False
        if flag:
            patchAST += (line)
    print(counter)


    for i in range(len(tokens)):
        token = tokens[i].strip()
        edit_script = edit_scripts[i].strip()
        vtype = types[i].strip()
        patch = patches[i].strip()
        insert_statement = insert_template.format(vtype, token, edit_script, patch)
        inserts.append(insert_statement)

    for i in range(len(inserts) - 1):
        sql_template = sql_template + inserts[i]
    sql_template = sql_template + inserts[len(inserts) - 1][:-2]

    sql_script = os.path.join(conf.fixed_dir, 'data_repo2.sql')
    with open(sql_script, 'w') as f:
        f.write(sql_template)
    f.close()




