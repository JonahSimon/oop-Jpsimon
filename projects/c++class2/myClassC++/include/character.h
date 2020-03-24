#pragma once

#include <memory>

namespace go {

    class Character {
    private: bool Dead;

    public: Character(bool _Dead = false);
    public: virtual void setdead();
    public: virtual void setalive();

    public: virtual bool isDead() const;
    };

    typedef std::shared_ptr < Character > CharacterPtr;
 }

