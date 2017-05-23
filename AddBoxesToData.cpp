#include <dlib/svm_threaded.h>
#include <dlib/gui_widgets.h>
#include <dlib/image_processing.h>
#include <dlib/data_io.h>

#include <iostream>
#include <fstream>

using namespace std;
using namespace dlib;

// ----------------------------------------------------------------------------------------

int main()
{  

    try
    {
        std::string path = "../helen_1"
        dlib::vector<array<unsigned char> > dataset;
        object_detector<image_scanner_type> detector;
        ofstream coordsFile;

        for (std::string & p : fs::directory_iterator(path))
        {
            if(p.find(".jpg") != std::string::npos)
            {
                dataset.push_back(p);
            }
        }

        deserialize("face_detector.svm") >> detector;
        coordsFile.open("helena_training_labels.xml");
        coordsFile << "<?xml version='1.0' encoding='ISO-8859-1'?>\n"
        "<?xml-stylesheet type='text/xsl' href='image_metadata_stylesheet.xsl'?>\n"
        "<dataset>\n<name>Training faces</name>\n<images>\n";


        for (unsigned long i = 0; i < dataset.size(); ++i)
        {
            Rectangle detectRect = detector(dataset[i]);
            coordsFile << " <image file ="+dataset[i]+">\n";
            coordsFile << "  <box top='"+detectRect.top()"' left='"+detectRect.left()+"' width='"+detectRect.right()-detectRect.left()+"' height='"+detectRect.top()-detectRect.bottom()+"'>\n</box>\n";
        }

        coordsFile << "</images>\n</dataset>";
        coorsdFile.close();

    }
    catch (exception& e)
    {
        cout << "\nexception thrown!" << endl;
        cout << e.what() << endl;
    }
}