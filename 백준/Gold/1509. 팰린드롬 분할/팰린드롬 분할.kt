package problemSolving

import java.util.*

fun main() = with(Scanner(System.`in`)) {
    val a: String = nextLine()
    val aArray = ArrayList<Char>(a.map { it })
    val isPalindromic =
        ArrayList<ArrayList<Boolean>>(List(a.length) { ArrayList(List(a.length) { false }) })
    for (x in a.indices) {
        for (y in 0 until a.length - x) {
            val j = y + x
            if (y + 1 > j - 1) {
                isPalindromic[y][j] = (aArray[y] == aArray[j])
                continue
            }
            isPalindromic[y][j] = (aArray[y] == aArray[j]) and (isPalindromic[y + 1][j - 1])
        }
    }
    val minimalPartitionCount: ArrayList<Int> = ArrayList(List(a.length) { 0 })
    minimalPartitionCount[0] = 1
    for (i in 1 until a.length) {
        val subCounts = ArrayList<Int>(List(1) { minimalPartitionCount[i - 1] + 1 })
        for (j in 0 until i) {
            if (isPalindromic[j][i]) {
                subCounts.add(if (j >= 1) minimalPartitionCount[j - 1] + 1 else 1)
            }
        }
        minimalPartitionCount[i] = subCounts.min()
    }
    println(minimalPartitionCount[minimalPartitionCount.size - 1])
}