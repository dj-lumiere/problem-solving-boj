namespace ProblemSolving;

public class BojContest1543Q1
{
    public static void Main(string[] args)
    {
        var MOD = 998_244_353;
        var n = Int32.Parse(Console.ReadLine());
        var a = Console.ReadLine()
                       .Split(" ")
                       .Select(Int32.Parse)
                       .ToArray();
        var answer = 1L;
        for (var i = 0; i < n; i += 1)
        {
            if (a[i] != i + 1)
            {
                answer *= n - 2;
                answer %= MOD;
            }
            else
            {
                answer *= n - 1;
                answer %= MOD;
            }
        }

        Console.WriteLine(answer);
    }
}