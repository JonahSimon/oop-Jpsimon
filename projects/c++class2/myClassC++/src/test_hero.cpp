#include "hero.h"
#include "gtest/gtest.h"
#include "head.h"

using namespace std;
using namespace go;


// https://github.com/google/googletest/blob/master/googletest/docs/primer.md
TEST(Hero, Defaults)
{   
    Hero hero("blue", 15);
    ASSERT_EQ(hero.getColor(), "blue" );
    ASSERT_EQ(hero.isDead(), false);
    ASSERT_EQ(hero.getHP(), 15);
    hero.setHP(-15);
    ASSERT_EQ(hero.getHP(), 0);
    ASSERT_EQ(hero.isDead(), true);
    
}

TEST(Hero, Specific)
{   
    Hero hero("blue", 15);
    ASSERT_EQ(hero.getColor(), "blue" );
    ASSERT_EQ(hero.isDead(), false);
    ASSERT_EQ(hero.getHP(), 15);
    hero.setPower("immortal");
    hero.setHP(-15);
    ASSERT_EQ(hero.getHP(), 1000);
    ASSERT_EQ(hero.isDead(), false);
    
}


int main(int argc, char** argv){
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}