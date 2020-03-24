#pragma once

#include "character.h"
#include <vector>
#include <memory>
#include "head.h"

namespace go{

    class Hero : public Character{
        
        private: std::vector <std::shared_ptr < Head > >heads;
        private: int Hit_points;
        private: int Num_heads;
        private: std::string color;
        private: std::string power = "none";
        private: bool dead;

        public: Hero(const std::string &_color, int _HitPoints = Head::DEFAULT_HIT_POINTS);

        public: const std::string &getPower() const;
        public: void setPower(const std::string &value);

        public: const std::string &getColor() const;
        public: void setColor(const std::string &value);

        public: const int  &getHP() const;
        public: void setHP(const int value);

        public: Head& getHead(int value);
        public: const Head& getHead(int value) const;

        public: bool isDead() const;

        public: bool isCrippled(int value) const;
    
    };
    typedef std::shared_ptr < Hero > HeroPtr;
}