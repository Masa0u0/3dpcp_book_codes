import sys
import numpy as np
import open3d as o3d

filename = sys.argv[1]

print("Loading a point cloud from", filename)
pcd = o3d.io.read_point_cloud(filename)      # 点群として読み込み
# pcd = o3d.io.read_triangle_mesh(filename)  # メッシュデータとして読み込み

print(pcd)
print(np.asarray(pcd.points))

o3d.visualization.draw_geometries([pcd])
