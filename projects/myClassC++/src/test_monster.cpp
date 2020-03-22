#include "monster.h"
#include "gtest/gtest.h"
#include "Head.h"

using namespace std;
using namespace go;


// https://github.com/google/googletest/blob/master/googletest/docs/primer.md
TEST(Monster, Defaults)
{   
    Monster monster("blue", 15);
    ASSERT_EQ(monster.getColor(), "blue" );
    ASSERT_EQ(monster.isDead(), false);
    ASSERT_EQ(monster.getHP(), 15);
    monster.setHP(-15);
    ASSERT_EQ(monster.getHP(), 0);
    ASSERT_EQ(monster.isDead(), true);
    
}


int main(int argc, char** argv){
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}