import shutil
import os

def copy_static_to_public():

    def copy_files_from_dir(dir_path, dst_path):
        os.mkdir(dst_path)
        objects = os.listdir(dir_path)
        for object in objects:
            object_path = os.path.join(dir_path, object)
            if os.path.isfile(object_path):
                shutil.copy(object_path, dst_path)
            else:
                copy_files_from_dir(object_path, os.path.join(dst_path, object))

    dst_path = "public"
    shutil.rmtree(dst_path, True)
    src_path = "static"
    if os.path.exists(src_path):
        copy_files_from_dir(src_path, dst_path)