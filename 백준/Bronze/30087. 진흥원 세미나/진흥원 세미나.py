# 30087 진흥원 세미나

room_info = {
    "Algorithm": "204",
    "DataAnalysis": "207",
    "ArtificialIntelligence": "302",
    "CyberSecurity": "B101",
    "Network": "303",
    "Startup": "501",
    "TestStrategy": "105",
}
n = int(input())
for _ in range(n):
    class_name = input()
    print(room_info[class_name])