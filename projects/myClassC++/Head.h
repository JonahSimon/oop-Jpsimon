#pragma once

#include <stdexcept>

namespace go {

    class Head {
        public: static const int DEFAULT_HIT_POINTS;
        public: static const int DEFAULT_CRIPPLED; 
        private: int hp;
        private: bool CRIPPLED;
        
        public: Head(int _hp = DEFAULT_HIT_POINTS, bool _crippled = DEFAULT_CRIPPLED);

        public: int getHP() const;

        public: void setHP(int value);

        public: bool isCrippled() const;


    };

}