#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <cmath>
#pragma GCC optimize ("O3")
#pragma GCC optimize ("Ofast")
#pragma GCC optimize ("unroll-loops")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,avx,avx2")

void fastIO(){
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    std::ios_base::sync_with_stdio(false);
}

int main() {
    fastIO();
    int N;
    std::cin >> N;
    std::vector<int> A(N);
    for (int i = 0; i < N; i++) {
        std::cin >> A[i];
    }
    std::vector<int> sortedA = A;
    std::sort(sortedA.begin(), sortedA.end());
    sortedA.erase(std::unique(sortedA.begin(), sortedA.end()), sortedA.end());
    std::map<int, int> A_order;
    for (int i = 0; i < sortedA.size(); i++) {
        A_order[sortedA[i]] = i;
    }
    for (int i = 0; i < N; i++) {
        A[i] = A_order[A[i]];
    }
    int Q;
    std::cin >> Q;
    std::vector<std::pair<int, int>> queries(Q);
    for (int i = 0; i < Q; i++) {
        int s, e;
        std::cin >> s >> e;
        queries[i] = {s - 1, e - 1};
    }
    std::map<std::pair<int, int>, std::vector<int>> query_order;
    for (int i = 0; i < Q; i++) {
        query_order[queries[i]].push_back(i);
    }
    int bucket_size = sqrt(N) + 1;
    std::sort(queries.begin(), queries.end(), [bucket_size](const std::pair<int, int>& a, const std::pair<int, int>& b) {
        if (a.first / bucket_size != b.first / bucket_size) {
            return a.first / bucket_size < b.first / bucket_size;
        }
        return a.second < b.second;
    });
    std::vector<int> current_counter(N, 0);
    int current_length = 0;
    std::vector<int> answer(Q, 0);
    std::pair<int, int> last_query = {0, 0};
    for (int i = 0; i < Q; i++) {
        int s = queries[i].first;
        int e = queries[i].second;
        if (i == 0) {
            for (int j = s; j <= e; j++) {
                current_counter[A[j]]++;
                if (current_counter[A[j]] == 1) {
                    current_length++;
                }
            }
            for (int j : query_order[{s, e}]) {
                answer[j] = current_length;
            }
            last_query = {s, e};
            continue;
        }
        int s_before = last_query.first;
        int e_before = last_query.second;
        if (s_before > s) {
            for (int j = s; j < s_before; j++) {
                current_counter[A[j]]++;
                if (current_counter[A[j]] == 1) {
                    current_length++;
                }
            }
        } else if (s_before < s) {
            for (int j = s_before; j < s; j++) {
                current_counter[A[j]]--;
                if (current_counter[A[j]] == 0) {
                    current_length--;
                }
            }
        }
        if (e_before > e) {
            for (int j = e + 1; j <= e_before; j++) {
                current_counter[A[j]]--;
                if (current_counter[A[j]] == 0) {
                    current_length--;
                }
            }
        } else if (e_before < e) {
            for (int j = e_before + 1; j <= e; j++) {
                current_counter[A[j]]++;
                if (current_counter[A[j]] == 1) {
                    current_length++;
                }
            }
        }
        for (int j : query_order[{s, e}]) {
            answer[j] = current_length;
        }
        last_query = {s, e};
    }
    for (int ans : answer) {
        std::cout << ans << "\n";
    }
    return 0;
}
