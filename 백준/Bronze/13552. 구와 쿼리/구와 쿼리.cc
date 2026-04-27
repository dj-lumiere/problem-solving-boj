// 13552 구와 쿼리

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


using namespace std;

typedef int64_t int64;
typedef int32_t int32;
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

None fastIO()
{
    std::cin.tie(NULL);
    std::cout.tie(NULL);
    std::ios_base::sync_with_stdio(false);
}

struct point
{
    int32 x_coordinate = 0;
    int32 y_coordinate = 0;
    int32 z_coordinate = 0;
};

struct sphere
{
    int32 center_x_coordinate = 0;
    int32 center_y_coordinate = 0;
    int32 center_z_coordinate = 0;
    int32 radius = 0;
};

bool is_in_sphere(point& point, sphere& sphere)
{
    int64 x_distance = point.x_coordinate - sphere.center_x_coordinate;
    int64 y_distance = point.y_coordinate - sphere.center_y_coordinate;
    int64 z_distance = point.z_coordinate - sphere.center_z_coordinate;
    int64 distance_squared = x_distance * x_distance + y_distance * y_distance + z_distance * z_distance;
    return (distance_squared <= static_cast<int64>(sphere.radius) * sphere.radius);
}

int32 main()
{
    fastIO();
    int32 N = 0, M = 0;
    int32 x = 0, y = 0, z = 0, r = 0;
    int32 answer = 0;
    point point_element;
    sphere sphere_element;
    vector<point> point_list;
    input >> N;
    for (int32 i = 0; i < N; i++)
    {
        input >> x >> y >> z;
        point_element.x_coordinate = x;
        point_element.y_coordinate = y;
        point_element.z_coordinate = z;
        point_list.append(point_element);
    }
    input >> M;
    for (int32 i = 0; i < M; i++)
    {
        answer = 0;
        input >> x >> y >> z >> r;
        sphere_element.center_x_coordinate = x;
        sphere_element.center_y_coordinate = y;
        sphere_element.center_z_coordinate = z;
        sphere_element.radius = r;
        for (auto it = point_list.begin(); it != point_list.end(); ++it)
        {
            if (is_in_sphere(*it, sphere_element))
            {
                answer += 1;
            }
        }
        print << answer << "\n";
    }
}
