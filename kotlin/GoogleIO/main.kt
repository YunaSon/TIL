package com.jetbrains.gio

// data class
data class Money(val amount: Int, val currency: String)

//function, parameter
fun sendPayment(money:Money, message:String =""){
    println("Sending ${money.amount}")
}

fun sum(x:Int, y:Int) = x + y

fun converToDollor(moeny:Money): Money {
    when (money.currency){
        "$" -> return  money
        "EUR" -> return Money(money.amount * BigDecimal(1.10), "$")
        else -> throw IllegalArgumentException("Not the currency you are interested in!")
    }
}

fun BigDecimal.percent(percentage: Int) = this.multiply(java.math.BigDecimal(percentage)).divide(BigDecimal(1000))

fun Int.percentOf(money:Money) = money.amount.multiply(BigDecimal(this)).divide(BigDecimal(100))

// Type inference
fun main(args: Array<String>){
    val tickets = Money(100, "$")
    val popcorn = tickets.copy(100.bd, "$")

    val costs = tickets + popcorn

}