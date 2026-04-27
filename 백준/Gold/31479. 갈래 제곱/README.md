# [Gold II] 갈래 제곱 - 31479 

[문제 링크](https://www.acmicpc.net/problem/31479) 

### 성능 요약

메모리: 161500 KB, 시간: 1352 ms

### 분류

수학, 구현, 문자열, 파싱, 미적분학

### 제출 일자

2026년 04월 28일 00:43:33

### 문제 설명

<p>미적분을 하던 다익망가는 견딜 수 없는 난이도에 문득 '인테그랄($\int$)이 양갈래 미소녀가 아닐까?' 하는 망상에 빠져버렸다! 그리하여 다익망가는 망상의 힘으로 인테그랄 양을 만들어내게 되었다!</p>

<p>다익망가는 인테그랄 양의 탄생을 무척이나 좋아하였고, 인테그랄 양의 특성을 분석하기 시작했다. 인테그랄 양은 주변에 보이는 수식을 안아준다. 그리고 이 수식은 기쁨에 겨워 <strong>두 번 적분된다!!</strong> 우리는 이 기쁨에 겨운 수식을 양갈래를 적분한다는 의미로 <strong>양(</strong>$2$<strong>)갈래 → 갈래 제곱식</strong>이라고 부르기로 하였다.</p>

<p>인테그랄 양이 하는 적분은 부정적분이며, 두 번 적분한다는 것의 의미는 부정적분이 두 번 시행된다는 것을 의미한다. 즉, 처음 적분할 때 식은 주어지는 다항식을 적분한 결과 뒤에 적분 상수를 뜻하는 $C$가 추가되며, 두 번째 적분에서는 다른 적분 상수 $D$를 사용하여 적분됨을 나타낸다.</p>

<p>하지만 문제가 있다. 인테그랄 양이 수식을 껴안는 것을 너무나도 좋아하는 나머지, 원래의 수식을 알 수가 없다는 것이다! 결국 원래의 수식과 갈래 제곱식이 뒤죽박죽 섞여버렸고, 인테그랄 양은 죄책감에 우울해하고 있다.</p>

<p>다익망가는 인테그랄 양이 우울해하는 모습은 보고 싶지 않기에, 갈래 제곱식과 임의의 수식 하나를 골라 이 수식이 갈래 제곱식이 되기 전의 올바른 수식인지 구해보려고 한다. 하지만 다익망가는 "수학 시러!"를 외치며 도망가 버렸다!</p>

<p>당신은 다익망가가 내심 인테그랄 양을 도와주고 싶어한다는 사실을 알고 있다. 다익망가를 도와서 수식을 안았을 때 갈래 제곱식이 되는지 판별해보자!</p>

### 입력 

 <p>첫째 줄에 테스트 케이스의 개수 $T(1 \le T \le 100)$가 주어진다. 각각의 테스트 케이스마다 갈래 제곱식 $i$와 다익망가가 고른 임의의 다항식 $m$이 공백을 사이에 두고 주어진다.</p>

<p>$i$와 $m$은 다음과 같이 주어진다.</p>

<ul style="list-style-type:square;">
	<li>$i$를 나타내는 갈래 제곱식은 두번 부정적분된 식이다. 처음 적분될 때 나타나는 적분 상수를 $C$, 두 번째로 적분될 때 나타나는 적분 상수를 $D$로 표현하여 나타내며, $i$에 반드시 포함된다.</li>
	<li>$i$와 $m$은 <span style="color:#e74c3c;"><항><항><항><항>...<항></span>의 형식으로 주어진다. </li>
	<li><span style="color:#e74c3c;"><항></span>은 <span style="color:#e74c3c;"><부호><계수>x^<차수></span> 형식이다. 
	<ul>
		<li><span style="color:#e74c3c;"><차수></span>가 $0$인 경우 <span style="color:#e74c3c;">x^<차수></span>를 생략한다. </li>
		<li><span style="color:#e74c3c;"><차수></span>가 $1$인 경우 <span style="color:#e74c3c;">^<차수></span>를 생략한다. </li>
		<li><span style="color:#e74c3c;"><계수></span>가 $1$인 경우 <span style="color:#e74c3c;"><계수></span>를 생략한다. </li>
		<li>$i$와 $m$의 첫번째 항에서 <span style="color:#e74c3c;"><부호></span>가 <span style="color:#e74c3c;">+</span>인 경우 <span style="color:#e74c3c;"><부호></span>를 생략한다. </li>
		<li>$i$의 항에서 <span style="color:#e74c3c;"><계수></span>가 <span style="color:#e74c3c;">C</span>인 경우 <span style="color:#e74c3c;"><부호></span>는 <span style="color:#e74c3c;">+</span>, <span style="color:#e74c3c;"><차수></span>는 <span style="color:#e74c3c;">1</span>이다. </li>
		<li>$i$의 항에서 <span style="color:#e74c3c;"><계수></span>가 <span style="color:#e74c3c;">D</span>인 경우 <span style="color:#e74c3c;"><부호></span>는 <span style="color:#e74c3c;">+</span>, <span style="color:#e74c3c;"><차수></span>는 <span style="color:#e74c3c;">0</span>이다. </li>
		<li>이는 현재 다항식의 <span style="color:#e74c3c;"><차수></span>차 항의 계수가 <span style="color:#e74c3c;"><부호><계수></span>임을 나타낸다. </li>
	</ul>
	</li>
	<li><span style="color:#e74c3c;"><차수></span>는 $0$ 이상 $500$ 이하의 정수이다. 
	<ul>
		<li>$i$와 $m$의 항의 <span style="color:#e74c3c;"><차수></span>는 감소하는 순서로 주어진다. </li>
		<li>$i$와 $m$에서 한 다항식에 같은 <span style="color:#e74c3c;"><차수></span>를 가지는 두 항이 없다. </li>
	</ul>
	</li>
	<li><span style="color:#e74c3c;"><부호></span>는 <span style="color:#e74c3c;">+</span> 또는 <span style="color:#e74c3c;">-</span>이다. </li>
	<li><span style="color:#e74c3c;"><계수></span>는 $0$보다 큰 정수 또는 유리수, <span style="color:#e74c3c;">C</span> 또는 <span style="color:#e74c3c;">D</span>중 하나이다. 
	<ul>
		<li>$m$의 항에서 <span style="color:#e74c3c;"><계수></span>는 <span style="color:#e74c3c;">C</span>, <span style="color:#e74c3c;">D</span>가 아니다. </li>
		<li>$m$의 항에서 <span style="color:#e74c3c;"><계수></span>는 $124\,750\,000$ 이하이다. </li>
		<li>$i$의 항에서 <span style="color:#e74c3c;">C</span>, <span style="color:#e74c3c;">D</span>가 아닌 <span style="color:#e74c3c;"><계수></span>는 $500$ 이하이다. </li>
		<li><span style="color:#e74c3c;"><계수></span>가 유리수일때 <span style="color:#e74c3c;"><계수></span>는 <span style="color:#e74c3c;"><분자>/<분모> </span>형식으로 주어진다. 
		<ul>
			<li>$i$의 항에서 <span style="color:#e74c3c;"><분자></span>는 $1$ 이상 $500$ 이하의 정수이다. </li>
			<li>$m$의 항에서 <span style="color:#e74c3c;"><분자></span>는 $1$ 이상 $124\,750\,000$ 이하의 정수이다. </li>
			<li><span style="color:#e74c3c;"><분모></span>는 $2$ 이상 $500$ 이하의 정수이다. </li>
			<li><span style="color:#e74c3c;"><분자></span>와 <span style="color:#e74c3c;"><분모></span>의 최대공약수는 $1$이다. 즉, 기약분수이다. </li>
		</ul>
		</li>
	</ul>
	</li>
</ul>

### 출력 

 <p>각 테스트 케이스에 대해서 $i$의 원래 식이 $m$이라면 <span style="color:#e74c3c;">Yes</span>를 출력한다. 그렇지 않다면 <span style="color:#e74c3c;">No</span>를 출력한다.</p>

