import os
import shutil

def move_images_to_dir():
    # 获取当前的工作目录
    cwd = os.getcwd()

    # 在当前工作目录下，创建一个新的子目录 "img"
    img_dir = os.path.join(cwd, '../../img')
    os.makedirs(img_dir, exist_ok=True)

    # 定义一个图片文件的扩展名列表
    img_exts = ['.jpg', '.png', '.jpeg', '.gif', '.bmp']

    # 遍历当前目录
    for filename in os.listdir(cwd):
        # 获取文件的绝对路径
        file_path = os.path.join(cwd, filename)

        # 检查该文件是否是图片（通过检查其扩展名是否在我们定义的列表中）
        if os.path.isfile(file_path) and any(filename.lower().endswith(ext) for ext in img_exts):
            # 目标路径
            dst_path = os.path.join(img_dir, filename)
            # 如果已经存在同名文件，先删除
            if os.path.exists(dst_path):
                os.remove(dst_path)

            # 将图片文件移动到 "img" 子目录下
            shutil.move(file_path, img_dir)

    print("All image files have been moved to the 'img' directory.")