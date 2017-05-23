#include <dlib/svm_threaded.h>
#include <dlib/gui_widgets.h>
#include <dlib/image_processing.h>
#include <dlib/data_io.h>

#include <iostream>
#include <fstream>


using namespace std;
using namespace dlib;

// ----------------------------------------------------------------------------------------

int main(int argc, char** argv)
{  

    try
    {
        //Load Dataset
        if (argc != 2)
        {
            cout << "Give the path to the examples/faces directory as the argument to this" << endl;
            cout << "program.  For example, if you are in the examples folder then execute " << endl;
            cout << "this program by running: " << endl;
            cout << "   ./fhog_object_detector_ex faces" << endl;
            cout << endl;
            return 0;
        }
        const std::string faces_directory = argv[1];
        //variables that hold dataset
        dlib::array<array2d<unsigned char> > images_train, images_test;
        std::vector<std::vector<rectangle> > face_boxes_train, face_boxes_test;

        //load data from xml files
        load_image_dataset(images_train, face_boxes_train, faces_directory+"/training.xml");
        load_image_dataset(images_test, face_boxes_test, faces_directory+"/testing.xml");

        //increase the size of image samples
        upsample_image_dataset<pyramid_down<2> >(images_train, face_boxes_train);
        //flip images so we can use the same faces twice.
        add_image_left_right_flips(images_train, face_boxes_train);
        cout << "num training images: " << images_train.size() << endl;
        cout << "num testing images:  " << images_test.size() << endl;
 
        //native implementation of Felzenszwalb's version of the Histogram of Oriented
        //Gradients. 
        typedef scan_fhog_pyramid<pyramid_down<6> > image_scanner_type; 
        image_scanner_type scanner;
        // The sliding window detector will be 80 pixels wide and 80 pixels tall.
        scanner.set_detection_window_size(80, 80); 
        structural_object_detection_trainer<image_scanner_type> trainer(scanner);
        // Number of Cores on machine.
        trainer.set_num_threads(2);  
        // C parameter for SVM.
        trainer.set_c(1);
        // Print progress to console.
        trainer.be_verbose();
        // run until risk gap is less than 1 percent  
        trainer.set_epsilon(0.01);


        // run trainer
        object_detector<image_scanner_type> detector = trainer.train(images_train, face_boxes_train);

        // print the precision, recall, and then average precision.
        cout << "training results: " << test_object_detection_function(detector, images_train, face_boxes_train) << endl;
        //use detector on test images and check results
        cout << "testing results:  " << test_object_detection_function(detector, images_test, face_boxes_test) << endl;


        // Saves detector to hard disk.
        serialize("face_detector.svm") << detector;

    }
    catch (exception& e)
    {
        cout << "\nexception thrown!" << endl;
        cout << e.what() << endl;
    }
}

// ----------------------------------------------------------------------------------------
