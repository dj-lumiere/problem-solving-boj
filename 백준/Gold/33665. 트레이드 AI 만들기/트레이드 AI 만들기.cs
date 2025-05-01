namespace ProblemSolving;

public class BOJ33665
{
    public static List<List<Int32>> propertyScores = new();

    public static Int32 cashWeight;
    public static Int32 mortgagePenalty;

    public class GameState
    {
        public List<Boolean> propertyState;
        public List<Boolean> mortgageState;
        public Int32 currentCash;

        public GameState(List<Boolean> propertyState, List<Boolean> mortgageState,
            Int32 currentCash)
        {
            this.propertyState = propertyState;
            this.mortgageState = mortgageState;
            this.currentCash = currentCash;
        }
    }

    public class TradeState
    {
        public List<Boolean> propertyState;
        public Int32 tradeCash;

        public TradeState(List<Boolean> propertyState, Int32 tradeCash)
        {
            this.propertyState = propertyState;
            this.tradeCash = tradeCash;
        }
    }

    public static void Trade(GameState myState, GameState opponentState, TradeState myTradeState,
        TradeState opponentTradeState)
    {
        for (var i = 0; i < myTradeState.propertyState.Count; i += 1)
        {
            if (myTradeState.propertyState[i])
            {
                (myState.propertyState[i], opponentState.propertyState[i]) = (
                    opponentState.propertyState[i], myState.propertyState[i]);
                (myState.mortgageState[i], opponentState.mortgageState[i]) = (
                    opponentState.mortgageState[i], myState.mortgageState[i]);
            }
        }

        for (var i = 0; i < opponentTradeState.propertyState.Count; i += 1)
        {
            if (opponentTradeState.propertyState[i])
            {
                (myState.propertyState[i], opponentState.propertyState[i]) = (
                    opponentState.propertyState[i], myState.propertyState[i]);
                (myState.mortgageState[i], opponentState.mortgageState[i]) = (
                    opponentState.mortgageState[i], myState.mortgageState[i]);
            }
        }

        myState.currentCash += opponentTradeState.tradeCash;
        opponentState.currentCash -= opponentTradeState.tradeCash;
        myState.currentCash -= myTradeState.tradeCash;
        opponentState.currentCash += myTradeState.tradeCash;
    }

    public static Int32 CalculatePropertyScore(GameState state)
    {
        var score = 0;
        for (var i = 0; i < state.propertyState.Count / 4; i += 1)
        {
            var propertyCountPerColor = 0;
            for (var j = 0; j < 4; j += 1)
            {
                if (state.propertyState[i * 4 + j])
                {
                    propertyCountPerColor += 1;
                }
            }

            score += propertyScores[i][propertyCountPerColor];
        }

        score += state.currentCash * cashWeight / 100;
        for (var i = 0; i < state.propertyState.Count; i += 1)
        {
            if (state.mortgageState[i])
            {
                score -= mortgagePenalty;
            }
        }

        return score;
    }

    public static void Main(string[] args)
    {
        for (var i = 0; i < 10; i += 1)
        {
            var input = Console.ReadLine().Split(' ').Select(Int32.Parse).ToList();
            input.Insert(0, 0);
            propertyScores.Add(input);
        }

        var propertyStateList = Console.ReadLine().ToCharArray().Select(c => c - '0').ToList();
        var tradeStateList = Console.ReadLine().ToCharArray().Select(c => c - '0').ToList();
        var mortgageStateList = Console.ReadLine().ToCharArray().Select(c => c - '0').ToList();

        var myCash = Int32.Parse(Console.ReadLine());
        var opponentCash = Int32.Parse(Console.ReadLine());

        var myTradeCash = Int32.Parse(Console.ReadLine());
        var opponentTradeCash = Int32.Parse(Console.ReadLine());

        cashWeight = Int32.Parse(Console.ReadLine());
        mortgagePenalty = Int32.Parse(Console.ReadLine());

        var myProperty = new List<Boolean>();
        var opponentProperty = new List<Boolean>();

        for (var i = 0; i < propertyStateList.Count; i += 1)
        {
            if (propertyStateList[i] == 1)
            {
                myProperty.Add(true);
            }
            else
            {
                myProperty.Add(false);
            }

            if (propertyStateList[i] == 2)
            {
                opponentProperty.Add(true);
            }
            else
            {
                opponentProperty.Add(false);
            }
        }

        var myTrade = new List<Boolean>();
        var opponentTrade = new List<Boolean>();

        for (var i = 0; i < tradeStateList.Count; i += 1)
        {
            if (tradeStateList[i] == 2)
            {
                myTrade.Add(true);
            }
            else
            {
                myTrade.Add(false);
            }

            if (tradeStateList[i] == 1)
            {
                opponentTrade.Add(true);
            }
            else
            {
                opponentTrade.Add(false);
            }
        }

        var myMortgage = new List<Boolean>();
        var opponentMortgage = new List<Boolean>();

        for (var i = 0; i < mortgageStateList.Count; i += 1)
        {
            if (propertyStateList[i] == 1 && mortgageStateList[i] == 1)
            {
                myMortgage.Add(true);
            }
            else
            {
                myMortgage.Add(false);
            }

            if (propertyStateList[i] == 2 && mortgageStateList[i] == 1)
            {
                opponentMortgage.Add(true);
            }
            else
            {
                opponentMortgage.Add(false);
            }
        }

        var myTradeState = new TradeState(myTrade, myTradeCash);
        var opponentTradeState = new TradeState(opponentTrade, opponentTradeCash);

        var myState = new GameState(myProperty, myMortgage, myCash);
        var opponentState = new GameState(opponentProperty, opponentMortgage, opponentCash);

        var myScoreBeforeTrade = CalculatePropertyScore(myState);
        var opponentScoreBeforeTrade = CalculatePropertyScore(opponentState);

        Trade(myState, opponentState, myTradeState, opponentTradeState);

        var myScoreAfterTrade = CalculatePropertyScore(myState);
        var opponentScoreAfterTrade = CalculatePropertyScore(opponentState);
        
        if ((myScoreBeforeTrade - opponentScoreBeforeTrade) <=
            (myScoreAfterTrade - opponentScoreAfterTrade))
        {
            Console.WriteLine("YES");
        }
        else
        {
            Console.WriteLine("NO");
        }
    }
}