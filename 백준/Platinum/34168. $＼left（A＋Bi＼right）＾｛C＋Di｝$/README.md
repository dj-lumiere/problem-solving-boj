# [Platinum III] $\left(A+Bi\right)^{C+Di}$ - 34168 

[문제 링크](https://www.acmicpc.net/problem/34168) 

### 성능 요약

메모리: 142660 KB, 시간: 244 ms

### 분류

수학, 조합론, 많은 조건 분기

### 제출 일자

2026년 04월 28일 00:43:33

### 문제 설명

<p>동우와 하늘이, 주영이는 과거 복소해석학 과목을 듣고 감명받았다. 이에 무슨 과목을 들을지 고민하던 민재에게 복소해석학 과목을 들으라고 추천해 주었다. 예습도 할 겸 대학원까지 수학과로 간 세준이에게 $\left( A+Bi \right)^{C+Di}$의 값을 구하는 방법을 물어보았다.</p>

<p>세준이는 고등학교만 졸업했어도 알고 있을 지식을 왜 모르냐며 화를 냈다. 컴퓨터만 하다가 $0$과 $1$ 말고 아무것도 알지 못하게 된 민재를 위해 다음 식을 알려주었다.</p>

<p>먼저 실수 $x,y$에 대해 $\operatorname{Arg}\left( x+iy \right) =\operatorname{atan2}\left( y,x \right) =\begin{cases}\arctan\left( \frac yx \right)&\text{if } x>0,\\\arctan\left( \frac yx \right) +\pi&\text{if } x<0\text{ and } y\ge 0,\\\arctan\left( \frac yx \right) -\pi&\text{if } x<0\text{ and } y<0,\\ +\frac{\pi}{2}&\text{if } x=0\text{ and } y>0,\\ -\frac{\pi}{2}&\text{if } x=0\text{ and } y<0,\\\text{undefined}&\text{if } x=0\text{ and } y=0.\end{cases}$인데, 그냥 편의상 $x=y=0$일 때 $\operatorname{Arg}\left( x+iy \right) =0$이라고 하자. 그럼 일반적인 경우에 다음 식이 성립해.</p>

<p>\[\left( A+Bi \right)^{C+Di}=\left( \sqrt{A^2+B^2} \right)^{C+Di}\exp\left( {\left( -D+Ci \right)\operatorname{Arg}\left( A+Bi \right)} \right)\]</p>

<p>단, 다음 두 가지 중 하나 이상 적용되는 예외 상황에서는 수가 정의되지 않아.</p>

<ul>
	<li>$A=B=0$이고, $D\ne 0$</li>
	<li>$A=B=0$이고, $C\le 0$</li>
</ul>

<p>나머지 식 계산 중 필요한 것은 $\exp\left( {ix} \right) =\cos{x} +i\sin{x}$만 알면 모든 것을 계산할 수 있어.</p>

<p>민재가 잘 이해했는지 궁금했던 세준이는 다음과 같은 질문을 했다.</p>

<p>정수 $A,B$가 주어질 때, $\left( A+Bi \right)^{C+Di}$의 값을 실수로 만드는 순서쌍 $\left( C,D \right)$의 개수를 구해봐. 단, 답이 무한할 수 있으니 $C$와 $D$는 절댓값이 $M$ 이하인 정수로만 한정하고, 답이 너무 커질 수 있으니 $998\, 244\, 353$으로 나눈 나머지를 구해봐.</p>

<p>단, 정의되지 않는 수는 실수가 아니라고 가정한다.</p>

### 입력 

 <p>첫 번째 줄에 테스트 케이스의 개수 $T(1\le T\le 10^5)$이 주어진다.</p>

<p>두 번째 줄부터 $T$개의 줄에 걸쳐 정수 $A,B,M(0\le A,B,M\le 10^{18})$이 공백으로 구분되어 주어진다.</p>

### 출력 

 <p>각 테스트 케이스 별로 정답을 $998\, 244\, 353$으로 나눈 나머지를 출력한다.</p>

