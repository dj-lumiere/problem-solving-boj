# [Bronze III] Counting Peaks of Infection - 25527 

[문제 링크](https://www.acmicpc.net/problem/25527) 

### 성능 요약

메모리: 131016 KB, 시간: 256 ms

### 분류

구현

### 제출 일자

2024년 12월 11일 10:04:32

### 문제 설명

<p style="user-select: auto !important;">For the new infectious disease, COVID-99, numbers of new positive cases of PCR tests conducted in the city are reported daily. You are requested by the municipal public relations department to write a program that counts the number of the peaks so far of the positive cases.</p>

<p style="user-select: auto !important;">Here, the number of peaks is the number of days on which the number of positive cases reported is more than both of the day before and the next day.</p>

<p style="user-select: auto !important;">As the PCR tests started before the disease started spreading in the city, the number of positive cases is zero on the first day. The last reported day is not counted as a peak. No two consecutive days have the same number of positive cases.</p>

<p style="text-align: center; user-select: auto !important;"><img alt="" src="https://upload.acmicpc.net/4434ac32-a66c-4775-b7f4-1974091990a1/-/preview/" style="user-select: auto !important;"></p>

<p style="text-align: center; user-select: auto !important;">Figure A-1: Numbers of positive cases of the last dataset in Sample Input. Red circles indicate the peaks.</p>

### 입력 

 <p style="user-select: auto !important;">The input consists of multiple datasets. Each dataset is in the following format.</p>

<pre style="user-select: auto !important;"><var style="user-select: auto !important;">n</var>
<var style="user-select: auto !important;">v</var><sub style="user-select: auto !important;">1</sub> ... <var style="user-select: auto !important;">v</var><sub style="user-select: auto !important;"><var style="user-select: auto !important;">n</var></sub></pre>

<p style="user-select: auto !important;"><var style="user-select: auto !important;">n</var> is the number of days on which the numbers of positive cases are reported (3 ≤ <var style="user-select: auto !important;">n</var> ≤ 1000). <var style="user-select: auto !important;">v</var><sub style="user-select: auto !important;"><var style="user-select: auto !important;">i</var></sub> is the number of positive cases on the <var style="user-select: auto !important;">i</var>-th day, an integer between zero and 1000, inclusive. Note that <var style="user-select: auto !important;">v</var><sub style="user-select: auto !important;">1</sub> is zero, and <var style="user-select: auto !important;">v</var><sub style="user-select: auto !important;"><var style="user-select: auto !important;">i</var></sub> ≠ <var style="user-select: auto !important;">v</var><sub style="user-select: auto !important;"><var style="user-select: auto !important;">i</var>+1</sub> for 1 ≤ <var style="user-select: auto !important;">i</var> < <var style="user-select: auto !important;">n</var>, as stated above.</p>

<p style="user-select: auto !important;">The end of the input is indicated by a line containing a zero. The input consists of at most 100 datasets.</p>

### 출력 

 <p style="user-select: auto !important;">For each dataset, output the number of peaks in a line.</p>

