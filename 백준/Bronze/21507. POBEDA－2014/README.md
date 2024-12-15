# [Bronze II] POBEDA-2014 - 21507 

[문제 링크](https://www.acmicpc.net/problem/21507) 

### 성능 요약

메모리: 127516 KB, 시간: 244 ms

### 분류

수학

### 제출 일자

2024년 12월 15일 10:33:20

### 문제 설명

<p style="user-select: auto !important;">Как известно, современные видеокарты умеют формировать изображения с использованием только треугольников. Видеокарта POBEDA-2014 не отстает от современных тенденций. Известно, что она умеет отображать только прямоугольные равнобедренные треугольники четырех типов ориентации, представленные на рисунках ниже. Изменять ориентацию этих треугольников видеокарта не может. </p>

<table class="table table-bordered td-center" style="user-select: auto !important;">
	<tbody style="user-select: auto !important;">
		<tr style="user-select: auto !important;">
			<td style="user-select: auto !important;"><img alt="" src="https://upload.acmicpc.net/5fc20b4e-4942-4bec-8e31-6cf1972a38c4/-/preview/" style="width: 115px; height: 119px; user-select: auto !important;"></td>
			<td style="user-select: auto !important;"><img alt="" src="https://upload.acmicpc.net/8e32932b-119b-4e4d-ac0e-135e25a0aba1/-/preview/" style="width: 118px; height: 119px; user-select: auto !important;"></td>
			<td style="user-select: auto !important;"><img alt="" src="https://upload.acmicpc.net/a1518ff8-820b-475e-86ff-48bddf1eaa83/-/preview/" style="width: 126px; height: 119px; user-select: auto !important;"></td>
			<td style="user-select: auto !important;"><img alt="" src="https://upload.acmicpc.net/c3645870-fcc0-4721-a5eb-7408555552c6/-/preview/" style="width: 118px; height: 119px; user-select: auto !important;"></td>
		</tr>
		<tr style="user-select: auto !important;">
			<td style="user-select: auto !important;"> 1 тип</td>
			<td style="user-select: auto !important;">2 тип</td>
			<td style="user-select: auto !important;">3 тип</td>
			<td style="user-select: auto !important;">4 тип</td>
		</tr>
	</tbody>
</table>

<p style="user-select: auto !important;">Длина катета каждого из представленных выше треугольников равна одному сантиметру. За один такт видеокарта не может отобразить более чем ai треугольников i-того типа.</p>

<p style="user-select: auto !important;">Необходимо определить максимально возможную длину стороны квадрата, который может быть изображен видеокартой на экране монитора за один такт. При этом квадрат должен быть расположен так, чтобы его стороны были параллельны краям монитора.</p>

<p style="user-select: auto !important;">Требуется написать программу, которая решает поставленную задачу. </p>

### 입력 

 <p style="user-select: auto !important;">Первая строка входного файла содержит разделенные пробелами четыре целых числа: a<sub style="user-select: auto !important;">1</sub>, a<sub style="user-select: auto !important;">2</sub>, a<sub style="user-select: auto !important;">3</sub>, a<sub style="user-select: auto !important;">4</sub> (0 ≤ a<sub style="user-select: auto !important;">1</sub>, a<sub style="user-select: auto !important;">2</sub>, a<sub style="user-select: auto !important;">3</sub>, a<sub style="user-select: auto !important;">4</sub> ≤ 10<sup style="user-select: auto !important;">18</sup>). Входные данные могут превышать максимальные значения для 32 битного типа данных. </p>

### 출력 

 <p style="user-select: auto !important;">Выходной файл должен содержать одно число – максимально возможную длину стороны квадрата. </p>

