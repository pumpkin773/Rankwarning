import os

if __name__ == "__main__":
    file_path = "D:\\data\\Alarms\\"
    type_list = os.listdir(file_path)
    for t in type_list:
        if os.path.isdir(file_path + t):
            with open(file_path + t + "\\20_CNNoutput.csv", 'r') as f:
                data = f.readlines()
            f.close()

            with open(file_path + t + "\\sourceCodeFeatures.list", 'w') as f:
                for d in data:
                    f.write(d)
            f.close()