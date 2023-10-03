import zipfile
import pathlib


def extract_archive(archivepath, dest_dir):
    archivepath = pathlib.Path(archivepath)
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
    extract_archive("files/compressed.zip", "files")
