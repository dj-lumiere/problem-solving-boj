# [Gold III] Append Sort - 22890 

[문제 링크](https://www.acmicpc.net/problem/22890) 

### 성능 요약

메모리: 129240 KB, 시간: 300 ms

### 분류

임의 정밀도 / 큰 수 연산, 그리디 알고리즘

### 제출 일자

2024년 10월 23일 14:54:08

### 문제 설명

<p>We have a list of integers X<sub>1</sub>, X<sub>2</sub>, …, X<sub>N</sub>. We would like them to be in strictly increasing order, but unfortunately, we cannot reorder them. This means that usual sorting algorithms will not work.</p>

<p>Our only option is to change them by appending digits 0 through 9 to their right (in base 10). For example, if one of the integers is 10, you can turn it into 10<strong>0</strong> or 10<strong>9</strong> with a single append operation, or into 10<strong>34</strong> with two operations (as seen in the image below).</p>

<p>Given the current list, what is the minimum number of single digit append operations that are necessary for the list to be in strictly increasing order?</p>

<p>For example, if the list is 100,7,10, we can use 4 total operations to make it into a sorted list, as the following image shows.</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/c9b1174d-0a57-4144-8c01-d691ac7c0da1/-/preview/"></p>

### 입력 

 <p>The first line of the input gives the number of test cases, T. T test cases follow. Each test case is described in two lines. The first line of a test case contains a single integer N, the number of integers in the list. The second line contains N integers X<sub>1</sub>, X<sub>2</sub>, …, X<sub>N</sub>, the members of the list.</p>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where x is the test case number (starting from 1) and y is the minimum number of single digit append operations needed for the list to be in strictly increasing order.</p>

