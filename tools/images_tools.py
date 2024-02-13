from tools.aruco_recognizer.frame import Frame

import numpy as np
import cv2


def draw_markers(frame: Frame) -> np.ndarray:
    if frame.len:
        return cv2.aruco.drawDetectedMarkers(frame.img, frame.corners, frame.ids)


def draw_circle_with_label(frame: Frame, x: int, y: int, label: str, radius: int, thickness: int,
                           color: tuple[int, int, int]) -> None:
    cv2.circle(
        frame.img,
        (x, y),
        radius,
        color,
        thickness
    )

    cv2.putText(
        frame.img,
        label,
        (x + 10, y + 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        color,
        2
    )


def draw_corners(frame: Frame, radius=5, thickness=2) -> Frame:
    # Corners deco
    corners_deco = [
        {"label": "A", "color": (255, 255, 0)},
        {"label": "B", "color": (0, 255, 255)},
        {"label": "C", "color": (255, 0, 255)},
        {"label": "D", "color": (255, 255, 255)},
    ]
    for index in range(frame.len):
        for deco_index in range(len(corners_deco)):
            draw_circle_with_label(
                frame,
                int(frame.corners[index][0][deco_index][0]),
                int(frame.corners[index][0][deco_index][1]),
                corners_deco[deco_index]["label"],
                radius,
                thickness,
                corners_deco[deco_index]["color"]
            )

    return frame


def draw_barycenter(frame: Frame, radius=5, thickness=2, color=(255, 0, 0)) -> Frame:
    for index in range(frame.len):
        cv2.line(
            frame.img,
            (int(frame.corners[index][0][0][0]), int(frame.corners[index][0][0][1])),
            (int(frame.corners[index][0][2][0]), int(frame.corners[index][0][2][1])),
            color,
            thickness
        )
        cv2.line(
            frame.img,
            (int(frame.corners[index][0][1][0]), int(frame.corners[index][0][1][1])),
            (int(frame.corners[index][0][3][0]), int(frame.corners[index][0][3][1])),
            color,
            thickness
        )

        # Calcul Xcenter
        x = (int(frame.corners[index][0][0][0]) + int(frame.corners[index][0][2][0])) // 2
        y = (int(frame.corners[index][0][0][1]) + int(frame.corners[index][0][2][1])) // 2

        draw_circle_with_label(
            frame,
            x,
            y,
            f"X: {x}  Y:{y}",
            radius,
            thickness,
            color
        )

    return frame

def extract_ellipse_info(founds):
    rayons = []
    if founds.len:
        for index in range(founds.len):
            points = np.array([
                [founds.corners[index][0][0][0], founds.corners[index][0][0][1]],
                [founds.corners[index][0][1][0], founds.corners[index][0][1][1]],
                [founds.corners[index][0][2][0], founds.corners[index][0][2][1]],
                [founds.corners[index][0][3][0], founds.corners[index][0][3][1]]
            ])
            center = points.mean(axis=0)
            points_centered = points - center
            covariance = np.cov(points_centered.T)

            # Résoudre le problème de valeur propre généralisé
            eigenvalues, eigenvectors = eig(covariance)

            # Le rayon maximum est la racine carrée de la valeur propre maximale
            max_radius = abs(np.sqrt(max(eigenvalues)))

            rayons.append(
                {
                    "center": center,
                    "max_radius": max_radius
                }
            )

    return rayons