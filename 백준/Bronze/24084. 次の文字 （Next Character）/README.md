# [Bronze IV] 次の文字 (Next Character) - 24084 

[문제 링크](https://www.acmicpc.net/problem/24084) 

### 성능 요약

메모리: 127496 KB, 시간: 260 ms

### 분류

구현, 문자열

### 제출 일자

2024년 12월 21일 15:25:03

### 문제 설명

<p style="user-select: auto !important;">長さ <var style="user-select: auto !important;">N</var> の文字列 <var style="user-select: auto !important;">S</var> が与えられる．<var style="user-select: auto !important;">S</var> の各文字は <code style="user-select: auto !important;">J</code>，<code style="user-select: auto !important;">O</code>，<code style="user-select: auto !important;">I</code> のいずれかである．</p>

<p style="user-select: auto !important;">ビーバーのビ太郎は，<var style="user-select: auto !important;">N - 1</var> 回の動作を行った．<var style="user-select: auto !important;">i</var> 回目 (<var style="user-select: auto !important;">1 ≦ i ≦ N - 1</var>) の動作は，次のように行われた．</p>

<ul style="user-select: auto !important;">
	<li style="user-select: auto !important;"><var style="user-select: auto !important;">S</var> の <var style="user-select: auto !important;">i + 1</var> 文字目を確認する．さらに，<var style="user-select: auto !important;">S</var> の <var style="user-select: auto !important;">i + 1</var> 文字目が <code style="user-select: auto !important;">J</code> であったならば，<var style="user-select: auto !important;">S</var> の <var style="user-select: auto !important;">i</var> 文字目を黒板に書く．</li>
</ul>

<p style="user-select: auto !important;"><var style="user-select: auto !important;">N - 1</var> 回の動作においてビ太郎が黒板に書いたすべての文字を，ビ太郎が書いた順に改行区切りで出力せよ．</p>

### 입력 

 <p style="user-select: auto !important;">入力は以下の形式で標準入力から与えられる．</p>

<pre style="user-select: auto !important;"><var style="user-select: auto !important;">N</var>
<var style="user-select: auto !important;">S</var></pre>

### 출력 

 <p style="user-select: auto !important;"><var style="user-select: auto !important;">N - 1</var> 回の動作においてビ太郎が黒板に書いたすべての文字を，ビ太郎が書いた順に改行区切りで出力せよ．</p>

