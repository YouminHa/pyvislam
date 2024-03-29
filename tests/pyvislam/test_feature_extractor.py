import cv2
import numpy as np

import pyvislam.info

from pyvislam import feature_extractor

def test_feature_extractor_example_1():
    fe = feature_extractor.FeatureExtractor()
    assert fe != None

    img = np.full((400, 400, 3), 255, np.uint8)
    cv2.rectangle(img, (100, 100), (300, 300), 0, -1, cv2.LINE_AA)

    keypoints, descriptors = fe.extract(img)
    assert len(keypoints) == len(descriptors)

    # visualize
    if pyvislam.info.__test_visualize__: 
        img_kp = cv2.drawKeypoints(img, keypoints, None, color=(0, 255, 0), flags=0)
        cv2.imshow('img_kp', img_kp)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    octave0_keypoints = list(filter(lambda k: k.octave == 0, keypoints))
    assert len(octave0_keypoints) == 4

