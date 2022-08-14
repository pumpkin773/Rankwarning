import os

if __name__ == '__main__':
    fixed_path = 'D:\\data\\FixedViolations\\Types'
    fixed_cluster_path = 'D:\\data\\fixedViolationsClusters\\'
    type_list = os.listdir(fixed_path)
    for t in type_list:
        if not os.path.exists(fixed_cluster_path + t):
            os.makedirs(fixed_cluster_path + t)