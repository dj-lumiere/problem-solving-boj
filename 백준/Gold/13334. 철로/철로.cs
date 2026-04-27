namespace ProblemSolving;

public class Boj13334
{
    public static void Main(string[] args)
    {
        var n = Int32.Parse(Console.ReadLine());
        var hoPair = new List<(Int32 left, Int32 right)>();
        var orderedNumbers = new SortedSet<int>();

        for (int i = 0; i < n; i += 1)
        {
            var _ = Console.ReadLine()
                           .Split(' ')
                           .Select(Int32.Parse)
                           .ToArray();
            var h = _[0];
            var o = _[1];
            if (h > o)
            {
                (h, o) = (o, h);
            }

            hoPair.Add((h, o));
            orderedNumbers.Add(h);
            orderedNumbers.Add(o);
        }

        var d = Int32.Parse(Console.ReadLine());
        var filteredHoPair = hoPair.Where(x => x.right - x.left <= d)
                                   .OrderBy(x => x.right)
                                   .ThenBy(x => x.left)
                                   .ToList();
        if (filteredHoPair.Count == 0)
        {
            Console.WriteLine(0);
            return;
        }

        var availableUsers = new PriorityQueue<(int left, int right), int>();
        var lastIdx = 0;
        var maxUserCount = availableUsers.Count;

        foreach (var (left, right) in filteredHoPair)
        {
            var segmentStart = right - d;
            availableUsers.Enqueue((left, right), left);
            while (availableUsers.Count > 0 && availableUsers.Peek()
                                                             .left < segmentStart)
            {
                availableUsers.Dequeue();
            }

            maxUserCount = Math.Max(maxUserCount, availableUsers.Count);
        }

        Console.WriteLine(maxUserCount);
    }
}