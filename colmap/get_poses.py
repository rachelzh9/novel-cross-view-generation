import numpy as np
import os
from PIL import Image


class ColmapDataLoader:
    
    def __init__(self) -> None:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.file_path = os.path.join(dir_path, 'custom/sparse/0/images.txt')
        self.img_path = os.path.join(dir_path, 'custom/images')
        self.img_names = []
        self.cameras = []

        file = open(self.file_path, 'r')
        Lines = file.readlines()

        count = 0
        for line in Lines:
            if count >= 5:
                data = line.strip().split(" ")
                self.img_names.append(int(data[-1].split(".")[0]))
                self.cameras.append(np.concatenate((data[5:8], data[1:5])).astype(float))
            count+=1
        idx = np.argsort(self.img_names)
        self.img_names = np.array(self.img_names)[idx]
        self.cameras = np.array(self.cameras)[idx]

    def __len__(self):
        return len(self.img_names)

    def __getitem__(self, i):
        img_name = self.img_names[i]
        frames = np.array(Image.open(os.path.join(self.img_path, str(img_name)+".jpg")))
        cameras = self.cameras[i]
        return frames, cameras

if __name__ == "__main__":
    c = ColmapDataLoader()
    frames, cameras = c[0]
    print(cameras)