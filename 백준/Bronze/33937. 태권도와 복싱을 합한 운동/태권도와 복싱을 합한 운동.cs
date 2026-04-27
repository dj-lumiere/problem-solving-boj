namespace ProblemSolving;

public class BOJContest1506Q1
{
    private static readonly Char[] vowels = new[] { 'a', 'e', 'i', 'o', 'u' };

    public static void Main(string[] args)
    {
        var a = Console.ReadLine();
        var b = Console.ReadLine();
        var aFirstSyllable = "";
        var bFirstSyllable = "";
        var aHasFirstSyllable = TryExtractFirstSyllable(a, out aFirstSyllable);
        var bHasFirstSyllable = TryExtractFirstSyllable(b, out bFirstSyllable);
        if (aHasFirstSyllable && bHasFirstSyllable)
        {
            Console.WriteLine(aFirstSyllable + bFirstSyllable);
        }
        else
        {
            Console.WriteLine("no such exercise");
        }
    }
    private static Boolean TryExtractFirstSyllable(String target, out String result)
    {

        String firstSyllable = "";
        var vowelEncountered = false;
        var consonantEncountered = false;
        foreach (var (i, v) in target.Select((item, index) => (index, item)))
        {
            if (vowels.Contains(v) && !consonantEncountered)
            {
                vowelEncountered = true;
                firstSyllable += v;
            }
            else if (!vowelEncountered)
            {
                firstSyllable += v;
            }
            else if (vowelEncountered)
            {
                consonantEncountered = true;
            }
        }

        if (firstSyllable == target)
        {
            result = "";
            return false;
        }

        result = firstSyllable;
        return true;
    }
}