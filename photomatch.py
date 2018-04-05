import numpy as np
from scipy.misc import imread
from scipy.spatial.distance import cosine


class PhotoMatch(object):
    def __init__(self, svg_file, robot_file):
        self.svg_file = self.rgb2gray(imread(svg_file))
        self.robot_file = self.rgb2gray(imread(robot_file))
        self.cosine = cosine(self.svg_file, self.robot_file)

    @staticmethod
    def rgb2gray(rgb):
        v = np.dot(rgb[:, :, :3], [0.299, 0.587, 0.114])
        return v.reshape((v.shape[0] * v.shape[1],))


if __name__ == '__main__':
    pm1 = PhotoMatch('data/heart-svg-crop.png', 'data/heart-robot-crop.png')
    print('Heart:', pm1.cosine)
