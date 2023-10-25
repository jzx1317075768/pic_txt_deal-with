# 导入所需的模块
import os
import zipfile
import time
import shutil
import re

# 记录开始时间
start_time = time.time()

# 解压文件到D盘根目录
with zipfile.ZipFile("E:\Files.zip", "r") as zip_ref:
    zip_ref.extractall("E:\\")

# 在D盘创建目录FilesInOrder
Path_filesinorder = "E:\\FilesInOrder"
if not os.path.exists(Path_filesinorder):
    os.mkdir(Path_filesinorder)
pic_type1 = os.path.join(Path_filesinorder, "android")
if not os.path.exists(pic_type1):
    os.mkdir(pic_type1)
pic_type2 = os.path.join(Path_filesinorder, "python")
if not os.path.exists(pic_type2):
    os.mkdir(pic_type2)
pic_type3 = os.path.join(Path_filesinorder, "superman")
if not os.path.exists(pic_type3):
    os.mkdir(pic_type3)
# pic目录中包括Android、Python、Superman三类图标文件，在FilesInOrder目录中分别根据图片类型、图片拓展名类型、图片像素大小创建目录，并将对应的图片放入对应目录中
pic_path = "E:\\Files\\pic"  # pic目录的路径
pic_files = os.listdir(pic_path)  # pic目录下的所有文件名
for file in pic_files:  # 遍历每个文件名
    file_path = os.path.join(pic_path, file)  # 文件的完整路径
    if os.path.isfile(file_path):  # 如果是文件
        file = file.lower()
        if "android" in file:
            str01 = os.path.join(pic_path, file)
            file_name, file_ext = os.path.splitext(str01)  # 分离文件名和扩展名
            str02 = os.path.join(pic_type1, file_ext)
            if not os.path.exists(str02):
                os.mkdir(str02)
            for i in file_name.split("_"):
                if "px" in i:
                    str03 = os.path.join(str02, i)  # 分离文件类型和像素大小
                    if not os.path.exists(str03):
                        os.mkdir(str03)
                    str04 = os.path.join(str03, file)
                    shutil.copy(str01, str04)


        if "python" in file:
            str01 = os.path.join(pic_path, file)
            file_name, file_ext = os.path.splitext(str01)  # 分离文件名和扩展名
            str02 = os.path.join(pic_type2, file_ext)
            if not os.path.exists(str02):
                os.mkdir(str02)
            for i in file_name.split("_"):
                if "px" in i:
                    str03 = os.path.join(str02, i)  # 分离文件类型和像素大小
                    if not os.path.exists(str03):
                        os.mkdir(str03)
                    str04 = os.path.join(str03, file)
                    shutil.copy(str01, str04)
        if "superman" in file:
            str01 = os.path.join(pic_path, file)
            file_name, file_ext = os.path.splitext(str01)  # 分离文件名和扩展名
            str02 = os.path.join(pic_type3, file_ext)
            if not os.path.exists(str02):
                os.mkdir(str02)
            for i in file_name.split("_"):
                if "px" in i:
                    str03 = os.path.join(str02, i)  # 分离文件类型和像素大小
                    if not os.path.exists(str03):
                        os.mkdir(str03)
                    str04 = os.path.join(str03, file)
                    shutil.copy(str01, str04)


# txt目录包含5篇欧亨利短篇小说，将每篇短篇小说重命名加上小说标题，并创建并复制到FilesInOrder下Story目录中
txt_path = "E:\\Files\\txt"  # txt目录的路径
txt_files = os.listdir(txt_path)  # txt目录下的所有文件名
story_dir = "E:\\FilesInOrder\\Story"  # Story目录的路径
if not os.path.exists(story_dir):
    os.mkdir(story_dir)  # 创建Story目录
for file in txt_files:  # 遍历每个文件名
    file_path = os.path.join(txt_path, file)  # 文件的完整路径
    if os.path.isfile(file_path):  # 如果是文件
        with open(file_path, "r", encoding="utf-8") as f:  # 以读模式打开文件，指定编码为utf-8
            first_line = f.readline()  # 读取第一行，即小说标题
            first_line = first_line.strip()  # 去掉首尾空格和换行符
            first_line = ''.join(re.findall('[\u4e00-\u9fa5]', first_line))
            new_file_name = "欧亨利_" + first_line + ".txt"  # 生成新的文件名，加上小说标题
            new_file_path = os.path.join(story_dir, new_file_name)  # 生成新的文件路径，放在Story目录下
            shutil.copy(file_path, new_file_path)  # 将文件复制到新的路径

# 将FilesInOrder按照目录结构压缩FilesInOrder.zip文件
shutil.make_archive("E:\\FilesInOrder", "zip", "E:\\FilesInOrder")

# 记录结束时间
end_time = time.time()

# 统计以上操作的执行时间，压缩前文件大小和压缩包大小，计算压缩比
exec_time = end_time - start_time  # 执行时间，单位秒
orig_size = 0  # 压缩前文件大小，单位字节
zip_size = 0  # 压缩包大小，单位字节
for root, dirs, files in os.walk("E:\\FilesInOrder"):  # 遍历FilesInOrder目录下的所有子目录和文件
    for file in files:  # 遍历每个文件
        file_path = os.path.join(root, file)  # 文件的完整路径
        orig_size += os.path.getsize(file_path)  # 累加文件的大小
zip_size = os.path.getsize("E:\\FilesInOrder.zip")  # 获取压缩包的大小
compression_ratio = orig_size / zip_size  # 计算压缩比

# 打印结果
print("执行时间：{:.2f}秒".format(exec_time))
print("压缩前文件大小：{}字节".format(orig_size))
print("压缩包大小：{}字节".format(zip_size))
print("压缩比：{:.2f}".format(compression_ratio))
