import java.util.*
import kotlin.collections.ArrayList
import kotlin.math.max

var noColorChange = -1
fun findBoxNumber(boxConfiguration: String): Long {
    if (boxConfiguration.isEmpty()) {
        return 0L
    }
    var boxList: ArrayList<Long> = ArrayList(List<Long>(0) { 0 })
    for (i in boxConfiguration.indices) {
        val isBlack: Long = if (boxConfiguration[i] == 'B') {
            1L
        } else {
            -1L
        }
        boxList.add(isBlack)
    }
    var sign = 1L
    var result: Long
    val multiplier = 1L shl 40
    if (boxList[0] == -1L) {
        sign = -1L
        for (i in boxList.indices) {
            boxList[i] = boxList[i] * -1L
        }
    }
    var firstColorChange = noColorChange
    for (i in boxList.indices) {
        if (i == 0) {
            continue
        }
        if (boxList[i] != boxList[i - 1]) {
            firstColorChange = i - 1
            break
        }
    }
    if (firstColorChange == noColorChange) {
        result = multiplier * boxConfiguration.length * sign
        return result
    }
    result = multiplier * firstColorChange
    for (i in boxList.indices) {
        if (i < firstColorChange) {
            continue
        }
        result += boxList[i] * (multiplier shr (i - firstColorChange))
    }
    return sign * result
}

fun registerCombination(
    sumsMap: MutableMap<Long, Long>,
    status: Long,
    size: Int,
    numbers: ArrayList<ArrayList<Long>>,
    offset: Int
) {
    var totalValue = 0L
    var totalBoxCount = 0L
    for (i in 0 until size) {
        if (((status shr i) and 1) == 0L) {
            continue
        }
        totalValue += numbers[offset + i][0]
        totalBoxCount += numbers[offset + i][1]
    }
    if (!sumsMap.containsKey(totalValue)) {
        sumsMap[totalValue] = totalBoxCount
    } else {
        sumsMap[totalValue] = max(sumsMap[totalValue]!!, totalBoxCount)
    }
}

fun findMaxBoxNumber(numbers: ArrayList<ArrayList<Long>>): Int {
    val n = numbers.size
    val n1 = n / 2
    val n2 = n - n / 2
    val sumsLeft: MutableMap<Long, Long> = mutableMapOf()
    val sumsRight: MutableMap<Long, Long> = mutableMapOf()
    for (status in 1L until (1L shl n1)) {
        registerCombination(sumsLeft, status, n1, numbers, 0)
    }
    for (status in 1L until (1L shl n2)) {
        registerCombination(sumsRight, status, n2, numbers, n1)
    }
    var maxBoxCount = 0
    sumsLeft.forEach {
        val (value, boxCount) = it
        if (sumsRight.containsKey(-value)) {
            maxBoxCount = max(maxBoxCount, (boxCount + sumsRight[-value]!!).toInt())
        }
    }
    return maxBoxCount
}

fun main() = with(Scanner(System.`in`)) {
    val n = nextLine().toInt()
    val boxNumbers = ArrayList<ArrayList<Long>>(List(n) { ArrayList(List(2) { 0L }) })
    for (i in 0 until n) {
        val boxConfiguration = nextLine()
        boxNumbers[i] = arrayListOf(findBoxNumber(boxConfiguration), boxConfiguration.length.toLong())
    }
    boxNumbers.sortBy { (it[0] shl 10) - it[1] }
    val result = findMaxBoxNumber(boxNumbers)
    println(result)
}