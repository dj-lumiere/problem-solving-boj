#include <iostream>

int main(){
    std::string a, b, result;
    int i, a_digit, b_digit, carry, result_digit, len_a, len_b, maxlen;
    std::cin >> a >> b;
    len_a = a.length();
    len_b = b.length();
    result_digit = 0;
    carry = 0;
    if (len_a > len_b)
        maxlen = len_a;
    else
        maxlen = len_b;
    for (i = 1; i <= maxlen; i++) {
        if (len_a - i >= 0)
            a_digit = int(a[len_a - i]) - 48;
        else
            a_digit = 0;
        if (len_b - i >= 0)
            b_digit = int(b[len_b - i]) - 48;
        else
            b_digit = 0;
        result_digit = carry + a_digit + b_digit;
        if (result_digit >= 10){
            carry = 1;
            result_digit -= 10;
        }
        else{
            carry = 0;
        }
        result = char(result_digit + 48) + result;
    }
    if (carry == 1){
        result = char(carry + 48) + result;
        std::cout << result;
    }
    else{
        std::cout << result;
    }
}