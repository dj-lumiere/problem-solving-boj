# [Bronze II] Черно-белая графика - 21675 

[문제 링크](https://www.acmicpc.net/problem/21675) 

### 성능 요약

메모리: 128804 KB, 시간: 236 ms

### 분류

구현, 문자열

### 제출 일자

2024년 12월 20일 13:54:04

### 문제 설명

<p style="user-select: auto !important;">Одна из базовых задач компьютерной графики – обработка черно-белых изображений. Изображения можно представить в виде прямоугольников шириной w и высотой h, разбитых на w×h единичных квадратов, каждый из которых имеет либо белый, либо черный цвет. Такие единичные квадраты называются пикселами. В памяти компьютера сами изображения хранятся в виде прямоугольных таблиц, содержащих нули и единицы.</p>

<p style="user-select: auto !important;">Во многих областях очень часто возникает задача комбинации изображений. Одним из простейших методов комбинации, который используется при работе с черно-белыми изображениями, является попиксельное применение некоторой логической операции. Это означает, что значение пиксела результата получается применением этой логической операции к соответствующим пикселам аргументов. Логическая операция от двух аргументов обычно задается таблицей истинности, которая содержит значения операции для всех возможных комбинаций аргументов. Например, для операции «исключающее ИЛИ» эта таблица выглядит так.</p>

<table class="table table-bordered th-center td-center table-center-30" style="user-select: auto !important;">
	<thead style="user-select: auto !important;">
		<tr style="user-select: auto !important;">
			<th style="user-select: auto !important;">Первый аргумент</th>
			<th style="user-select: auto !important;">Второй аргумент</th>
			<th style="user-select: auto !important;">Результат</th>
		</tr>
	</thead>
	<tbody style="user-select: auto !important;">
		<tr style="user-select: auto !important;">
			<td style="user-select: auto !important;">0</td>
			<td style="user-select: auto !important;">0</td>
			<td style="user-select: auto !important;">0</td>
		</tr>
		<tr style="user-select: auto !important;">
			<td style="user-select: auto !important;">0</td>
			<td style="user-select: auto !important;">1</td>
			<td style="user-select: auto !important;">1</td>
		</tr>
		<tr style="user-select: auto !important;">
			<td style="user-select: auto !important;">1</td>
			<td style="user-select: auto !important;">0</td>
			<td style="user-select: auto !important;">1</td>
		</tr>
		<tr style="user-select: auto !important;">
			<td style="user-select: auto !important;">1</td>
			<td style="user-select: auto !important;">1</td>
			<td style="user-select: auto !important;">0</td>
		</tr>
	</tbody>
</table>

<p style="user-select: auto !important;">Требуется написать программу, которая вычислит результат попиксельного применения заданной логической операции к двум черно-белым изображениям одинакового размера.</p>

### 입력 

 <p style="user-select: auto !important;">Первая строка входного файла содержит два целых числа w и h (1 ≤ w, h ≤ 100). Последующие h строк описывают первое изображение и каждая из этих строк содержит w символов, каждый из которых равен нулю или единице. Далее следует описание второго изображения в аналогичном формате. Последняя строка входного файла содержит описание логической операции в виде четырех чисел, каждое из которых – ноль или единица. Первое из них есть результат применения логической операции в случае, если оба аргумента – нули, второе – результат в случае, если первый аргумент – ноль, второй – единица, третье – результат в случае, если первый аргумент – единица, второй – ноль, а четвертый – в случае, если оба аргумента – единицы.</p>

### 출력 

 <p style="user-select: auto !important;">В выходной файл необходимо вывести результат применения заданной логической операции к изображениям в том же формате, в котором изображения заданы во входном файле.</p>

