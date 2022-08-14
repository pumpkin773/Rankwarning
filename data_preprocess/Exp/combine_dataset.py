import os
import csv

if __name__ == '__main__':
    root_dir = 'D:\\data_repo\\data\\commons-lang\\list\\'
    alarm_file = root_dir + 'alarm.csv'
    output_file = root_dir + 'output.txt'
    test_file = 'D:\\graduated_design\\data_preprocess\\Exp\\commons-lang\\result\\test\\bb8709f3e30e7c13530dfef458a4c370783de2be.csv'
    category_proportion_path = 'D:\\graduated_design\\data_preprocess\\Exp\\commons-lang\\result\\category_proportion.csv'
    category_dic = {}

    with open(category_proportion_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            category_dic[row[0]] = row[1]
    f.close()

    with open(output_file, 'r') as f:
        res_list = f.readlines()
    f.close()

    alarm_list = []
    with open(alarm_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            alarm_list.append(row)
    f.close()

    for i in range(len(alarm_list)):
        res = res_list[i].strip()
        if res == 'unknown':
            alarm_list[i].append('-1')
            alarm_list[i].append('-1')
            alarm_list[i].append('-1')
            alarm_list[i].append('-1')
        else:
            similarity_list = res.split(' ')
            proportion = float(category_dic.get(alarm_list[i][2]))
            alarm_list[i].append(similarity_list[0])
            alarm_list[i].append(similarity_list[1])
            similarity1 = float(similarity_list[2]) * proportion
            similarity2 = float(similarity_list[3]) * proportion
            # similarity1 = float(similarity_list[2])
            # similarity2 = float(similarity_list[3])
            alarm_list[i].append(str(similarity1))
            alarm_list[i].append(str(similarity2))

    final_res = []
    with open(test_file, 'r') as f:
        reader = csv.reader(f)

        for row in reader:
            flag = False
            for j in alarm_list:
                if row[0] == j[0] and row[1] == j[1] and row[2] == j[2] and row[3] == j[3] and row[4] == j[4] and row[5] == j[5] and row[6] == j[6] and row[7] == j[7]:
                    flag = True
                    row.append(j[8])
                    row.append(j[9])
                    row.append(j[10])
                    row.append(j[11])
                    final_res.append(row)
                    break
            if not flag:
                row.append('-2')
                row.append('-2')
                row.append('-2')
                row.append('-2')
                final_res.append(row)


    with open('commons-lang/alarm_nomal.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(final_res)
    f.close()

