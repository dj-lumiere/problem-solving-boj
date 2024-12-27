# [Bronze IV] Cornhole - 27855 

[문제 링크](https://www.acmicpc.net/problem/27855) 

### 성능 요약

메모리: 127496 KB, 시간: 220 ms

### 분류

사칙연산, 구현, 수학

### 제출 일자

2024년 12월 28일 00:53:22

### 문제 설명

<p style="user-select: auto !important;">Cornhole is a popular game in which players take turns throwing bean bags at an angled board with a hole in its far end. The object is to score points by either landing a bag on the board (one point) or getting the bag in the hole (three points).</p>

<p style="text-align: center; user-select: auto !important;"><img alt="" src="https://upload.acmicpc.net/15eeb681-12ff-4cac-8118-1c9bb2530070/-/preview/" style="width: 247px; height: 236px; user-select: auto !important;"></p>

<p style="text-align: center; user-select: auto !important;">(<a href="https://www.playcornhole.org/pages/rules" style="user-select: auto !important;">https://www.playcornhole.org/pages/rules</a>)</p>

<p style="user-select: auto !important;">Each player is given four bean bags. Players stand about 30 feet from the board and alternate throwing the bags, on at-a-time, toward the board. After each player has thrown their four bags, cancellation scoring is performed. That is, each player tally’s up their score (three points for each of their bags that went through the hole, and one point for each of their bags that’s on the board). If player 1 has more points than player 2, player one scores the difference in points. If player 2 has more points than player 1, player 2 scores the difference in points. If both players have the same number of points, then neither player scores any points. As an example, suppose that player 1 had two bags go through the hole and one bag on the board and player 2 had four bags on the board. The result is that player 1 would score three points for that round.</p>

<p style="user-select: auto !important;">For this problem, you will be given the number of bags that each player had go through the hole and the number of bags that stayed on the board. You will calculate who (if anyone) scores any points using cancellation scoring for the round and if so, how many.</p>

### 입력 

 <p style="user-select: auto !important;">Input consists of two lines. The first line of input contains two space separated non-negative integers H<sub style="user-select: auto !important;">1</sub> and B<sub style="user-select: auto !important;">1</sub>, where H<sub style="user-select: auto !important;">1</sub> is the number of bags player 1 got through the hole and B<sub style="user-select: auto !important;">1</sub> is the number of bags player 1 got on the board (0 ≤ H<sub style="user-select: auto !important;">1</sub> + B<sub style="user-select: auto !important;">1</sub> ≤ 4). The second line of input contains two space separated decimal integers H<sub style="user-select: auto !important;">2</sub> and B<sub style="user-select: auto !important;">2</sub>, where H<sub style="user-select: auto !important;">2</sub> is the number of bags player 2 got through the hole and B<sub style="user-select: auto !important;">2</sub> is the number of bags player 2 got on the board (0≤ H<sub style="user-select: auto !important;">2</sub> + B<sub style="user-select: auto !important;">2</sub> ≤ 4).</p>

### 출력 

 <p style="user-select: auto !important;">There is a single line of output. If no one scores any points, the output is the string NO SCORE, otherwise, the line contains two space separated decimal integers P and N, where P is the player number (1 or 2) and N is the number of points the player scored (1 ≤ N ≤ 12).</p>

