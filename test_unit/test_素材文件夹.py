from MaterialPath.class_1_素材文件夹 import Class素材文件夹

mf = Class素材文件夹(root_folder=r"F:\小夕素材\10000-20000\10421")
for obj in mf.fun_所有素材文件后缀排序:
    print(obj.material_file)
    print(obj.preview_image)
    print(obj.preview_folder_image)
    print(obj.web_folder_image)

    print("\n")
