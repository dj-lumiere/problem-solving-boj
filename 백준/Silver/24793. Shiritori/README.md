# [Silver IV] Shiritori - 24793 

[문제 링크](https://www.acmicpc.net/problem/24793) 

### 성능 요약

메모리: 176320 KB, 시간: 320 ms

### 분류

자료 구조, 해시를 사용한 집합과 맵, 구현, 문자열

### 제출 일자

2024년 12월 28일 10:52:53

### 문제 설명

<figure style="width: 300px; float: right; user-select: auto !important;"><img alt="" src="https://upload.acmicpc.net/4bb02293-8500-44da-b67f-44f0bf4a7cde/-/preview/" style="width: 300px; height: 302px; user-select: auto !important;">
<figcaption style="user-select: auto !important;">The original version of Shiritori is played using Japanese hiragana, katakana, or kanji characters. Source <a href="https://commons.wikimedia.org/wiki/File:Shiritori.png" style="user-select: auto !important;">WikiMedia</a></figcaption>
</figure>

<p style="user-select: auto !important;">The Japanese game of Shiritori is the perfect game for a long car ride. The rules are simple: the first player picks any word to say, then the second player must choose a new word that begins with the last letter of the word that the first player just said. Your job is to determine if the game was played according to these rules, given a history of the words used in a particular game. In a game, player $1$ always starts first.</p>

### 입력 

 <p style="user-select: auto !important;">Input consists of one test case that begins with an integer $N$ ($2 \leq N \leq 100\,000$) on a single line.  Each of the following $N$ lines contains $1$ word.  The words are presented in the order in which the players called them out, starting with player $1$. All words consist of between $1$ and $120$ lowercase English letters.</p>

### 출력 

 <p style="user-select: auto !important;">If the game was played according to the rules, output "<code style="user-select: auto !important;">Fair Game</code>". Otherwise, find out which player first violated the rules of the game.  That player lost the game, so output "<code style="user-select: auto !important;">Player <i> lost</code>". For example, if player $1$ violated the rules first, output "<code style="user-select: auto !important;">Player 1 lost</code>".</p>

