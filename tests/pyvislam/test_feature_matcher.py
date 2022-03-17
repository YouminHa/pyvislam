import cv2
import numpy as np

from pyvislam import feature_matcher

def test_feature_matcher_basic_translation():
    # create 2 images
    rect = np.array([200, 200])
    move = (np.array([50, 100]), np.array([100, 100]))  # move to right by 50 px

    img1 = np.full((400, 400, 3), 255, np.uint8)
    cv2.rectangle(img1, move[0], move[0] + rect, 0, -1, cv2.LINE_AA)

    img2 = np.full((400, 400, 3), 255, np.uint8)
    cv2.rectangle(img2, move[1], move[1] + rect, 0, -1, cv2.LINE_AA)

    fm = feature_matcher.FeatureMatcher()
    match = fm.match(img1, img2)


