from savReaderWriter import SavReader
import os

# 设定数据存储路径
file_directory = r'C:\Users\zou\Desktop\read fca data\数据'

# 遍历所有文件
for filename in os.listdir(file_directory):
    if filename.endswith('.sav'):  # 只处理 .sav 文件
        file_path = os.path.join(file_directory, filename)

        try:
            # 使用 SavReader 读取 .sav 文件（不指定 encoding）
            with SavReader(file_path) as reader:
                # 打印文件的头几行，查看文件结构
                data = reader.all()
                print(f"Data from {filename}:")
                print(data[:5])  # 打印前5行数据，检查数据内容
        except Exception as e:
            print(f"Error reading {filename}: {e}")
