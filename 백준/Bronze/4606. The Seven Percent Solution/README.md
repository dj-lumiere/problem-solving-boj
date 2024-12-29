# [Bronze II] The Seven Percent Solution - 4606 

[문제 링크](https://www.acmicpc.net/problem/4606) 

### 성능 요약

메모리: 127496 KB, 시간: 220 ms

### 분류

구현, 문자열

### 제출 일자

2024년 12월 29일 11:33:37

### 문제 설명

<p style="user-select: auto !important;">Uniform Resource Identifiers (or URIs) are strings like http://icpc.baylor.edu/icpc/, mailto:foo@bar.org, ftp://127.0.0.1/pub/linux, or even just readme.txt that are used to identify a resource, usually on the Internet or a local computer. Certain characters are reserved within URIs, and if a reserved character is part of an identifier then it must be percent-encoded by replacing it with a percent sign followed by two hexadecimal digits representing the ASCII code of the character. A table of seven reserved characters and their encodings is shown below. Your job is to write a program that can percent-encode a string of characters.</p>

<table class="table table-bordered" style="width: 30%; user-select: auto !important;">
	<thead style="user-select: auto !important;">
		<tr style="user-select: auto !important;">
			<th style="user-select: auto !important;">Character</th>
			<th style="user-select: auto !important;">Encoding</th>
		</tr>
	</thead>
	<tbody style="user-select: auto !important;">
		<tr style="user-select: auto !important;">
			<td style="user-select: auto !important;">" " (space)</td>
			<td style="user-select: auto !important;">%20</td>
		</tr>
		<tr style="user-select: auto !important;">
			<td style="user-select: auto !important;">"!" (exclamation point)</td>
			<td style="user-select: auto !important;">%21</td>
		</tr>
		<tr style="user-select: auto !important;">
			<td style="user-select: auto !important;">"<span style="user-select: auto !important;">$</span>" (dollar sign)</td>
			<td style="user-select: auto !important;">%24</td>
		</tr>
		<tr style="user-select: auto !important;">
			<td style="user-select: auto !important;">"%" (percent sign)</td>
			<td style="user-select: auto !important;">%25</td>
		</tr>
		<tr style="user-select: auto !important;">
			<td style="user-select: auto !important;">"(" (left parenthesis)</td>
			<td style="user-select: auto !important;">%28</td>
		</tr>
		<tr style="user-select: auto !important;">
			<td style="user-select: auto !important;">")" (right parenthesis)</td>
			<td style="user-select: auto !important;">%29</td>
		</tr>
		<tr style="user-select: auto !important;">
			<td style="user-select: auto !important;">"*" (asterisk)</td>
			<td style="user-select: auto !important;">%2a</td>
		</tr>
	</tbody>
</table>

### 입력 

 <p style="user-select: auto !important;">The input consists of one or more strings, each 1–79 characters long and on a line by itself, followed by a line containing only "#" that signals the end of the input. The character "#" is used only as an end-of-input marker and will not appear anywhere else in the input. A string may contain spaces, but not at the beginning or end of the string, and there will never be two or more consecutive spaces.</p>

### 출력 

 <p style="user-select: auto !important;">For each input string, replace every occurrence of a reserved character in the table above by its percent-encoding, exactly as shown, and output the resulting string on a line by itself. Note that the percent-encoding for an asterisk is %2a (with a lowercase "a") rather than %2A (with an uppercase "A").</p>

