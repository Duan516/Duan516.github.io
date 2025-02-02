import os
import shutil

def 复制并重命名图片(文件夹路径):
    # 检查文件夹是否存在
    if not os.path.exists(文件夹路径):
        print(f"文件夹 '{文件夹路径}' 不存在！")
        return

    # 获取文件夹中的所有文件
    for 文件名 in os.listdir(文件夹路径):
        # 获取文件的完整路径
        文件路径 = os.path.join(文件夹路径, 文件名)

        # 检查是否是文件（而不是文件夹）
        if os.path.isfile(文件路径):
            # 获取文件名和扩展名
            文件名, 扩展名 = os.path.splitext(文件名)

            # 只处理图片文件（可以根据需要添加更多扩展名）
            if 扩展名.lower() in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']:
                # 新文件名
                新文件名 = f"{文件名}-thumbnail{扩展名}"
                新文件路径 = os.path.join(文件夹路径, 新文件名)

                # 复制文件
                shutil.copy2(文件路径, 新文件路径)
                print(f"已复制并重命名: {文件名}{扩展名} -> {新文件名}")

# 使用示例
文件夹路径 = "E:/personal website/4.0 20250201/Duan516.github.io/assets/photography/苏杭"  # 替换为你的文件夹路径
复制并重命名图片(文件夹路径)

