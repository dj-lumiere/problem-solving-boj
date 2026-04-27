namespace ProblemSolving;

public class BOJContest11476Q2
{
    public static void Main(string[] args)
    {
        var n = int.Parse(Console.ReadLine());
        var a = Console.ReadLine();
        if (a.StartsWith("A") && a.EndsWith("B"))
        {
            Console.WriteLine("Yes");
        }
        else
        {
            Console.WriteLine("No");
        }
    }
}