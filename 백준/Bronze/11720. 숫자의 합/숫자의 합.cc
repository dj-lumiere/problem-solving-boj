#include <iostream>

int main(){
    int N, i, ith_number, sum_number;
    std::string number_string;
    std::cin >> N;
    std::cin >> number_string;
    sum_number = 0;
    for(i = 0; i < N; i++){
        sum_number += int(number_string[i]) - 48;
    }
    std::cout << sum_number;
}