#include <iostream>
#include <cstdint>
#include <vector>
#include <string>

using namespace std;

int main()
{
    int32_t t;
    cin >> t;
    for (int32_t i = 1; i <= t; i++) {
        cout << "Data Set " << i << ":\n";
        int32_t h, w;
        cin >> h >> w;
        vector<int32_t> oil_cost(w, 0);
        vector<bool> found_oil(w, false);
        for (int32_t j = 0; j < h; j++) {
            string line;
            cin >> line;
            for (int32_t k = 0; k < w; k++) {
                char s = line[k];
                if (s == 'X') {
                    found_oil[k] = true;
                }
                else if (not found_oil[k] and s == 'H') {
                    oil_cost[k] += 3;
                }
                else if (not found_oil[k] and s == 'S') {
                    oil_cost[k] += 1;
                }
            }
        }
        for (int32_t k = 0; k < w; k++) {
            if (found_oil[k]) {
                cout << oil_cost[k];
            }
            else {
                cout << "N";
            }
            if (k + 1 < w) {
                cout << " ";
            }
        }
        cout << "\n\n";
    }
}