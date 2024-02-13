from configuration import APP_CONFIG

from tools.camera.object import Camera

camera = Camera(
    res_w=APP_CONFIG.CAMERA_RESOLUTION[0],
    res_h=APP_CONFIG.CAMERA_RESOLUTION[1],
    captures_path=APP_CONFIG.CAMERA_SAVE_PATH,
    undistorted_coefficients_path=APP_CONFIG.COEFFICIENT_PATH
)
