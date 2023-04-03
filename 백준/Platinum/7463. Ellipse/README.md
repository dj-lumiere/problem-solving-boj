# [Platinum II] Ellipse - 7463 

[문제 링크](https://www.acmicpc.net/problem/7463) 

### 성능 요약

메모리: 40480 KB, 시간: 572 ms

### 분류

수학, 기하학, 선형대수학

### 문제 설명

<p>Alex has got a tedious homework from his geometry teacher as a punishment for his conduct at geometry lessons — Alex didn’t do anything while the rest of his class was computing areas of different geometric figures!</p>

<p>Now, Alex has to compute the areas of several ellipses drawn on a sheet of paper torn from a textbook. This paper has a rectangular grid drawn on it which can be used to determine the coordinates of different points. However, the task of finding the area of an ellipse can be quite complicated even in this case, especially if the axes of the ellipse are not vertical or horizontal.</p>

<p>Of course, Alex is very lazy, so he wants you to write a program that would determine the area of an ellipse from the coordinates of five different points lying on it. He would then enter the coordinates of these points for each ellipse himself and thus compute the areas of all ellipses.</p>

### 입력 

 <p>The first line of the input contains the number of ellipses k (1 ≤ k ≤ 1 000). Each of the next k lines contains the coordinates of five points that lie on corresponding ellipse. All coordinates are integer and do not exceed 1 000 by their absolute values.<span style="display: none;"> </span></p>

### 출력 

 <p>On each of k lines of the output write either “IMPOSSIBLE” if the area cannot be determined (e.g. there is no ellipse passing through five given points, or there is more than one such ellipse) or the area itself precise to six digits after decimal point. Note that whenever such an ellipse exists, it always fits completely into the textbook page, i.e. all points (x, y) of the ellipse satisfy inequalities |x|, |y| ≤ 1 000.</p>

