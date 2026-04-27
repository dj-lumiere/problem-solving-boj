namespace ProblemSolving;

public class BOJ34001
{
    public record QuestTier(int BaseLevel, int FirstDiminish, int SecondDiminish);

    private static int CalculateMonsterCount(int playerLevel, QuestTier tier)
    {
        if (playerLevel < tier.BaseLevel)
        {
            return 0;
        }
        if (playerLevel < tier.FirstDiminish)
        {
            return 500;
        }
        if (playerLevel < tier.SecondDiminish)
        {
            return 300;
        }
        return 100;
    }
    
    public static void Main(string[] args)
    {
        var arcaneQuestLevel = new QuestTier[]
        {
            new QuestTier(200, 210, 220),
            new QuestTier(210, 220, 225),
            new QuestTier(220, 225, 230),
            new QuestTier(225, 230, 235),
            new QuestTier(230, 235, 245),
            new QuestTier(235, 245, 250)
        };
        var grandisQuestLevel = new QuestTier[]
        {
            new QuestTier(260, 265, 270),
            new QuestTier(265, 270, 275),
            new QuestTier(270, 275, 280),
            new QuestTier(275, 280, 285),
            new QuestTier(280, 285, 290),
            new QuestTier(285, 290, 295),
            new QuestTier(290, 295, 300)
        };
        var level = int.Parse(Console.ReadLine());
        var arcaneAnswer = arcaneQuestLevel.Select(x=>CalculateMonsterCount(level, x)).ToArray();
        var grandisAnswer = grandisQuestLevel.Select(x=>CalculateMonsterCount(level, x)).ToArray();
        Console.WriteLine(string.Join(" ", arcaneAnswer));
        Console.WriteLine(string.Join(" ", grandisAnswer));
    }
}