# [Diamond II] 이산로그가 장난이냐? - 21864 

[문제 링크](https://www.acmicpc.net/problem/21864) 

### 성능 요약

메모리: 114328 KB, 시간: 5596 ms

### 분류

이산 로그, 수학, 정수론, 런타임 전의 전처리

### 문제 설명

<p>BOJ에서 <a href="https://www.acmicpc.net/problem/21094" target="_blank">어떤 문제</a>를 풀었던 Sait2000은 입력 범위를 늘려서 장난 아니고 이산로그를 구해야 하는 문제를 만들기로 했습니다.</p>

<p><em>M</em> = 10<sup>18</sup> + 31은 소수이고, <em>g</em> = 42는 <em>M</em>의 원시근입니다. 즉, <em>g</em><sup>1</sup> mod <em>M</em>, <em>g</em><sup>2</sup> mod <em>M</em> ... <em>g</em><sup><em>M</em> - 1</sup> mod <em>M</em>은 각각 서로 다른 [1; <em>M</em>) 범위의 정수입니다. <em>f</em>(<em>x</em>)를 <em>g</em><sup><em>p</em></sup> mod <em>M</em> = <em>x</em>를 만족하는 최소의 양의 정수 <em>p</em>로 정의합니다. 그러면 <em>f</em>는 [1; <em>M</em>)에서 [1; <em>M</em>)으로 가는 전단사함수(일대일 대응)입니다.</p>

<p>수열 {<em>a</em><sub><em>n</em></sub>}을 다음과 같이 정의합니다.</p>

<ul>
	<li><em>a</em><sub>0</sub> = 960002411612632915</li>
	<li><em>a</em><sub><em>i</em> + 1</sub> = <em>f</em>(<em>a</em><sub><em>i</em></sub>)</li>
</ul>

<p><em>n</em>이 주어졌을 때, <em>a</em><sub><em>n</em></sub>을 찾아봅시다.</p>

### 입력 

 <p>첫번째 줄에 정수 <em>n</em>이 주어집니다. (0 ≤ <em>n</em> ≤ 2 × 10<sup>6</sup>)</p>

### 출력 

 <p><em>a</em><sub><em>n</em></sub>을 출력합니다.</p>

