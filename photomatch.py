import numpy as np
from scipy.misc import imread, imresize
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
    pm1 = PhotoMatch('data/swan-svg-crop.png', 'data/swan-robot-crop.png')
    print('Swan:', pm1.cosine)

    pm2 = PhotoMatch('data/flower-svg-crop.png', 'data/flower-robot-crop.png')
    print('Flower:', pm2.cosine)

    pm3 = PhotoMatch('data/heart-svg.jpg', 'data/heart-robot.jpg')
    print('Heart:', pm3.cosine)

    pm4 = PhotoMatch('data/giraffe-svg.jpg', 'data/giraffe-robot.jpg')
    print('Giraffe:', pm4.cosine)
