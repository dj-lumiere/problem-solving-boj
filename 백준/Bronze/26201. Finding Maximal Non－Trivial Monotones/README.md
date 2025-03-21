# [Bronze II] Finding Maximal Non-Trivial Monotones - 26201 

[문제 링크](https://www.acmicpc.net/problem/26201) 

### 성능 요약

메모리: 128444 KB, 시간: 232 ms

### 분류

구현, 문자열

### 제출 일자

2024년 12월 15일 10:35:07

### 문제 설명

<p style="user-select: auto !important;">In this problem we will be dealing with character sequences, often called <em style="user-select: auto !important;">strings</em>. A sequence is <em style="user-select: auto !important;">non-trivial</em> if it contains at least two elements.</p>

<p style="user-select: auto !important;">Given a sequence <mjx-container class="MathJax" jax="CHTML" style="font-size: 99.7%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D460 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>s</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$s$</span></mjx-container>, we say that a chunk <mjx-container class="MathJax" jax="CHTML" style="font-size: 99.7%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D460 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mo class="mjx-n" space="2"><mjx-c class="mjx-c2026"></mjx-c></mjx-mo><mjx-mo class="mjx-n" space="2"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-msub space="2"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D460 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D457 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>s</mi><mi>i</mi></msub><mo>,</mo><mo>…</mo><mo>,</mo><msub><mi>s</mi><mi>j</mi></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$s_i , \dots , s_j$</span></mjx-container> is <em style="user-select: auto !important;">monotone</em> if all its characters are equal, and we say that it is <em style="user-select: auto !important;">maximal</em> if this chunk cannot be extended to left or right without losing the monotonicity.</p>

<p style="user-select: auto !important;">Given a sequence composed only of characters “<code style="user-select: auto !important;">a</code>” and “<code style="user-select: auto !important;">b</code>”, determine how many characters “<code style="user-select: auto !important;">a</code>” occur in non-trivial maximal monotone chunks.</p>

### 입력 

 <p style="user-select: auto !important;">The input consists of two lines. The first line contains a single integer <mjx-container class="MathJax" jax="CHTML" style="font-size: 99.7%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>, where <mjx-container class="MathJax" jax="CHTML" style="font-size: 99.7%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-msup space="4"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-script style="vertical-align: 0.393em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c35"></mjx-c></mjx-mn></mjx-script></mjx-msup></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><msup><mn>10</mn><mn>5</mn></msup></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 ≤ N ≤ 10^5$</span></mjx-container>. The second line contains a string with exactly <mjx-container class="MathJax" jax="CHTML" style="font-size: 99.7%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container> characters, composed only of the characters “<code style="user-select: auto !important;">a</code>” and “<code style="user-select: auto !important;">b</code>”.</p>

### 출력 

 <p style="user-select: auto !important;">Print a single line containing an integer representing the total number of times the character “<code style="user-select: auto !important;">a</code>” occurs in non-trivial maximal monotone chunks.</p>

