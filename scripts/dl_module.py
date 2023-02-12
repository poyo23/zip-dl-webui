import os
import shutil
from datetime import datetime

def webui_print(s,end="\n"):
    print(f"[zip-dl-webui] {s}",end=end)

def donwload_images(dl_grid_images):
    main_dir = os.path.dirname(__file__)
    webui_print(f"main_dir: {main_dir}")
    webui_print(f"pwd: {os.getcwd()}")
    outputs_dir = os.path.join(os.getcwd(),"outputs")

    dl_src = outputs_dir

    if dl_grid_images and os.name == 'posix':
        #
        symbol_outputs=os.path.join(main_dir,"temp_outputs_for_dl")
        os.makedirs(symbol_outputs,exist_ok=True)
        # delete symlink if exist
        _path_list = [os.path.join(symbol_outputs,f) for f in os.listdir(outputs_dir)]
        link_path_list = [p for p in _path_list if not os.path.islink(p)]
        for lp in link_path_list:
            os.unlink(lp)

        # create symlink
        for d in [f for f in os.listdir(outputs_dir) if not f.endswith("-grids")]:
            src = os.path.join(outputs_dir,d)
            dst = os.path.join(symbol_outputs,d)
            os.symlink(src, dst)
        dl_src = symbol_outputs

    time_str = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    zipname = f"outputs_{time_str}"
    zip_path = os.path.join(main_dir,zipname)
    shutil.make_archive(zip_path, 'zip', root_dir=dl_src)

    return f"Finish {time_str}",f"{zip_path}.zip"
