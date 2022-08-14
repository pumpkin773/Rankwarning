import os
import csv

if __name__ == '__main__':
    alarm_path = 'D:\\graduated_design\\data_preprocess\\Exp\\maven-dependency-plugin\\alarm.csv'
    min1 = 1
    min2 = 1
    max1 = 0
    max2 = 0
    row_list = []
    with open(alarm_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if float(row[11]) > max1:
                max1 = float(row[11])
            if float(row[11]) < min1:
                min1 = float(row[11])
            if float(row[12]) > max2:
                max2 = float(row[12])
            if float(row[12]) < min2:
                min2 = float(row[12])
            row_list.append(row)
    for i in row_list:
        i[11] = str((float(i[11]) - min1) / (max1 - min1))
        i[12] = str((float(i[12]) - min2) / (max2 - min2))
    with open('D:\\graduated_design\\data_preprocess\\Exp\\maven-dependency-plugin\\alarm_normal.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for i in row_list:
            writer.writerow(i)
    f.close()

