// eye.cpp

#include <iostream>
#include "opencv2/core/core_c.h"
#include "opencv2/core/core.hpp"
#include "opencv2/flann/miniflann.hpp"
#include "opencv2/imgproc/imgproc_c.h"
#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/video/video.hpp"
#include "opencv2/features2d/features2d.hpp"
#include "opencv2/objdetect/objdetect.hpp"
#include "opencv2/calib3d/calib3d.hpp"
#include "opencv2/ml/ml.hpp"
#include "opencv2/highgui/highgui_c.h"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/contrib/contrib.hpp"

using namespace cv;
using namespace std;

int main() {
	Mat img = imread("C:/Users/dilpreet/Documents/GitHub/MEPC-MK1/main follow image.jpg");
	if (img.empty()) {
		return -1;
	}

	// Convert to grayscale
	Mat gray;
	cvtColor(img, gray, CV_BGR2GRAY);

	// Convert to binary using Canny
	Mat bw;
	Canny(gray, bw, 0, 50, 5);

	// Find contours
	vector<std::vector<Point>> contours;
	findContours(bw.clone(), contours, CV_RETR_EXTERNAL, CV_CHAIN_APPROX_SIMPLE);

	// Array for soring the approximation curve
	vector<Point> approx;

	// We'll put the labels in this destination image
	Mat dst = img.clone();

	for (int i = 0; i < contours.size(); i++) {
		// Approximate contour with accuracy proportional
		// to the contour perimeter
		approxPolyDP (
			Mat(contours[i]),
			approx,
			arcLength(Mat(contours[i]), true) * 0.02,
			true
		);

		// Ignore small or non-convex objects
		if (fabs(contourArea(contours[i])) < 100 || !isContourConvex(approx)) {
			continue;
		}

		if (approx.size() == 4) {
			// Number of verticies of polygon curve
			int vtc = approx.size();

			// Get the degree (in cosine) of all corners
			vector<double> cos;
			for (int j = 2; j < vtc+1; j++) {
				cos.push_back(angle(approx[j%vtc], approx[j-2], approx[j-1]));
			}

			// Sort ascending the corner degree values
			sort(cos.begin(), cos.end());

			// Get the lowest and the highest degree
			double mincos = cos.front();
			double maxcos = coe.back();

			// Use the degree obtained above and the number of verticies
			// to determine the shape of the contour
			if (vtc == 4 && mincos >= -0.1 && maxcos <= 0.3) {
				// Detect rectangle or square
				Rect r = boundingRect(contours[i]);
				double ratio = abs(1 - (double)r.width / r.height);

				setLable(dst, ratio <= 0.02 ? "SQU" : "RECT", contours[i]);
			}
		}
	}

	imshow("Source", img);
	imshow("Detect Rectangles", dst);

	waitKey(0);

	return 0;
}