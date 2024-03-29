# [Platinum I] Xorshift32 - 18776 

[문제 링크](https://www.acmicpc.net/problem/18776) 

### 성능 요약

메모리: 209320 KB, 시간: 276 ms

### 분류

이산 로그, 선형대수학, 수학, 중간에서 만나기, 정수론, 런타임 전의 전처리

### 문제 설명

<p><a href="https://en.wikipedia.org/wiki/Xorshift">Xorshift32</a>는 1 이상 4,294,967,295 이하의 자연수로 이루어진 수열을 만들어내는 유사 난수 알고리즘입니다. 이 수열의 주기는 4,294,967,295로 1 이상 4,294,967,295 이하의 모든 자연수가 한 번씩 나온 다음에는 수열의 첫 번째 수가 다시 나오게 됩니다.</p>

<p>아래는 수열의 첫 번째 수를 입력받아 Xorshift32 알고리즘에 의한 수열을 출력하는 C 코드입니다.</p>

<pre class="brush:c++; toolbar:false;">#include <stdio.h>
#include <inttypes.h>

uint32_t xorshift32(uint32_t x) {
    x ^= x << 13;
    x ^= x >> 17;
    x ^= x << 5;
    return x;
}

int main(void) {
    uint32_t x;
    scanf("%" SCNu32, &x);
    for (;;) {
        printf("%" PRIu32 "\n", x);
        x = xorshift32(x);
    }
    return 0;
}</pre>

<p>예를 들어 2,463,534,242로 시작하는 수열은 다음과 같습니다.</p>

<p>2463534242, 723471715, 2497366906, 2064144800, 2008045182, ...(4,294,967,288개 생략), 1232801914, 1174207936, <strong>2463534242</strong>, 723471715, 2497366906, ...</p>

<p>이때 723,471,715는 이 수열에서 2번째에 처음으로 나오고, 1,232,801,914는 4,294,967,294번째에 처음으로 나온다는 사실을 알 수 있습니다.</p>

<p>사잇은 <em>x</em>로 시작하는 Xorshift32 수열에서 특정한 수 <em>t</em>가 몇 번째에 나오는지 예측할 수 있으면 좋겠다고 생각했습니다. 여러분이 사잇을 도와주세요.</p>

### 입력 

 <p>첫째 줄에 두 개의 자연수 <em>x</em>와 <em>t</em>가 주어집니다. (1 ≤ <em>x</em>, <em>t</em> ≤ 4,294,967,295)</p>

### 출력 

 <p><em>x</em>로 시작하는 Xorshift32 수열에서 <em>t</em>가 처음으로 나오는 것은 몇 번째인지 출력합니다.</p>

