import java.util.*

fun main() = with(Scanner(System.`in`)) {
    val a = nextInt()
    val b = nextInt()
    val c = nextInt()
    val d = nextInt()
    val e = nextInt()
    val isFrozen = (a < 0)
    val time = if (isFrozen) {
        c * (-a) + d + e * b
    } else {
        e * (b - a)
    }
    println(time)
}