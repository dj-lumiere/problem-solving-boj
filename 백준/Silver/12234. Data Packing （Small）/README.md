# [Silver IV] Data Packing (Small) - 12234 

[문제 링크](https://www.acmicpc.net/problem/12234) 

### 성능 요약

메모리: 128156 KB, 시간: 224 ms

### 분류

정렬, 두 포인터

### 제출 일자

2024년 12월 25일 18:22:27

### 문제 설명

<p style="user-select: auto !important;">Adam, being a well-organized man, has always been keenly interested in organizing all his stuff. In particular, he fondly remembers the many hours of his youth that were spent moving files from his computer onto Compact Discs.</p>

<p style="user-select: auto !important;">There were two very important rules involved in this procedure. First, in order to ensure that all discs could be labeled clearly, Adam would never place more than two files on the same disc. Second, he would never divide a single file over multiple discs. Happily, the discs he was using were always large enough to make this possible.</p>

<p style="user-select: auto !important;">Thinking back, Adam is now wondering whether he arranged his files in the best way, or whether he ended up wasting some Compact Discs. He will provide you with the capacity of the discs he used (all his discs had the same capacity) as well as a list of the sizes of the files that he stored. Please help Adam out by determining the minimum number of discs needed to store all his files—following the two very important rules, of course.</p>

### 입력 

 <p style="user-select: auto !important;">The first line of the input gives the number of test cases, <strong style="user-select: auto !important;">T</strong>. <strong style="user-select: auto !important;">T</strong> test cases follow. Each test case begins with a line containing two integers: the number of files to be stored <strong style="user-select: auto !important;">N</strong>, and the capacity of the discs to be used <strong style="user-select: auto !important;">X</strong> (in MBs). The next line contains the <strong style="user-select: auto !important;">N</strong> integers representing the sizes of the files <strong style="user-select: auto !important;">S</strong><strong style="user-select: auto !important;"><sub style="user-select: auto !important;">i</sub></strong> (in MBs), separated by single spaces.</p>

<p style="user-select: auto !important;">Limits</p>

<ul style="user-select: auto !important;">
	<li style="user-select: auto !important;">1 ≤ <strong style="user-select: auto !important;">T</strong> ≤ 100.</li>
	<li style="user-select: auto !important;">1 ≤ <strong style="user-select: auto !important;">X</strong> ≤ 700.</li>
	<li style="user-select: auto !important;">1 ≤ <strong style="user-select: auto !important;">S</strong><strong style="user-select: auto !important;"><sub style="user-select: auto !important;">i</sub></strong> ≤ X.</li>
	<li style="user-select: auto !important;"><span style="line-height: 1.6em; user-select: auto !important;">1 ≤ </span><strong style="line-height: 1.6em; user-select: auto !important;">N</strong><span style="line-height: 1.6em; user-select: auto !important;"> ≤ 10.</span></li>
</ul>

### 출력 

 <p style="user-select: auto !important;">For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is the minimum number of discs needed to store the given files.</p>

