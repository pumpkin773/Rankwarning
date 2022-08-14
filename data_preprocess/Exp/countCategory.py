import os
import csv

if __name__ == '__main__':
    pro_name = 'commons-lang'
    root_path = 'D:\\graduated_design\\data_preprocess\\Exp\\'
    result_path = root_path + pro_name + '\\result\\'
    train_path = result_path + 'train\\'
    fixed_dir = 'D:\\graduated_design\\exp\\commons-lang\\fixed_repo\\'

    csv_list = os.listdir(train_path)
    category_dic = {}
    for i in csv_list:
        with open(train_path + i, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[2] not in category_dic.keys():
                    category_dic[row[2]] = 0
                else:
                    category_dic[row[2]] = category_dic.get(row[2]) + 1
        f.close()

    for i in category_dic.keys():
        print(i + ': ' + str(category_dic.get(i)))


    type_list = os.listdir(fixed_dir)
    fixed_dic = {}
    for i in type_list:
        if os.path.isdir(fixed_dir + i):
            with open(fixed_dir + i + '\\Tokens.list', 'r') as f:
                alarms = f.readlines()
            f.close()
            fixed_dic[i] = len(alarms)

    for i in category_dic.keys():
        if i not in fixed_dic.keys():
            category_dic[i] = 0
        else:
            category_dic[i] = fixed_dic.get(i) / category_dic.get(i)

    for i in category_dic.keys():
        print(i + ': ' + str(category_dic.get(i)))

    with open(result_path + '\\category_proportion.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for i in category_dic.keys():
            writer.writerow((i, category_dic.get(i)))
    f.close()



