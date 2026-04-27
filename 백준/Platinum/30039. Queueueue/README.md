# [Platinum V] Queueueue - 30039 

[문제 링크](https://www.acmicpc.net/problem/30039) 

### 성능 요약

메모리: 192340 KB, 시간: 1664 ms

### 분류

구현, 자료 구조, 많은 조건 분기, 덱, 연결 리스트

### 제출 일자

2026년 04월 28일 00:43:33

### 문제 설명

<p>지금까지 세상에 존재하지 않았던 새로운 자료구조 <strong>Queueueue</strong>를 소개한다. 자료구조 <strong>Queueueue</strong>는 가로 Queue와 세로 Queue로 구성되어 있으며, 두 Queue가 십자가로 겹친 형태이다. 즉, 원소 1개에 대해서 중간 지점을 공유하고 있다. <strong>Queueueue</strong>의 정확한 정의는 다음과 같다.</p>

<ul>
	<li>가로 Queue의 원소 개수를 $n_h$, 세로 Queue의 원소 개수를 $n_v$로 정의한다.</li>
	<li>가로 Queue의 $\left\lceil \frac{n_h}{2} \right\rceil$번째 원소와 세로 Queue의 $\left\lceil \frac{n_v}{2} \right\rceil$번째 원소는 서로 공유하는 같은 원소이다. 이 원소를 <strong>공유 원소</strong>라고 정의한다.</li>
	<li><strong>Queueueue</strong>는 명령을 수행하고 나서 매번 <strong>공유 원소</strong>를 새로 갱신한다.</li>
	<li>비어있는 <strong>Queueueue</strong>에는 <strong>공유 원소</strong>가 없다. 비어있는 <strong>Queueueue</strong>에 원소를 넣으면 그 원소가 <strong>공유 원소</strong>가 되며 $n_h = 1$, $n_v = 1$이다.
	<ul>
		<li>$n_h = 0$, $n_v = 0$인 경우를 제외하고 $n_h \times n_v = 0$인 경우는 없다. 따라서 <strong>Queueueue</strong>가 비어있지 않다면 항상 $n_h \ge 1$, $n_v \ge 1$이다.</li>
	</ul>
	</li>
</ul>

<p>처음에 <strong>Queueueue</strong>는 비어있으며 <strong>Queueueue</strong>는 다음 13가지 명령을 할 수 있다.</p>

<ul>
	<li><span style="color:#e74c3c;"><code>hpush x</code></span> : 가로 Queue의 맨 뒤에 정수 $x$를 넣는다. $(1 \le x \le 100\,000)$</li>
	<li><span style="color:#e74c3c;"><code>hpop</code></span> : 가로 Queue에 정수가 있다면 맨 앞에 있는 정수를 빼고 출력한다. 없다면 <span style="color:#e74c3c;"><code>-1</code></span>을 대신 출력한다.</li>
	<li><span style="color:#e74c3c;"><code>hfront</code></span> : 가로 Queue에 정수가 있다면 맨 앞에 있는 정수를 출력한다. 없다면 <span style="color:#e74c3c;"><code>-1</code></span>을 대신 출력한다.</li>
	<li><span style="color:#e74c3c;"><code>hback</code> </span>: 가로 Queue에 정수가 있다면 맨 뒤에 있는 정수를 출력한다. 없다면 <span style="color:#e74c3c;"><code>-1</code></span>을 대신 출력한다.</li>
	<li><span style="color:#e74c3c;"><code>hsize</code> </span>: 가로 Queue에 들어있는 정수의 개수를 출력한다.</li>
	<li><span style="color:#e74c3c;"><code>vpush x</code> </span>: 세로 Queue의 맨 뒤에 정수 $x$를 넣는다. $(1 \le x \le 100\,000)$</li>
	<li><span style="color:#e74c3c;"><code>vpop</code> </span>: 세로 Queue에 정수가 있다면 맨 앞에 있는 정수를 빼고 출력한다. 없다면 <span style="color:#e74c3c;"><code>-1</code></span>을 대신 출력한다.</li>
	<li><span style="color:#e74c3c;"><code>vfront</code> </span>: 세로 Queue에 정수가 있다면 맨 앞에 있는 정수를 출력한다. 없다면 <span style="color:#e74c3c;"><code>-1</code></span>을 대신 출력한다.</li>
	<li><span style="color:#e74c3c;"><code>vback</code> </span>: 세로 Queue에 정수가 있다면 맨 뒤에 있는 정수를 출력한다. 없다면 <span style="color:#e74c3c;"><code>-1</code></span>을 대신 출력한다.</li>
	<li><span style="color:#e74c3c;"><code>vsize</code> </span>: 세로 Queue에 들어있는 정수의 개수를 출력한다.</li>
	<li><span style="color:#e74c3c;"><code>size</code> </span>: <strong>Queueueue</strong>에 들어있는 정수의 개수를 출력한다.</li>
	<li><span style="color:#e74c3c;"><code>empty</code> </span>: <strong>Queueueue</strong>가 비어있으면 <span style="color:#e74c3c;"><code>1</code></span>, 아니면 <span style="color:#e74c3c;"><code>0</code></span>을 출력한다.</li>
	<li><span style="color:#e74c3c;"><code>middle</code> </span>: <strong>Queueueue</strong>에 정수가 있다면 <strong>Queueueue</strong>의 <strong>공유 원소</strong>에 해당하는 정수를 출력한다. 없다면 <span style="color:#e74c3c;"><code>-1</code></span>을 대신 출력한다.</li>
</ul>

### 입력 

 <p>첫 번째 줄에 명령의 수 $N$이 주어진다. $(1 \le N \le 2\,000\,000)$</p>

<p>두 번째 줄부터 $N$개의 줄에 걸쳐 명령이 하나씩 주어진다.</p>

### 출력 

 <p>출력을 요구하는 명령이 주어질 때마다, 명령의 결과를 한 줄에 하나씩 출력한다.</p>

