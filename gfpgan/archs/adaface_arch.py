from .arcface_arch import ResNetArcFace
from basicsr.utils.registry import ARCH_REGISTRY

@ARCH_REGISTRY.register()
class ResNetAdaFace(ResNetArcFace):
    """AdaFace network with the same architecture as ResNetArcFace."""
    pass

