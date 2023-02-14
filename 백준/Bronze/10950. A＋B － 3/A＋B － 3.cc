#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int main(){
    int calc_count, a, b, i;
    cin >> calc_count;
    for (i = 0; i < calc_count; i++){
        cin >> a >> b;
        cout << a + b << "\n";
    }
}