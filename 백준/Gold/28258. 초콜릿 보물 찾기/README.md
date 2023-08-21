# [Gold II] 초콜릿 보물 찾기 - 28258 

[문제 링크](https://www.acmicpc.net/problem/28258) 

### 성능 요약

메모리: 13676 KB, 시간: 88 ms

### 분류

애드 혹, 많은 조건 분기

### 문제 설명

<p>한별이와 함께 어느 해변에 놀러 가기로 한 코코는 해변에 미리 와서 보물찾기 게임을 준비했다. 먼저 모래사장에 <mjx-container class="MathJax" jax="CHTML" style="font-size: 99.9%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-cD7"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="3"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>10</mn><mo>×</mo><mn>10</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$10\times 10$</span></mjx-container> 크기의 격자를 그린 후, <mjx-container class="MathJax" jax="CHTML" style="font-size: 99.9%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$100$</span></mjx-container>개의 칸 중에서 가로 또는 세로로 이웃한 두 칸을 골라 <mjx-container class="MathJax" jax="CHTML" style="font-size: 99.9%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-cD7"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="3"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>2</mn><mo>×</mo><mn>1</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$2\times 1$</span></mjx-container> 크기의 보물상자를 묻어 놓았다.</p>

<p>보물찾기 게임 준비를 마친 코코는 한별이에게 이런 제안을 했다. “최대 <mjx-container class="MathJax" jax="CHTML" style="font-size: 99.9%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c35"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$50$</span></mjx-container>칸만 파 보고 보물상자의 위치를 정확히 알아내면 보물상자에 든 초콜릿을 모두 줄게. 보물상자가 있는 두 칸을 모두 파낼 필요는 없고, 두 칸의 좌표만 맞으면 돼.” 과연 한별이는 보물상자의 초콜릿을 얻을 수 있을까?</p>

### 입력 

 Empty

### 출력 

 <p>다음을 한 줄에 출력하여 인터랙터에게 쿼리를 할 수 있다. 쿼리는 최대 <mjx-container class="MathJax" jax="CHTML" style="font-size: 99.9%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c35"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$50$</span></mjx-container>번까지 할 수 있다.</p>

<ul>
	<li><code>? r c</code> : <code>r</code>행 <code>c</code>열을 파 본다. 행 번호와 열 번호는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 99.9%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0$</span></mjx-container>에서 시작하며, 따라서 올바른 값의 범위는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 99.9%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D45F TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="2"><mjx-c class="mjx-c1D450 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c39"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>≤</mo><mi>r</mi><mo>,</mo><mi>c</mi><mo>≤</mo><mn>9</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0\le r,c\le 9$</span></mjx-container>이다.</li>
</ul>

<p>각 쿼리의 결과는 한 줄을 입력받아 알 수 있다. 가능한 결과는 다음과 같다.</p>

<ul>
	<li><code>1</code> : <code>r</code>행 <code>c</code>열에 보물상자의 일부가 있다.</li>
	<li><code>0</code> : <code>r</code>행 <code>c</code>열에 보물상자의 일부가 없다.</li>
</ul>

<p>쿼리를 출력한 후에는 반드시 표준 출력 버퍼를 flush해야 한다.</p>

<p>보물상자의 위치를 알아냈으면 다음과 같이 출력하고 flush한 후 프로그램을 종료해야 한다.</p>

<ul>
	<li><code>! r1 c1 r2 c2</code> : 보물상자는 <code>r1</code>행 <code>c1</code>열과 <code>r2</code>행 <code>c2</code>열에 걸쳐 있다. 좌표의 순서는 관계 없다. 보물상자의 위치가 맞으면 <span style="color:#16a085;"><strong>맞았습니다</strong></span>, 아니면 <span style="color:#dd4124;">틀렸습니다</span>를 받는다.</li>
</ul>

<p>출력 형식을 지키지 않거나 쿼리를 <mjx-container class="MathJax" jax="CHTML" style="font-size: 99.9%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c35"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>50</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$50$</span></mjx-container>번보다 많이 한 경우에는 예상치 못한 채점 결과를 받을 수 있음에 유의한다.</p>

