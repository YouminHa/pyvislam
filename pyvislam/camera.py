import numpy as np
import camera_type

class Camera:
    class Config:
        def 
        resolution = [320, 240]
        f = [1, 1]]
        c = [resolution[0] * 0.5, resolution[1] * 0.5]
        depth_scale = 1

    def __init__(self):
        self.config = Config()

    def __init__(self, config):
        self.config = config

    def camera_to_pixel(self, p_c):
        return np.array([
            self.f_x * p_c(0, 0) / p_c(2, 0) + self.c_x,
            self.f_y * p_c(1, 0) / p_c(2, 0) + self.c_y])

    def pixel_to_camera(self, p_p, depth):
        return np.array([
            (p_p(0, 0) - self.c_x) * depth / self.f_x,
            (p_p(1, 0) - self.c_y) * depth / self.f_y,
            depth)
