namespace ProblemSolving;

public class BOJContest1508Q1
{
    public static void Main(string[] args)
    {
        var n = Int32.Parse(Console.ReadLine());
        var abc = new List<Int32>();
        for (var i = 0; i < n; i += 1)
        {
            var input = Console.ReadLine()
                .Split(' ')
                .Select(Int32.Parse)
                .ToArray();
            abc.Add(input[0] + input[1] + input[2]);
        }

        var answer = -1;
        foreach (var x in abc)
        {
            if (x >= 512 && Math.Abs(answer - 512) > Math.Abs(x - 512))
            {
                answer = x;
            }
        }

        Console.WriteLine(answer);
    }
}