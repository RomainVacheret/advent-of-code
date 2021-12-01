import scala.io.Source

object Pb1 {	
	def solution(ints: List[Int]): Int = {
		return (0 to ints.length - 2).map(idx => if(ints(idx) < ints(idx + 1)) 1 else 0).sum
	}

	def solution2(ints: List[Int]): Int = {
		return solution((0 to ints.length - 3).map(idx => ints(idx) + ints(idx + 1) + ints(idx + 2)).toList)
	}

	def main(args: Array[String]) = {
		val elements = io.Source.fromFile("../resources/input1.txt").getLines.toList.map(x => x.toInt)
		println("Solution part n° 1: " + solution(elements))
		println("Solution part n° 2: " + solution2(elements))
	}
}