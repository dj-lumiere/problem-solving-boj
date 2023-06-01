#include <iostream>
#include <random>

#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#pragma GCC target("avx,avx2")

using namespace std;

typedef __int128_t int128;
typedef int64_t int64;
typedef int32_t int32;
typedef __uint128_t uint128;
typedef uint64_t uint64;
typedef uint32_t uint32;
typedef long double float80;
typedef double float64;
typedef float float32;
typedef string str;
typedef void None;

#define print cout
#define input cin
#define append push_back
#define appendleft push_front
#define popleft pop_front
#define elif else if

None fastIO()
{
    std::cin.tie(NULL);
    std::cout.tie(NULL);
    std::ios_base::sync_with_stdio(false);
}

int32 main()
{
    fastIO();
    int64 N;
    input >> N;
    vector<int64> K;
    vector<int64> K_acc_sum = {0};
    int64 element;
    for (int64 index = 0; index < N; index++)
    {
        input >> element;
        K.append(element);
    }
    for (int64 index = 0; index < N; index++)
    {
        K_acc_sum.append(K_acc_sum[K_acc_sum.size() - 1] + K[index]);
    }
    for (int64 index = 0; index < N; index++)
    {
        K_acc_sum.append(K_acc_sum[K_acc_sum.size() - 1] + K[index]);
    }
    int64 total_sum = K_acc_sum[N];
    int64 answer = 0;
    for (int64 offset = 0; offset < N; offset++)
    {
        for (int64 items = 0; items < N; items++)
        {
            int64 index_start = offset;
            int64 index_end = offset + items + 1;
            int64 acc_sum = K_acc_sum[index_end] - K_acc_sum[index_start];
            if (acc_sum < 0)
            {
                answer += static_cast<int64>(ceill(static_cast<float80>(-acc_sum) / static_cast<float80>(total_sum)));
            }
        }
    }
    print << answer;
}
