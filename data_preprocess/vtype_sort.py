import csv

with open(r"D:\graduated_design\findbugs-violations-master\violation-collection\commons-lang-vtype-stat1.csv", 'r') as f:
    vtypes = f.readlines()
f.close()

data = []
for vtype in vtypes:
    tokens = vtype.split("=>")
    type = tokens[0]
    count = int(tokens[1].strip())
    data.append([type, count])

data.sort(key=lambda x: x[1], reverse=True)
print(data)

with open("types.list", 'w') as f:
    for i in data:
        f.write(i[0] + '\n')
f.close()

with open("top-vtype.csv", 'w', encoding='utf-8',newline="") as f:
    writer = csv.writer(f)
    for i in data:
        writer.writerow([i[0]])
f.close()
