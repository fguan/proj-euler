object P1 extends Application {
  println((1 to 999).foldLeft (0) {(total, x) => 
    x match {
      case i if (i % 3 == 0 || i % 5 ==0) => i + total
      case _ => total
    }
  }) // 233168
}
