# [Bronze I] 幹線道路 (Trunk Road) - 15476 

[문제 링크](https://www.acmicpc.net/problem/15476) 

### 성능 요약

메모리: 129508 KB, 시간: 256 ms

### 분류

브루트포스 알고리즘

### 제출 일자

2024년 12월 15일 10:25:47

### 문제 설명

<p style="user-select: auto !important;">JOI 市は，東西方向にまっすぐに伸びる <var style="user-select: auto !important;">H</var> 本の道路と，南北方向にまっすぐに伸びる <var style="user-select: auto !important;">W</var> 本の道路によって，碁盤の目の形に区分けされている．道路と道路の間隔は <var style="user-select: auto !important;">1</var> である．JOI 市では，これら <var style="user-select: auto !important;">H+W</var> 本の道路から，東西方向に <var style="user-select: auto !important;">1</var> 本，南北方向に <var style="user-select: auto !important;">1</var> 本，合計 <var style="user-select: auto !important;">2</var> 本の道路を幹線道路として選ぶことになった．</p>

<p style="user-select: auto !important;">北から <var style="user-select: auto !important;">i</var> 本目 (<var style="user-select: auto !important;">1≦i≦H</var>) の道路と，西から <var style="user-select: auto !important;">j</var> 本目 (<var style="user-select: auto !important;">1≦j≦W</var>) の道路の交差点を，交差点 <var style="user-select: auto !important;">(i,j)</var> とする．交差点 <var style="user-select: auto !important;">(i,j)</var> と北から <var style="user-select: auto !important;">m</var> 本目 (<var style="user-select: auto !important;">1≦m≦H</var>) の道路の距離は <var style="user-select: auto !important;">|i-m|</var> であり，交差点 <var style="user-select: auto !important;">(i,j)</var> と西から <var style="user-select: auto !important;">n</var> 本目 (<var style="user-select: auto !important;">1≦n≦W</var>) の道路の距離は <var style="user-select: auto !important;">|j-n|</var> である． また，交差点 <var style="user-select: auto !important;">(i,j)</var> の近くには <var style="user-select: auto !important;">A_{i,j}</var> 人の住人が住んでいる．</p>

<p style="user-select: auto !important;"><var style="user-select: auto !important;">2</var> 本の幹線道路を選んだときの，JOI 市の全ての住人に対する，最寄りの交差点から近い方の幹線道路への距離の総和の最小値を求めよ．</p>

### 입력 

 <p style="user-select: auto !important;">入力は以下の形式で標準入力から与えられる．</p>

<pre style="user-select: auto !important;"><var style="user-select: auto !important;">H</var> <var style="user-select: auto !important;">W</var>
<var style="user-select: auto !important;">A_{1,1}</var> <var style="user-select: auto !important;">A_{1,2}</var> ... <var style="user-select: auto !important;">A_{1,W}</var>
:
<var style="user-select: auto !important;">A_{H,1}</var> <var style="user-select: auto !important;">A_{H,2}</var> ... <var style="user-select: auto !important;">A_{H,W}</var>
</pre>

### 출력 

 <p style="user-select: auto !important;">JOI 市の全ての住人に対する，最寄りの交差点から近い方の幹線道路への距離の総和の最小値を出力せよ．</p>

