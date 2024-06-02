from pathlib import Path

from MaterialPath.class_素材文件 import Class素材文件


def test_素材文件():
    mf = Class素材文件(
        material_file=Path(r"F:\小夕素材\10000-20000\10421\10421\小夕素材(1).psd"),
        root_folder=r"F:\小夕素材\10000-20000\10421",
    )

    assert mf.fun_预览图文件夹.as_posix() == r"F:/小夕素材/10000-20000/10421/预览图"
    assert mf.preview_image == Path(
        r"F:\小夕素材\10000-20000\10421\10421\小夕素材(1).png"
    )
    assert mf.preview_folder_image == Path(
        r"F:\小夕素材\10000-20000\10421\预览图\小夕素材(1).png"
    )
    assert mf.format == "psd"
