# [Bronze I] 사토르 마방진 - 20112 

[문제 링크](https://www.acmicpc.net/problem/20112) 

### 성능 요약

메모리: 127492 KB, 시간: 228 ms

### 분류

구현, 문자열

### 제출 일자

2024년 12월 24일 09:45:39

### 문제 설명

<p style="user-select: auto !important;">사토르 마방진에 대해 들어본 적이 있는가? 사토르 마방진은 간단히 말하면 "가로로 읽었을 때와 세로로 읽었을 때 똑같이 읽히는 단어 집합"이다. 예시로는 다음과 같은 것들이 있다.</p>

<pre style="user-select: auto !important;">라팔아
팔렸니
아니오</pre>

<pre style="user-select: auto !important;">호반우
반기는
우는나</pre>

<p style="user-select: auto !important;">술을 좋아하는 드립이는 전날 과음한 나머지 수학 수업 시간에 졸다가 선생님에게 걸려버렸고, 단어 집합들이 사토르 마방진인지 아닌지 판단해야 하는 숙제를 받았다.</p>

<p style="user-select: auto !important;">하지만 <em style="user-select: auto !important;">N</em> × <em style="user-select: auto !important;">N</em> 크기의 큰 단어 집합이 사토르 마방진인지 눈으로 확인하는 것은 쉽지 않았다.</p>

<p style="user-select: auto !important;">불쌍한 드립이는 숙제를 다 끝내기 전까지 집에 갈 수 없다. <em style="user-select: auto !important;">N</em> × <em style="user-select: auto !important;">N</em> 크기의 단어 집합이 주어지면, 주어진 단어 집합이 사토르 마방진인지 아닌지 판단하는 프로그램을 작성하자.</p>

<p style="user-select: auto !important;">드립이를 도와주자!</p>

### 입력 

 <p style="user-select: auto !important;">첫째 줄에 단어의 길이 <em style="user-select: auto !important;">N</em>이 주어진다. (2 ≤ <em style="user-select: auto !important;">N</em> ≤ 100)</p>

<p style="user-select: auto !important;">둘째 줄부터 <em style="user-select: auto !important;">N</em>개의 줄에 걸쳐 단어 집합의 각 행의 단어들이 공백 없이 주어진다. 단어들은 알파벳 대문자로만 이루어져 있다.</p>

### 출력 

 <p style="user-select: auto !important;">주어진 단어 집합이 사토르 마방진이면 "<code style="user-select: auto !important;">YES</code>", 아니면 "<code style="user-select: auto !important;">NO</code>"를 출력한다. (따옴표 제외)</p>

