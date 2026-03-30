# [Silver V] StackExplosion - 35482 

[문제 링크](https://www.acmicpc.net/problem/35482) 

### 성능 요약

메모리: 324136 KB, 시간: 1636 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2026년 3월 30일 14:33:45

### 문제 설명

<blockquote>
<p>생일 파티에는 폭ㅂ... 아니, 폭죽이지! ─ 폭탄마 메구밍</p>
</blockquote>

<p>생일 파티는 화려할수록 좋다는 말을 들은 메구밍은 루미의 생일을 맞아 화려한 폭발 쇼를 보여주려고 한다. 물론 가능만 하다면 주특기인 폭렬 마법을 보여주고 싶지만, 그렇다고 폭렬 마법을 쓰면 생일 파티장이 통째로 지도에서 사라져 버리기 때문에 메구밍은 아쉬움을 무릅쓰고 스택을 이용해서 연쇄 폭발 쇼를 보여주기로 했다.</p>

<p>이 세계의 스택은 <strong>메모리</strong>와 <strong>용량</strong>이라는 두 가지 인자를 가지고 있다. 만일 메모리가 용량을 초과하게 된다면 그 스택은 3초 후 화려한 빛을 내면서 폭발하며, 그 즉시 파티장 내에 있는 모든 스택의 메모리에 폭발 직전 가지고 있던 메모리의 절반에서 소수점 아래를 버린 만큼을 추가한다. 예를 들어 현재 메모리가 <mjx-container class="MathJax" jax="CHTML" style="font-size: 99.9%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c39"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>9</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$9$</span></mjx-container>인 스택이 폭발하면 모든 스택의 메모리에는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 99.9%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c34"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>4</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$4$</span></mjx-container>만큼이 추가된다. 이 과정은 연쇄적으로 일어날 수 있다. 즉, 다른 스택의 폭발에 의하여 메모리가 용량을 초과하게 되는 스택 역시 3초 후 폭발한다. 이미 폭발한 스택은 다시 폭발하지 않는다.</p>

<p>메구밍은 생일 파티장에 <mjx-container class="MathJax" jax="CHTML" style="font-size: 99.9%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>개의 스택을 밀반입한 뒤 스택의 메모리를 충전했다. 당신의 목표는 이 스택 중 몇 개가 터질지 미리 알아내어 혼란을 방지하는 것이다.</p>

### 입력 

 <p>첫째 줄에 메구밍이 밀반입한 스택의 수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 99.9%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 주어진다.</p>

<p>둘째 줄에 각 스택의 용량을 의미하는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 99.9%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>개의 양의 정수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 99.9%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D450 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-script></mjx-msub><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mo class="mjx-n" space="2"><mjx-c class="mjx-c22EF"></mjx-c></mjx-mo><mjx-mo class="mjx-n" space="2"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-msub space="2"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D450 TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>c</mi><mn>1</mn></msub><mo>,</mo><mo>⋯</mo><mo>,</mo><msub><mi>c</mi><mi>N</mi></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$c_1,\cdots,c_N$</span></mjx-container>이 공백으로 구분되어 주어진다.</p>

<p>셋째 줄에 메구밍이 각 스택에 충전한 메모리를 의미하는 <mjx-container class="MathJax" jax="CHTML" style="font-size: 99.9%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>개의 양의 정수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 99.9%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-msub><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45A TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mn class="mjx-n" size="s"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-script></mjx-msub><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mo class="mjx-n" space="2"><mjx-c class="mjx-c22EF"></mjx-c></mjx-mo><mjx-mo class="mjx-n" space="2"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-msub space="2"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D45A TEX-I"></mjx-c></mjx-mi><mjx-script style="vertical-align: -0.15em;"><mjx-mi class="mjx-i" size="s"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-script></mjx-msub></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>m</mi><mn>1</mn></msub><mo>,</mo><mo>⋯</mo><mo>,</mo><msub><mi>m</mi><mi>N</mi></msub></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$m_1,\cdots,m_N$</span></mjx-container>이 공백으로 구분되어 주어진다.</p>

### 출력 

 <p>첫째 줄에 폭발하게 되는 스택의 수를 출력한다.</p>

