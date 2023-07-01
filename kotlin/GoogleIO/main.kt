package com.jetbrains.gio

// data class
data class Money(val amount: Int, val currency: String)

//function, parameter
fun sendPayment(money:Money, message:String =""){
    println("Sending ${money.amount}")
}

fun sum(x:Int, y:Int) = x + y

fun converToDollor(moeny:Money): Money {
    return when (money.currency){
        "$" -> return  money
        "EUR" -> return Money(money.amount * BigDecimal(1.10), "$")
        else -> throw IllegalArgumentException("Not the currency you are interested in!")
    }
}

// Type inference
fun main(args: Array<String>){
    val tickets = Money(100, "$")
    val popcorn = tickets.copy(500, "EUR")

    //function, parameter
    sendPayment(message="Good lock", money =tickets)

    if (tickets != popcorn){
        println("They are different!")
    }

}

