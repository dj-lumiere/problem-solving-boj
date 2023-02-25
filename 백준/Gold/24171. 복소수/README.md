# [Gold II] 복소수 - 24171 

[문제 링크](https://www.acmicpc.net/problem/24171) 

### 성능 요약

메모리: 39680 KB, 시간: 148 ms

### 분류

유클리드 호제법(euclidean), 구현(implementation), 수학(math), 정수론(number_theory)

### 문제 설명

<p>$\displaystyle{{b_0 + c_0 \sqrt{d_0} \over a_0} + {b_1 + c_1 \sqrt{d_1} \over a_1} i}$</p>

<ul>
	<li>$i = \sqrt{-1}$</li>
	<li>$j=0, \, 1$에 대해
	<ul>
		<li>$a_j, \, b_j, \, c_j, \, d_j$는 정수</li>
		<li>$a_j > 0$; $0 \le d_j \ne 1$</li>
		<li>$\gcd (a_j, \, b_j, \, c_j) = 1$</li>
		<li>'$c_j = 0$'과 '$d_j = 0$'는 필요충분조건</li>
		<li>$d_j > 0$일 때 $d_j$의 약수 중 $1$보다 큰 제곱수가 없음</li>
	</ul>
	</li>
	<li>$d_0=d_1$</li>
</ul>

<p>위 형식으로 표현되는 복소수 $A$와 $B$가 주어질 때, $A+B$, $A-B$, $A \times B$, $A \div B$의 값을 출력하는 프로그램을 작성하세요.</p>

### 입력 

 <p>첫 번째 줄에 $A$의 $a_0, \, b_0, \, c_0, \, d_0, \, a_1, \, b_1, \, c_1, \, d_1$ 값이 하나씩 주어집니다.</p>

<p>두 번째 줄에는 마찬가지로 $B$의 $a_0, \, b_0, \, c_0, \, d_0, \, a_1, \, b_1, \, c_1, \, d_1$ 값이 하나씩 주어집니다.</p>

### 출력 

 <p>첫 번째 줄부터 네 번째 줄까지 각각 $A+B$, $A-B$, $A \times B$, $A \div B$의 값을 문제에서 설명한 형식으로 표현했을 때의 $a_0, \, b_0, \, c_0, \, d_0, \, a_1, \, b_1, \, c_1, \, d_1$ 값을 출력합니다.</p>

