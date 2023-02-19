#include <iostream>
#include <cstring>

int main()
{
    int a_list[10001];
    int b_list[10001];
    int answer[10002];
    int i;
    int final_digit;
    int carry;
    carry = 0;
    std::string a, b, answer_string;
    std::cin >> a >> b;
    final_digit = std::max(a.size(), b.size());
    for (i = 0; i < a.size(); i++)
    {
        a_list[i] = (int)a[a.size() - i - 1] - 48;
    }
    for (i = 0; i < b.size(); i++)
    {
        b_list[i] = (int)b[b.size() - i - 1] - 48;
    }
    for (i = 0; i < final_digit; i++)
    {
        answer[i] = carry + a_list[i] + b_list[i];
        if (answer[i] > 9)
        {
            carry = 1;
            answer[i] = answer[i] % 10;
        }
        else{
            carry = 0;
        }
    }
    if (carry){
        final_digit += 1;
        answer[final_digit-1] = carry;
    }
    for (i = final_digit - 1; i >= 0; i--){
        std::cout << answer[i];
    }
    std::cout << std::endl;
}