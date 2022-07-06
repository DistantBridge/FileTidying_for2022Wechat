import os
import shutil


# ----------



# 填入微信的某个个人用户的文件夹路径，这一文件夹名应该是"MsgAttach"
# 样例：D:\Software_Files\微信\WeChat Files\wxid_ndfuybdias\FileStorage
Wechat_File_MsgAttach = r'' 

#填入需要导出（复制、移动）的文件路径
# 样例：D:\Documents_Sort\WECHAT-TEMP
Files_Export = r'' 



# ----------



# 类的创建。每一个文件的
class OneFile ():
    def __init__(self,File_Name,File_Path,File_Splitext):
        self.File_Name = File_Name
        self.File_Path = File_Path
        self.File_Splitext = File_Splitext


        
Files_List = []

Complete_File_Info = OneFile('','','')

def Get_All_Files():
    global Files_Sum
    for Path,Dir,Names in os.walk(Wechat_File_MsgAttach):
        for Name in Names:
            Complete_File_Info = OneFile('','','')

            Complete_File_Info.File_Name = str(Name)
            Complete_File_Info.File_Path = os.path.join(Path,Name)
            Complete_File_Info.File_Splitext = os.path.splitext(Name)[-1]

            Files_List.append(Complete_File_Info)
            


Get_All_Files()



# ----------

Image_Type = '.jpg'
Video_Type = '.mp4'
dat_Type = '.dat'

Image_Files_List = []
Video_Files_List = []
dat_Files_List = []

Other_Files_List = []


def Cache_Files_Sort ():
    for File_Info in Files_List:
        if File_Info.File_Splitext == Image_Type:
            Image_Files_List.append(File_Info)
        elif File_Info.File_Splitext == Video_Type:
            Video_Files_List.append(File_Info)
        elif File_Info.File_Splitext == dat_Type:
            dat_Files_List.append(File_Info)
        else :
            Other_Files_List.append(File_Info)

Cache_Files_Sort()


def Image_Files_Tidy ():
    for File_Info in Image_Files_List:
        print(File_Info.File_Name)
    
    print("检测到以上图片文件。")
    print("一般这一类文件是聊天缓存文件。")
    print("输入'D'删除，输入'M'移动，输入'C'复制,输入'I'忽略。")

    Input_CMD = input()

    if Input_CMD == 'C' :
        for File_Info in Image_Files_List:
            shutil.copy(File_Info.File_Path , Files_Export)
        print('复制成功。')

    elif Input_CMD == 'D':
        for File_Info in Image_Files_List:
            os.unlink(File_Info.File_Path)
        print("删除成功。")

    elif Input_CMD == 'M':
        for File_Info in Image_Files_List:
            shutil.move(File_Info.File_Path , Files_Export)
        print("移动成功。")

    else:
        print("已忽略这一类文件的操作。")

Image_Files_Tidy ()

def Video_Files_Tidy ():
    for File_Info in Video_Files_List:
        print(File_Info.File_Name)
    
    print("检测到以上视频文件。")
    print("一般这一类文件是聊天缓存文件。")
    print("输入'D'删除，输入'M'移动，输入'C'复制,输入'I'忽略。")

    Input_CMD = input()

    if Input_CMD == 'C' :
        for File_Info in Video_Files_List:
            shutil.copy(File_Info.File_Path , Files_Export)
        print('复制成功。')

    elif Input_CMD == 'D':
        for File_Info in Video_Files_List:
            os.unlink(File_Info.File_Path)
        print("删除成功。")

    elif Input_CMD == 'M':
        for File_Info in Video_Files_List:
            shutil.move(File_Info.File_Path , Files_Export)
        print("移动成功。")

    else:
        print("已忽略这一类文件的操作。")

Video_Files_Tidy ()

def dat_Files_Tidy ():
    for File_Info in dat_Files_List:
        print(File_Info.File_Name)
    
    print("检测到以上.dat文件。")
    print("一般这一类文件是聊天缓存文件。")
    print("输入'D'删除，输入'M'移动，输入'C'复制,输入'I'忽略。")

    Input_CMD = input()

    if Input_CMD == 'C' :
        for File_Info in dat_Files_List:
            shutil.copy(File_Info.File_Path , Files_Export)
        print('复制成功。')

    elif Input_CMD == 'D':
        for File_Info in dat_Files_List:
            os.unlink(File_Info.File_Path)
        print("删除成功。")

    elif Input_CMD == 'M':
        for File_Info in dat_Files_List:
            shutil.move(File_Info.File_Path , Files_Export)
        print("移动成功。")

    else:
        print("已忽略这一类文件的操作。")

dat_Files_Tidy ()

def Other_Files_Tidy ():
    for File_Info in Other_Files_List:
        print(File_Info.File_Name)
    
    print("检测到以上.dat文件。")
    print("一般这一类文件是聊天缓存文件。")
    print("输入'D'删除，输入'M'移动，输入'C'复制,输入'I'忽略。")

    Input_CMD = input()

    if Input_CMD == 'C' :
        for File_Info in Other_Files_List:
            shutil.copy(File_Info.File_Path , Files_Export)
        print('复制成功。')

    elif Input_CMD == 'D':
        for File_Info in Other_Files_List:
            os.unlink(File_Info.File_Path)
        print("删除成功。")

    elif Input_CMD == 'M':
        for File_Info in Other_Files_List:
            shutil.move(File_Info.File_Path , Files_Export)
        print("移动成功。")

    else:
        print("已忽略这一类文件的操作。")

Other_Files_Tidy ()