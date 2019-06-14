import os

dir = os.listdir(r"T:")
print(dir)
file = [name for name in dir if name.endswith('jpeg') or name.endswith('jpg') or name.endswith('.png')]