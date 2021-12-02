object Pb2 {
	def solution(directions: List[Tuple]): Int = {
		var depth = 0
		var horizontal = 0
		for((a: String, b: Int) <- directions) {
			a match {
				case "forward" => horizontal += b
				case "down" => depth += b
				case "up" => depth -= b
			}
		}

		return depth * horizontal
	}

	def solution2(directions: List[Tuple]): Int = {
		var depth = 0
		var horizontal = 0
		var aim = 0
		for((a: String, b: Int) <- directions) {
			a match {
				case "forward" => horizontal += b; depth += aim * b
				case "down" => aim += b
				case "up" => aim -= b
			}
		}

		return depth * horizontal
	}	
	
	def main(args: Array[String]) = {
		val directions = io.Source.fromFile("../resources/input2.txt")
			.getLines.toList.map(line => line.split(" ")).map(x => (x(0), x(1).toInt))
		println("Solution part n° 1: " + solution(directions))
		println("Solution part n° 2: " + solution2(directions))
	}	
}