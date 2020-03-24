#include <iostream>
#include "hero.h"

namespace go {

    Hero::Hero(const std::string &_color, int _HitPoints)
        : color(_color), heads(2), dead(false)
        {
            Hero::Hit_points = _HitPoints;
            heads[0]=std::shared_ptr<Head>(new Head(_HitPoints));
            heads[1]=std::shared_ptr<Head>(new Head(_HitPoints));
        }

    const std::string &Hero::getPower() const { return power;}
    void Hero::setPower(const std::string &value) { power = value; }

    const std::string &Hero::getColor() const { return color;}
    void Hero::setColor(const std::string &value) { color = value; }

    Head& Hero::getHead(int value) {return *heads[value];}
    const Head& Hero::getHead(int value) const {return *heads[value];} 

    const int &Hero::getHP() const {return Hit_points;}
    void Hero::setHP(int value) 
    {
        if(power == "immortal")
            Hit_points = 1000;

        else if ((Hit_points + value) <= 0){
            dead =true;
            Hit_points = 0;
        }

        else if(dead)
            Hit_points = 0;

        else Hit_points += value;
    }

    bool Hero::isDead() const {return dead;}

    bool Hero::isCrippled(int value) const {return getHead(value).isCrippled();}



}