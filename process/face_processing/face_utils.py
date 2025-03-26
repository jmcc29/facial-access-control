import os
import numpy as np
import cv2
import datetime
from typing import List, Tuple, Any
from process.face_processing.face_detect_models.face_detect import FaceDetectMediaPipe

class FaceUtils:
    def  __init__(self):
        #face detect
        self.face_detector = FaceDetectMediaPipe()
        #face mesh
        #face matcher

        pass
    def check_face(self, face_image: np.ndarray) -> Tuple[bool, Any, np.ndarray]:
        face_save = face_image.copy()
        check_face, face_info = self.face_detector.face_detect_mediapipe(face_image)
        return check_face, face_info, face_save