# [Platinum III] NATO 음성 기호와 쿼리 - 26151 

[문제 링크](https://www.acmicpc.net/problem/26151) 

### 성능 요약

메모리: 312272 KB, 시간: 2432 ms

### 분류

이분 탐색, 다이나믹 프로그래밍, 재귀, 문자열

### 제출 일자

2023년 11월 29일 17:42:51

### 문제 설명

<p>NATO 음성 문자는 통신의 혼란 등을 방지하기 위해 만들어졌으며, 아래 규칙에 따라 알파벳을 단어로 변환한다.</p>

<p>아래 문자열을 일일이 따라칠 필요는 없다. 하단의 '노트' 탭에 각 언어별로 작성되어있다.</p>

<table class="table table-bordered table-center-50">
	<tbody>
		<tr>
			<td><strong>알파벳</strong></td>
			<td><strong>NATO</strong></td>
			<td><strong>알파벳</strong></td>
			<td><strong>NATO</strong></td>
		</tr>
		<tr>
			<td><strong>A</strong></td>
			<td>ALFA</td>
			<td><strong>N</strong></td>
			<td>NOVEMBER</td>
		</tr>
		<tr>
			<td><strong>B</strong></td>
			<td>BRAVO</td>
			<td><strong>O</strong></td>
			<td>OSCAR</td>
		</tr>
		<tr>
			<td><strong>C</strong></td>
			<td>CHARLIE</td>
			<td><strong>P</strong></td>
			<td>PAPA</td>
		</tr>
		<tr>
			<td><strong>D</strong></td>
			<td>DELTA</td>
			<td><strong>Q</strong></td>
			<td>QUEBEC</td>
		</tr>
		<tr>
			<td><strong>E</strong></td>
			<td>ECHO</td>
			<td><strong>R</strong></td>
			<td>ROMEO</td>
		</tr>
		<tr>
			<td><strong>F</strong></td>
			<td>FOXTROT</td>
			<td><strong>S</strong></td>
			<td>SIERRA</td>
		</tr>
		<tr>
			<td><strong>G</strong></td>
			<td>GOLF</td>
			<td><strong>T</strong></td>
			<td>TANGO</td>
		</tr>
		<tr>
			<td><strong>H</strong></td>
			<td>HOTEL</td>
			<td><strong>U</strong></td>
			<td>UNIFORM</td>
		</tr>
		<tr>
			<td><strong>I</strong></td>
			<td>INDIA</td>
			<td><strong>V</strong></td>
			<td>VICTOR</td>
		</tr>
		<tr>
			<td><strong>J</strong></td>
			<td>JULIETT</td>
			<td><strong>W</strong></td>
			<td>WHISKEY</td>
		</tr>
		<tr>
			<td><strong>K</strong></td>
			<td>KILO</td>
			<td><strong>X</strong></td>
			<td>XRAY</td>
		</tr>
		<tr>
			<td><strong>L</strong></td>
			<td>LIMA</td>
			<td><strong>Y</strong></td>
			<td>YANKEE</td>
		</tr>
		<tr>
			<td><strong>M</strong></td>
			<td>MIKE</td>
			<td><strong>Z</strong></td>
			<td>ZULU</td>
		</tr>
	</tbody>
</table>

<p>예를 들면, "HCPC"라는 문자열은 "<strong>H</strong>OTEL<strong>C</strong>HARLIE<strong>P</strong>APA<strong>C</strong>HARLIE"가 된다.</p>

<p>원래는 각 단어 사이에 공백을 넣지만, 이 문제에서는 편의상 붙여쓰기로 하자.</p>

<p>하이비는 이런 방식의 변환이 너무 재밌어서, 문자열 $ S $를 들고 와서 아래 쿼리를 적용시키기로 했다.</p>

<ul>
	<li>1 $ x $: $ S $에 NATO 음성 문자 변환을 $ x $번 적용한다. $( 1 \le x \le 10^{18} )$</li>
	<li>2 $ p $: $ S $의 $ p $번째 글자를 출력한다. $( 1 \le p \le \min(|S|, 10^{18}))$</li>
</ul>

<p>하이비는 쿼리가 끝난 뒤에 출력된 글자들을 알고 싶었지만, 문자열의 길이가 너무 길어져서 지친 관계로 여러분들에게 이 작업을 넘기기로 했다.</p>

<p>지친 하이비에게 쿼리의 출력값을 대신 알려주자.</p>

### 입력 

 <p>첫째 줄에 알파벳 대문자로만 이루어진 문자열 $ S $와 쿼리의 횟수 $ Q $가 주어진다. $( 1 \le |S| \le 200\,000; $ $ 1 \le Q \le 200\,000 )$</p>

<p>이어 $ Q $개의 줄에 걸쳐 쿼리가 주어진다.</p>

### 출력 

 <p>2번 쿼리가 들어올 때마다 출력되는 글자를 <strong>공백 없이</strong> 출력한다.</p>

