def import_model_by_backend(tensorflow_cmd, pytorch_cmd):
    import sys
    for _backend in sys.modules["multimodal"].backend:
        if _backend == "tensorflow":
            exec(tensorflow_cmd)
        elif _backend == "pytorch":
            exec(pytorch_cmd)
            break


import sys
for _backend in sys.modules["external"].backend:
    if _backend == "tensorflow":
        pass
    elif _backend == "pytorch":
        from .grcn.GRCN import GRCN
        from .lattice.LATTICE import LATTICE
        from .mgat.MGAT import MGAT
        from .mmgcn.MMGCN import MMGCN
        from .vbpr.VBPR import VBPR
