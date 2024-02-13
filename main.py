from configuration import APP_CONFIG

from tools import camera, aruco_recognizer, plan_transposer
import tools.images_tools as img_tools

if __name__ == "__main__":
    # First load the undistort coef
    camera.load_undistor_coefficients()

    while True:
        camera.capture()
        camera.undistor_image()

        frame = aruco_recognizer.detect(camera.get_capture())

        frame.draw_markers()
        frame.draw_corners()
        frame.draw_barycenter()
        ellipses = frame.compute_and_draw_ellipses()

        # Get the relative position of the objects
        for ellipse in ellipses:
            x, y = plan_transposer.image_to_relative_position(
                img=frame.img,
                segment=ellipse.get("max_radius"),
                center_point=ellipse.get("center")
            )
            print(f"X: {x:.2f} Y: {y:.2f}")

        camera.update_monitor(img=frame.img)
