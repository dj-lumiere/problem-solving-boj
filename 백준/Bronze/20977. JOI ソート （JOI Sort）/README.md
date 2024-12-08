# [Bronze II] JOI ソート (JOI Sort) - 20977 

[문제 링크](https://www.acmicpc.net/problem/20977) 

### 성능 요약

메모리: 126568 KB, 시간: 224 ms

### 분류

구현, 정렬, 문자열

### 제출 일자

2024년 12월 8일 23:34:08

### 문제 설명

<p style="user-select: auto !important;">長さ <var style="user-select: auto !important;">N</var> の文字列 <var style="user-select: auto !important;">S</var> が与えられる．<var style="user-select: auto !important;">S</var> の各文字は ‘<code style="user-select: auto !important;">J</code>’，‘<code style="user-select: auto !important;">O</code>’，‘<code style="user-select: auto !important;">I</code>’ のいずれかである．</p>

<p style="user-select: auto !important;">あなたは <var style="user-select: auto !important;">S</var> の文字を並び替えて次の条件を満たすようにしたい．</p>

<ul style="user-select: auto !important;">
	<li style="user-select: auto !important;">すべての文字 ‘<code style="user-select: auto !important;">J</code>’ と文字 ‘<code style="user-select: auto !important;">O</code>’ の組について ‘<code style="user-select: auto !important;">J</code>’ が ‘<code style="user-select: auto !important;">O</code>’ よりも前にある．</li>
	<li style="user-select: auto !important;">すべての文字 ‘<code style="user-select: auto !important;">O</code>’ と文字 ‘<code style="user-select: auto !important;">I</code>’ の組について ‘<code style="user-select: auto !important;">O</code>’ が ‘<code style="user-select: auto !important;">I</code>’ よりも前にある．</li>
	<li style="user-select: auto !important;">すべての文字 ‘<code style="user-select: auto !important;">J</code>’ と文字 ‘<code style="user-select: auto !important;">I</code>’ の組について ‘<code style="user-select: auto !important;">J</code>’ が ‘<code style="user-select: auto !important;">I</code>’ よりも前にある．</li>
</ul>

<p style="user-select: auto !important;">文字列 <var style="user-select: auto !important;">S</var> が与えられたとき，上の条件を満たすように <var style="user-select: auto !important;">S</var> の文字を並び替えた文字列を出力するプログラムを作成せよ．</p>

### 입력 

 <p style="user-select: auto !important;">入力は以下の形式で標準入力から与えられる．</p>

<p style="user-select: auto !important;"><var style="user-select: auto !important;">N</var><br style="user-select: auto !important;">
<var style="user-select: auto !important;">S</var></p>

### 출력 

 <p style="user-select: auto !important;">条件を満たすように <var style="user-select: auto !important;">S</var> の文字を並び替えた文字列を出力せよ．</p>

