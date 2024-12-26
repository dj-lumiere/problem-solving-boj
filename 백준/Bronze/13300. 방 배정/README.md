# [Bronze II] 방 배정 - 13300 

[문제 링크](https://www.acmicpc.net/problem/13300) 

### 성능 요약

메모리: 128152 KB, 시간: 248 ms

### 분류

구현, 수학

### 제출 일자

2024년 12월 26일 11:08:49

### 문제 설명

<p style="user-select: auto !important;">정보 초등학교에서는 단체로 2박 3일 수학여행을 가기로 했다. 여러 학년이 같은 장소로 수학여행을 가려고 하는데 1학년부터 6학년까지 학생들이 묵을 방을 배정해야 한다. 남학생은 남학생끼리, 여학생은 여학생끼리 방을 배정해야 한다. 또한 한 방에는 같은 학년의 학생들을 배정해야 한다. 물론 한 방에 한 명만 배정하는 것도 가능하다.</p>

<p style="user-select: auto !important;">한 방에 배정할 수 있는 최대 인원 수 K가 주어졌을 때, 조건에 맞게 모든 학생을 배정하기 위해 필요한 방의 최소 개수를 구하는 프로그램을 작성하시오.</p>

<p style="user-select: auto !important;">예를 들어, 수학여행을 가는 학생이 다음과 같고 K = 2일 때 12개의 방이 필요하다. 왜냐하면 3학년 남학생을 배정하기 위해 방 두 개가 필요하고 4학년 여학생에는 방을 배정하지 않아도 되기 때문이다.</p>

<table class="table table-bordered table-center-30" style="user-select: auto !important;">
	<thead style="user-select: auto !important;">
		<tr style="user-select: auto !important;">
			<th style="user-select: auto !important;">학년</th>
			<th style="user-select: auto !important;">여학생</th>
			<th style="user-select: auto !important;">남학생</th>
		</tr>
	</thead>
	<tbody style="user-select: auto !important;">
		<tr style="user-select: auto !important;">
			<td style="user-select: auto !important;">1학년</td>
			<td style="user-select: auto !important;">영희</td>
			<td style="user-select: auto !important;">동호, 동진</td>
		</tr>
		<tr style="user-select: auto !important;">
			<td style="user-select: auto !important;">2학년</td>
			<td style="user-select: auto !important;">혜진, 상희</td>
			<td style="user-select: auto !important;">경수</td>
		</tr>
		<tr style="user-select: auto !important;">
			<td style="user-select: auto !important;">3학년</td>
			<td style="user-select: auto !important;">경희</td>
			<td style="user-select: auto !important;">동수, 상철, 칠복</td>
		</tr>
		<tr style="user-select: auto !important;">
			<td style="user-select: auto !important;">4학년</td>
			<td style="user-select: auto !important;"> </td>
			<td style="user-select: auto !important;">달호</td>
		</tr>
		<tr style="user-select: auto !important;">
			<td style="user-select: auto !important;">5학년</td>
			<td style="user-select: auto !important;">정숙</td>
			<td style="user-select: auto !important;">호동, 건우</td>
		</tr>
		<tr style="user-select: auto !important;">
			<td style="user-select: auto !important;">6학년</td>
			<td style="user-select: auto !important;">수지</td>
			<td style="user-select: auto !important;">동건</td>
		</tr>
	</tbody>
</table>

### 입력 

 <p style="user-select: auto !important;">표준 입력으로 다음 정보가 주어진다. 첫 번째 줄에는 수학여행에 참가하는 학생 수를 나타내는 정수 N(1 ≤ N ≤ 1,000)과 한 방에 배정할 수 있는 최대 인원 수 K(1 < K ≤ 1,000)가 공백으로 분리되어 주어진다. 다음 N 개의 각 줄에는 학생의 성별 S와 학년 Y(1 ≤ Y ≤ 6)가 공백으로 분리되어 주어진다. 성별 S는 0, 1중 하나로서 여학생인 경우에 0, 남학생인 경우에 1로 나타낸다. </p>

### 출력 

 <p style="user-select: auto !important;">표준 출력으로 학생들을 모두 배정하기 위해 필요한 최소한의 방의 수를 출력한다.</p>

