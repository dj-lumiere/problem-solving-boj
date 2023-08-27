# 13727 5차원 구사과 초콜릿

from itertools import product

MOD = 10**9 + 7


def find_recurrence_polynomial(sequence: list[int]) -> list[int]:
    last_recurrence = []
    current_recurrence = []
    last_fail_position = 0
    last_discrepancy = 0
    for i in range(len(sequence)):
        temp = 0
        for j in range(len(current_recurrence)):
            temp += sequence[i - j - 1] * current_recurrence[j] % MOD
            temp %= MOD
        discrepancy = (temp - sequence[i]) % MOD
        if not discrepancy:
            continue
        if not current_recurrence:
            current_recurrence.extend([0] * (i + 1 - len(current_recurrence)))
            last_fail_position = i
            last_discrepancy = discrepancy
            continue

        k = -(sequence[i] - temp) * pow(last_discrepancy, -1, MOD) % MOD
        new_poly = [0] * (i - last_fail_position - 1) + [k]
        for v in last_recurrence:
            new_poly.append(-v * k % MOD)
        if len(new_poly) < len(current_recurrence):
            new_poly.extend([0] * (len(current_recurrence) - len(new_poly)))
        for j, v in enumerate(current_recurrence):
            new_poly[j] += v
            new_poly[j] %= MOD
        if i - last_fail_position + len(last_recurrence) >= len(current_recurrence):
            last_recurrence, last_fail_position, last_discrepancy = (
                current_recurrence[:],
                i,
                discrepancy,
            )
        current_recurrence = new_poly[:]

    for i, v in enumerate(current_recurrence):
        current_recurrence[i] = v % MOD
    return current_recurrence


def polynomial_multiply(target1, target2, recurrence_polynomial):
    polynomial_order = len(target1)
    result = [0] * (2 * polynomial_order)
    for i, j in product(range(polynomial_order), repeat=2):
        result[i + j] += target1[i] * target2[j] % MOD
        result[i + j] %= MOD
    for i, j in product(
        range(2 * polynomial_order - 1, polynomial_order - 1, -1),
        range(1, polynomial_order + 1),
    ):
        result[i - j] += result[i] * recurrence_polynomial[j - 1] % MOD
        result[i - j] %= MOD
    result = result[:polynomial_order]
    return result


def get_value(recurrence_polynomial, sequence, index):
    polynomial_order = len(recurrence_polynomial)
    accumulated_polynomial = [0] * polynomial_order
    squared_polynomial = [0] * polynomial_order
    accumulated_polynomial[0] = 1
    if polynomial_order != 1:
        squared_polynomial[1] = 1
    else:
        squared_polynomial[0] = recurrence_polynomial[0]
    while index > 0:
        if index & 1:
            accumulated_polynomial = polynomial_multiply(
                accumulated_polynomial, squared_polynomial, recurrence_polynomial
            )
        squared_polynomial = polynomial_multiply(
            squared_polynomial, squared_polynomial, recurrence_polynomial
        )
        index >>= 1
    result = 0
    for v1, v2 in zip(accumulated_polynomial, sequence):
        result += v1 * v2 % MOD
    return result % MOD


def get_nth_term(sequence, index):
    if index < len(sequence):
        return sequence[index]
    recurrence_polynomial = find_recurrence_polynomial(sequence)
    if not recurrence_polynomial:
        return 0
    return get_value(recurrence_polynomial, sequence, index)


sequence = [272, 589185, 930336768, 853401154, 217676188, 136558333, 415722813, 985269529, 791527976, 201836136, 382110354, 441223705, 661537677, 641601343, 897033284, 816519670, 365311407, 300643484, 936803543, 681929467, 462484986, 13900203, 657627114, 96637209, 577140657, 600647073, 254604056, 102389682, 811580173, 592550067, 587171680, 526467503, 265885773, 951722780, 219627841, 371508152, 283501391, 159234514, 439380999, 722868959, 125599834, 351398134, 456317548, 365496182, 614778702, 502680047, 193063685, 309004764, 743901785, 870955115, 312807829, 160375015, 691844624, 137034372, 350330868, 895680450, 282610535, 317897557, 28600551, 583305647, 539409363, 327406961, 627805385, 680183978, 681299085, 954964592, 743524009, 788048339, 699454626, 666369521, 857206425, 490463127, 477198247, 599963928, 21247982, 107843532, 753662937, 239039324, 608530376, 523383010, 654448101, 801430395, 393034561, 93313778, 983052766, 240336620, 825539982, 525118275, 563899476, 706271688, 547405697, 477082486, 664058071, 353207278, 729486413, 795704637, 999271072, 540749624, 411451016, 736422999, 879369181, 918733916, 982303557, 512499644, 261033810, 391766409, 334092786, 931794834, 854181848, 821090190, 751839258, 433126935, 571194155, 52438113, 552977155, 320805296, 173355929, 969659468, 258854248, 159509877, 374487748, 401382023, 44060530, 510164669, 336596764, 652050424, 373872552, 517226592, 719871041, 43959496, 235333335, 304962191, 253114421, 43638769, 361871585, 8060121, 147014624, 114846460, 430864038, 368951246, 863795701, 36066788, 971606149, 935875286, 486724123, 73790652, 236936530, 307697424, 753314001, 40450345, 529462842, 166162047, 974102330, 600865526, 63237062, 749041914, 670937123, 806399597, 776678839, 842565920, 608499253, 469062485, 842196981, 247762946, 778570576, 237951782, 286343384, 988318575, 147255879, 905747089, 711062313, 21396079, 826846622, 443781794, 786474911, 400737121, 844768961, 686214818, 590050845, 855473150, 18501778, 33258755, 398169058, 811192244, 710397887, 591757177, 775311969, 168256434, 509615161, 489764304, 605188191, 498085780, 164388183, 524662873, 322602324, 853641480, 205349527, 308211944, 93153206, 734257752]
index = int(input())
index -= 1
print(get_nth_term(sequence, index))