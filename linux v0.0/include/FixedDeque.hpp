#include <deque>

// FixedDqueue limits the size of deque to provided MaxLen
template <typename T, int MaxLen>
class FixedDeque: public std::deque<T>{
    public:
        void push_back(T item){
            if(this->size() >= MaxLen){
                this->pop_front();
            }
            std::deque<T>::push_back(item);
        }

        T get_avg(){
            return (std::accumulate(std::deque<T>::begin(), std::deque<T>::end(), 1.0) / std::deque<T>::size());
        }
};