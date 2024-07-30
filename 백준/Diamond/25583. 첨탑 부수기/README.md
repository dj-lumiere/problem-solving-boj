# [Diamond V] 첨탑 부수기 - 25583 

[문제 링크](https://www.acmicpc.net/problem/25583) 

### 성능 요약

메모리: 111712 KB, 시간: 132 ms

### 분류

오일러 피 함수, 분할 정복을 이용한 거듭제곱, 수학, 정수론, 파싱, 문자열

### 제출 일자

2024년 6월 18일 11:14:48

### 문제 설명

<p>현기는 평소에 첨탑 부수기라는 게임을 즐겨한다. 첨탑 부수기 게임은 1층에 존재하는 첨탑의 입구로 들어가 꼭대기 층까지 한 층씩 등반하며 첨탑 내의 모든 괴물을 쓰러뜨리는 게임이다. 첨탑의 꼭대기까지 등반하여 게임을 클리어하더라도 다시 도전하면 그때마다 또 다른 괴물을 만날 수 있어 몇 번을 하더라도 새로운 재미를 선사한다.</p>

<p>첨탑 부수기 게임은 새로운 게임을 시작할 때 무작위로 생성되는 시드$(=Seed)$를 바탕으로 각 층에 생성되는 괴물의 강함$(=Strength)$이 정해진다. 시드는 알파벳 대소문자와 0을 제외한 숫자로 이루어진 10자리 문자열이다. 괴물의 강함을 계산하기 위해 시드의 각 자리 문자를 사용할 때에는 아래의 표와 같이 다른 정숫값으로 바꿔 연산한다.</p>

<table class="table table-bordered">
	<tbody>
		<tr>
			<td style="text-align: center;"><strong>$Seed$의 각 자리 문자</strong></td>
			<td style="text-align: center;">1</td>
			<td style="text-align: center;">$\cdots$</td>
			<td style="text-align: center;">8</td>
			<td style="text-align: center;">9</td>
			<td style="text-align: center;">A</td>
			<td style="text-align: center;">B</td>
			<td style="text-align: center;">$\cdots$</td>
			<td style="text-align: center;">Y</td>
			<td style="text-align: center;">Z</td>
			<td style="text-align: center;">a</td>
			<td style="text-align: center;">b</td>
			<td style="text-align: center;">$\cdots$</td>
			<td style="text-align: center;">y</td>
			<td style="text-align: center;">z</td>
		</tr>
		<tr>
			<td style="text-align: center;"><strong>값</strong></td>
			<td style="text-align: center;">1</td>
			<td style="text-align: center;">$\cdots$</td>
			<td style="text-align: center;">8</td>
			<td style="text-align: center;">9</td>
			<td style="text-align: center;">10</td>
			<td style="text-align: center;">11</td>
			<td style="text-align: center;">$\cdots$</td>
			<td style="text-align: center;">34</td>
			<td style="text-align: center;">35</td>
			<td style="text-align: center;">36</td>
			<td style="text-align: center;">37</td>
			<td style="text-align: center;">$\cdots$</td>
			<td style="text-align: center;">60</td>
			<td style="text-align: center;">61</td>
		</tr>
	</tbody>
</table>

<p>예를 들어 시드가 "AB1z8DcdT4"일 경우에 시드의 첫 번째 문자$(=Seed[0])$인 'A'는 정수 10을 의미한다. 여기서, $Seed[i]$는 시드를 구성하는 문자 중 왼쪽에서 $i+1$번째 문자에 해당한다.</p>

<p>층 수가 $N$인 첨탑 부수기 게임을 플레이할 때, 1층에서 마주치는 괴물의 강함은 1이고 $k(\neq 1)$층에서 마주치는 괴물의 강함은 아래와 같이 계산한다.</p>

<p>$\begin{cases} f(i,k) = Seed[(i\times k)\ \textrm{mod}\ 10] \\ g(k) = \sum_{i=1}^{10} f(i,k) \times k \\ Strength(k) = g(k) ^ {Strength(k-1)} \end{cases}$</p>

<p>현기가 꼭대기 층이 $N$층인 첨탑 부수기 게임을 새로 시작할 때, 꼭대기 층에서 마주치는 괴물의 강함을 구하여라. 단, 괴물의 강함이 매우 클 수 있으므로 괴물의 강함을 $M$으로 나눈 나머지를 출력하라.</p>

### 입력 

 <p>첫째 줄에 두 정수 $N$과 $M$이 주어진다. $(1\le N, M \le10^9)$  </p>

<p>둘째 줄에 $Seed$가 주어진다. $Seed$는 알파벳 대소문자와 0을 제외한 숫자로 이루어진 10자리 문자열이다.</p>

### 출력 

 <p>첫째 줄에 괴물의 강함을 $M$으로 나눈 나머지를 출력한다.</p>

