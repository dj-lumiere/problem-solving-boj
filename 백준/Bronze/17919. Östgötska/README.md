# [Bronze II] Östgötska - 17919 

[문제 링크](https://www.acmicpc.net/problem/17919) 

### 성능 요약

메모리: 127496 KB, 시간: 228 ms

### 분류

구현, 문자열

### 제출 일자

2024년 12월 25일 18:19:35

### 문제 설명

<p style="user-select: auto !important;">Anders talks in the Swedish dialect of <em style="user-select: auto !important;">östgötska</em>. Unfortunately, this makes it somewhat hard to get a programming job in the Swedish capital of Stockholm. The trendy Stockholm hipsters only accept applicants speaking the standard Swedish dialect, <em style="user-select: auto !important;">rikssvenska</em>.</p>

<p style="user-select: auto !important;">To increase his chances of passing interviews, he wishes to practice talking rikssvenska. To help him with this, he wants you to write a program that can determine whenever he accidentally reverts to speaking östgötska.</p>

<p style="user-select: auto !important;">A simple way of determining if a sentence is written in östgötska is if at least <mjx-container class="MathJax" jax="CHTML" style="font-size: 99.7%; position: relative; user-select: auto !important;"><mjx-math class="MJX-TEX" aria-hidden="true" style="user-select: auto !important;"><mjx-mn class="mjx-n" style="user-select: auto !important;"><mjx-c class="mjx-c34" style="user-select: auto !important;"></mjx-c><mjx-c class="mjx-c30" style="user-select: auto !important;"></mjx-c></mjx-mn><mjx-mi class="mjx-n" style="user-select: auto !important;"><mjx-c class="mjx-c25" style="user-select: auto !important;"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline" style="user-select: auto !important;"><math xmlns="http://www.w3.org/1998/Math/MathML" style="user-select: auto !important;"><mn style="user-select: auto !important;">40</mn><mi mathvariant="normal" style="user-select: auto !important;">%</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext" style="user-select: auto !important;">$40\%$</span></mjx-container> of the words in the sentence contains the letter <code style="user-select: auto !important;">ä</code>. For simplicity, this is encoded as the letter combination <code style="user-select: auto !important;">ae</code> (meaning any appearance of the substring \texttt{ae} is to be regarded as an occurrence of the letter <code style="user-select: auto !important;">ä</code>).</p>

### 입력 

 <p style="user-select: auto !important;">The first and only line of input contains a sequence of space-separated words. Each word consists only of letters <code style="user-select: auto !important;">a-z</code>. There are at most <mjx-container class="MathJax" jax="CHTML" style="font-size: 99.7%; position: relative; user-select: auto !important;"><mjx-math class="MJX-TEX" aria-hidden="true" style="user-select: auto !important;"><mjx-mn class="mjx-n" style="user-select: auto !important;"><mjx-c class="mjx-c31" style="user-select: auto !important;"></mjx-c><mjx-c class="mjx-c30" style="user-select: auto !important;"></mjx-c><mjx-c class="mjx-c30" style="user-select: auto !important;"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline" style="user-select: auto !important;"><math xmlns="http://www.w3.org/1998/Math/MathML" style="user-select: auto !important;"><mn style="user-select: auto !important;">100</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext" style="user-select: auto !important;">$100$</span></mjx-container> words, and each word contains at most <mjx-container class="MathJax" jax="CHTML" style="font-size: 99.7%; position: relative; user-select: auto !important;"><mjx-math class="MJX-TEX" aria-hidden="true" style="user-select: auto !important;"><mjx-mn class="mjx-n" style="user-select: auto !important;"><mjx-c class="mjx-c31" style="user-select: auto !important;"></mjx-c><mjx-c class="mjx-c35" style="user-select: auto !important;"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline" style="user-select: auto !important;"><math xmlns="http://www.w3.org/1998/Math/MathML" style="user-select: auto !important;"><mn style="user-select: auto !important;">15</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext" style="user-select: auto !important;">$15$</span></mjx-container> letters <code style="user-select: auto !important;">a-z</code> (meaning that the <code style="user-select: auto !important;">ae</code> combination counts as two letters for this limit).</p>

### 출력 

 <p style="user-select: auto !important;">Output "<code style="user-select: auto !important;">dae ae ju traeligt va"</code> if the input sentence is in östgötska, otherwise output "<code style="user-select: auto !important;">haer talar vi rikssvenska</code>".</p>

