# [Platinum V] 크로아티아 수 읽기 - 3177 

[문제 링크](https://www.acmicpc.net/problem/3177) 

### 성능 요약

메모리: 115304 KB, 시간: 140 ms

### 분류

구현, 수학

### 문제 설명

<p>아래 표는 크로아티아어에서 숫자를 읽는 발음을 정리한 것이다. 크로아티아 숫자는 1,000 단위로 끊어서 읽는다. 가장 큰 자리수의 숫자가 1 이 아닐 경우 해당 숫자를 읽는다. 가장 큰 자리수의 숫자가 1일 경우, 1을 생략하고 자리수를 나타내는 숫자부터 읽는다. 예외적으로 1은 jedan 그대로 발음하며,  1,000 단위로 끊은 결과가 11과 19 사이의 값일 경우, 아래 표에 나와있는 값을 읽는다. 예를 들어 40 은 <strong>č</strong>etiri 로 시작하고, 705 는 <strong>s</strong>edam으로, 150 은 <strong>s</strong>to로, 1 500 은 <strong>t</strong>isuću로, 15 000 은 <strong>p</strong>etnaest로 시작한다.</p>

<table class="table table-bordered" style="width:60%">
	<tbody>
		<tr>
			<th>1</th>
			<td><strong>j</strong>edan</td>
			<th>10</th>
			<td><strong>d</strong>eset</td>
			<th>1xx</th>
			<td><strong>s</strong>to</td>
		</tr>
		<tr>
			<th>2</th>
			<td><strong>d</strong>va</td>
			<th>11</th>
			<td><strong>j</strong>edanaest</td>
			<th>1xxx</th>
			<td><strong>t</strong>isuću</td>
		</tr>
		<tr>
			<th>3</th>
			<td><strong>t</strong>ri</td>
			<th>12</th>
			<td><strong>d</strong>vanaest</td>
			<th>1xxxx</th>
			<td><strong>d</strong>eset tisuća</td>
		</tr>
		<tr>
			<th>4</th>
			<td><strong>č</strong>etiri</td>
			<th>13</th>
			<td><strong>t</strong>rinaest</td>
			<th>1xxxxx</th>
			<td><strong>s</strong>to tisuća</td>
		</tr>
		<tr>
			<th>5</th>
			<td><strong>p</strong>et</td>
			<th>14</th>
			<td><strong>č</strong>etrnaest</td>
			<th>1xxxxxx</th>
			<td><strong>m</strong>ilijun</td>
		</tr>
		<tr>
			<th>6</th>
			<td><strong>š</strong>est</td>
			<th>15</th>
			<td><strong>p</strong>etnaest</td>
			<th>1xxxxxxx</th>
			<td><strong>d</strong>eset milijuna</td>
		</tr>
		<tr>
			<th>7</th>
			<td><strong>s</strong>edam</td>
			<th>16</th>
			<td><strong>š</strong>esnaest</td>
			<th>1xxxxxxxx</th>
			<td><strong>s</strong>to milijuna</td>
		</tr>
		<tr>
			<th>8</th>
			<td><strong>o</strong>sam</td>
			<th>17</th>
			<td><strong>s</strong>edamnaest</td>
			<th>1xxxxxxxxx</th>
			<td><strong>m</strong>ilijarda</td>
		</tr>
		<tr>
			<th>9</th>
			<td><strong>d</strong>evet</td>
			<th>18</th>
			<td><strong>o</strong>samnaest</td>
			<th>1xxxxxxxxxx</th>
			<td><strong>d</strong>eset milijardi</td>
		</tr>
		<tr>
			<th> </th>
			<td> </td>
			<th>19</th>
			<td><strong>d</strong>evetnaest</td>
			<th>1xxxxxxxxxxx</th>
			<td><strong>s</strong>to milijardi</td>
		</tr>
	</tbody>
</table>

<p>주어진 알파벳으로 시작하는 양수의 수열을 생각해보자. 예를 들어 P로 시작하는 수들의 수열은 5, 15, 50, 51, 52, ..., 59, 500, 501, ... 이다.</p>

<p>주어진 알파벳으로 시작하는 양수의 수열에서 N번째 수를 찾는 프로그램을 작성하자.</p>

### 입력 

 <p>입력으로는 D, J, M, O, P, S, T 중 하나와 정수 N이 입력된다.</p>

<p>단, 출력은 10<sup>12</sup>을 넘지 않는다.</p>

### 출력 

 <p>수열의 N번째 수를 출력한다.</p>

