# [Gold V] Reverse Roman Notation - 4773 

[문제 링크](https://www.acmicpc.net/problem/4773) 

### 성능 요약

메모리: 133036 KB, 시간: 272 ms

### 분류

자료 구조, 구현, 파싱, 시뮬레이션, 스택, 문자열

### 제출 일자

2024년 10월 16일 17:42:21

### 문제 설명

<p>Hermes Poseidon (HP) has produced a new calculator, the HP CXX, using the very latest in modern technology. It supports the four basic arithmetic operations on integer values from I to MMMMCMXCIX.</p>

<p>In this problem, you are simulating The HP CXX. Each line of input will be either a roman numeral representation of a positive integer (between I(1) and MMMMCMXCIX(4999)), which will then be pushed to the top of the virtual stack, or it will be an arithmetic operation (+ − * /) to be performed on the top two values of the stack. In addition, there is the = operation, which is a request to print the value of the top of the stack (in roman numerals, of course).</p>

<p>For the − operation, subtract the ﬁrst number on the stack from the second. For /, divide the second number on the stack by the ﬁrst. An attempt to divide by 0 should result in the error message “division by zero exception”. When that happens, push the dividend (non-zero number) back onto the stack, but not the divisor (zero).</p>

<p>If an operation is requested, and there are insufﬁcient numbers on the stack, print the error “stack underﬂow” and leave the stack unchanged. This applies to both the binary operations +−*/ and the print operation =.</p>

<p>If an attempt is made to print a number whose value is 0 or less, or whose value is greater than MMMMCMXCIX(4999), display the error message “out of range exception” and go on to the next line of input.</p>

<p>Roman Numerals</p>

<p>For those who are unfamiliar with Roman Numerals, here is a quick summary:</p>

<p>Each letter used in Roman numerals stands for a different number:</p>

<table class="table" style="width:30%">
	<thead>
		<tr>
			<th style="width:15%">Roman Numeral</th>
			<th style="width:15%">Number</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>I</td>
			<td>1</td>
		</tr>
		<tr>
			<td>V</td>
			<td>5</td>
		</tr>
		<tr>
			<td>X</td>
			<td>10</td>
		</tr>
		<tr>
			<td>L</td>
			<td>50</td>
		</tr>
		<tr>
			<td>C</td>
			<td>100</td>
		</tr>
		<tr>
			<td>D</td>
			<td>500</td>
		</tr>
		<tr>
			<td>M</td>
			<td>1000</td>
		</tr>
	</tbody>
</table>

<p>A string of letters means that their values should be added together. For example, XXX = 10 + 10 + 10 = 30, and LXI = 50 + 10 + 1 = 61. If a smaller value is placed before a larger one, we subtract instead of adding. For instance, IV = 5 − 1 = 4 and XC = 100 − 10 = 90.</p>

<ul>
	<li>Except for M, do not add more than three of the same letters together.</li>
	<li>Subtract only powers of ten, such as I, X, or C. Writing VL for 45 is not allowed: write XLV instead.</li>
	<li>Subtract only a single letter from a single numeral. Write VIII for 8, not IIX; 19 is XIX, not IXX.</li>
	<li>Don’t subtract a letter from another letter more than ten times greater. This means that you can only subtract I from V or X, and X from L or C, so MIM is illegal.</li>
</ul>

### 입력 

 <p>Each input line consists of either:</p>

<ul>
	<li>A Roman numeral between I and MMMMCMXCIX, or</li>
	<li>An arithmetic operation +, −, /, or *, or the print operator, =</li>
</ul>

<p>The input ends at the end-of-ﬁle.</p>

### 출력 

 <p>A line will be output:</p>

<ul>
	<li>For every print operation, print the value at the top of the stack, or</li>
	<li>One of the error messages, on a line by itself:
	<ul>
		<li>division by zero exception</li>
		<li>stack underflow</li>
		<li>out of range exception</li>
	</ul>
	</li>
</ul>

<p>No other output should be produced</p>

