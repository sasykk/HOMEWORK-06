import sys
from pathlib import Path

image_files = list()
video_files = list()
document_files = list()
music_files = list()
archives = list()
folders = list()
others = list()
unknown = set()
extensions = set()

registered_extensions = {
    'JPEG': image_files,
    'PNG': image_files,
    'JPG': image_files,
    'SVG': image_files,
    'AVI': video_files,
    'MP4': video_files,
    'MOV': video_files,
    'MKV': video_files,
    'DOC': document_files,
    'DOCX': document_files,
    'TXT': document_files,
    'PDF': document_files,
    'XLS': document_files,
    'XLSX': document_files,
    'PPTX': document_files,
    'MP3': music_files,
    'OGG': music_files,
    'WAW': music_files,
    'AMR': music_files,
    'ZIP': archives,
    'GZ': archives,
    'TAR': archives
}


def get_extensions(file_name):
    return Path(file_name).suffix[1:].upper()


def scan(folder):
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ('images', 'video', 'audio', 'documents', 'archives', 'other'):
                folders.append(item)
                scan(item)
            continue

        extension = get_extensions(file_name=item.name)
        new_name = folder/item.name
        if not extension:
            others.append(new_name)
        else:
            try:
                container = registered_extensions[extension]
                extensions.add(extension)
                container.append(new_name)
            except KeyError:
                unknown.add(extension)
                others.append(new_name)


if __name__ == '__main__':
    path = sys.argv[1]
    print(f"Start in {path}")

    folder = Path(path)

    scan(folder)

    print(f"images: {image_files}")
    print(f"videos: {video_files}")
    print(f"music: {music_files}")
    print(f"documents: {document_files}")
    print(f"archives: {archives}")
    print(f"unknown: {others}")
    print(f"All extensions: {extensions}")
    print(f"Unknown extensions: {unknown}")
    print(f"Folder: {folders}")
