import os
from datetime import datetime
import zipfile
import argparse
from tqdm import tqdm

def webui_print(s,end="\n"):
    print(f"[zip-dl-webui] {s}",end=end)

def donwload_images(no_grids):
    main_dir = os.path.dirname(__file__)
    webui_print(f"main_dir: {main_dir}")
    webui_print(f"pwd: {os.getcwd()}")
    outputs_dir = os.path.join(os.getcwd(),"outputs")

    if no_grids:
        output_data = search_directory(outputs_dir,"-grids")
    else:
        output_data = search_directory(outputs_dir)

    #
    time_str = datetime.now().strftime("%Y%m%d%H%M%S")
    zipname = f"outputs_{time_str}.zip"
    zip_path = os.path.join(main_dir,zipname)

    with zipfile.ZipFile(zip_path, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        for f in tqdm(output_data.files,desc="zip"):
            z.write(filename=os.path.join(outputs_dir,f),arcname=f)

    return f"{datetime.now().strftime('%Y/%m/%d %H:%M:%S')} : finish",zip_path



def search_directory(input_dir,exclude_directory=None):
    dirs = [""]
    searched_directories = []
    all_files = []
    pbar = tqdm(desc="file searching")
    while len(dirs) > 0:
        d = dirs.pop()
        if exclude_directory is not None and d.endswith(exclude_directory):
            continue
        if ".ipynb_checkpoints" in d:
            continue
        searching_dir = os.path.join(input_dir,d)
        searched_directories.append(d)
        _l = [os.path.join(d,p) for p in os.listdir(searching_dir)]
        dir_list = [p for p in _l if os.path.isdir(os.path.join(input_dir,p))]
        file_list = [p for p in _l if os.path.isfile(os.path.join(input_dir,p))]

        dirs += dir_list
        all_files += file_list
        pbar.update(1)
    pbar.close()

    return argparse.Namespace(files=all_files,sub_dirs=searched_directories)


