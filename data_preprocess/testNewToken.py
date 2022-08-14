import os

if __name__ == "__main__":
    file_path = "D:\data\FixedViolations\selectedData\SelectedNewTokens.list"
    with open(file_path, 'r') as f:
        newTokens = f.readlines()
    f.close()
    newTokenSet = []
    for newToken in newTokens:
        words = newToken.strip().split(" ")
        for word in words:
            if word not in newTokenSet:
                newTokenSet.append(word)
    print(len(newTokenSet))