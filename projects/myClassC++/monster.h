#pragma once

#include <vector>
#include <memory>
#include <Head.h>

namespace go{

    class Monster{
        
        private: std::vector <std::shared_ptr < Head > >heads;
        private: int Hit_points;
        private: int Num_heads;
        private: std::string color;
        private: bool dead;

        public: Monster(const std::string &_color, int _HitPoints = Head::DEFAULT_HIT_POINTS);

        public: const std::string &getColor() const;
        public: void setColor(const std::string &value);

        public: Head& getHead(int value);

        public: bool isDead() const;

    
    };
}