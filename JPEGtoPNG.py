import sys
import os
from PIL import Image

input_folder = sys.argv[1]
output_folder = sys.argv[2]

parent_dir = os.getcwd()
path = os.path.join(parent_dir, output_folder)
os.makedirs(path, exist_ok=True)

for filename in os.listdir(input_folder):
    clean_name = os.path.splitext(filename)[0]
    img = Image.open(f'{input_folder}{filename}')
    img.save(f'{output_folder}/{clean_name}.png', 'png')
    print(f'Converted {clean_name} to png')
print("All done!")
