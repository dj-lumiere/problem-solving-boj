namespace ProblemSolving;

public class BOJ01106
{
    private static readonly Int32 INF = Int32.MaxValue >> 1;
    public static void Main(string[] args)
    {
        var firstLine = Console.ReadLine()
            .Split(' ')
            .Select(Int32.Parse)
            .ToArray();
        var c = firstLine[0];
        var n = firstLine[1];
        var cities = Enumerable.Range(0, n)
            .Select(x => Console.ReadLine()
                .Split(' ')
                .Select(Int32.Parse)
                .ToList())
            .ToList();

        var dp = new Int32[n + 1, c + 101];

        for (var i = 0; i <= n; i += 1)
        {
            for (var j = 1; j <= c + 100; j += 1)
            {
                dp[i, j] = INF;
            }
        }

        for (var i = 1; i <= n; i += 1)
        {
            for (var j = 1; j <= c + 100; j += 1)
            {
                for (var k = 1; k <= i; k += 1)
                {
                    if (j >= cities[k - 1][1])
                    {
                        dp[i, j] = Math.Min(Math.Min(dp[i, j], dp[i - 1, j]),
                            dp[i, j - cities[k - 1][1]] + cities[k - 1][0]);
                    }
                }

                dp[i, j] = Math.Min(dp[i, j], dp[i - 1, j]);
            }
        }

        var answer = INF;

        for (var i = c; i <= c + 100; i += 1)
        {
            answer = Math.Min(answer, dp[n, i]);
        }

        Console.WriteLine(answer);
    }
}