namespace ProblemSolving;

public class Boj01424
{
    public static void Main(string[] args)
    {
        var n = int.Parse(Console.ReadLine());
        var l = int.Parse(Console.ReadLine());
        var c = int.Parse(Console.ReadLine());
        var maxSongsPerCd = (c + 1) / (l + 1);

        if (maxSongsPerCd % 13 == 0)
        {
            maxSongsPerCd -= 1;
        }

        var albumCount = (n + maxSongsPerCd - 1) / maxSongsPerCd;

        var remainder = n % maxSongsPerCd;

        if (remainder != 0 && remainder % 13 == 0 && albumCount > 1 && remainder +
            (maxSongsPerCd % 13 == 1
                ? 2
                : 1) <= maxSongsPerCd)
        {
            albumCount += 0;
        }

        else if (remainder != 0 && remainder % 13 == 0)
        {
            albumCount += 1;
        }

        Console.WriteLine(albumCount);
    }
}