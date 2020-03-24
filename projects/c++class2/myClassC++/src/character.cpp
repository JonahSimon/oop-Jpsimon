#include "character.h"

namespace go {

    Character::Character(bool _Dead)
      :  Dead(_Dead)
    {
    }
    void Character::setdead() {
        Dead = true;
    }
    void Character::setalive() {
        Dead = false;
    }

    bool Character::isDead() const {
        return Dead;
    }

 }

