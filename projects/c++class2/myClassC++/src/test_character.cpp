#include "character.h"
#include "hero.h"
#include "monster.h"
#include "gtest/gtest.h"

using namespace std;
using namespace go;

// https://github.com/google/googletest/blob/master/googletest/docs/primer.md
TEST(character, AsObjects) {
  Character character;
  Hero hero("blue",50);
  ASSERT_EQ(hero.isDead(),false);
  character = hero;
  ASSERT_EQ(character.isDead(),false);
}

TEST(character, AsPointers) {
  CharacterPtr character = CharacterPtr(new Character());
  HeroPtr hero = HeroPtr(new Hero("red",50));
  ASSERT_EQ(hero->isDead(),false);
  character = hero;
  ASSERT_EQ(character->isDead(),false);
}

int main(int argc, char** argv) {
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
