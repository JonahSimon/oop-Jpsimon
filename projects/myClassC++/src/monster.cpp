#include <iostream>
#include "monster.h"

namespace go {

    Monster::Monster(const std::string &_color, int _HitPoints)
        : color(_color), heads(2), dead(false)
        {
            Monster::Hit_points = _HitPoints;
            heads[0]=std::shared_ptr<Head>(new Head(_HitPoints));
            heads[1]=std::shared_ptr<Head>(new Head(_HitPoints));
        }

    const std::string &Monster::getColor() const { return color;}
    void Monster::setColor(const std::string &value) { color = value; }

    Head& Monster::getHead(int value) {return *heads[value];}
    const Head& Monster::getHead(int value) const {return *heads[value];} 

    const int &Monster::getHP() const {return Hit_points;}
    void Monster::setHP(int value) 
    {
        Hit_points += value;

        if (Hit_points <= 0)
        {
            dead =true;
        }
        
        if(dead)
        {
            Hit_points = 0;
        }
    }

    bool Monster::isDead() const {return dead;}

    bool Monster::isCrippled(int value) const {return getHead(value).isCrippled();}



}