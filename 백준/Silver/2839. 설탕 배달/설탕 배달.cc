#include <iostream>
#include <stdio.h>

int main (){
    int N, bag_5, bag_3, rest, bag_count;
    std::cin >> N;
    bag_5 = N / 5;
    bag_3 = 0;
    rest = (N % 5);
    bag_count = bag_5 + bag_3;
    while (true){
        bag_3 += rest / 3;
        rest = N - bag_5 * 5 - bag_3 * 3;
        bag_count = bag_5 + bag_3;
        if (rest == 0){
            std::cout << bag_count;
            break;
        }
        else{
            bag_5 -= 1;
            rest += 5;
            if (bag_5 < 0){
                std::cout << -1;
                break;
            }
        }
    }
}