# [Platinum IV] 가희와 코드 - 27887 

[문제 링크](https://www.acmicpc.net/problem/27887) 

### 성능 요약

메모리: 111972 KB, 시간: 2196 ms

### 분류

구현, 자료 구조, 문자열, 파싱, 큐

### 문제 설명

<p>가희의 오빠는 노래를 듣고 즉석에서 반주를 하는 능력이 있습니다. 이번에도 가희는 새로운 노래를 듣고 가희만의 방식으로 반주를 하려고 합니다. 문제에서 등장하는 음의 이름은 12개가 있습니다.</p>

<table class="table table-bordered table-center-50">
	<tbody>
		<tr>
			<td style="text-align: center;">순번</td>
			<td style="text-align: center;">음의 이름</td>
			<td style="text-align: center;">마디에서 주어지는 입력</td>
		</tr>
		<tr>
			<td style="text-align: center;">1</td>
			<td style="text-align: center;"><code>C</code></td>
			<td style="text-align: center;"><code>C</code></td>
		</tr>
		<tr>
			<td style="text-align: center;">2</td>
			<td style="text-align: center;"><code>C#</code> 또는 <code>D$</code></td>
			<td style="text-align: center;"><code>C#</code> 또는 <code>D$</code></td>
		</tr>
		<tr>
			<td style="text-align: center;">3</td>
			<td style="text-align: center;"><code>D</code></td>
			<td style="text-align: center;"><code>D</code></td>
		</tr>
		<tr>
			<td style="text-align: center;">4</td>
			<td style="text-align: center;"><code>D#</code> 또는 <code>E$</code></td>
			<td style="text-align: center;"><code>D#</code> 또는 <code>E$</code></td>
		</tr>
		<tr>
			<td style="text-align: center;">5</td>
			<td style="text-align: center;"><code>E</code></td>
			<td style="text-align: center;"><code>E</code></td>
		</tr>
		<tr>
			<td style="text-align: center;">6</td>
			<td style="text-align: center;"><code>F</code></td>
			<td style="text-align: center;"><code>F</code></td>
		</tr>
		<tr>
			<td style="text-align: center;">7</td>
			<td style="text-align: center;"><code>F#</code> 또는 <code>G$</code></td>
			<td style="text-align: center;"><code>F#</code> 또는 <code>G$</code></td>
		</tr>
		<tr>
			<td style="text-align: center;">8</td>
			<td style="text-align: center;"><code>G</code></td>
			<td style="text-align: center;"><code>G</code></td>
		</tr>
		<tr>
			<td style="text-align: center;">9</td>
			<td style="text-align: center;"><code>G#</code> 또는 <code>A$</code></td>
			<td style="text-align: center;"><code>G#</code> 또는 <code>A$</code></td>
		</tr>
		<tr>
			<td style="text-align: center;">10</td>
			<td style="text-align: center;"><code>A</code></td>
			<td style="text-align: center;"><code>A</code></td>
		</tr>
		<tr>
			<td style="text-align: center;">11</td>
			<td style="text-align: center;"><code>A#</code> 또는 <code>B$</code></td>
			<td style="text-align: center;"><code>A#</code> 또는 <code>B$</code></td>
		</tr>
		<tr>
			<td style="text-align: center;">12</td>
			<td style="text-align: center;"><code>B</code></td>
			<td style="text-align: center;"><code>B</code></td>
		</tr>
	</tbody>
</table>

<p style="text-align: center;"><strong>[표 1] 문제에 등장하는 12개의 음의 이름</strong></p>

<p>음의 이름은 같지만, 높이가 다를 수 있습니다. 이는 {<code>octave</code>}로 결정됩니다.</p>

<p>음에 대한 정보는 아래 두 형식 중 하나로 주어집니다.</p>

<ul>
	<li>{<code>character</code>}{<code>octave</code>}

	<ul>
		<li>{<code>octave</code>} 옥타브에 있는 음의 이름이 {<code>character</code>}인 음입니다.</li>
	</ul>
	</li>
	<li>{<code>character</code>}{<code>octave</code>}{<code>additional_character</code>}
	<ul>
		<li>{<code>octave</code>}옥타브에 있는 음의 이름이 {<code>character</code>}{<code>additional_character</code>}인 음입니다.</li>
		<li>{<code>additional_character</code>}는 <code>#</code> 또는 <code>$</code> 중 하나입니다.</li>
	</ul>
	</li>
</ul>

<p>즉, 음에 대한 정보는 {<code>octave</code>} 와 음의 이름으로 이루어져 있습니다. 아래 [그림 1]은 피아노 건반을 나타내며, <strong>오른쪽으로 갈수록 음높이가 높아집니다.</strong></p>

<p style="text-align: center;"><img alt="" src=""></p>

<p style="text-align: center;"><strong>[그림 1] 0 옥타브에 있는 음들과 대응되는 피아노 건반</strong></p>

<p>두 음이 인접한다면 아래 조건 중 하나를 만족합니다.</p>

<ul>
	<li>두 음이 같은 옥타브에 있는 경우
	<ul>
		<li>음의 이름이 <code>n<sub>1</sub></code>인 것의 순번 <code>s<sub>1</sub></code>과 음의 이름이 <code>n<sub>2</sub></code>인 것의 순번 <code>s<sub>2</sub></code>의 차이가 1일 때, 두 음은 인접합니다.</li>
		<li>음의 이름이 <code>n<sub>1</sub></code>인 것의 순번은 [표 1]에 있습니다.</li>
	</ul>
	</li>
	<li><code>octave</code> 옥타브이고 음의 이름이 <code>B</code>인 음과 <code>ocvate+1</code> 옥타브이고 음의 이름이 <code>C</code>인 두 음은 인접합니다.</li>
</ul>

<p>예를 들어, <code>0</code> 옥타브 <code>C</code>와 <code>0</code> 옥타브 <code>C#</code>은 1번 조건을, <code>0</code> 옥타브 <code>B</code>와 <code>1</code> 옥타브 <code>C</code>는 2번 조건을 만족시킵니다. 따라서, <code>1</code> 옥타브 <code>C</code>와 1 옥타브 <code>C#</code>, <code>0</code> 옥타브 <code>B</code>와 <code>1</code> 옥타브 <code>C</code>는 인접합니다. 아래 [그림 2]에서 빨간 화살표는 인접한 두 음을 보여줍니다.</p>

<p style="text-align: center;"><img alt="" src=""></p>

<p style="text-align: center;"><strong>[그림 2] 인접한 두 음의 예시</strong></p>

<p>인접한 두 음 사이의 거리는 반음입니다. 음 <code>note<sub>1</sub></code>과 음 <code>note<sub>2</sub></code>의 반음 거리가 <code>n</code>이라는 의미는 아래 둘 중 하나를 의미합니다.</p>

<ul>
	<li>음 <code>note<sub>1</sub></code>보다 3개의 반음만큼 음높이가 높아진 음은 <code>note<sub>2</sub></code>입니다.</li>
	<li>음 <code>note<sub>1</sub></code>보다 3개의 반음만큼 음높이가 낮아진 음은 <code>note<sub>2</sub></code>입니다.</li>
</ul>

<p>아래 [표 3]은 문제에 자주 등장하는 용어들을 나타낸 것입니다.</p>

<table class="table table-bordered table-center-50">
	<tbody>
		<tr>
			<td style="text-align: center;">반음 거리</td>
			<td style="text-align: center;">완전/장/단</td>
		</tr>
		<tr>
			<td style="text-align: center;">3</td>
			<td style="text-align: center;">단 3도</td>
		</tr>
		<tr>
			<td style="text-align: center;">4</td>
			<td style="text-align: center;">장 3도</td>
		</tr>
		<tr>
			<td style="text-align: center;">12</td>
			<td style="text-align: center;">완전 8도</td>
		</tr>
	</tbody>
</table>

<p style="text-align: center;"><strong>[표 2] 문제에 자주 나오는 용어들과 대응되는 반음 거리</strong></p>

<p style="text-align: center;"><img alt="" src=""> <strong>[그림 3] 0 옥타브 도 <code>C0</code>로부터 단 3도 위, 장 3도 위에 있는 음</strong></p>

<p>[그림 1]에서 <strong>각 화살표들은 반음 1개의 거리</strong>를 나타냅니다. 음 <code>C0</code>으로부터 단 3도 위에 있는 음은 <code>D0#</code>이고 음의 이름은 <code>D#</code>입니다. <code>C0</code>에서 출발하여 빨간색 화살표 따라 이동하면 도착하는 음이기 때문입니다. 음 <code>C0</code>으로부터 장 3도 위에 있는 음은 <code>E0</code>이고, 음의 이름은 <code>E</code>입니다. <code>C0</code>에서 출발하여, 빨간색 화살표와 보라색 화살표를 따라 이동하면 도착하는 음이기 때문입니다.</p>

<p>이제 코드에 대해 설명하겠습니다. 코드에서 근음(1음)이란 뿌리가 되는 음을 의미합니다. 그 위에 장 3도, 또 그 위에 단 3도를 쌓아 올려서 만든 코드를 <code>Major</code> 코드라고 합니다. 몇 개의 <code>Major</code> 코드의 예시가 [표 3]에 있습니다.</p>

<table class="table table-bordered table-center-50">
	<tbody>
		<tr>
			<td style="text-align: center;"> </td>
			<td style="text-align: center;">1 음의 이름</td>
			<td style="text-align: center;">3 음의 이름</td>
			<td style="text-align: center;">5 음의 이름</td>
			<td style="text-align: center;">출력할 때 표시</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>C Major</code></td>
			<td style="text-align: center;"><code>C</code></td>
			<td style="text-align: center;"><code>E</code></td>
			<td style="text-align: center;"><code>G</code></td>
			<td style="text-align: center;"><code>CM</code></td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>F Major</code></td>
			<td style="text-align: center;"><code>F</code></td>
			<td style="text-align: center;"><code>A</code></td>
			<td style="text-align: center;"><code>C</code></td>
			<td style="text-align: center;"><code>FM</code></td>
		</tr>
	</tbody>
</table>

<p style="text-align: center;"><strong>[표 3] <code>Major</code> 코드 예시</strong></p>

<p>다음에 <code>minor</code> 코드를 알아보겠습니다. <code>Major</code> 코드에서 3음을 반음 내린 것을 <code>minor</code> 코드라고 합니다. 몇 가지 <code>minor</code> 코드의 예제가 [표 4]에 있습니다.</p>

<table class="table table-bordered table-center-50">
	<tbody>
		<tr>
			<td style="text-align: center;"> </td>
			<td style="text-align: center;">1 음의 이름</td>
			<td style="text-align: center;">3 음의 이름</td>
			<td style="text-align: center;">5 음의 이름</td>
			<td style="text-align: center;">출력할 때 표시</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>C minor</code></td>
			<td style="text-align: center;"><code>C</code></td>
			<td style="text-align: center;"><code>E$</code></td>
			<td style="text-align: center;"><code>G</code></td>
			<td style="text-align: center;"><code>Cm</code></td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>F minor</code></td>
			<td style="text-align: center;"><code>F</code></td>
			<td style="text-align: center;"><code>A$</code></td>
			<td style="text-align: center;"><code>C</code></td>
			<td style="text-align: center;"><code>Fm</code></td>
		</tr>
	</tbody>
</table>

<p style="text-align: center;"><strong>[표 4] <code>minor</code> 코드 예시</strong></p>

<p>다음에 <code>aug</code> 코드를 알아보겠습니다. <code>Major</code> 코드에서의 5음을 반음 올린 것을 <code>aug</code> 코드라고 합니다. 몇 가지 <code>aug</code> 코드의 예제가 [표 5]에 있습니다.</p>

<table class="table table-bordered table-center-50">
	<tbody>
		<tr>
			<td style="text-align: center;"> </td>
			<td style="text-align: center;">1 음의 이름</td>
			<td style="text-align: center;">3 음의 이름</td>
			<td style="text-align: center;">5 음의 이름</td>
			<td style="text-align: center;">출력할 때 표시</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>C aug</code></td>
			<td style="text-align: center;"><code>C</code></td>
			<td style="text-align: center;"><code>E</code></td>
			<td style="text-align: center;"><code>G#</code></td>
			<td style="text-align: center;"><code>Caug</code></td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>F aug</code></td>
			<td style="text-align: center;"><code>F</code></td>
			<td style="text-align: center;"><code>A</code></td>
			<td style="text-align: center;"><code>C#</code></td>
			<td style="text-align: center;"><code>Faug</code></td>
		</tr>
	</tbody>
</table>

<p style="text-align: center;"><strong>[표 5] <code>aug</code> 코드 예시</strong></p>

<p>다음에 <code>dim</code> 코드를 알아보겠습니다. <code>Major</code> 코드에서의 3음, 5음을 반음 내린 것을 <code>dim</code> 코드라고 합니다. 몇 가지 <code>dim</code> 코드의 예제가 [표 6]에 있습니다.</p>

<table class="table table-bordered table-center-50">
	<tbody>
		<tr>
			<td style="text-align: center;"> </td>
			<td style="text-align: center;">1 음의 이름</td>
			<td style="text-align: center;">3 음의 이름</td>
			<td style="text-align: center;">5 음의 이름</td>
			<td style="text-align: center;">출력할 때 표시</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>C dim</code></td>
			<td style="text-align: center;"><code>C</code></td>
			<td style="text-align: center;"><code>E$</code></td>
			<td style="text-align: center;"><code>G$</code></td>
			<td style="text-align: center;"><code>Cdim</code></td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>F dim</code></td>
			<td style="text-align: center;"><code>F</code></td>
			<td style="text-align: center;"><code>A$</code></td>
			<td style="text-align: center;"><code>B</code></td>
			<td style="text-align: center;"><code>Fdim</code></td>
		</tr>
	</tbody>
</table>

<p style="text-align: center;"><strong>[표 6] <code>dim</code> 코드 예시</strong></p>

<p>가희는 아래와 같은 알고리즘으로 반주를 하려고 합니다.</p>

<ul>
	<li>이전 <code>p</code>개의 마디에서 <code>k</code>번 이상 쓰였던 코드들은 제외합니다. 이 작업을 수행한 후 남은 코드의 개수가 <code>r</code>이라면

	<ul>
		<li><code>r</code>이 0인 경우, 가장 오랫동안 사용하지 않은 코드를 선택합니다.

		<ul>
			<li>그러한 코드가 여러 개 있다면, 아스키코드 사전 순으로 가장 앞에 있는 것을 선택합니다.</li>
		</ul>
		</li>
		<li><code>r</code>이 0보다 큰 경우
		<ul>
			<li><strong>코드를 이루는 음의 이름이 <code>m</code>번째 마디에 총 몇 번 나왔는지를 계산합니다. </strong>이 수치가 가장 높은 코드를 선택합니다.</li>
			<li>그러한 것이 여러 개인 경우, 아스키코드 사전 순으로 가장 앞선 코드를 선택합니다.</li>
		</ul>
		</li>
	</ul>
	</li>
</ul>

<p>이 알고리즘에 따라, <code>p</code>와 <code>k</code>가 1이고 마디 수가 1인 음악에 대해 반주해 보겠습니다.</p>

<table class="table table-bordered table-center-50">
	<tbody>
		<tr>
			<td style="text-align: center;">마디</td>
			<td style="text-align: center;"> </td>
		</tr>
		<tr>
			<td style="text-align: center;">1</td>
			<td style="text-align: center;"><code>F2E2D2E2F2</code></td>
		</tr>
	</tbody>
</table>

<p style="text-align: center;"><strong>[표 7] 예제 1의 곡</strong></p>

<p>먼저 첫 번째 마디에 <code>F2</code>, <code>E2</code>, <code>D2</code>, <code>E2</code>, <code>F2</code>, 순서대로 나옵니다. 즉, 음의 이름이 <code>D</code>(레)인 것이 1번, <code>E</code>(미)인 것이 2번, <code>F</code>(파)인 것이 2번 나옵니다. <code>C Major</code> 코드를 이루는 음의 이름이 1번째 마디에서 몇 번 나왔는지 세 보겠습니다.</p>

<table class="table table-bordered table-center-50">
	<tbody>
		<tr>
			<td style="text-align: center;">음의 이름</td>
			<td style="text-align: center;">빈도</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>C</code></td>
			<td style="text-align: center;">-</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>E</code></td>
			<td style="text-align: center;">2</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>G</code></td>
			<td style="text-align: center;">-</td>
		</tr>
	</tbody>
</table>

<p style="text-align: center;"><strong>[표 8] <code>C</code>, <code>E</code>, <code>G</code>가 1번째 마디에 나온 횟수</strong></p>

<p><code>C Major</code>를 이루는 음의 이름이 <code>C</code>, <code>E</code>, <code>G</code>인 것이 나온 횟수를 모두 합하면 2가 됩니다. 이런 식으로 모든 코드에 대해, <strong>코드를 이루는 음의 이름이 <code>1</code>번째 마디에 총 몇 번 나왔는지</strong> 계산합니다. 그 결과는 [표 9]에 있습니다.</p>

<table class="table table-bordered table-center-50">
	<tbody>
		<tr>
			<td style="text-align: center;">코드</td>
			<td style="text-align: center;">코드를 이루는 음의 이름이 마디에 나온 총횟수</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>A#M</code></td>
			<td style="text-align: center;">3</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>Bdim</code></td>
			<td style="text-align: center;">3</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>Ddim</code></td>
			<td style="text-align: center;">3</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>Dm</code></td>
			<td style="text-align: center;">3</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>CM</code></td>
			<td style="text-align: center;">2</td>
		</tr>
		<tr>
			<td style="text-align: center;">...</td>
			<td style="text-align: center;">....</td>
		</tr>
	</tbody>
</table>

<p style="text-align: center;"><strong>[표 9] 코드를 이루는 음의 이름이 1번째 마디에 나온 횟수 </strong></p>

<p>이 중, 아스키코드 사전 순으로 가장 앞선 것은 <code>A#M</code>이 됩니다.</p>

<p>이제 <code>p</code>가 2, <code>k</code>가 1이고 마디 수가 3인 음악에 대해 반주해 보겠습니다.</p>

<table class="table table-bordered table-center-50">
	<tbody>
		<tr>
			<td style="text-align: center;">마디</td>
			<td style="text-align: center;"> </td>
		</tr>
		<tr>
			<td style="text-align: center;">1</td>
			<td style="text-align: center;"><code>F2F3F2F3F2F3F2F3</code></td>
		</tr>
		<tr>
			<td style="text-align: center;">2</td>
			<td style="text-align: center;"><code>F0F1F0F1F0F1F0F1</code></td>
		</tr>
		<tr>
			<td style="text-align: center;">3</td>
			<td style="text-align: center;"><code>F2F2F3F2F3F2F3F2</code></td>
		</tr>
	</tbody>
</table>

<p style="text-align: center;"><strong>[표 10] 예제 2의 곡</strong></p>

<p>먼저 첫 번째 마디에 <code>F2</code>, <code>F3</code>, <code>F2</code>, <code>F3</code>, <code>F2</code>, <code>F3</code>, <code>F2</code>, <code>F3</code> 순서대로 나옵니다. 즉 음의 이름이 <code>F</code>(파)인 것이 8번 나옵니다.</p>

<table class="table table-bordered table-center-50">
	<tbody>
		<tr>
			<td style="text-align: center;">코드</td>
			<td style="text-align: center;">코드를 이루는 음의 이름이 마디에 나온 총횟수</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>C#M</code></td>
			<td style="text-align: center;">8</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>FM</code></td>
			<td style="text-align: center;">8</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>A#M</code></td>
			<td style="text-align: center;">8</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>Dm</code></td>
			<td style="text-align: center;">8</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>Fm</code></td>
			<td style="text-align: center;">8</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>A#m</code></td>
			<td style="text-align: center;">8</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>C#aug</code></td>
			<td style="text-align: center;">8</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>Faug</code></td>
			<td style="text-align: center;">8</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>Aaug</code></td>
			<td style="text-align: center;">8</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>Ddim</code></td>
			<td style="text-align: center;">8</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>Fdim</code></td>
			<td style="text-align: center;">8</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>Bdim</code></td>
			<td style="text-align: center;">8</td>
		</tr>
		<tr>
			<td style="text-align: center;">나머지</td>
			<td style="text-align: center;">0</td>
		</tr>
	</tbody>
</table>

<p style="text-align: center;"><strong>[표 11] 각 코드가 이루는 음의 이름이 1번째 마디에 나온 횟수</strong></p>

<p>코드를 이루는 음의 이름이 총 몇 번 나왔는지 셉니다. 가장 많이 나온 코드는 8회였고, 이를 만족하는 코드는 총 12개입니다. <code>r</code>이 0보다 크므로, 12개의 코드 중 아스키코드 사전 순으로 가장 앞선 <code>A#M</code>을선택합니다.</p>

<p>2번째 마디를 반주해 보겠습니다. 두 번째 마디에는 <code>F0</code>, <code>F1</code>, <code>F0</code>, <code>F1</code>, <code>F0</code>, <code>F1</code>, <code>F0</code>, <code>F1</code> 순서대로 나옵니다. 1번째 마디와 같이 음의 이름이 F(파)인 것이 8번 나옵니다. 이전 2개의 마디에서 1번 이상 쓰인 <code>A#M</code>을 제외한 나머지 코드들에 대해, 각 코드가 이루는 음의 이름이 총 몇 번 나왔는지 셉니다.</p>

<table class="table table-bordered table-center-50">
	<tbody>
		<tr>
			<td style="text-align: center;">코드</td>
			<td style="text-align: center;">코드를 이루는 음의 이름이 마디에 나온 총횟수</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>C#M</code></td>
			<td style="text-align: center;">8</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>FM</code></td>
			<td style="text-align: center;">8</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>Dm</code></td>
			<td style="text-align: center;">8</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>Fm</code></td>
			<td style="text-align: center;">8</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>A#m</code></td>
			<td style="text-align: center;">8</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>Aaug</code></td>
			<td style="text-align: center;">8</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>C#aug</code></td>
			<td style="text-align: center;">8</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>Faug</code></td>
			<td style="text-align: center;">8</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>Ddim</code></td>
			<td style="text-align: center;">8</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>Fdim</code></td>
			<td style="text-align: center;">8</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>Bdim</code></td>
			<td style="text-align: center;">8</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>A#M</code>를 제외한 나머지</td>
			<td style="text-align: center;">0</td>
		</tr>
	</tbody>
</table>

<p style="text-align: center;"><strong>[표 12] 각 코드가 이루는 음의 이름이 2번째 마디에 나온 횟수</strong></p>

<p>코드를 이루는 음의 이름이 총 몇 번 나왔는지 셉니다. 가장 많이 나온 횟수는 8번이었고, 이를 만족하는 코드는 11개입니다. <code>r</code>이 0보다 크므로, 11개의 코드 중 아스키코드 사전 순으로 가장 앞선 <code>A#m</code>를 선택합니다.</p>

<p>3번째 마디를 반주해 보겠습니다. 세 번째 마디에는 <code>F2</code>, <code>F2</code>, <code>F3</code>, <code>F2</code>, <code>F3</code>, <code>F2</code>, <code>F3</code>, <code>F2</code> 순서대로 나옵니다. 1, 2번째 마디와 같이 음의 이름이 <code>F</code>(파)인 것만 8번 나옵니다. 이전 2개의 마디에서 1번 이상 쓰인 <code>A#M</code>, <code>A#m</code>을 제외한 나머지 코드들에 대해, 각 코드가 이루는 음의 이름이 총 몇 번 나왔는지 셉니다.</p>

<table class="table table-bordered table-center-50">
	<tbody>
		<tr>
			<td style="text-align: center;">코드</td>
			<td style="text-align: center;">코드를 이루는 음의 이름이 마디에 나온 총횟수</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>C#M</code></td>
			<td style="text-align: center;">8</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>FM</code></td>
			<td style="text-align: center;">8</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>Dm</code></td>
			<td style="text-align: center;">8</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>Fm</code></td>
			<td style="text-align: center;">8</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>Aaug</code></td>
			<td style="text-align: center;">8</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>C#aug</code></td>
			<td style="text-align: center;">8</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>Faug</code></td>
			<td style="text-align: center;">8</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>Ddim</code></td>
			<td style="text-align: center;">8</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>Fdim</code></td>
			<td style="text-align: center;">8</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>Bdim</code></td>
			<td style="text-align: center;">8</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>A#M</code>과 <code>A#m</code>을 제외한 나머지</td>
			<td style="text-align: center;">0</td>
		</tr>
	</tbody>
</table>

<p style="text-align: center;"><strong>[표 13] 각 코드 이루는 음의 이름이 3번째 마디에 나온 횟수</strong></p>

<p>가장 많이 나온 횟수는 8번이었고, 이를 만족하는 코드는 10개입니다. <code>r</code>이 0보다 크므로, 10개의 코드 중 아스키코드 사전 순으로 가장 앞선 <code>Aaug</code>를 선택합니다.</p>

### 입력 

 <p>첫 줄에 마디 수 <code>m</code>과 문제에서 설명한 <code>p</code>, <code>k</code>가 공백으로 구분되어 주어집니다.</p>

<p>다음 <code>m</code>개의 줄에 마디에 나오는 음의 정보들이 주어집니다. 이때 음은 아래와 같은 형식으로 주어집니다.</p>

<p style="text-align: center;">{<code>character</code>}{<code>octave</code>}{<code>addtional_character</code>}</p>

<ul>
	<li>{<code>character</code>}

	<ul>
		<li><code>A</code>, <code>B</code>, <code>C</code>, <code>D</code>, <code>E</code>, <code>F</code>, <code>G</code> 중 하나로 주어집니다. 한국식 음의 이름은 각각 라, 시, 도, 레, 미, 파, 솔을 의미합니다.</li>
	</ul>
	</li>
	<li>{<code>octave</code>}
	<ul>
		<li>-2보다 크거나 같고 7보다 작거나 같은 수로 주어집니다.</li>
	</ul>
	</li>
	<li>{<code>addtional_character</code>} <strong>(optional)</strong>
	<ul>
		<li>{<code>character</code>}{<code>octave</code>}보다 <strong>반음 높은 경우 #으로</strong>, <strong>반음 낮은 경우 $</strong>으로 주어집니다.</li>
		<li>이때, <strong>해당 음에서만 반음이 높아지거나 낮아지는 효력이 발생</strong>합니다.</li>
	</ul>
	</li>
</ul>

<p>예를 들어 한 마디에 0 옥타브 레, -1 옥타브 시, 0 옥타브 레#, 0 옥타브 레♭이 있다고 했을 때, 아래와 같이 입력이 주어집니다.</p>

<p style="text-align: center;"><code>D0B-1D0#D0$</code></p>

<p>또한 한 마디에 0 옥타브 레#, 0 옥타브 레, 0 옥타브 레#, 0 옥타브 레#이 있다고 했을 때, 아래와 같이 입력이 주어집니다.</p>

<p style="text-align: center;"><code>D0#D0D0#D0#</code></p>

<p>단, 아래의 입력은 주어지지 않습니다.</p>

<table align="center" border="1" cellpadding="1" cellspacing="1" class="table table-bordered" style="width: 400px;">
	<tbody>
		<tr>
			<td style="text-align: center;"><code>character</code></td>
			<td style="text-align: center;"><code>additional_character</code></td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>B</code></td>
			<td style="text-align: center;">#</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>C</code></td>
			<td style="text-align: center;">$</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>E</code></td>
			<td style="text-align: center;">#</td>
		</tr>
		<tr>
			<td style="text-align: center;"><code>F</code></td>
			<td style="text-align: center;">$</td>
		</tr>
	</tbody>
</table>

<p style="text-align: center;"><strong>[표 14] 주어지지 않는 입력</strong></p>

### 출력 

 <p><code>m</code>개의 줄에 답을 출력해 주세요. 이때</p>

<p style="text-align: center;">{<code>character</code>}{<code>additional_character</code>}{<code>type</code>}</p>

<p>형식으로 출력해 주세요.</p>

<ul>
	<li>{<code>character</code>}

	<ul>
		<li><code>A</code>, <code>B</code>, <code>C</code>, <code>D</code>, <code>E</code>, <code>F</code>, <code>G</code> 중 하나입니다. 한국식 음의 이름은 각각 라, 시, 도, 레, 미, 파, 솔을 의미합니다.</li>
	</ul>
	</li>
	<li>{<code>addtional_character</code>} <strong>(optional)</strong>
	<ul>
		<li><strong>근음이 {<code>character</code>}보다 반음 위에 있는 경우</strong> #으로 출력합니다.
		<ul>
			<li><strong>단 {<code>character</code>}가 <code>B</code>이거나 <code>E</code>인 경우 뒤에 #을 붙이지 않습니다.</strong></li>
		</ul>
		</li>
		<li>#을 붙인 경우,<strong> 해당 음에서만 반음이 높아지는 효력이 발생</strong>합니다.</li>
	</ul>
	</li>
	<li>{<code>type</code>}
	<ul>
		<li>문제에 제시된 <code>M</code>, <code>m</code>, <code>aug</code>, <code>dim</code>중 하나입니다.</li>
	</ul>
	</li>
</ul>

<p>예를 들어, <code>D#M</code>의 경우, <code>E$M</code>으로도 표시될 수 있습니다. 이는 같은 옥타브에 있는 음의 이름이 <code>D#</code>인 것과, <code>E$</code>인 것이 같은 음(딴이름 한소리)이기 때문입니다. <strong>이로 인해 발생하는 혼동을 방지하기 위해 출력 형식 제한이 있다는 것을 유의해 주세요.</strong></p>

