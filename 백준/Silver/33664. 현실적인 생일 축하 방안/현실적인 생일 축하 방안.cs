namespace ProblemSolving
{
    public class BOJ33664
    {
        public static void Main(string[] args)
        {
            Int64 b, n, m;
            var input = Console.ReadLine().Split(' ').Select(Int64.Parse).ToArray();
            b = input[0];
            n = input[1];
            m = input[2];
            var priceMap = new Dictionary<String, Int64>();
            for (var i = 0; i < n; i += 1)
            {
                var input2 = Console.ReadLine().Split(' ');
                priceMap[input2[0]] = Int64.Parse(input2[1]);
            }

            var totalPrice = 0L;
            for (var i = 0; i < m; i += 1)
            {
                var input3 = Console.ReadLine().Split(' ');
                totalPrice += priceMap[input3[0]];
            }

            if (totalPrice > b)
            {
                Console.WriteLine("unacceptable");
            }
            else
            {
                Console.WriteLine("acceptable");
            }
        }
    }
}