from router_素材信息.class_素材信息 import ClassMaterialInfo


def test_material_info():
    cla = ClassMaterialInfo(root_path=r"F:\饭桶设计\3000-3999\3127")

    assert len(list(cla.all_material_file)) == 20
