import os
import hashlib
from collections import Counter

#md5
def file_hash(file_path: str, hash_method) -> str:
    if not os.path.isfile(file_path):
        print('文件不存在。')
        return ''
    h = hash_method()
    with open(file_path, 'rb') as f:
        while True:
            b = f.read(8192)
            if not b:
                break	
            h.update(b)
    return h.hexdigest()

def file_md5(file_path: str) -> str:
    return file_hash(file_path, hashlib.md5)

#获取各文件md5值
def get_md5(path: str) -> dict:
    path_list = os.listdir(path)#获取路径下文件列表

    hash_dict = {}

    for i in path_list:
        file_path = os.path.join(path,i)
        file_mad5 = file_md5(file_path) #计算文件md5值
        hash_dict[i] = file_mad5 #导入字典
    return hash_dict

#检查重复文件
def De_duplicate(hash_dict: dict):
    values = list(hash_dict.values())
    keys = list(hash_dict.keys())

    a = dict(Counter(values))
    repeat = [key for key,value in a.items()if value > 1] #列出重复value

    indexs = []
    indexs_dict = {}
    for i in repeat:
        for index, value in enumerate(values):
            if value == i:
                indexs.append(index) #确定重复值的索引
                indexs_dict[i] = indexs
        indexs = []

    Source_Files = [] #源文件
    Link_Files = [] #链接文件

    for value in list(indexs_dict.values()):
        Source_Files.append(keys[value[0]])
        for i in value[1:]:
            Link_Files.append(keys[i])

    return Source_Files,Link_Files,repeat,values

def main(path: str):
    Source_Files , Link_Files , repeat , values = De_duplicate(get_md5(path))

    N = []
    for i in repeat:
        N.append(values.count(i)) #统计各value出现次数
    
    for n in N:
        i = 0
        for source_file in Source_Files:
            for i in range(1,n):
                link_file = Link_Files[i-1]
                link_path = path+link_file
                source_path = path+source_file
                os.system("del %s"%link_path)
                os.system("mklink %s %s"%(link_path,source_path))
    os.system("pause")

if __name__ == "__main__":
    main("C:\\Users\\c1826\\Desktop\\TEST\\")