#include "genbase.h"


template <typename ModType>
class LCGenerator : public RandomGenBase {
    protected:
        ModType a = 32;
        ModType b = 32;

    public:
        LCGenerator(ModType a, ModType b) : a_(a), b_(b) {}
        LCGenerator() = default;
        ModType generate() const {
            if (this->seed == this->current) {
                this->current = (a * this->seed + b) % this->modulo;
            }
            else {
                this->current = (a * this->current + b) % this->modulo;
            }
            return this->current;
        }
};