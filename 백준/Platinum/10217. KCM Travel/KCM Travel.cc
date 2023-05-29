// 10217 KCM Travel

#include <iostream>
#include <algorithm>
#include <complex>
#include <random>
#include <unordered_map>
#include <unordered_set>
#include <deque>
#include <queue>
#include <cmath>
#include <list>
#include <map>
#include <set>
#include <chrono>

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
typedef complex<float80> complex80;
typedef complex<float64> complex64;
typedef complex<float32> complex32;
typedef string str;
typedef void None;

#define print cout
#define input cin
#define append push_back
#define appendleft push_front
#define popleft pop_front
#define elif else if

const int32 INF = 1e9;

typedef tuple<int32, int32, int32> Node;

vector<vector<Node>> graph_list;

None graphify(int32 ticket_count)
{
    for (int32 i = 0; i < ticket_count; i++)
    {
        int32 departing_port, arriving_port, cost, travel_time;
        input >> departing_port >> arriving_port >> cost >> travel_time;
        graph_list[departing_port].push_back(make_tuple(travel_time, cost, arriving_port));
    }
}

None dijkstra(int32 init, int32 dst, int32 cost_limit)
{
    if (init == dst)
    {
        return;
    }
    else
    {
        priority_queue<Node, vector<Node>, greater<Node>> heap;
        heap.push(make_tuple(0, 0, init));
        vector<vector<int32>> time_cost_list(dst + 1, vector<int32>(cost_limit + 1, INF));
        time_cost_list[init][0] = 0;
        while (not heap.empty())
        {
            Node current_node = heap.top();
            heap.pop();
            int32 time = get<0>(current_node);
            int32 cost = get<1>(current_node);
            int32 vertex = get<2>(current_node);
            if (time_cost_list[vertex][cost] < time)
            {
                continue;
            }
            for (Node next_node : graph_list[vertex])
            {
                int32 next_cost = cost + get<1>(next_node);
                int32 next_time = time + get<0>(next_node);
                if (next_cost > cost_limit)
                {
                    continue;
                }
                if ((next_cost <= cost_limit) and (next_time < time_cost_list[get<2>(next_node)][next_cost]))
                {
                    time_cost_list[get<2>(next_node)][next_cost] = next_time;
                    heap.push(make_tuple(next_time, next_cost, get<2>(next_node)));
                }
            }
        }
        int32 min_time = *min_element(time_cost_list[dst].begin(), time_cost_list[dst].end());
        if (min_time == INF)
        {
            print << "Poor KCM\n";
        }
        else
        {
            print << min_time << "\n";
        }
    }
}

int32 main()
{
    int32 T;
    cin >> T;
    for (int32 t = 0; t < T; t++)
    {
        int32 node_count, total_budget, ticket_count;
        cin >> node_count >> total_budget >> ticket_count;
        graph_list = vector<vector<Node>>(node_count + 1, vector<Node>());
        graphify(ticket_count);
        dijkstra(1, node_count, total_budget);
    }
}
