namespace ProblemSolving;

public class BOJContest1503Q2
{
    public static void Main(string[] args)
    {
        var firstLine = Console.ReadLine()
            .Split(' ')
            .Select(Int32.Parse)
            .ToArray();
        var a = firstLine[0];
        var b = firstLine[1];
        var c = firstLine[2];
        
        var secondLine = Console.ReadLine()
            .Split(' ')
            .Select(Int32.Parse)
            .ToArray();
        var s = secondLine[0];
        var v = secondLine[1];
        
        var l = Int32.Parse(Console.ReadLine());

        var requiredExpPoints = (250 - l) * 100;
        var answer = 0;
        // first use the vip map
        var vipExpPoints = v * 30 * c;
        // second use the "심신수련관" map
        var simsinExpPoints = s * 30 * b;
        // and then use the event map.
        if (requiredExpPoints <= vipExpPoints)
        {
            answer = (requiredExpPoints + c - 1) / c;
        }
        else if (requiredExpPoints <= vipExpPoints + simsinExpPoints)
        {
            answer = v * 30 + (requiredExpPoints - vipExpPoints + b - 1) / b;
        }
        else
        {
            answer = (v + s) * 30 +
                     (requiredExpPoints - vipExpPoints - simsinExpPoints + a - 1) / a;
        }

        Console.WriteLine(answer);
    }
}