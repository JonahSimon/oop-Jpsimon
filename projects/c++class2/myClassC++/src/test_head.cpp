#include "monster.h"
#include "gtest/gtest.h"
#include "head.h"

using namespace std;
using namespace go;


// https://github.com/google/googletest/blob/master/googletest/docs/primer.md
TEST(Monster, Defaults){

}



int main(int argc, char** argv){
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}