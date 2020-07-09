#include <fstream>

#include <gtest/gtest.h>
#include <opencv2/opencv.hpp>
#include <opencv2/core/utils/filesystem.hpp>

#include "header.hpp"

using namespace cv;
using namespace cv::utils::fs;

TEST(Check_travis, belive_i_can_fly) {
  int k = 5;
  
  EXPECT_EQ(5, k);
}