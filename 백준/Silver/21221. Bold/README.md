# [Silver V] Bold - 21221 

[문제 링크](https://www.acmicpc.net/problem/21221) 

### 성능 요약

메모리: 128672 KB, 시간: 228 ms

### 분류

구현

### 제출 일자

2024년 12월 19일 18:55:56

### 문제 설명

<p style="user-select: auto !important;">In addition to the usual age-related health problems such as first signs of RSI<sup style="user-select: auto !important;">1</sup> and physical injuries that accumulate faster than they heal, Daniel’s eyesight has suddenly worsened.</p>

<p style="user-select: auto !important;">Paula wrote him a letter, but he can’t read it without glasses. She needs to <strong style="user-select: auto !important;">bold</strong> the text, so Daniel can read it.</p>

<p style="user-select: auto !important;">The letter can be represented as a matrix consisting of characters '<code style="user-select: auto !important;">.</code>' and '<code style="user-select: auto !important;">#</code>'. To bold it, Paula will replace each '<code style="user-select: auto !important;">#</code>' in the original letter with a 2 × 2 square of '<code style="user-select: auto !important;">#</code>' in the down-right direction.</p>

<p style="user-select: auto !important;"><sup style="user-select: auto !important;">1</sup>Repetitive strain injury. Never ignore the pain caused by typing. Ergonomic aids and chairs are generally always worth it. Sit straight. “A gram of prevention is worth a kilo of cure.”</p>

### 입력 

 <p style="user-select: auto !important;">The first line contains integers n and m (2 ≤ n, m ≤ 100), the dimensions of the letter.</p>

<p style="user-select: auto !important;">Each of the following n lines contains m characters '<code style="user-select: auto !important;">.</code>' and '<code style="user-select: auto !important;">#</code>' that represent Paula’s letter.</p>

<p style="user-select: auto !important;">The last row and column won’t contain any '<code style="user-select: auto !important;">#</code>'.</p>

### 출력 

 <p style="user-select: auto !important;">Output n lines containing m characters '<code style="user-select: auto !important;">.</code>' and '<code style="user-select: auto !important;">#</code>', representing the bold letter.</p>

