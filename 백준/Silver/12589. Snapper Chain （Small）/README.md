# [Silver V] Snapper Chain (Small) - 12589 

[문제 링크](https://www.acmicpc.net/problem/12589) 

### 성능 요약

메모리: 130668 KB, 시간: 624 ms

### 분류

비트마스킹, 구현, 수학, 시뮬레이션

### 제출 일자

2024년 12월 28일 10:47:42

### 문제 설명

<p style="user-select: auto !important;">The <em style="user-select: auto !important;">Snapper</em> is a clever little device that, on one side, plugs its input plug into an output socket, and, on the other side, exposes an output socket for plugging in a light or other device.</p>

<p style="user-select: auto !important;">When a <em style="user-select: auto !important;">Snapper</em> is in the ON state and is receiving power from its input plug, then the device connected to its output socket is receiving power as well. When you snap your fingers -- making a clicking sound -- any <em style="user-select: auto !important;">Snapper</em> receiving power at the time of the snap toggles between the ON and OFF states.</p>

<p style="user-select: auto !important;">In hopes of destroying the universe by means of a singularity, I have purchased <strong style="user-select: auto !important;">N</strong><em style="user-select: auto !important;">Snapper</em> devices and chained them together by plugging the first one into a power socket, the second one into the first one, and so on. The light is plugged into the <strong style="user-select: auto !important;">N</strong>th <em style="user-select: auto !important;">Snapper</em>.</p>

<p style="user-select: auto !important;">Initially, all the <em style="user-select: auto !important;">Snapper</em>s are in the OFF state, so only the first one is receiving power from the socket, and the light is off. I snap my fingers once, which toggles the first <em style="user-select: auto !important;">Snapper</em> into the ON state and gives power to the second one. I snap my fingers again, which toggles both <em style="user-select: auto !important;">Snapper</em>s and then promptly cuts power off from the second one, leaving it in the ON state, but with no power. I snap my fingers the third time, which toggles the first <em style="user-select: auto !important;">Snapper</em>again and gives power to the second one. Now both <em style="user-select: auto !important;">Snapper</em>s are in the ON state, and if my light is plugged into the second <em style="user-select: auto !important;">Snapper</em> it will be <em style="user-select: auto !important;">on</em>.</p>

<p style="user-select: auto !important;">I keep doing this for hours. Will the light be <em style="user-select: auto !important;">on</em> or <em style="user-select: auto !important;">off</em> after I have snapped my fingers <strong style="user-select: auto !important;">K</strong>times? The light is <em style="user-select: auto !important;">on</em> if and only if it's receiving power from the <em style="user-select: auto !important;">Snapper</em> it's plugged into.</p>

### 입력 

 <p style="user-select: auto !important;">The first line of the input gives the number of test cases, <strong style="user-select: auto !important;">T</strong>.  <strong style="user-select: auto !important;">T</strong> lines follow. Each one contains two integers, <strong style="user-select: auto !important;">N</strong> and <strong style="user-select: auto !important;">K</strong>.</p>

<h3 style="user-select: auto !important;">Limits</h3>

<ul style="user-select: auto !important;">
	<li style="user-select: auto !important;">1 ≤ <strong style="user-select: auto !important;">T</strong> ≤ 10,000.</li>
	<li style="user-select: auto !important;">1 ≤ <strong style="user-select: auto !important;">N</strong> ≤ 10;</li>
	<li style="user-select: auto !important;">0 ≤ <strong style="user-select: auto !important;">K</strong> ≤ 100;</li>
</ul>

### 출력 

 <p style="user-select: auto !important;">For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is either "ON" or "OFF", indicating the state of the light bulb.</p>

