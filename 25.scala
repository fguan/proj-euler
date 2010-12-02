import java.math.BigInteger

object P25 extends Application {
  var cur = new BigInteger("1")
  var prev = new BigInteger("1")
  var next = new BigInteger("1") // dummy value for now
  var index = 2

  // find the index
  while (cur.toString().length() < 1000) {
    next = cur.add(prev)
    prev = cur
    cur = next
    index += 1
  }
  
  println(index) // 4782
}

