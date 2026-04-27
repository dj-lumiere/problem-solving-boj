# [Gold V] ASCII Art - 29782 

[문제 링크](https://www.acmicpc.net/problem/29782) 

### 성능 요약

메모리: 114328 KB, 시간: 128 ms

### 분류

수학, 브루트포스 알고리즘, 이분 탐색

### 제출 일자

2026년 04월 28일 00:43:33

### 문제 설명

<p>Cody-Jamal has heard about generative artificial intelligence producing art. He is excited about the new art opportunities, but also worried about human-created art being displaced. He thought a good compromise would be to use computers to create art that humans simply cannot.</p>

<p>Since Cody-Jamal is just beginning at computer-generated art, he started simple. He wants to create an immense string that shows the English alphabet in a doubly-repeated way, to represent its ubiquity and permanence.</p>

<p>Cody-Jamal wrote the following program:</p>

<pre>for i = 1 to 1e100:
  for letter = A to Z:
    print letter i times
</pre>

<p>Here <code>1e100</code> represents the integer $10^{100}$. For example:</p>

<ul>
	<li>When $i=1$, the program prints <code>ABCD....XYZ</code>.</li>
	<li>When $i=2$, the program prints <code>AABBCC...XXYYZZ</code>.</li>
	<li>When $i=3$, the program prints <code>AAABBBCCC...XXXYYYZZZ</code>.</li>
</ul>

<p>Of course, Cody-Jamal's program takes a long time to finish. Can you help him know what the $\mathbf{N}$-th printed letter will be without waiting for it to be printed?</p>

### 입력 

 <p>The first line of the input gives the number of test cases, $\mathbf{T}$. $\mathbf{T}$ test cases follow.</p>

<p>Each test case consists of a single line with an integer $\mathbf{N}$.</p>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where $x$ is the test case number (starting from 1) and $y$ is the $\mathbf{N}$-th character printed by Cody-Jamal's program.</p>

