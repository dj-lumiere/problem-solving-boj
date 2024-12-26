# [Silver IV] 배열 전체 탐색하기 - 26168 

[문제 링크](https://www.acmicpc.net/problem/26168) 

### 성능 요약

메모리: 165772 KB, 시간: 392 ms

### 분류

이분 탐색, 정렬

### 제출 일자

2024년 12월 26일 11:05:04

### 문제 설명

<p style="user-select: auto !important;">크기 <em style="user-select: auto !important;">n</em>인 정수형 배열 <em style="user-select: auto !important;">A</em>가 주어진다. 배열 <em style="user-select: auto !important;">A</em>의 원소는 <em style="user-select: auto !important;">A</em>[0], <em style="user-select: auto !important;">A</em>[1], ... , <em style="user-select: auto !important;">A</em>[<em style="user-select: auto !important;">n</em>-1]이다. 배열 <em style="user-select: auto !important;">A</em>에는 같은 값을 갖는 원소가 여러 개 존재할 수 있다. 배열 <em style="user-select: auto !important;">A</em>에 대한 <em style="user-select: auto !important;">m</em>개의 질의가 저장된 배열 <em style="user-select: auto !important;">B</em>가 주어진다. 배열 <em style="user-select: auto !important;">B</em>에 저장된 <em style="user-select: auto !important;">m</em>개의 질의는 아래 세 가지 유형으로 구분된다. 첫 번째가 유형 1, 두 번째가 유형 2, 세 번째가 유형 3이다.</p>

<ul style="user-select: auto !important;">
	<li style="user-select: auto !important;">1 <em style="user-select: auto !important;">k</em>: 배열 <em style="user-select: auto !important;">A</em>의 원소 중 <em style="user-select: auto !important;">k</em>보다 크거나 같은 원소의 개수를 출력한다.</li>
	<li style="user-select: auto !important;">2 <em style="user-select: auto !important;">k</em>: 배열 <em style="user-select: auto !important;">A</em>의 원소 중 <em style="user-select: auto !important;">k</em>보다 큰 원소의 개수를 출력한다.</li>
	<li style="user-select: auto !important;">3 <em style="user-select: auto !important;">i</em> <em style="user-select: auto !important;">j</em>: 배열 <em style="user-select: auto !important;">A</em>의 원소 중 <em style="user-select: auto !important;">i</em>보다 크거나 같고 <em style="user-select: auto !important;">j</em>보다 작거나 같은 원소의 개수를 출력한다.</li>
</ul>

<p style="user-select: auto !important;">배열 <em style="user-select: auto !important;">B</em>에 저장된 첫 번째 질의부터 <em style="user-select: auto !important;">m</em>번째 질의까지 순서대로 처리하면서 질의 결과를 출력하자.</p>

### 입력 

 <p style="user-select: auto !important;">첫 번째 줄에 <em style="user-select: auto !important;">n</em>과 <em style="user-select: auto !important;">m</em>이 공백을 사이에 두고 순서대로 주어진다.</p>

<p style="user-select: auto !important;">두 번째 줄에 배열 <em style="user-select: auto !important;">A</em>의 원소 <em style="user-select: auto !important;">A</em>[0], <em style="user-select: auto !important;">A</em>[1], ... , <em style="user-select: auto !important;">A</em>[<em style="user-select: auto !important;">n</em>-1]이 공백을 사이에 두고 순서대로 주어진다.</p>

<p style="user-select: auto !important;">세 번째 줄부터 <em style="user-select: auto !important;">m</em>개의 줄에 걸쳐 배열 <em style="user-select: auto !important;">B</em>에 저장된 m개의 질의가 순서대로 주어진다. 한 줄에 하나의 질의를 나타내는 정수가 공백을 사이에 두고 순서대로 주어진다.</p>

### 출력 

 <p style="user-select: auto !important;">첫 번째 줄부터 질의 결과를 순서대로 한 줄씩 출력한다.</p>

