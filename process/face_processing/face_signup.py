import numpy as np
from typing import Tuple

from process.face_processing.face_utils import FaceUtils
from process.database.config import DataBasePaths

class FaceSignUp:
    def __init__(self):
        self.database = DataBasePaths()
        self.face_utilities = FaceUtils()
    def process(self, face_image: np.ndarray, user_code: str):
        #step 1: check face detection
        check_face_detect, face_info, face_save = self.face_utilities.check_face(face_image)
        return check_face_detect, face_info