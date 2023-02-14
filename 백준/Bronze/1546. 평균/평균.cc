#include <iostream>

int main (){
    int class_count, i, score_max, class_score_temp;
    float total_manip_score;
    int class_score[10000];
    score_max = 0;
    std::cin >> class_count;
    for (i = 0; i < class_count; i++){
        std::cin >> class_score_temp;
        if (score_max < class_score_temp)
            score_max = class_score_temp;
        class_score[i] = class_score_temp;
    }
    for (i = 0; i < class_count; i++){
        total_manip_score += class_score[i] * 100. / score_max;
    }
    std::cout << total_manip_score / class_count;
}