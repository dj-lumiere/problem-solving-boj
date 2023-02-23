#include <iostream>
#include <vector>
#include <deque>
#include <tuple>

int x_size, y_size;

std::vector<std::vector<int>> graph;
std::vector<std::vector<int>> graph2;
std::vector<std::tuple<int, int>> dx_dy_list = {std::make_tuple(-1, 0), std::make_tuple(1, 0), std::make_tuple(0, -1), std::make_tuple(0, 1)};

int dfs(int pos_x, int pos_y)
{
    int dx, dy;
    if (pos_x < 0 || pos_x >= x_size || pos_y < 0 || pos_y >= y_size)
    {
        return 0;
    }
    if (graph[pos_y][pos_x] != 0)
    {
        graph[pos_y][pos_x] = 0;
        for (std::vector<std::tuple<int, int>>::iterator it = dx_dy_list.begin(); dx_dy_list.end() != it; ++it)
        {
            auto [dx, dy] = *it;
            int new_x = pos_x + dx;
            int new_y = pos_y + dy;
            dfs(new_x, new_y);
        }
        return 1;
    }
    return 0;
}
void ice_melting(std::deque<std::tuple<int, int>> queue)
{
    int x, y, dx, dy;
    while (queue.size() != 0)
    {
        auto [x, y] = queue[0];
        queue.pop_front();
        int melting_direction_counter = 0;
        for (std::vector<std::tuple<int, int>>::iterator it = dx_dy_list.begin(); dx_dy_list.end() != it; ++it)
        {
            auto [dx, dy] = *it;
            int new_x = x + dx;
            int new_y = y + dy;
            if (new_x < 0 || new_x >= x_size || new_y < 0 || new_y >= y_size)
            {
                continue;
            }
            if (graph2[new_y][new_x] == 0)
            {
                melting_direction_counter += 1;
            }
        }
        graph[y][x] = std::max(graph2[y][x] - melting_direction_counter, 0);
    }
}

int main()
{
    std::cin >> y_size >> x_size;
    int T = 0;
    int item;
    int icebergs;
    int x, y;
    std::vector<std::tuple<int, int>> dfs_stack;
    std::deque<std::tuple<int, int>> bfs_queue;
    std::vector<int> graph_sub;
    std::vector<int> graph_sub2;
    for (int y = 0; y < y_size; y++)
    {
        for (int x = 0; x < x_size; x++)
        {
            std::cin >> item;
            graph_sub.push_back(item);
            graph_sub2.push_back(0);
        }
        graph.push_back(graph_sub);
        graph2.push_back(graph_sub2);
        graph_sub.clear();
        graph_sub2.clear();
    }
    while (1)
    {
        for (int y = 0; y < y_size; y++)
        {
            for (int x = 0; x < x_size; x++)
            {
                graph2[y][x] = graph[y][x];
            }
        }
        icebergs = 0;
        for (int y = 0; y < y_size; y++)
        {
            for (int x = 0; x < x_size; x++)
            {
                if (graph[y][x] > 0)
                {
                    dfs_stack.push_back(std::make_tuple(x, y));
                    bfs_queue.push_back(std::make_tuple(x, y));
                }
            }
        }
        for (std::vector<std::tuple<int, int>>::iterator it = dfs_stack.begin(); dfs_stack.end() != it; ++it)
        {
            auto [x, y] = *it;
            icebergs += dfs(x, y);
        }
        dfs_stack.clear();
        if (icebergs > 1)
        {
            break;
        }
        else if (bfs_queue.size() == 0)
        {
            T = 0;
            break;
        }
        else
        {
            ice_melting(bfs_queue);
            for (int y = 0; y < y_size; y++)
            {
                for (int x = 0; x < x_size; x++)
                {
                    graph2[y][x] = graph[y][x];
                }
            }
            bfs_queue.clear();
            T += 1;
        }
    }
    std::cout << T << std::endl;
}
