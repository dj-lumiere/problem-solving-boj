# [Gold III] ! - 22693 

[문제 링크](https://www.acmicpc.net/problem/22693) 

### 성능 요약

메모리: 115908 KB, 시간: 1040 ms

### 분류

수학

### 문제 설명

<p>You are one of ICPC participants and in charge of developing a library for multiprecision numbers and radix conversion. You have just finished writing the code, so next you have to test if it works correctly. You decided to write a simple, well-known factorial function for this purpose:</p>

<p><mjx-container class="MathJax" jax="CHTML" display="true" style="font-size: 99.9%; position: relative;"> <mjx-math display="true" class="MJX-TEX" aria-hidden="true" style="margin-left: 0px; margin-right: 0px;"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c21"></mjx-c></mjx-mo><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3D"></mjx-c></mjx-mo><mjx-munderover space="4"><mjx-over style="padding-bottom: 0.2em; padding-left: 0.267em;"><mjx-texatom size="s" texclass="ORD"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi></mjx-texatom></mjx-over><mjx-box><mjx-munder><mjx-row><mjx-base><mjx-mo class="mjx-lop"><mjx-c class="mjx-c220F TEX-S2"></mjx-c></mjx-mo></mjx-base></mjx-row><mjx-row><mjx-under style="padding-top: 0.167em; padding-left: 0.065em;"><mjx-texatom size="s" texclass="ORD"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n"><mjx-c class="mjx-c3D"></mjx-c></mjx-mo><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn></mjx-texatom></mjx-under></mjx-row></mjx-munder></mjx-box></mjx-munderover><mjx-texatom space="2" texclass="ORD"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D456 TEX-I"></mjx-c></mjx-mi></mjx-texatom><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3D"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-cD7"></mjx-c></mjx-mo><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c28"></mjx-c></mjx-mo><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D440 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c2212"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="3"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c29"></mjx-c></mjx-mo><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-cD7"></mjx-c></mjx-mo><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-c22EF"></mjx-c></mjx-mo><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-cD7"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="3"><mjx-c class="mjx-c32"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="3"><mjx-c class="mjx-cD7"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="3"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c2C"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="2"><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n"><mjx-c class="mjx-c21"></mjx-c></mjx-mo><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c3D"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mtext class="mjx-n"><mjx-c class="mjx-c2E"></mjx-c></mjx-mtext></mjx-math><mjx-assistive-mml unselectable="on" display="block"><math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><mi>M</mi><mo>!</mo><mo>=</mo><munderover><mo data-mjx-texclass="OP">∏</mo><mrow data-mjx-texclass="ORD"><mi>i</mi><mo>=</mo><mn>1</mn></mrow><mrow data-mjx-texclass="ORD"><mi>M</mi></mrow></munderover><mrow data-mjx-texclass="ORD"><mi>i</mi></mrow><mo>=</mo><mi>M</mi><mo>×</mo><mo stretchy="false">(</mo><mi>M</mi><mo>−</mo><mn>1</mn><mo stretchy="false">)</mo><mo>×</mo><mo>⋯</mo><mo>×</mo><mn>2</mn><mo>×</mo><mn>1</mn><mo>,</mo><mn>0</mn><mo>!</mo><mo>=</mo><mn>1</mn><mtext>.</mtext></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$$M! = \prod_{i=1}^{M}{i} = M \times (M - 1) \times \cdots \times 2 \times 1, 0! = 1\text{.}$$</span> </mjx-container></p>

<p>Your task is to write a program that shows the number of trailing zeros when you compute <i>M</i>! in base <i>N</i>, given <i>N</i> and <i>M</i>.</p>

### 입력 

 <p>The input contains multiple data sets. Each data set is described by one line in the format below:</p>

<pre><i>N M</i>
</pre>

<p>where <i>N</i> is a decimal number between 8 and 36 inclusive, and <i>M</i> is given in the string repre- sentation in base <i>N</i>. Exactly one white space character appears between them.</p>

<p>The string representation of <i>M</i> contains up to 12 characters in base <i>N</i>. In case <i>N</i> is greater than 10, capital letters A, B, C, ... may appear in the string representation, and they represent 10, 11, 12, ..., respectively.</p>

<p>The input is terminated by a line containing two zeros. You should not process this line.</p>

### 출력 

 <p>For each data set, output a line containing a decimal integer, which is equal to the number of trailing zeros in the string representation of <i>M</i>! in base <i>N</i>.</p>

