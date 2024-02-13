from configuration import APP_CONFIG

from tools.aruco_recognizer.recognizer import ArucoRecognizer

aruco_recognizer = ArucoRecognizer(
    aruco_type=APP_CONFIG.ARUCO_DICT_TYPE
)
