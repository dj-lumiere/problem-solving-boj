using System.Text;

namespace ProblemSolving;

public class BojContest1524Q1
{
    public static void Main(string[] args)
    {
        var t = Int32.Parse(Console.ReadLine());
        var sb = new StringBuilder();
        for (var i = 0; i < t; i += 1)
        {
            var _ = Console.ReadLine()
                .Split(' ')
                .Select(Int32.Parse)
                .ToArray();
            var n = _[0];
            var k = _[1];
            if (k == 1 && n <= 3)
            {
                sb.AppendLine("-1");
            }
            else if (k == 1 && n == 4)
            {
                sb.AppendLine("3 1 4 2");
            }
            else if (k == 1)
            {
                //all odd all even
                var result = new List<Int32>();
                for (var j = 1; j <= n; j += 2)
                {
                    result.Add(j);
                }

                for (var j = 2; j <= n; j += 2)
                {
                    result.Add(j);
                }

                sb.AppendLine(string.Join(" ", result));
            }
            else
            {
                //simple sequence
                var result = new List<Int32>();
                for (var j = 1; j <= n; j += 1)
                {
                    result.Add(j);
                }

                sb.AppendLine(string.Join(" ", result));
            }
        }
        Console.WriteLine(sb.ToString());
    }
}