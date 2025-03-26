import numpy as np
import mediapipe as mp
import cv2
from typing import Tuple, Any

class FaceDetectMediaPipe:
    def __init__(self):
        #mediapipe
        self.object_face_mp = mp.solutions.face_detection
        self.face_detector_mp = self.object_face_mp.FaceDetection(min_detection_confidence=0.7, model_selection=1)

    def face_detect_mediapipe(self,face_image: np.ndarray)-> Tuple[bool,Any]:
        rgb_image = face_image.copy()
        rgb_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2RGB)

        faces = self.face_detector_mp.process(rgb_image)
        if faces.detections is None:
            return False, faces
        else:
            return True, faces

