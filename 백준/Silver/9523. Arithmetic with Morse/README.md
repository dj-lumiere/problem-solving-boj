# [Silver III] Arithmetic with Morse - 9523 

[문제 링크](https://www.acmicpc.net/problem/9523) 

### 성능 요약

메모리: 128680 KB, 시간: 252 ms

### 분류

자료 구조, 구현, 수학, 파싱, 스택, 문자열

### 제출 일자

2024년 12월 14일 22:57:27

### 문제 설명

<p style="user-select: auto !important;">Morse code is a method used to transmit text messages as a series of dots “<code style="user-select: auto !important;">.</code>” and dashes “<code style="user-select: auto !important;">-</code>”. For example, the letter “<code style="user-select: auto !important;">A</code>” is represented with “<code style="user-select: auto !important;">.-</code>” and the letter “<code style="user-select: auto !important;">B</code>” with “<code style="user-select: auto !important;">-...</code>”. This code has been used for several years in the army and civil applications, but you are going to use it to do math.</p>

<p style="user-select: auto !important;">With this in mind, we assign values to dots and dashes, and to save space we use two additional characters. The following table shows the four allowed characters and their values.</p>

<table class="table table-bordered" style="width: 40%; user-select: auto !important;">
	<thead style="user-select: auto !important;">
		<tr style="user-select: auto !important;">
			<th style="user-select: auto !important;">Character</th>
			<th style="user-select: auto !important;">Value</th>
			<th style="user-select: auto !important;"> </th>
		</tr>
	</thead>
	<tbody style="user-select: auto !important;">
		<tr style="user-select: auto !important;">
			<td style="user-select: auto !important;">.</td>
			<td style="user-select: auto !important;">1</td>
			<td style="user-select: auto !important;"> </td>
		</tr>
		<tr style="user-select: auto !important;">
			<td style="user-select: auto !important;"><code style="user-select: auto !important;">-</code></td>
			<td style="user-select: auto !important;">5</td>
			<td style="user-select: auto !important;"> </td>
		</tr>
		<tr style="user-select: auto !important;">
			<td style="user-select: auto !important;"><code style="user-select: auto !important;">:</code></td>
			<td style="user-select: auto !important;">2</td>
			<td style="user-select: auto !important;">(two times “<code style="user-select: auto !important;">.</code>”)</td>
		</tr>
		<tr style="user-select: auto !important;">
			<td style="user-select: auto !important;"><code style="user-select: auto !important;">=</code></td>
			<td style="user-select: auto !important;">10</td>
			<td style="user-select: auto !important;">(two times “<code style="user-select: auto !important;">-</code>”)</td>
		</tr>
	</tbody>
</table>

<p style="user-select: auto !important;">A Morse number is a string that only contains the above four characters; its value is the sum of the values assigned to each individual character. As an example, the value of “<code style="user-select: auto !important;">=.-..</code>” is 10+1+5+1+1 = 18. Notice that each Morse number represents a unique value, but there are values that can be represented with several Morse numbers. For instance, there are three Morse numbers with value 3: “<code style="user-select: auto !important;">...</code>”, “<code style="user-select: auto !important;">.:</code>” and “<code style="user-select: auto !important;">:.</code>”.</p>

<p style="user-select: auto !important;">Well, numbers are ready. To form expressions we also need operators. We consider two arithmetic operators: “<code style="user-select: auto !important;">+</code>” represents addition, while “<code style="user-select: auto !important;">*</code>” represents multiplication. A Morse expression is a sequence of strings that interleaves Morse numbers and operators, that starts and ends with a Morse number, and contains at least one operator. Morse expressions can be evaluated by replacing each Morse number by its value, and then evaluating the obtained mathematical expression using the common operators precedence and associativity. For example, the value of the Morse expression “<code style="user-select: auto !important;">=.-.. + ... * :.</code>” is 18 + 3 × 3 = 18 + (3 × 3) = 27. Given a Morse expression, print its value.</p>

### 입력 

 <p style="user-select: auto !important;">The first line contains an integer N (1 ≤ N ≤ 4) representing the number of operators in the Morse expression. The second line contains 2N + 1 non-empty strings representing the Morse expression. The line interleaves Morse numbers and operators, being the first and last strings Morse numbers. Each Morse number is at most 7 characters long, where each character is either “<code style="user-select: auto !important;">.</code>”, “<code style="user-select: auto !important;">-</code>”, “<code style="user-select: auto !important;">:</code>” or “<code style="user-select: auto !important;">=</code>”. Each operator is either “<code style="user-select: auto !important;">+</code>” or “<code style="user-select: auto !important;">*</code>”.</p>

### 출력 

 <p style="user-select: auto !important;">Output a line with an integer representing the value of the Morse expression.</p>

