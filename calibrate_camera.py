from configuration import APP_CONFIG

from tools import camera, camera_calibrator

if __name__ == "__main__":
    # First take a picture of the chessboard from different angles and distances
    #camera.chessboard_calibration_images_capture(
    #    save_path=APP_CONFIG.CALIBRATION_IMAGES_PATH,
    #    nb_pictures=30,
    #    frequency=1
    #)

    # Then calculate the undistort coef from the pictures and save them
    camera_calibrator.load_images()
    camera_calibrator.chessboard_detection()
    camera_calibrator.compute_distortion_coefficients()
    camera_calibrator.save_coefficients()
