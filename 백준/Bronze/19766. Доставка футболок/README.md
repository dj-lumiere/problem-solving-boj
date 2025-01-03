# [Bronze II] Доставка футболок - 19766 

[문제 링크](https://www.acmicpc.net/problem/19766) 

### 성능 요약

메모리: 137076 KB, 시간: 276 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2024년 12월 15일 10:29:06

### 문제 설명

<p>Завершилась Командная Интернет-олимпиада Новой Зеландии по Алгоритмам (КИНЗА). После олимпиады оргкомитет принял решение отправить футболки всем призерам олимпиады. Доставка футболок была поручена компании, в которой работает курьер Билл.</p>

<p>Биллу требуется доставить $n$ футболок. Он должен доставлять посылки в том порядке, в котором они значатся в его обходном листе. При этом, если посылку доставить не удалось, то в обходном листе ставится отказ, и Билл едет по следующему адресу.</p>

<p>Билл начинает свой рабочий день в офисе компании в момент 0. Приезжая к адресату посылки, он ждет не более $k$ минут, и если за это время адресат открывает дверь, то Билл отдает ему посылку, процесс передачи посылки без учета времени ожидания занимает $t$ минут. Если же в течение $k$ минут дверь не открывается и получатель не появляется, то Билл едет дальше. При этом, если получатель появился ровно ровно через $k$ минут после приезда Билла, то Билл успевает это заметить, и посылка оказывается доставлена. Рабочий день Билла заканчивается, когда он заканчивает передавать последнюю посылку, либо отмечает в обходном листе отказ от ее получения.</p>

<p>Начальник Билла Джон хочет проверить, насколько добросовестно тот работает. Джону известно, сколько времени ему потребуется на то, чтобы доехать от офиса до первого адресата, а также время на переезд от очередного адресата до следующего. Кроме того, он провел телефонный опрос и знает время, начиная с которого каждый из  получателей футболок  будет дома. Теперь Джон хочет узнать, в какой момент Билл закончит свой рабочий день.</p>

### 입력 

 <p>В первой строке входного файла находятся три целых числа $n$, $k$, $t$ ($1 \le n \le 50\,000$, $1 \le k, t \le 10^4$).</p>

<p>Во второй строке находятся $n$ натуральных чисел $z_0, z_1, \ldots, z_{n-1}$, где $z_0$ --- это время, которое требуется Биллу, чтобы доехать от офиса до первого адресата, а $z_i$ --- это время, которое требуется Биллу для преодоления пути от $i$-го до $i+1$-го адресата. Все $z_i$ не превосходят $10^4$.</p>

<p>В третьей строке находятся $n$ неотрицательных целых чисел $s_1, s_2, \ldots, s_n$ ($0 \le s_i \le 10^{9}$), \mbox{где $s_i$ --- это момент}, начиная с которого $i$-й адресат готов принять посылку. Билл начинает свой путь в момент времени 0.</p>

### 출력 

 <p>Выведите одно число --- минимальное время, за которое Билл сможет выполнить свое задание.</p>

