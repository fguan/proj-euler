import java.math.BigInteger

object P16 extends Application {
  val i = new BigInteger("2").pow(1000).toString()

  def sumDigits(num: String): Int = {
    var sum = 0
    num foreach { c => sum += c.asDigit }
    sum
  }
  println(sumDigits(i)) // 1366
}

