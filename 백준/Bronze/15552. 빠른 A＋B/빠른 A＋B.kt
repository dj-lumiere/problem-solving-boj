import java.io.*
import java.util.*

// Custom input function
val input: () -> String = {
    if (tokens.hasNext()) tokens.next()
    else throw NoSuchElementException("No more tokens available")
}

// Custom print function for standard output
fun print(vararg args: Any?, sep: String = " ", end: String = "\n") {
    val output = args.joinToString(separator = sep) { it.toString() }
    System.out.print(output + end)
}

// Custom eprint function for standard error
fun eprint(vararg args: Any?, sep: String = " ", end: String = "\n") {
    val output = args.joinToString(separator = sep) { it.toString() }
    System.err.print(output + end)
}

// Custom fprint function for file output
fun fprint(vararg args: Any?, sep: String = " ", end: String = "\n", file: PrintWriter) {
    val output = args.joinToString(separator = sep) { it.toString() }
    file.print(output + end)
    file.flush()
}

lateinit var tokens: Iterator<String>

fun main() {
    val USE_FILE = false // Set to 'false' to use standard input

    // Set up input stream
    val inputStream: InputStream = if (USE_FILE) {
        File("input2.txt").inputStream()
    } else {
        System.`in`
    }

    val reader = BufferedReader(InputStreamReader(inputStream))
    var tokenizer = StringTokenizer("")

    val input: () -> String = {
        while (!tokenizer.hasMoreTokens()) {
            val line = reader.readLine() ?: throw NoSuchElementException("No more tokens available")
            tokenizer = StringTokenizer(line)
        }
        tokenizer.nextToken()
    }
    val t = input().toInt()
    val DELTA = arrayListOf(0 to 0, 0 to -1, 0 to 1, -1 to 0, 1 to 0)
    val isInbound =
        { posX: Int, sizeX: Int, posY: Int, sizeY: Int -> (0 <= posX) && (posX < sizeX) && (0 <= posY) && (posY < sizeY) }
    val answers = arrayListOf<String>()
    for (h in 1..t) {
        val a = input().toInt()
        val b = input().toInt()
        val answer = a+b
        answers.add("${a+b}")
    }
    print(*answers.toTypedArray(), sep="\n")
}