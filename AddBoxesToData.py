import os
import sys
import glob


import dlib

detector = dlib.simple_object_detector("./build/face_detector.svm")

if len(sys.argv) != 2:
    print(
        "Give the path to the examples/faces directory as the argument to this "
        "program. For example, if you are in the python_examples folder then "
        "execute this program by running:\n"
        "    ./train_object_detector.py ../examples/faces")
    exit()
faces_folder = sys.argv[1]

options = dlib.simple_object_detector_training_options()

options.add_left_right_image_flips = True

options.C = 5

options.num_threads = 2
options.be_verbose = True

training_xml_path = os.path.join(faces_folder, "training.xml")
testing_xml_path = os.path.join(faces_folder, "testing.xml")

print("")  # Print blank line to create gap from previous output
print("Training accuracy: {}".format(
    dlib.test_simple_object_detector(training_xml_path, "detector.svm")))

detector = dlib.simple_object_detector("detector.svm")

