import os
#引入系统 operation system

print(os.name)
#这个名称也决定了模块中哪些功能是可用的，哪些是没有相应实现的。

print(os.environ["HOMEPATH"])
#HOMEPATH”（Windows 下，Linux 下为“HOME”）的项，对应的值就是用户主目录的路径。

for item in os.walk("."):
    print(item)
#这个函数需要传入一个路径作为top参数，
# 函数的作用是在以top为根节点的目录树中游走，
# 对树中的每个目录生成一个由(dirpath, dirnames, filenames)三项组成的三元组。

def get_filelists(file_dir='.'):
     list_directory = os.listdir(file_dir)
     filelists = []
     for directory in list_directory:
         if(os.path.isfile(directory)):
             filelists.append(directory)
     return filelists
#列出（当前）目录下的全部路径（及文件）
#默认为“.”，即“当前路径”

os.mkdir("hello")
#创建一个名为hello的文件夹，
# 如果指定路径已存在，则会抛出FileExistsError异常。

os.removedir("文件夹名")
#删除源路径的最下级目录。

os.remove("文件名")
#用于删除文件，
# 如果指定路径是目录而非文件的话，就会抛出IsADirectoryError异常。

os.rename()
#该函数的作用是将文件或路径重命名，
# 一般调用格式为os.rename(src, dst)，即将src指向的文件或路径重命名为dst指定的名称。

os.getcwd()
#获得当前工作路径

os.chdir()
#改变当前工作路劲为。。。

os.path.join("just", "do", "python", "dot", "com")
os.path.join("just", "do", "d:/", "python", "dot", "com")
#可以将多个传入路径组合为一个路径
#但如果传入路径中存在一个“绝对路径”格式的字符串，
# 且这个字符串不是函数的第一个参数，
# 那么其他在这个参数之前的所有参数都会被丢弃，余下的参数再进行组合。
