# [Bronze I] Contact Tracer - 20225 

[문제 링크](https://www.acmicpc.net/problem/20225) 

### 성능 요약

메모리: 128980 KB, 시간: 232 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2024년 12월 23일 09:47:10

### 문제 설명

<p style="user-select: auto !important;">Novel virus infections are spreading. The virus is known to transmit on close contact with carriers, whether or not with any symptoms. Therefore, it is effective for epidemic prevention to identify and test those who had close contact with persons confirmed or were judged highly probable to be infected. To realize this, a system is desired that perpetually records all the close contact events by an application on mobile phones and, when infection is confirmed, identifies all persons with direct or indirect infection risks based on the record.</p>

<p style="user-select: auto !important;">You were asked to develop such a system, and have already finished the mobile phone part. When the installed application detects a close contact event with another person carrying a phone with the same application installed, it sends IDs of both to the surveillance center.</p>

<p style="user-select: auto !important;">Your next task is to develop a program that, when infection of a user is confirmed, identifies users with risks of direct or indirect transmission from the infected user.</p>

<p style="user-select: auto !important;">When a user of the system is confirmed to be infected, those users who made close contacts with the infected user within a certain time period (period of communicability) are suspected of infection. If a suspected user had close contact with still another user after that possible infection event, that user also is suspected of infection. The suspects are propagated repetitively in this manner.</p>

<p style="user-select: auto !important;">When a user is confirmed infected, the ID of the user and the list of all the close contact events of all users with all users happened after the time when the confirmed user possibly becomes a carrier are given. All the events in the given list should be assumed to be within the period of communicability of the confirmed user. The output should be the number of users to whom the virus was possibly transmitted directly or indirectly from the infected user.</p>

### 입력 

 <p style="user-select: auto !important;">The input consists of multiple datasets, each in the following format.</p>

<blockquote style="user-select: auto !important;"><i style="user-select: auto !important;">m</i> <i style="user-select: auto !important;">n</i> <i style="user-select: auto !important;">p</i> <i style="user-select: auto !important;">a</i><sub style="user-select: auto !important;">1</sub> <i style="user-select: auto !important;">b</i><sub style="user-select: auto !important;">1</sub> … <i style="user-select: auto !important;">a<sub style="user-select: auto !important;">n</sub></i> <i style="user-select: auto !important;">b<sub style="user-select: auto !important;">n</sub></i></blockquote>

<p style="user-select: auto !important;">Each of the datasets starts with a line containing three integers: <i style="user-select: auto !important;">m</i> (1 ≤ <i style="user-select: auto !important;">m</i> ≤ 100) is the number of users, <i style="user-select: auto !important;">n</i> (0 ≤ <i style="user-select: auto !important;">n</i> ≤ 1000) is the number of events in the list, and <i style="user-select: auto !important;">p</i> (1 ≤ <i style="user-select: auto !important;">p</i> ≤ <i style="user-select: auto !important;">m</i>) is the ID of the user confirmed to be infected.</p>

<p style="user-select: auto !important;">The following <i style="user-select: auto !important;">n</i> lines contain the close contact events between users, one event per line, in time order. Each line indicates that the users whose IDs are <i style="user-select: auto !important;">a<sub style="user-select: auto !important;">i</sub></i> and <i style="user-select: auto !important;">b<sub style="user-select: auto !important;">i</sub></i> had close contact. Here, <i style="user-select: auto !important;">a<sub style="user-select: auto !important;">i</sub></i> and <i style="user-select: auto !important;">b<sub style="user-select: auto !important;">i</sub></i> satisfy 1 ≤ <i style="user-select: auto !important;">a<sub style="user-select: auto !important;">i</sub></i> ≤ <i style="user-select: auto !important;">m,</i> 1 ≤ <i style="user-select: auto !important;">b<sub style="user-select: auto !important;">i</sub></i> ≤ <i style="user-select: auto !important;">m,</i> and <i style="user-select: auto !important;">a<sub style="user-select: auto !important;">i</sub></i> ≠ <i style="user-select: auto !important;">b<sub style="user-select: auto !important;">i</sub></i>.</p>

<p style="user-select: auto !important;">The end of the input is indicated by a line containing three zeros. The number of datasets does not exceed 50.</p>

### 출력 

 <p style="user-select: auto !important;">For each dataset, output a single line containing the total number of users including the user confirmed to be infected and users to whom the virus was possibly transmitted directly or indirectly from the confirmed user.</p>

