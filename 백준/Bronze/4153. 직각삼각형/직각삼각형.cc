#include <iostream>

int main(){
    int a, b, c;
    a = 0;
    b = 0;
    c = 0;
    while (true){
        std::cin >> a >> b >> c;
        if (not((a && b && c))){
            break;
        }
        else if ((a*a + b*b - c*c) && (b*b + c*c - a*a) && (c*c + a*a - b*b)){
            std::cout << "wrong" << std::endl;
        }
        else{
            std::cout << "right" << std::endl;
        }
    }
}