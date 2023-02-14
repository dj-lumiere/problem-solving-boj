#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int main(){
    int a, b;
    cin >> a;
    cin >> b;
    cout << a * ((b / 1) % 10) << endl;
    cout << a * ((b / 10) % 10) << endl;
    cout << a * ((b / 100) % 10) << endl;
    cout << a * b;
}