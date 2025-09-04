import os
import numpy as np
import pyreadstat
import scipy.io as sio

# 设定数据存储路径
file_directory = r'C:\Users\zou\Desktop\read fca data\数据'

# 存储每个高度的u, v值和对应的次数
u_values = {}
v_values = {}
counts = {}

# 遍历所有文件
for filename in os.listdir(file_directory):
    if filename.endswith('.sav'):  # 只处理 .sav 文件
        file_path = os.path.join(file_directory, filename)

        # 读取 .sav 文件
        df, meta = pyreadstat.read_sav(file_path)

        # 假设每个文件有26个数组，每个数组代表一个高度窗口
        # 每个数组的第4个和第5个数字是 u 和 v 值
        height_index = 0

        # 遍历每个文件的数据，假设每个文件的数组存储顺序是从50km到100km，每2km一个数组
        for i in range(0, len(df), 26):  # 每个文件包含26个数据点
            # 假设每个数组的第4个和第5个数字是 u 和 v 值
            u = df.iloc[i + 3, 0]  # 第4个数字是 u
            v = df.iloc[i + 4, 1]  # 第5个数字是 v

            height = 50 + height_index * 2  # 假设高度从50km到100km，每2km一个
            if u != 0 and v != 0:  # 如果u和v都不为0
                if height not in u_values:
                    u_values[height] = 0
                    v_values[height] = 0
                    counts[height] = 0

                u_values[height] += u
                v_values[height] += v
                counts[height] += 1

            height_index += 1

# 计算平均u和v
averages = {}
for height in sorted(u_values.keys()):
    if counts[height] > 0:
        avg_u = u_values[height] / counts[height]
        avg_v = v_values[height] / counts[height]
        averages[height] = {'avg_u': avg_u, 'avg_v': avg_v}

# 保存为MATLAB格式的文件
output_data = {
    'heights': list(averages.keys()),
    'avg_u': [averages[height]['avg_u'] for height in averages],
    'avg_v': [averages[height]['avg_v'] for height in averages]
}

output_filename = '/mnt/data/averages.mat'
sio.savemat(output_filename, output_data)

print(f"Data saved to {output_filename}")
