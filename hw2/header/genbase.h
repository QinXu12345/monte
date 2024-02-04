#include <cstdint>

template <typename ModType>
class RandomGenBase {
    protected:
        ModType seed = 0;
        ModType current = 0;
    public:
        RandomGenBase() = default;
        static void set_seed(ModType seed) { seed = seed;}
        static Modtype get_seed() const { return seed;}
        virtual ModType generate() const = 0;
};