# [Bronze II] 分割 (Split) - 24074 

[문제 링크](https://www.acmicpc.net/problem/24074) 

### 성능 요약

메모리: 108080 KB, 시간: 92 ms

### 분류

구현

### 제출 일자

2024년 12월 5일 17:25:50

### 문제 설명

<p style="user-select: auto !important;">長さ <var style="user-select: auto !important;">N</var> の整数列 <var style="user-select: auto !important;">A = (A<sub style="user-select: auto !important;">1</sub>, A<sub style="user-select: auto !important;">2</sub>, ..., A<sub style="user-select: auto !important;">N</sub>)</var> が与えられる．数列 <var style="user-select: auto !important;">A</var> の値はすべて異なる．</p>

<p style="user-select: auto !important;">最大値で数列を分割したとき，最大値より前にある値の和と，最大値より後ろにある値の和を出力せよ．</p>

<p style="user-select: auto !important;">すなわち，数列 <var style="user-select: auto !important;">A</var> の最大値を <var style="user-select: auto !important;">A<sub style="user-select: auto !important;">x</sub></var> とすると，<var style="user-select: auto !important;">A<sub style="user-select: auto !important;">1</sub> + A<sub style="user-select: auto !important;">2</sub> + … + A<sub style="user-select: auto !important;">x-1</sub></var> と <var style="user-select: auto !important;">A<sub style="user-select: auto !important;">x+1</sub> + A<sub style="user-select: auto !important;">x+2</sub> + … +A<sub style="user-select: auto !important;">N</sub></var> を出力せよ．</p>

<p style="user-select: auto !important;">ただし最大値より前に値がない場合，最大値より前にある値の和は <var style="user-select: auto !important;">0</var> になる．</p>

<p style="user-select: auto !important;">同様に最大値より後ろに値がない場合，最大値より後ろにある値の和は <var style="user-select: auto !important;">0</var> になる．</p>

### 입력 

 <p style="user-select: auto !important;">入力は以下の形式で標準入力から与えられる．</p>

<pre style="user-select: auto !important;"><var style="user-select: auto !important;">N</var>
<var style="user-select: auto !important;">A<sub style="user-select: auto !important;">1</sub></var> <var style="user-select: auto !important;">A<sub style="user-select: auto !important;">2</sub></var> <var style="user-select: auto !important;">…</var> <var style="user-select: auto !important;">A<sub style="user-select: auto !important;">N</sub></var></pre>

### 출력 

 <p style="user-select: auto !important;">出力は <var style="user-select: auto !important;">2</var> 行からなる．</p>

<p style="user-select: auto !important;"><var style="user-select: auto !important;">1</var> 行目に，整数列 <var style="user-select: auto !important;">A</var> の，最大値より前にある値の和を出力せよ．</p>

<p style="user-select: auto !important;"><var style="user-select: auto !important;">2</var> 行目に，整数列 <var style="user-select: auto !important;">A</var> の，最大値より後ろにある値の和を出力せよ．</p>

