#include <iostream>
#include <cmath>

int main(){
    int a, b, n, v, v_rest;
    std::cin >> a >> b >> v;
    n = (v - b) / (a - b);
    v_rest = (v - b) % (a - b);
    if (v_rest){
        n += 1;
    }
    std::cout << n;
}