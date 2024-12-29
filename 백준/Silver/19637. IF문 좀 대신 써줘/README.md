# [Silver III] IF문 좀 대신 써줘 - 19637 

[문제 링크](https://www.acmicpc.net/problem/19637) 

### 성능 요약

메모리: 168744 KB, 시간: 296 ms

### 분류

이분 탐색

### 제출 일자

2024년 12월 29일 10:55:13

### 문제 설명

<p style="user-select: auto !important;">게임 개발자인 밀리는 전투력 시스템을 만들어, 캐릭터가 가진 전투력을 기준으로 칭호를 붙여주려고 한다.</p>

<p style="user-select: auto !important;">예를 들어, 전투력 10,000 이하의 캐릭터는 WEAK, 10,000 초과 그리고 100,000 이하의 캐릭터는 NORMAL, 100,000 초과 그리고 1,000,000 이하의 캐릭터는 STRONG 칭호를 붙여준다고 하자. 이를 IF문으로 작성한다면 아래와 같이 구현할 수 있다.</p>

<pre style="user-select: auto !important;"><code style="user-select: auto !important;">if power <= 10000
 print WEAK
else if power <= 100000
 print NORMAL
else if power <= 1000000
 print STRONG</code></pre>

<p style="user-select: auto !important;">혼자서 게임을 개발하느라 매우 바쁜 밀리를 대신해서, 캐릭터의 전투력에 맞는 칭호를 출력하는 프로그램을 작성하자.</p>

### 입력 

 <p style="user-select: auto !important;">첫 번째 줄에는 칭호의 개수 <em style="user-select: auto !important;">N</em> (1 ≤ <em style="user-select: auto !important;">N</em> ≤ 10<sup style="user-select: auto !important;">5</sup>)과 칭호를 출력해야 하는 캐릭터들의 개수 <em style="user-select: auto !important;">M</em> (1 ≤ <em style="user-select: auto !important;">M</em> ≤ 10<sup style="user-select: auto !important;">5</sup>)이 빈칸을 사이에 두고 주어진다. (1 ≤ <em style="user-select: auto !important;">N, M</em> ≤ 10<sup style="user-select: auto !important;">5</sup>)</p>

<p style="user-select: auto !important;">두 번째 줄부터 <em style="user-select: auto !important;">N</em>개의 줄에 각 칭호의 이름을 나타내는 길이 1 이상, 11 이하의 영어 대문자로만 구성된 문자열과 해당 칭호의 전투력 상한값을 나타내는 10<sup style="user-select: auto !important;">9</sup> 이하의 음이 아닌 정수가 주어진다. 칭호는 전투력 상한값의 비내림차순으로 주어진다. </p>

<p style="user-select: auto !important;"><em style="user-select: auto !important;">N </em>+ 2번째 줄부터<em style="user-select: auto !important;"> M</em>개의 각 줄에는 캐릭터의 전투력을 나타내는 음이 아닌 정수가 주어진다. 해당하는 칭호가 없는 전투력은 입력으로 주어지지 않는다.</p>

### 출력 

 <p style="user-select: auto !important;"><em style="user-select: auto !important;">M</em>개의 줄에 걸쳐 캐릭터의 전투력에 맞는 칭호를 입력 순서대로 출력한다. 어떤 캐릭터의 전투력으로 출력할 수 있는 칭호가 여러 개인 경우 가장 먼저 입력된 칭호 하나만 출력한다.</p>

