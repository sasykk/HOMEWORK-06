#Головний модуль

import normalize
import scan
import sys
import os
import shutil
from pathlib import Path

def handle_file(path, root_folder, dist):
    target_folder = root_folder/dist
    target_folder.mkdir(exist_ok=True)
    path.replace(target_folder/normalize.normalize(path.name))

def handle_archive(path, root_folder, dist):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    new_name = path.name
    for i in ['.zip', '.tar.gz', '.tar']:
        new_name = normalize.normalize(new_name.replace(i, ''))
    archive_folder = target_folder / new_name
    archive_folder.mkdir(exist_ok=True)
    try:
        shutil.unpack_archive(str(path.resolve()), str(archive_folder.resolve()))
    except shutil.ReadError:
        archive_folder.rmdir()
        os.remove(str(path.resolve()))
        return
    except FileNotFoundError:
        archive_folder.rmdir()
        return
    path.unlink()

def remove_empty_folders(path):
    for item in path.iterdir():
        if item.is_dir():
            remove_empty_folders(item)
            try:
                item.rmdir()
            except OSError:
                pass

def main(folder_path):
    print(folder_path)
    scan.scan(folder_path)
    items = {'images': scan.image_files,
             'video': scan.video_files,
             'audio': scan.music_files,
             'documents': scan.document_files,
             'other': scan.others}
    for key, val in items.items():
        for file in items[key]:
            handle_file(file, folder_path, key)
    for file in scan.archives:
        handle_archive(file, folder_path, "archives")
    remove_empty_folders(folder_path)

def print_result(folder):
    for item in folder.iterdir():
        print(item.name)
        if item.is_dir():
            print_result(item)
        continue

if __name__ == '__main__':
    path = sys.argv[1]
    print(f'Start in {path}')
    folder = Path(path)
    main(folder.resolve())
    print_result(folder.resolve())
