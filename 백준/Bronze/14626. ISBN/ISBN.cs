namespace ProblemSolving;

public class BOJ14626
{
    public static void Main(string[] args)
    {
        var weights = new[] { 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1 };
        var code = Console.ReadLine();
        var answer = 0;
        var starDigitIndex = code.IndexOf('*');
        var codeList = code.Select(x => x - '0')
            .ToList();
        for (var i = 0; i < 10; i += 1)
        {
            codeList[starDigitIndex] = i;
            var checkIsbn = codeList.Zip(weights, (x, y) => x * y)
                .Sum();
            if (checkIsbn % 10 == 0)
            {
                answer = i;
                break;
            }
        }

        Console.WriteLine(answer);
    }
}