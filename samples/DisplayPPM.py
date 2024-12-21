from PIL import Image
import os
import sys

### usage: python3 DisplayPPM.py filename ###

if len(sys.argv) < 2:
    print("error: need a file name as an argument.")
    sys.exit(1)  
    
    
ppm_file_path = sys.argv[1]

try:
    image = Image.open(ppm_file_path)

    print(f"target: {ppm_file_path}")
    print(f"format: {image.format}") 
    print(f"mode: {image.mode}")  
    print(f"size: {image.size}")  
    print(f"width: {image.width}")  
    print(f"height: {image.height}") 
    

    file_size = os.path.getsize(ppm_file_path) / 1024
    print(f"file size: {file_size:.2f} KB")

    image.show()

except FileNotFoundError:
    print(f"error: cannot find {ppm_file_path}")
except Exception as e:
    print(f"error: {e}")
