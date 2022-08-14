#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import shutil
import csv


def choose_test():
    test_commit = ''
    positive_num = 0
    for i in commit_dic.keys():
        length = len(commit_dic.get(i))
        if length > positive_num:
            positive_num = length
            test_commit = i
    shutil.copyfile(result_report_dir + test_commit + '.csv', test_dir + test_commit + '.csv')


def choose_train(test_commit):
    with open(commit_sort_list, 'r') as f:
        commits = f.readlines()
    f.close()

    with open(result_dir + 'exist_positive_warning_commit.list', 'r') as f:
        p_commits = f.readlines()
    f.close()

    train_commits = []
    test_commits = []

    flag = False
    for i in commits:
        if flag and os.path.exists(result_report_dir + i.strip() + '.csv'):
            train_commits.append(i)
        if i.strip() == test_commit:
            flag = True
    for i in train_commits:
        shutil.copyfile(result_report_dir + i.strip() + '.csv', train_dir + i.strip() + '.csv')

    j = 0
    for i in p_commits:
        j += 1
        i = i.split()[0]
        if j%5==0 and os.path.exists(result_report_dir + i + '.csv'):
            test_commits.append(i)
        if i == test_commit:
            test_commits.append(i)
            break
    for i in test_commits:
        shutil.copyfile(result_report_dir + i + '.csv', test_dir + i + '.csv')

    with open(result_dir + 'train_commit.list', 'w') as f:
        for i in train_commits:
            f.write(i)
    f.close()


if __name__ == '__main__':
    pro_name = 'commons-math'
    #该项目的Exp文件夹，存放项目划分的结果
    root_dir = 'D:\\app\\IDEAworkspace\\data_preprocess\\Exp\\{}\\'.format(pro_name)
    #跟踪完警告后一步生成的正报警告list，即--项目名.list
    alarm_file = 'D:\\app\\IDEAworkspace\\data_preprocess\\Exp\\{}\\result\\{}.list'.format(pro_name, pro_name)
    #项目所有的SAT扫描出来的报告的上级目录，替换符替换项目
    report_dir = 'D:\\app\\IDEAworkspace\\Exp_data\\workings\\working-a\\reports\\{}\\'.format(pro_name)
    #这些目录需要手动创建一下
    result_dir = root_dir + 'result\\'
    #所有划分正误报的报告
    result_report_dir = result_dir + 'reports\\'
    #所有正保报告
    result_positive_dir = result_dir + 'positive_reports\\'
    test_dir = result_dir + 'test\\'
    train_dir = result_dir + 'train\\'
    #所有commitlist（复制过来）
    commit_sort_list = result_dir + '{}_commit.list'.format(pro_name)
    commit_dic = {}
    commit_list = []


    with open(alarm_file, 'r') as f:
        alarm_list = f.readlines()
    f.close()

    for i in alarm_list:
        tokens = i.strip().split(':')
        pro = tokens[0]
        commit_id = tokens[1]
        vtype = tokens[2]
        path = tokens[3]
        start = tokens[4]
        end = tokens[5]

        if commit_id not in commit_dic.keys():
            commit_dic[commit_id] = [[vtype, path, start, end]]
        else:
            commit_dic[commit_id].append([vtype, path, start, end])

    print('All positive_reports: ' + str(len(commit_dic.keys())))
    cm = []
    for i in commit_dic.keys():
        cm.append(i)
    cm.sort()

    counter = 0
    for i in cm:
        num = len(commit_dic.get(i))
        print(i + ': ' + str(num))
        counter += num
    print('All positive warning: ' + str(counter))

    for i in os.listdir(report_dir):
        with open(report_dir + i, 'r') as f:
            rows = f.readlines()
        f.close()
        warnings = []
        commit = i[0:-4]
        if commit not in commit_dic.keys():
            for j in rows:
                row = j.strip().replace('"', '').split(',')
                row.append('0')
                warnings.append(row)
        else:
            for j in rows:
                row = j.strip().replace('"', '').split(',')
                alarms = commit_dic.get(commit)
                flag = False
                for k in alarms:
                    if row[2] == k[0] and row[3].split('$')[0] == k[1] and row[6] == k[2] and row[7] == k[3]:
                        row.append('1')
                        warnings.append(row)
                        flag = True
                        break
                if not flag:
                    row.append('0')
                    warnings.append(row)
        with open(result_report_dir + commit + '.csv', 'w',encoding='utf8', newline='') as f:
            writer = csv.writer(f)
            for m in warnings:
                writer.writerow(m)
        f.close()

    with open(commit_sort_list, 'r') as f:
        commits = f.readlines()
    f.close()

    for commit in commits:
        for i in commit_dic.keys():
            if commit.strip() == i:
                str_list = ''
                str_list += (i + ' ' + str(len(commit_dic.get(i))) + '\n')
                commit_list.append(str_list)
                break
    #生成存在正保的commit的list
    with open(result_dir + 'exist_positive_warning_commit.list', 'w') as f:
        for i in commit_list:
            f.write(i)
    f.close()

    for i in commit_list:
        shutil.copyfile(result_report_dir + i.strip().split(' ')[0] + '.csv', result_positive_dir + i.strip().split(' ')[0] + '.csv')

    #寻找一个分界点
    # choose_train("7c82547037f037765d9bb8adff2308721265da84")