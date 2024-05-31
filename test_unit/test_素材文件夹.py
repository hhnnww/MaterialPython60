from MaterialPath.class_1_素材文件夹 import MaterialFolder

mf = MaterialFolder(root_folder=r"F:\小夕素材\10000-20000\10421")
for obj in mf.all_material_obj_sort_by_format:
    print(obj.material_file)
    print(obj.preview_image)
    print(obj.preview_folder_image)
    print(obj.web_folder_image)

    print("\n")
