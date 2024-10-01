from .nodes.UpscaleSlicer import UpscaleSlicer
from .nodes.ImageExport import ImageExport

NODE_CLASS_MAPPINGS = {
    "UpscaleSlicer": UpscaleSlicer,
    "ImageExport": ImageExport
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "UpscaleSlicer": "Upscale Slicer",
    "ImageExport": "Image Export"
}
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
