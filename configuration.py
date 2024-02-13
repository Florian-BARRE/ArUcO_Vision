import json
import os


def load_json_file(file_path):
    try:
        with open(file_path) as config:
            file_json = json.load(config)
    except FileNotFoundError:
        try:
            with open(os.path.join(BASE_DIR, file_path)) as config:
                file_json = json.load(config)
        except Exception:
            raise

    return file_json


BASE_DIR = os.path.dirname(os.path.realpath(__file__))


class Config:
    # General
    BASE_DIR = BASE_DIR

    # Camera configuration
    CAMERA_RESOLUTION = [800, 800]  # (w, h)
    CAMERA_SAVE_PATH = os.path.join(BASE_DIR, "captures")

    # Camera calibrator configuration
    CALIBRATION_IMAGES_PATH = os.path.join(BASE_DIR, "calibration_images")
    CHESSBOARD_SIZE = (6, 4)
    CHESS_SQUARE_SIZE = 0.044  # meters, 4.4cm
    COEFFICIENT_PATH = os.path.join(BASE_DIR, "undistort_coef.json")

    # Plan transposer configuration
    CAMERA_TABLE_DISTANCE = 0.2  # meters
    # Distance camera-object function, a * pow(x, b)
    CAMERA_OBJECT_FUNCTION_A = 1077.2
    CAMERA_OBJECT_FUNCTION_B = -0.809

    # Aruco recognizer configuration
    ARUCO_DICT_TYPE = "DICT_4X4_100"


class Configuration(dict):

    def from_object(self, obj):
        for attr in dir(obj):

            if not attr.isupper():
                continue

            self[attr] = getattr(obj, attr)

        self.__dict__ = self


APP_CONFIG = Configuration()
APP_CONFIG.from_object(Config)
