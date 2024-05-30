from class_material_path import ClassMaterialPath


def test_material_path():
    cla = ClassMaterialPath(r"F:\饭桶设计\3000-3999\3127")

    assert isinstance(cla.prev_path.as_posix(), str)

    all_material = cla.sort_materials()
    assert len(all_material) == 30
    assert all_material[0].material_file.stem == "饭桶设计(1)"
    assert all_material[-1].material_file.stem == "饭桶设计(30)"
    assert cla.prev_path.stem == "3126"
    assert cla.next_path.stem == "3128"
