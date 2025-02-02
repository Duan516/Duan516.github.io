import os

def read_image_names(folder_path, output_file):
    """
    读取指定文件夹中的图片名称，并按照特定格式写入到指定的文本文件中。
    
    :param folder_path: 包含图片的文件夹路径
    :param output_file: 输出的文本文件路径
    """
    # 支持的图片格式
    supported_formats = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']
    
    # 打开输出文件
    with open(output_file, 'w', encoding='utf-8') as f:
        # 遍历文件夹中的所有文件
        for filename in os.listdir(folder_path):
            # 检查文件扩展名是否为支持的图片格式
            if os.path.splitext(filename)[1].lower() in supported_formats:
                # 获取不带扩展名的文件名
                base_name = os.path.splitext(filename)[0]
                
                # 按照指定格式写入文件
                f.write(f"- filename: {base_name}\n")
                f.write(f"  original: {filename}\n")
                f.write(f"  thumbnail: {base_name}-thumbnail{os.path.splitext(filename)[1]}\n")
                f.write(f"  title: {base_name}\n")
                f.write(f"  caption: Re-Construct/\"Den djoef\" by I-Illusions\n\n")
    
    print(f"图片名称已写入到 {output_file}")

# 示例用法
folder_path = r"E:\personal website\4.0 20250201\Duan516.github.io\assets\photography\苏杭"  # 替换为你的图片文件夹路径
output_file = r"E:\personal website\4.0 20250201\Duan516.github.io\assets\photography\苏杭\file.txt"  # 替换为输出文件路径
read_image_names(folder_path, output_file)