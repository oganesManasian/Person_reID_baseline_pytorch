import os
from shutil import copyfile, rmtree
from tqdm import tqdm

# Folder which contains 'msmt17_raw' folder which contains list_train.txt, list_val.txt,
# list_query.txt, list_gallery.txt files and train, test folders with images
data_raw_path = 'msmt17'

# Processing train and test
for src_folder, sections in [["train", ["train", "val"]],
                             ["test", ["gallery", "query"]]]:
    for section in sections:
        with open(os.path.join(data_raw_path, "msmt17_raw", f"list_{section}.txt")) as f:
            filenames = f.readlines()
        print(f"In total {len(filenames)} files in folder {section}")

        if os.path.isdir(os.path.join(data_raw_path, section)):
            rmtree(os.path.join(data_raw_path, section))
        os.mkdir(os.path.join(data_raw_path, section))

        for filename in tqdm(filenames, desc=f"Processing section {section}"):
            label, name = filename.split(" ")[0].split("/")
            src_path = os.path.join(data_raw_path, "msmt17_raw", src_folder, label, name)
            dir_path = os.path.join(data_raw_path, section, label)
            if not os.path.isdir(dir_path):
                os.mkdir(dir_path)
            dst_path = os.path.join(dir_path, name)
            copyfile(src_path, dst_path)

