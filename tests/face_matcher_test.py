import unittest
import os
import cv2
import time

from tensorboard.backend.event_processing.event_file_inspector import summary_type

from process.face_processing.face_matcher_models.face_matcher import FaceMatcherModels

class TestFaceMatcher(unittest.TestCase):
    def setUp(self):
        self.face_matcher_model = FaceMatcherModels()

    def test_face_matcher_face_recognition_model_matcher_images(self):
        face1_input_folder = 'tests/face_matcher/images/similar/face_1'
        face2_input_folder = 'tests/face_matcher/images/similar/face_2'
        summary = {'face matcher correct': 0, 'face matcher incorrect': 0, 'time': 0,'face1_image': [],
                   'face2_image': [],'coincidence': [], 'distance': []}
        star_time = time.time()
        face1_images = [os.path.join(face1_input_folder, f) for f in os.listdir(face1_input_folder)
                        if f.endswith('.jpeg') or f.endswith('.jpg') or f.endswith('.png')]
        face2_images = [os.path.join(face2_input_folder, f) for f in os.listdir(face2_input_folder)
                        if f.endswith('.jpeg') or f.endswith('.jpg') or f.endswith('.png')]

        for face1_image_path, face2_image_path in zip(face1_images, face2_images):
            face1_image = cv2.imread(face1_image_path)
            face2_image = cv2.imread(face2_image_path)
            coincidence, distance= self.face_matcher_model.face_matching_face_recognition_model(face1_image, face2_image)
            if coincidence:
                summary['face matcher correct'] += 1
            else:
                summary['face matcher incorrect'] +=1

            summary['face1_image'].append(os.path.basename(face1_image_path))
            summary['face2_image'].append(os.path.basename(face2_image_path))
            summary['coincidence'].append(coincidence)
            summary['distance'].append(distance)

        end_time = time.time()
        execution_time = end_time - star_time
        summary ['time'] = round(execution_time, 3)

        print(f'Result: {summary}')

if __name__ == '__main__':
    unittest.main()