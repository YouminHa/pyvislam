import cv2

class FeatureExtractor:
    def __init__(self):
        '''
        @brief The ORB constructor

        @param nfeatures The maximum number of features to retain.
        @param scaleFactor Pyramid decimation ratio, greater than 1. scaleFactor==2 means the classical
        pyramid, where each next level has 4x less pixels than the previous, but such a big scale factor
        will degrade feature matching scores dramatically. On the other hand, too close to 1 scale factor
        will mean that to cover certain scale range you will need more pyramid levels and so the speed
        will suffer.
        @param nlevels The number of pyramid levels. The smallest level will have linear size equal to
        input_image_linear_size/pow(scaleFactor, nlevels - firstLevel).
        @param edgeThreshold This is size of the border where the features are not detected. It should
        roughly match the patchSize parameter.
        @param firstLevel The level of pyramid to put source image to. Previous layers are filled
        with upscaled source image.
        @param WTA_K The number of points that produce each element of the oriented BRIEF descriptor. The
        default value 2 means the BRIEF where we take a random point pair and compare their brightnesses,
        so we get 0/1 response. Other possible values are 3 and 4. For example, 3 means that we take 3
        random points (of course, those point coordinates are random, but they are generated from the
        pre-defined seed, so each element of BRIEF descriptor is computed deterministically from the pixel
        rectangle), find point of maximum brightness and output index of the winner (0, 1 or 2). Such
        output will occupy 2 bits, and therefore it will need a special variant of Hamming distance,
        denoted as NORM_HAMMING2 (2 bits per bin). When WTA_K=4, we take 4 random points to compute each
        bin (that will also occupy 2 bits with possible values 0, 1, 2 or 3).
        @param scoreType The default HARRIS_SCORE means that Harris algorithm is used to rank features
        (the score is written to KeyPoint::score and is used to retain best nfeatures features);
        FAST_SCORE is alternative value of the parameter that produces slightly less stable keypoints,
        but it is a little faster to compute.
        @param patchSize size of the patch used by the oriented BRIEF descriptor. Of course, on smaller
        pyramid layers the perceived image area covered by a feature will be larger.
        @param fastThreshold the fast threshold
        '''
        self.orb = cv2.ORB_create()

    def extract(self, image):
        keypoints = self.orb.detect(image, mask=None)
        keypoints, descriptors = self.orb.compute(image, keypoints)
        return keypoints, descriptors
