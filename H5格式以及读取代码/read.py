import h5py
import scipy.io as sio

# h5 文件路径
h5_path = r"C:\Users\zou\Desktop\met\20250806_szwq.h5"
# 输出 mat 文件路径
mat_path = r"C:\Users\zou\Desktop\met\20250806_szwq.mat"

data_dict = {}

with h5py.File(h5_path, "r") as f:
    print("文件中包含的数据集：")
    for name in f.keys():
        dataset = f[name][:]
        data_dict[name] = dataset  # 保存到字典
        print(f"{name:12s} -> shape={dataset.shape}, dtype={dataset.dtype}")

# 保存为 .mat 文件
sio.savemat(mat_path, data_dict)

print(f"\n所有数据已保存到 {mat_path}")
