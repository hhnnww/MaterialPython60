from pathlib import Path

from .class_复制到预览图 import ClassCopyPreviewImageToPreviewPathImage
from .class_移动到数字目录 import ClassMoveToNumPath
from .class_移动到根目录 import ClassMaterialFileMoveRootFolder
from .class_素材重命名 import ClassMatrialFileRename


class ClassMaterialFileAction(
    ClassMatrialFileRename,
    ClassMaterialFileMoveRootFolder,
    ClassMoveToNumPath,
    ClassCopyPreviewImageToPreviewPathImage,
):
    def __init__(self, material_file: Path, root_path: Path) -> None:
        super().__init__(material_file=material_file, root_path=root_path)
