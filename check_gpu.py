import torch

if torch.cuda.is_available():
    print(f"CUDA is available. GPU device: {torch.cuda.get_device_name(0)}")
else:
    print("CUDA is not available. Running on CPU.")