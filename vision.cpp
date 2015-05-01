#include <iostream>
#include <opencv2/highgui/highgui.hpp>

using namespace cv;
using namespace std;

int main() {
	Mat img = imread("C:/Users/dilpreet/Documents/GitHub/MEPC-MK1/main follow image.jpg");
	imshow("opencv rpi test", img);
	waitKey(0);

	return 0;
}