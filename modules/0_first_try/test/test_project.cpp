#include <fstream>

#include <gtest/gtest.h>
#include <opencv2/opencv.hpp>
#include <opencv2/core/utils/filesystem.hpp>

#include "header.hpp"

using namespace cv;
using namespace cv::utils::fs;

TEST(Check_travis, belive_i_can_fly_i) {
  int k = 5;
  
  EXPECT_EQ(5, k);
}

TEST(Check_f0, belive) {
  int k = 8;
  int j = FunctionName(k);
  
  EXPECT_EQ(0, j);
}

TEST(Check_f1_upalo, belive) {
  int k = 4;
  int j = FunctionName(k);
  
  EXPECT_EQ(1, j);
}