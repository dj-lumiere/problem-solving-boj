namespace ProblemSolving;

public class Boj01987
{
    public static void Main(string[] args)
    {
        var _ = Console.ReadLine()
                       .Split(' ')
                       .Select(int.Parse)
                       .ToArray();
        var (r, c) = (_[0], _[1]);
        var graph = new int[r, c];
        for (var i = 0; i < r; i++)
        {
            var s = Console.ReadLine();
            for (var j = 0; j < c; j++)
            {
                graph[i, j] = s[j] - 'A';
            }
        }

        var answer = 0L;
        // Bit arrangement: _______C CCCCCCCC ___XXXXX ___YYYYYY ______VV VVVVVVVV VVVVVVVV VVVVVVVV
        var deltaList = new List<(int, int)> { (1, 0), (-1, 0), (0, 1), (0, -1) };
        var stack = new Stack<long>();
        stack.Push((1 << 26) - 1);
        while (stack.Count > 0)
        {
            var state = stack.Pop();
            var availableAlphabet = (int)state;
            var y = state >> 32 & 0xff;
            var x = state >> 40 & 0xff;
            var count = state >> 48;
            var alphabet = graph[y, x];
            if ((availableAlphabet & (1 << alphabet)) == 0) continue;
            availableAlphabet ^= (1 << alphabet);
            answer = Math.Max(answer, count + 1);
            foreach (var (dx, dy) in deltaList)
            {
                var nx = x + dx;
                var ny = y + dy;
                if (nx < 0 || nx >= c || ny < 0 || ny >= r) continue;
                var nextState = count + 1 << 48 | nx << 40 | ny << 32 | (uint)availableAlphabet;
                stack.Push(nextState);
            }

            availableAlphabet ^= (1 << alphabet);
        }

        Console.WriteLine(answer);
    }
}