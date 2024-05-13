import open3d as o3d
import numpy as np

a = np.load("/home/starkit/Downloads/out/ds0/labels/16522.npy")
print(np.mean(a[:, -1]))

# pcd = o3d.io.read_point_cloud("/home/starkit/Downloads/out/ds0/pointcloud/15641.pcd")
# print(np.asarray(pcd.points).shape)
