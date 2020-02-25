#include <iostream>
#include "monster.h"

namespace go {

    Monster::Monster(const std::string &_color, int _HitPoints)
        : color(_color), heads(2), dead(false)
        {
            heads[0]=std::shared_ptr<Head>(new Head(_HitPoints));
            heads[1]=std::shared_ptr<Head>(new Head(_HitPoints));
        }

    const std::string &Monster::getColor() const { return color;}
    void Monster::setColor(const std::string &value) { color = value; }

    Head& Monster::getHead(int value) {return *heads[value];}
    const Head& Monster::getHead(int value) const {return *heads[value];} 

    bool Monster::isDead() const {return dead;}

    bool Monster::isCrippled(int value) const {return getHead(value).isCrippled();}



}