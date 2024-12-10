# [Bronze II] Zliczacz liter - 8635 

[문제 링크](https://www.acmicpc.net/problem/8635) 

### 성능 요약

메모리: 128204 KB, 시간: 228 ms

### 분류

구현, 문자열

### 제출 일자

2024년 12월 10일 23:50:06

### 문제 설명

<p style="user-select: auto !important;">Koło Młodych Miłośników Łamania Szyfrów pracuje nad oprogramowaniem służącym do odszyfrowania pewnego starożytnego manuskryptu. Jądrem systemu zostanie samouczący się analizator tekstu, a jego pierwszym modułem "zliczacz liter", którego opracowanie powierzono Tobie.</p>

<p style="user-select: auto !important;">Opracuj program, który:</p>

<ul style="user-select: auto !important;">
	<li style="user-select: auto !important;">wczyta ze standardowego wejścia tekst do analizy,</li>
	<li style="user-select: auto !important;">dla każdej litery obliczy liczbę jej wystąpień w tekście,</li>
	<li style="user-select: auto !important;">wypisze wynik na standardowe wyjście.</li>
</ul>

### 입력 

 <p style="user-select: auto !important;">W pierwszym wierszu wejścia znajduje się liczba $N$, oznaczająca liczbę wierszy tekstu do analizy ($N ≤ 150$). W każdym z następujących $N$ znajduje się ciąg złożony z maksymalnie $200$ znaków spośród małych i wielkich liter alfabetu łacińskiego ('a'..'z', 'A'..'Z') oraz spacji.</p>

### 출력 

 <p style="user-select: auto !important;">W kolejnych wierszach należy wypisywać litery od 'a' do 'z' i od 'A' do 'Z' (w tej kolejności), pojedyncza˛ spację oraz liczbę oznaczającą ilość wystąpień tej litery w analizowanym tekście. Litery nie występujące w tekście należy pominąć.</p>

