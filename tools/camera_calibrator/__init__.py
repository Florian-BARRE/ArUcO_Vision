from configuration import APP_CONFIG

from tools.camera_calibrator.object import CameraCalibrator

camera_calibrator = CameraCalibrator(
    calibration_images_path=APP_CONFIG.CALIBRATION_IMAGES_PATH,
    chessboard_size=APP_CONFIG.CHESSBOARD_SIZE,
    chess_square_size=APP_CONFIG.CHESS_SQUARE_SIZE,
    coefficient_path=APP_CONFIG.COEFFICIENT_PATH
)
