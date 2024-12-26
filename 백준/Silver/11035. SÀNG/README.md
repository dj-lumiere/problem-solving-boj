# [Silver III] SÀNG - 11035 

[문제 링크](https://www.acmicpc.net/problem/11035) 

### 성능 요약

메모리: 128156 KB, 시간: 232 ms

### 분류

수학, 정수론, 소수 판정, 에라토스테네스의 체

### 제출 일자

2024년 12월 26일 11:01:51

### 문제 설명

<p style="user-select: auto !important;">Sàng của Eratosthenes là thuật toán nổi tiếng để tìm tất cả các số nguyên tố nhỏ hơn N. Thuật toán như sau: </p>

<ol style="user-select: auto !important;">
	<li style="user-select: auto !important;">Ghi ra tất cả các số nguyên giữa 2 và N. </li>
	<li style="user-select: auto !important;">Tìm số nhỏ nhất chưa bị gạch và gọi nó là P (P là số nguyên tố). </li>
	<li style="user-select: auto !important;">Gạch bỏ P và tất cả các bội số của nó mà chưa bị gạch. </li>
	<li style="user-select: auto !important;">Nếu còn số chưa bị gạch bỏ, chuyển sang bước 2. </li>
</ol>

<p style="user-select: auto !important;">Viết một chương trình, cho N và K, tìm số nguyên thứ K bị gạch.</p>

### 입력 

 <p style="user-select: auto !important;">Gồm nhiều bộ test, mỗi bộ test nằm trên một dòng gồm các số nguyên N và K (2 ≤ K < N ≤ 1000). </p>

### 출력 

 <p style="user-select: auto !important;">Với mỗi test, in ra trên một dòng số thứ K bị gạch bỏ.</p>

