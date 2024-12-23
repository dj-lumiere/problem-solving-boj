# [Bronze III] Blueberry Waffle - 27566 

[문제 링크](https://www.acmicpc.net/problem/27566) 

### 성능 요약

메모리: 127496 KB, 시간: 232 ms

### 분류

사칙연산, 수학

### 제출 일자

2024년 12월 23일 09:20:47

### 문제 설명

<p>You are using a waffle maker machine to make a delicious blueberry waffle. One side of your waffle is covered in blueberries, while the other side is plain. Initially, the cooking pan of the waffle maker lies horizontally, and the blueberries are on the top side of the waffle. Once started, the cooking pan will rotate at a constant speed for a fixed duration, then stop. The cooking time is set so that when the waffle maker stops, the cooking pan will not be in a vertical position.</p>

<p>If the cooking pan is not horizontal after this time, the waffle maker will return to a horizontal position via the smallest rotation possible. Therefore, the waffle maker will rotate less than $90$ degrees, either forward or backward, until the cooking pan is horizontal again.</p>

<p>The pan rotates at a rate of 180 degrees every $r$ seconds, and stops after $f$ seconds. You don't want to take out your waffle with its blueberry side down. Therefore you'd like to figure out whether the blueberry side of the waffle is up or down after the cooking pan returns to a horizontal position.</p>

<p style="text-align: center;"><img alt="" src="" style="width: 257px; height: 223px;"></p>

### 입력 

 <p>The single line of input contains two integers $r$ and $f$ ($1 \leq r, f \leq 10^4$). The pan rotates at a rate of $180$ degrees every $r$ seconds, and stops after $f$ seconds. It is guaranteed that after $f$ seconds the cooking pan is not at a vertical position.</p>

### 출력 

 <p>Output a single line with a single string, which is <code>up</code> if the blueberry side of the waffle is up, or <code>down</code> otherwise.</p>

