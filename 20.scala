import java.math.BigInteger

object P20 extends Application {
  def factorial(upper: Int): String = {
    var curr = new BigInteger("1")
    for (i <- (1 to upper)) {
      curr = curr.multiply(new BigInteger(""+i))
    }
    curr.toString()
  }
  val x = factorial(100)
  //println(x)

  def sumDigits(num: String): Int = {
    var sum = 0
    num foreach { c => sum += c.asDigit }
    sum
  }
  println(sumDigits(x)) // 648
}

