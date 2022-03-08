import subprocess
import os
import shutil

# 分割文件夹,分割成num个文件夹
def mv_file(img, num):
    list_ = os.listdir(img)
    if num > len(list_):
        print('长度需小于：', len(list_))
        exit()
    num_file = int(len(list_)/num) + 1
    print(num_file)
    cnt = 0
    for n in range(1,num_file+1): # 创建文件夹
        new_file = os.path.join(img + '_zhuyao_' + str(n))
        if os.path.exists(new_file+'_zhuyao_'+str(cnt)):
            print('该路径已存在，请解决冲突', new_file)
            exit()
        print('创建文件夹：', new_file)
        os.mkdir(new_file)
        list_n = list_[num*cnt:num*(cnt+1)]
        for m in list_n:
            old_path = os.path.join(img, m)
            new_path = os.path.join(new_file, m)
            shutil.copy(old_path, new_path)
        cnt = cnt + 1
    print('============task OK!===========')

def enCrype(target_file, source_file):

    cmd = ['zip','-q','-r','-P','zhuyao',target_file,source_file]
    subprocess.check_output(cmd)

def check_zip(zip_path):
    # cwd_path = os.getcwd()
    zip_path = os.getcwd()
    _ = os.listdir(zip_path)
    all_path = []
    for i in _:

        if os.path.isdir(i) and "__pycache__" not in i and "idea" not in i:
                all_path.append(i)
    print(all_path)
    all_zipp = [txt.replace(".zip","") for txt in os.listdir(zip_path) if txt.endswith('.zip')]

    # 判断没压缩的文件夹
    zip_folder = (set(all_zipp)^set(all_path))
    print(zip_folder)
    return zip_folder

if __name__ == "__main__":

    # mv_file("./telegram_videos/part_1/",10)
    zip_folder = check_zip("")
    for zip in zip_folder:
        zip_name = zip+".zip"
        print(zip_name)
        enCrype(zip_name,zip)
