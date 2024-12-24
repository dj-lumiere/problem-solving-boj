# [Bronze I] Химия - 29483 

[문제 링크](https://www.acmicpc.net/problem/29483) 

### 성능 요약

메모리: 125484 KB, 시간: 212 ms

### 분류

사칙연산, 구현, 수학, 파싱, 문자열

### 제출 일자

2024년 12월 24일 09:43:40

### 문제 설명

<p style="user-select: auto !important;">Ваша задача --- вычислить массу молекулы вещества, заданного химической формулой. Формула представляет собой перечисление элементов входящих в молекулу вещества. Для сокращения записи формулы используется обозначение <mjx-container class="MathJax" jax="CHTML" style="font-size: 99.7%; position: relative; user-select: auto !important;"><mjx-math class="MJX-TEX" aria-hidden="true" style="user-select: auto !important;"><mjx-mi class="mjx-i" style="user-select: auto !important;"><mjx-c class="mjx-c1D438 TEX-I" style="user-select: auto !important;"></mjx-c></mjx-mi><mjx-mi class="mjx-i" style="user-select: auto !important;"><mjx-c class="mjx-c1D45B TEX-I" style="user-select: auto !important;"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline" style="user-select: auto !important;"><math xmlns="http://www.w3.org/1998/Math/MathML" style="user-select: auto !important;"><mi style="user-select: auto !important;">E</mi><mi style="user-select: auto !important;">n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext" style="user-select: auto !important;">$E n$</span></mjx-container>, которое означает, что элемент <mjx-container class="MathJax" jax="CHTML" style="font-size: 99.7%; position: relative; user-select: auto !important;"><mjx-math class="MJX-TEX" aria-hidden="true" style="user-select: auto !important;"><mjx-mi class="mjx-i" style="user-select: auto !important;"><mjx-c class="mjx-c1D438 TEX-I" style="user-select: auto !important;"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline" style="user-select: auto !important;"><math xmlns="http://www.w3.org/1998/Math/MathML" style="user-select: auto !important;"><mi style="user-select: auto !important;">E</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext" style="user-select: auto !important;">$E$</span></mjx-container> надо повторить <mjx-container class="MathJax" jax="CHTML" style="font-size: 99.7%; position: relative; user-select: auto !important;"><mjx-math class="MJX-TEX" aria-hidden="true" style="user-select: auto !important;"><mjx-mi class="mjx-i" style="user-select: auto !important;"><mjx-c class="mjx-c1D45B TEX-I" style="user-select: auto !important;"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline" style="user-select: auto !important;"><math xmlns="http://www.w3.org/1998/Math/MathML" style="user-select: auto !important;"><mi style="user-select: auto !important;">n</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext" style="user-select: auto !important;">$n$</span></mjx-container> раз. Масса молекулы вещества --- это сумма весов всех его элементов.</p>

<table class="table table-bordered th-center td-center table-center-30" style="user-select: auto !important;">
	<tbody style="user-select: auto !important;">
		<tr style="user-select: auto !important;">
			<th style="user-select: auto !important;">Название элемента</th>
			<th style="user-select: auto !important;">Обозначение</th>
			<th style="user-select: auto !important;">Масса</th>
		</tr>
		<tr style="user-select: auto !important;">
			<td style="user-select: auto !important;">Водород</td>
			<td style="user-select: auto !important;">H</td>
			<td style="user-select: auto !important;">1</td>
		</tr>
		<tr style="user-select: auto !important;">
			<td style="user-select: auto !important;">Углерод</td>
			<td style="user-select: auto !important;">C</td>
			<td style="user-select: auto !important;">12</td>
		</tr>
		<tr style="user-select: auto !important;">
			<td style="user-select: auto !important;">Азот</td>
			<td style="user-select: auto !important;">N</td>
			<td style="user-select: auto !important;">14</td>
		</tr>
		<tr style="user-select: auto !important;">
			<td style="user-select: auto !important;">Кислород</td>
			<td style="user-select: auto !important;">O</td>
			<td style="user-select: auto !important;">16</td>
		</tr>
	</tbody>
</table>

<p style="user-select: auto !important;">В единственной строке входного файла записана формула. Ее длина не превышает 20 символов. Формула состоит из букв <<CHNO>> и цифр от 1 до 9. Цифра всегда идет после буквы.</p>

### 입력 

 <p style="user-select: auto !important;">В выходной файл выведите одно число --- массу молекулы.</p>

### 출력 

 Empty

