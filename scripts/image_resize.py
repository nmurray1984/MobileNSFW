from PIL import Image
import glob
import argparse
import os

IMAGE_SIZE = (224, 224)

parser = argparse.ArgumentParser('Resize images')

parser.add_argument('--base_dir',
                    help='base directory for images')

parser.add_argument('--save_dir',
                    help='folder to save images')

args = parser.parse_args()

search_path = args.base_dir + "*/*.original.jpg"
all_files = glob.glob(search_path)
print("Found {} files in directory search path {}".format(len(all_files), search_path))

for file_path in all_files:
    im = Image.open(file_path).convert("RGB")
    im.resize(IMAGE_SIZE)
    new_file_name = file_path.replace(".224x224","",3)
    new_file_name = new_file_name.replace(".original.jpg", ".224x224.jpg")
    
    #create new file path
    try:
        im.save(new_file_name)
    except IOError:
        print("File already created for {}".format(new_file_name))
    print("Saved file {}".format(new_file_name))



