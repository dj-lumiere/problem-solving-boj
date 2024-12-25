# [Silver III] MULTIGRAM - 11875 

[문제 링크](https://www.acmicpc.net/problem/11875) 

### 성능 요약

메모리: 128848 KB, 시간: 252 ms

### 분류

브루트포스 알고리즘, 구현, 문자열

### 제출 일자

2024년 12월 25일 21:14:07

### 문제 설명

<p>Pero is a passionate lover of riddles. The newest type of riddles he has come across requires the solver to check whether the given word is a multigram.</p>

<p>A multigram is a word that consists of concatenating two or more words that are all mutually anagrams. The first of these words is called the root of the multigram. For instance, the word bbabab is a multigram with the root bba because it consists of anagrams bba and bab.</p>

<p>Help Pero solve the riddle by determining whether his word is a multigram and determining its root in case it is. If there are multiple possible roots of the multigram, output the shortest.</p>

<p>Please note: Two words are mutually anagrams if one of them can be obtained from the other by changing the letter order.</p>

### 입력 

 <p>The first and only line of input contains a word of length at most 100 000 lowercase English characters.</p>

### 출력 

 <p>If the given word is not a multigram, output −1.</p>

<p>Otherwise, output the shortest root of the given word in one line.</p>

