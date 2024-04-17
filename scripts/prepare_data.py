import argparse
from glob import glob
import os
import shutil


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--data_path",
        type=str,
        help="Path to dataset folder",
    )
    args = parser.parse_args()
    return args


def main():
    DATA_PATH = args.data_path
    NEW_PATH = f"{DATA_PATH}/landscapes"
    if not os.path.exists(NEW_PATH):
        os.mkdir(NEW_PATH)
    d = {}
    for i in range(2, 8):
        d[str(i)] = glob(f"{DATA_PATH}/*({str(i)}).jpg")
    all = glob(f"{DATA_PATH}/*.jpg")
    zero = []
    for path in all:
        flag = True
        for id in range(2, 8):
            if path in d[str(id)]:
                flag = False
                break
        if flag:
            zero.append(path)
    d["1"] = zero
    for i in range(1, 8):
        new_dir = f"{NEW_PATH}/{str(i)}"
        if not os.path.exists(new_dir):
            os.mkdir(new_dir)
        for path in d[str(i)]:
            img_name = path.split("/")[-1]
            src = path
            dest = f"{new_dir}/{img_name}"
            shutil.copy(src, dest)


if __name__ == "__main__":
    args = parser()
    main()
