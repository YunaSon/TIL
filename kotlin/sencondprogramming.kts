// variable update: var
// data type

// variable update
fun main() {
    var cartTotal = 0
    cartTotal = 20
    println("Total: $cartTotal")
}

main()

fun add() {
    var count = 10
    println("You have $count unread messages.")
    count = count + 1
    println("$count")
    count++
    println("$count")
    count--
    println("$count")
}

add()

//data type
fun datatype() {
    val trip1: Double = 3.20
    val trip2: Double = 4.10
    val trip3: Double = 1.72
    val totalTripLength: Double = trip1 + trip2 + trip3
    println("$totalTripLength miles left to destination")
}



datatype()

fun sentence() {
    val nextMeeting = "Next meeting is:"
    val date = "January 1"
    val reminder = nextMeeting + date
    println(reminder)
}

sentence()

fun tf() {
    val notificationsEnabled: Boolean = false
    println("Are notifications enabled? " + notificationsEnabled)
}

tf()

/*
Summary
A variable is a container for a single piece of data.
You must declare a variable first before you use it.
Use the val keyword to define a variable that is read-only where the value cannot change once it's been assigned.
Use the var keyword to define a variable that is mutable or changeable.
In Kotlin, it's preferred to use val over var when possible.
To declare a variable, start with the val or var keyword. Then specify the variable name, data type, and initial value.
For example: val count: Int = 2.
With type inference, omit the data type in the variable declaration if an initial value is provided.
Some common basic Kotlin data types include: Int, String, Boolean, Float, and Double.
Use the assignment operator (=) to assign a value to a variable either during declaration of the variable or updating the variable.
You can only update a variable that has been declared as a mutable variable (with var).
Use the increment operator (++) or decrement operator (--) to increase or decrease the value of an integer variable by 1, respectively.
Use the + symbol to concatenate strings together. You can also concatenate variables of other data types like Int and Boolean to Strings.
Learn more
        Variables
Basic types
        String templates
        Keywords and operators
Basic syntax
 */