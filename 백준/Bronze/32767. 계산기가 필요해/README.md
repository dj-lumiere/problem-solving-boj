# [Bronze II] 계산기가 필요해 - 32767 

[문제 링크](https://www.acmicpc.net/problem/32767) 

### 성능 요약

메모리: 128156 KB, 시간: 232 ms

### 분류

구현

### 제출 일자

2024년 12월 21일 15:27:59

### 문제 설명

<p style="user-select: auto !important;">세과영에서 생활을 하다 보니 계산기가 필요해진 세종이는 계산기를 살 돈이 없어서 직접 계산기를 만들기로 했다. 간단한 계산기를 만들어주자.</p>

### 입력 

 <p style="user-select: auto !important;">세 개의 수와 두 개의 연산자가 공백으로 구분되어 주어진다. 각 수는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 99.7%; position: relative; user-select: auto !important;"><mjx-math class="MJX-TEX" aria-hidden="true" style="user-select: auto !important;"><mjx-mn class="mjx-n" style="user-select: auto !important;"><mjx-c class="mjx-c30" style="user-select: auto !important;"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline" style="user-select: auto !important;"><math xmlns="http://www.w3.org/1998/Math/MathML" style="user-select: auto !important;"><mn style="user-select: auto !important;">0</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext" style="user-select: auto !important;">$0$</span></mjx-container> 이상 <mjx-container class="MathJax" jax="CHTML" style="font-size: 99.7%; position: relative; user-select: auto !important;"><mjx-math class="MJX-TEX" aria-hidden="true" style="user-select: auto !important;"><mjx-mn class="mjx-n" style="user-select: auto !important;"><mjx-c class="mjx-c31" style="user-select: auto !important;"></mjx-c><mjx-c class="mjx-c30" style="user-select: auto !important;"></mjx-c><mjx-c class="mjx-c30" style="user-select: auto !important;"></mjx-c></mjx-mn><mjx-mstyle style="user-select: auto !important;"><mjx-mspace style="width: 0.167em; user-select: auto !important;"></mjx-mspace></mjx-mstyle><mjx-mn class="mjx-n" style="user-select: auto !important;"><mjx-c class="mjx-c30" style="user-select: auto !important;"></mjx-c><mjx-c class="mjx-c30" style="user-select: auto !important;"></mjx-c><mjx-c class="mjx-c30" style="user-select: auto !important;"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline" style="user-select: auto !important;"><math xmlns="http://www.w3.org/1998/Math/MathML" style="user-select: auto !important;"><mn style="user-select: auto !important;">100</mn><mstyle scriptlevel="0" style="user-select: auto !important;"><mspace width="0.167em" style="user-select: auto !important;"></mspace></mstyle><mn style="user-select: auto !important;">000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext" style="user-select: auto !important;">$100\,000$</span></mjx-container> 이하의 실수이며, 소수점 아래로 최대 넷째 자리까지 주어진다.</p>

<p style="user-select: auto !important;">연산자는 <span style="color: rgb(231, 76, 60); user-select: auto !important;"><code style="user-select: auto !important;">+</code></span>, <code style="user-select: auto !important;"><span style="color: rgb(231, 76, 60); user-select: auto !important;">-</span></code>, <span style="color: rgb(231, 76, 60); user-select: auto !important;"><code style="user-select: auto !important;">*</code></span>, <span style="color: rgb(231, 76, 60); user-select: auto !important;"><code style="user-select: auto !important;">/</code></span> 중 하나이고 각각 덧셈, 뺄셈, 곱셈, 나눗셈을 나타낸다. <mjx-container class="MathJax" jax="CHTML" style="font-size: 99.7%; position: relative; user-select: auto !important;"><mjx-math class="MJX-TEX" aria-hidden="true" style="user-select: auto !important;"><mjx-mn class="mjx-n" style="user-select: auto !important;"><mjx-c class="mjx-c30" style="user-select: auto !important;"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline" style="user-select: auto !important;"><math xmlns="http://www.w3.org/1998/Math/MathML" style="user-select: auto !important;"><mn style="user-select: auto !important;">0</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext" style="user-select: auto !important;">$0$</span></mjx-container>으로 나누는 경우는 없다. </p>

### 출력 

 <p style="user-select: auto !important;">출력 예시를 참고하여 <strong style="user-select: auto !important;">앞에서부터</strong> 계산한 결과를 소수점 아래 넷째 자리에서 반올림하여 셋째 자리까지 출력한다. <strong style="user-select: auto !important;">일반적인 사칙연산의 우선순위를 따르지 않으며</strong>, 계산 결과는 항상 오른쪽 <code style="user-select: auto !important;"><span style="color: rgb(231, 76, 60); user-select: auto !important;">|</span></code>에 붙어있음에 주의하라.</p>

<p style="user-select: auto !important;">출력이 계산기의 크기를 넘어가는 입력은 주어지지 않으며 계산 결과는 0 또는 양수이다.</p>

