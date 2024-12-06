# [Bronze II] Kylskåpstransport - 26949 

[문제 링크](https://www.acmicpc.net/problem/26949) 

### 성능 요약

메모리: 108384 KB, 시간: 88 ms

### 분류

사칙연산, 브루트포스 알고리즘, 구현, 수학

### 제출 일자

2024년 12월 6일 21:35:13

### 문제 설명

<p>En fabrik som tillverkar kylskåp ska leverera ett större parti med $n, 1 \le n \le 1000$ kylar till en stormarknad. Till sitt förfogande har fabriken två bilar.</p>

<ul>
	<li>bil $A$ kostar $p_a$ kr/resa, $500 \le p_a \le 2000$ och kan lasta $k_a, 10 \le k_a \le 50$, kylskåp åt gången.</li>
	<li>bil $B$ kostar $p_b$ kr/resa, $500 \le p_b \le 2000$ och kan lasta $k_b, 10 \le k_b \le 50$, kylskåp åt gången.</li>
</ul>

<p>Din uppgift är nu att skriva ett program som tar emot uppgifter om de fem variablerna ovan och som med hjälp av dessa bestämmer hur många turer varje bil ska köra för att minimera <em>den totala transportkostnaden</em>.</p>

### 입력 

 <p>Indata består av de fem heltalen $p_a$, $k_a$, $p_b$, $k_b$ och $n$ på en rad, separerade med ett blanksteg.</p>

### 출력 

 <p>Utdatan ska bestå av tre heltal: antalet turer bil $A$ ska köra, antalet turer bil $B$ ska köra, samt den totala kostnaden i kronor. För alla givna testfall garanteras det att svaret är unikt.</p>

