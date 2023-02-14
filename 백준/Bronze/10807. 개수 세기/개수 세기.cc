#include <iostream>

int main(){
    int N, i, v, c;
    int array[100];
    c = 0;
    std::cin >> N;
    for (i = 0; i < N; i++){
        std::cin >> array[i];
    }
    std::cin >> v;
    for (i = 0; i < N; i++){
        if (array[i] == v)
            c += 1;
    }
    std::cout << c;
}