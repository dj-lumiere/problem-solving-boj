# [Bronze III] 差 (Difference) - 31617 

[문제 링크](https://www.acmicpc.net/problem/31617) 

### 성능 요약

메모리: 128140 KB, 시간: 236 ms

### 분류

사칙연산, 브루트포스 알고리즘, 구현, 수학

### 제출 일자

2024년 12월 22일 14:07:24

### 문제 설명

<p style="user-select: auto !important;">整数 <var style="user-select: auto !important;">K</var> と，長さ <var style="user-select: auto !important;">N</var> の整数列 <var style="user-select: auto !important;">A=(A<sub style="user-select: auto !important;">1</sub>,A<sub style="user-select: auto !important;">2</sub>,…,A<sub style="user-select: auto !important;">N</sub>)</var> および長さ <var style="user-select: auto !important;">M</var> の整数列 <var style="user-select: auto !important;">B=(B<sub style="user-select: auto !important;">1</sub>,B<sub style="user-select: auto !important;">2</sub>,…,B<sub style="user-select: auto !important;">M</sub>)</var> が与えられる．</p>

<p style="user-select: auto !important;">次の条件をすべて満たす <var style="user-select: auto !important;">2</var> つの整数の組 <var style="user-select: auto !important;">(p,q)</var> の個数を求めよ．</p>

<ul style="user-select: auto !important;">
	<li style="user-select: auto !important;"><var style="user-select: auto !important;">1 ≦ p ≦ N</var>．</li>
	<li style="user-select: auto !important;"><var style="user-select: auto !important;">1 ≦ q ≦ M</var>．</li>
	<li style="user-select: auto !important;"><var style="user-select: auto !important;">A<sub style="user-select: auto !important;">p</sub> + K = B<sub style="user-select: auto !important;">q</sub></var>．</li>
</ul>

### 입력 

 <p style="user-select: auto !important;">入力は以下の形式で与えられる．</p>

<pre style="user-select: auto !important;"><var style="user-select: auto !important;">K</var>
<var style="user-select: auto !important;">N</var>
<var style="user-select: auto !important;">A<sub style="user-select: auto !important;">1</sub></var>   <var style="user-select: auto !important;">A<sub style="user-select: auto !important;">2</sub></var>   <var style="user-select: auto !important;">…</var>   <var style="user-select: auto !important;">A<sub style="user-select: auto !important;">N</sub></var>
<var style="user-select: auto !important;">M</var>
<var style="user-select: auto !important;">B<sub style="user-select: auto !important;">1</sub></var>   <var style="user-select: auto !important;">B<sub style="user-select: auto !important;">2</sub></var> <var style="user-select: auto !important;">…</var>   <var style="user-select: auto !important;">B<sub style="user-select: auto !important;">M</sub></var></pre>

### 출력 

 <p style="user-select: auto !important;">条件をすべて満たす <var style="user-select: auto !important;">2</var> つの整数の組 <var style="user-select: auto !important;">(p,q)</var> の個数を出力せよ．</p>

<p style="user-select: auto !important;">答え以外は何も出力しないこと．(入力を促す文章なども出力しないこと．)</p>

