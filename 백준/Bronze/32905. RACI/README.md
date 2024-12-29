# [Bronze IV] RACI - 32905 

[문제 링크](https://www.acmicpc.net/problem/32905) 

### 성능 요약

메모리: 127496 KB, 시간: 224 ms

### 분류

구현

### 제출 일자

2024년 12월 29일 10:49:51

### 문제 설명

<p style="user-select: auto !important;">Nikolai assigned students the task of creating a RACI matrix for a project during management lectures. This is a responsibility assignment matrix that lists all stakeholders of the project and their levels of involvement in different tasks. The levels are denoted by the letters "<code style="user-select: auto !important;">R</code>", "<code style="user-select: auto !important;">A</code>", "<code style="user-select: auto !important;">C</code>", and "<code style="user-select: auto !important;">I</code>". If there is no involvement, "<code style="user-select: auto !important;">-</code>" is used. The levels of involvement have the following meaning:</p>

<ul style="user-select: auto !important;">
	<li style="user-select: auto !important;"><code style="user-select: auto !important;">R</code> (<em style="user-select: auto !important;">Responsible</em>): performs the task (if they are absent, then <em style="user-select: auto !important;">Accountable</em> performs the whole task)</li>
	<li style="user-select: auto !important;"><code style="user-select: auto !important;">A</code> (<em style="user-select: auto !important;">Accountable</em>): accepts the task from <em style="user-select: auto !important;">Responsible</em>; for each task, there must be exactly one instance of this level of involvement, unlike the other levels, of which there can be any number</li>
	<li style="user-select: auto !important;"><code style="user-select: auto !important;">C</code> (<em style="user-select: auto !important;">Consulted</em>): provides consultation during the execution of the task</li>
	<li style="user-select: auto !important;"><code style="user-select: auto !important;">I</code> (<em style="user-select: auto !important;">Informed</em>): receives information about the progress of the task</li>
</ul>

<p style="user-select: auto !important;">Help the students verify the correctness of the matrix.</p>

### 입력 

 <p style="user-select: auto !important;">The first line contains two integers <mjx-container class="MathJax" jax="CHTML" style="font-size: 99.7%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> and <mjx-container class="MathJax" jax="CHTML" style="font-size: 99.7%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45A TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$m$</span></mjx-container>: the number of rows and columns of the RACI matrix (<mjx-container class="MathJax" jax="CHTML" style="font-size: 99.7%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D45A TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>n</mi><mo>,</mo><mi>m</mi><mo>≤</mo><mn>100</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \le n, m \le 100$</span></mjx-container>).</p>

<p style="user-select: auto !important;">Next, <mjx-container class="MathJax" jax="CHTML" style="font-size: 99.7%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$n$</span></mjx-container> rows are listed, each containing <mjx-container class="MathJax" jax="CHTML" style="font-size: 99.7%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45A TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>m</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$m$</span></mjx-container> elements separated by spaces.</p>

<p style="user-select: auto !important;">Each row represents a task, and each column corresponds to a stakeholder.</p>

<p style="user-select: auto !important;">Each element of the matrix can be either an uppercase letter "<code style="user-select: auto !important;">R</code>", "<code style="user-select: auto !important;">A</code>", "<code style="user-select: auto !important;">C</code>", or "<code style="user-select: auto !important;">I</code>", or a minus sign, "<code style="user-select: auto !important;">-</code>", indicating that the given stakeholder has no level of involvement in this task.</p>

### 출력 

 <p style="user-select: auto !important;">Print "<code style="user-select: auto !important;">Yes</code>" if the matrix is correct, or "<code style="user-select: auto !important;">No</code>" otherwise.</p>

