# [Ruby V] Iloczyny Fibonacciego - 26665 

[문제 링크](https://www.acmicpc.net/problem/26665) 

### 성능 요약

메모리: 128744 KB, 시간: 1548 ms

### 분류

애드 혹, 많은 조건 분기, 고속 푸리에 변환, 구현, 수학

### 문제 설명

<p>Wielki informatyk Bajtazar od ponad 15 lat konstruuje niezwykły komputer, w którym liczby są reprezentowane w systemie Fibonacciego, czyli są zapisywane jako suma różnych, niekolejnych liczb Fibonacciego. Formalnie, jeśli zdefiniujemy liczby Fibonacciego, zaczynając od 1 i 2:</p>

<p style="text-align: center;">F<sub>1</sub> = 1, F<sub>2</sub> = 2, F<sub>i</sub> = F<sub>i−1</sub> + F<sub>i−2</sub> dla i ≥ 3,</p>

<p>to każda dodatnia liczba całkowita x przedstawia się jednoznacznie jako ciąg bitów (b<sub>1</sub>, b<sub>2</sub>, . . . , b<sub>n</sub>) dla pewnego n ≥ 1, spełniający następujące warunki:</p>

<ul>
	<li>x = b<sub>1</sub> · F<sub>1</sub> + b<sub>2</sub> · F<sub>2</sub> + . . . + b<sub>n</sub> · F<sub>n</sub>;</li>
	<li>b<sub>i</sub> ∈ {0, 1} dla wszystkich 1 ≤ i < n oraz b<sub>n</sub> = 1 (wyłącznie zera i jedynki, bez zer wiodących);</li>
	<li>b<sub>i</sub> · b<sub>i+1</sub> = 0 dla wszystkich 1 ≤ i < n (nie ma dwóch sąsiednich jedynek);</li>
</ul>

<p>Na przykład 2 = (0, 1), 4 = (1, 0, 1), 5 = (0, 0, 0, 1), zaś 20 = (0, 1, 0, 1, 0, 1) bo 20 = F<sub>2</sub> + F<sub>4</sub> + F<sub>6</sub> = 2 + 5 + 13.</p>

<p>Dawno temu Bajtazar poprosił uczestników Olimpiady Informatycznej o pomoc w implementacji dodawania liczb w systemie Fibonacciego. Historia ta działa się przy okazji zadania Sumy Fibonacciego z drugiego etapu XII OI i została opisana w „niebieskiej książeczce” Olimpiady.</p>

<p>Tym razem sprawa jest trudniejsza, a Bajtazar głowi się nad nią już dobrych parę lat. Postanowił więc poprosić o radę uczestników Potyczek Algorytmicznych. Pomóżcie mu zaimplementować mnożenie!</p>

### 입력 

 <p>W pierwszym wierszu wejścia znajduje się liczba zestawów testowych t (1 ≤ t ≤ 1000). W kolejnych 2t wierszach następuje opis zestawów.</p>

<p>Każdy zestaw składa się z dwóch wierszy. W pierwszym z nich dana jest reprezentacja dodatniej liczby całkowitej x w systemie Fibonacciego – najpierw liczba n oznaczająca jej długość, a następnie n bitów b<sub>1</sub>, b<sub>2</sub>, . . . , b<sub>n</sub>. W drugim wierszu dana jest w takim samym formacie reprezentacja dodatniej liczby całkowitej y.</p>

<p>Suma długości wszystkich reprezentacji z wejścia nie przekracza 10<sup>6</sup>.</p>

### 출력 

 <p>Dla każdego zestawu testowego z wejścia wypisz iloczyn x·y zapisany w systemie Fibonacciego w analogicznym formacie jak na wejściu – najpierw długość n′ , potem n′ bitów szukanej liczby. Poszczególne liczby w wierszach powinny być pooddzielane pojedynczymi odstępami.</p>

<p>Reprezentacje z wejścia i z wyjścia muszą spełniać warunki z zadania, więc w szczególności ciąg bitów musi kończyć się jedynką i nie może zawierać sąsiadujących jedynek.</p>

