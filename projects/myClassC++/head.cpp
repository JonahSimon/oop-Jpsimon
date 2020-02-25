#include <stdexcept>
#include "Head.h"

namespace go 
{

const int Head::DEFAULT_HIT_POINTS = 15;
const bool Head::DEFAULT_CRIPPLED = false;

Head::Head(int _HP, bool _crippled)
    : hp(_HP), CRIPPLED(_crippled)
    {
        if (hp <= 0){
            CRIPPLED = true;
        }
    }

int Head::getHP() const
{
    return hp;
}

bool Head::isCrippled() const 
{
    return CRIPPLED;
}

void Head::setHP(int value)
{
    hp += value;
    if (hp <= 0)
    {
        CRIPPLED =true;
    }
    if(CRIPPLED)
    {
        hp = 0;
    }
}

}