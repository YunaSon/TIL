// function structure
// variable declare : val
// variable format $, ${}
// type inference


// function structure
fun main() {
    println("Hello, world!")
}

main()

// variable declare
fun count() {
    val count: Int = 2
    println(count)
}

count()

// format
fun formatex() {
    val count: Int = 10
    println("You have $count unread messages.")
}

formatex()

//type inference
fun typeinference() {
    val unreadCount = 5
    val readCount = 100
    val messages = "numbers"
    println("You have ${unreadCount + readCount} total ${messages}  in your inbox.")
}

typeinference()
