import os
import shutil


def main():
    import argparse
    parser = argparse.ArgumentParser(description='count files')
    parser.add_argument('directory', default='.')
    args = parser.parse_args()

    target_dir = args.directory
    for d in next(os.walk(target_dir))[1]:
        dir = os.path.join(target_dir, d)
        n_files = len(os.listdir(dir))
        print('{}\t{}'.format(dir, n_files))
