#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int32_t T;
    cin >> T;
    for (int32_t t = 0; t < T; t += 1)
    {
        int N, M;
        cin >> N >> M;
        vector<vector<int32_t>> grid(N + 1, vector<int32_t>(N + 1, 0));
        for (int32_t i = 0; i < M; i++)
        {
            int32_t V;
            int32_t A, B;
            cin >> V >> A >> B;
            grid[A][B] += V;
        }

        vector<pair<int32_t, int32_t>> pairs;
        vector<int32_t> pair_values;
        for (int32_t a = 1; a <= N; a++)
        {
            for (int32_t b = 1; b <= N; b++)
            {
                if (a == b) continue;
                if (grid[a][b] > 0)
                {
                    pairs.emplace_back(a, b);
                    pair_values.emplace_back(grid[a][b]);
                }
            }
        }
        vector<int32_t> perm;
        for (int32_t i = 1; i <= N; i++) perm.push_back(i);
        int32_t max_score = 0;
        int32_t count = 0;
        do
        {
            vector<int32_t> pos(N + 1, 0);
            for (int32_t i = 0; i < N; i++) pos[perm[i]] = i;
            int32_t score = 0;
            for (int32_t i = 0; i < pairs.size(); i++)
            {
                int32_t a = pairs[i].first;
                int32_t b = pairs[i].second;
                if (pos[a] < pos[b])
                {
                    score += pair_values[i];
                }
            }
            if (score > max_score)
            {
                max_score = score;
                count = 1;
            }
            else if (score == max_score)
            {
                count += 1;
            }
        } while (next_permutation(perm.begin(), perm.end()));
        cout << max_score << " " << count << "\n";
    }
}
