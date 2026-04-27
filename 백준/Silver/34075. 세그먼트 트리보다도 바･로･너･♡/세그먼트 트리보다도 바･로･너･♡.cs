namespace ProblemSolving;

public class Boj34075
{
    public const string NoMatch = "~";
    public static void Main(string[] args)
    {
        var n = Int32.Parse(Console.ReadLine());
        var algos = new List<(String, Int32 )>();
        for (var i = 0; i < n; i += 1)
        {
            var _ = Console.ReadLine()
                .Split();
            var algo = _[0];
            var difficulty = Int32.Parse(_[1]);
            algos.Add((algo, difficulty));
        }

        var m = Int32.Parse(Console.ReadLine());
        var members = new List<(String, Int32 )>();
        for (var i = 0; i < m; i += 1)
        {
            var _ = Console.ReadLine()
                .Split();
            var member = _[0];
            var tier = Int32.Parse(_[1]);
            members.Add((member, tier));
        }

        var firstAlgorithmByTier = new String[32];
        var secondAlgorithmByTier = new String[32];

        for (var i = 0; i <= 31; i += 1)
        {
            var i1 = i;
            var algorithmByTierAndName = algos
                .OrderBy(x => (Math.Abs(i1 - x.Item2), x.Item1))
                .Select(x => x.Item1)
                .Take(2);
            firstAlgorithmByTier[i] = algorithmByTierAndName.FirstOrDefault(NoMatch);
            secondAlgorithmByTier[i] = algorithmByTierAndName.Skip(1)
                .FirstOrDefault(NoMatch);
        }

        // Console.WriteLine(firstAlgorithmByTier.Repr());
        // Console.WriteLine(secondAlgorithmByTier.Repr());

        var favoriteAlgorithms = new Dictionary<String, (String, String)>();

        for (var i = 0; i < m; i += 1)
        {
            favoriteAlgorithms[members[i].Item1] = (firstAlgorithmByTier[members[i].Item2],
                secondAlgorithmByTier[members[i].Item2]);
        }

        // Console.WriteLine(string.Join(", ", favoriteAlgorithms));
        var q = Int32.Parse(Console.ReadLine());
        var currentAnsweringMember = "";
        for (var i = 0; i < q; i += 1)
        {
            var query = Console.ReadLine();
            if (query == "nani ga suki?")
            {
                var secondFavorite = favoriteAlgorithms[currentAnsweringMember].Item2;
                var firstFavorite = favoriteAlgorithms[currentAnsweringMember].Item1;
                Console.WriteLine($"{secondFavorite} yori mo {firstFavorite}");
            }
            else
            {
                currentAnsweringMember = query.Split()[0];
                Console.WriteLine("hai!");
            }
        }
    }
}