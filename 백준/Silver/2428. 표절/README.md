# [Silver III] 표절 - 2428 

[문제 링크](https://www.acmicpc.net/problem/2428) 

### 성능 요약

메모리: 142228 KB, 시간: 252 ms

### 분류

이분 탐색, 정렬

### 제출 일자

2024년 12월 26일 11:42:49

### 문제 설명

<p style="user-select: auto !important;">세계적인 석유 재벌 "규현 조 압둘 티크리티 안드레스 후세인 리오넬 솔레르 살라 마리우 두스 산투스 펠리스 빈 자이드 술탄 친나왓 뱅거 7세"는 1등 상품으로 페라리를 걸고 프로그래밍 대회를 개최했다. 이 대회의 참석자는 총 N명이고 각각 솔루션 파일 1개를 제출했다. 이 솔루션 파일을 F<sub style="user-select: auto !important;">1</sub>, F<sub style="user-select: auto !important;">2</sub>, ..., F<sub style="user-select: auto !important;">n</sub>이라고 한다.</p>

<p style="user-select: auto !important;">채점 결과를 발표하기 전에, 남의 것을 배낀 사람이 있는지 찾아내려고 한다. 이 대회의 주최측은 두 파일을 비교해서 너무 비슷한지 아닌지 판별하는 프로그램이 있다.</p>

<p style="user-select: auto !important;">하지만, 제출한 파일의 개수가 너무 많아서, 모든 쌍을 검사한다면, 2012년 지구가 멸망할 때 까지도 검사를 해야할 판이다. 따라서, 파일 크기가 너무 다른 경우에는 그러한 쌍을 검사하지 않고 넘어가기로 했다.</p>

<p style="user-select: auto !important;">좀더 정확하게 하기 위해서, 대회의 심판들은 두 파일이 있을 때, 작은 파일의 크기가 큰 파일 크기의 90%보다도 작을 때는, 이러한 쌍은 검사하지 않고 넘어가기로 했다. 따라서, (F<sub style="user-select: auto !important;">i</sub>, F<sub style="user-select: auto !important;">j</sub>) 쌍을 검사해야 하는데, 이때, i≠j이고, size(F<sub style="user-select: auto !important;">i</sub>) ≤ size(F<sub style="user-select: auto !important;">j</sub>)이면서, size(F<sub style="user-select: auto !important;">i</sub>) ≥ 0.9 × size(F<sub style="user-select: auto !important;">j</sub>)인 쌍만 검사하려고 한다.</p>

<p style="user-select: auto !important;">몇 개의 쌍을 검사해야 하는 지 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p style="user-select: auto !important;">첫째 줄에 제출한 솔루션의 개수 N이 주어진다. 둘째 줄에는 각 솔루션 파일의 크기 size(F<sub style="user-select: auto !important;">1</sub>), size(F<sub style="user-select: auto !important;">2</sub>), ..., size(F<sub style="user-select: auto !important;">N</sub>)이 주어진다. (1 ≤ N ≤ 100,000, 1 ≤ size(F<sub style="user-select: auto !important;">i</sub>) ≤ 100,000,000) 솔루션 파일의 크기는 정수이다.</p>

### 출력 

 <p style="user-select: auto !important;">첫째 줄에 검사해야 하는 파일의 개수를 출력한다.</p>

