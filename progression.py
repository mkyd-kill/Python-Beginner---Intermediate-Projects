class Progression:

	def __init__(self, start=0):
		self._current = start

	def _advance(self):
		self._current += 1

	def __next__(self):
		if self._current is None:
			raise StopIteration()
		else:
			answer = self._current
			self._advance()
			return answer

	def __iter__(self):
		return self

	def print_progression(self, n):
		print(' '.join(str(next(self)) for j in range(n)))


class ArithmeticProgression(Progression):

	def __init__(self, increment=0, start=0):
		super().__init__(start)
		self._increment = increment

	def _advance(self):
		self._current += self._increment


class GeometricProgression(Progression):

	def __init__(self, base=2, start=1):
		super().__init__(start)
		self._base = base

	def _advance(self):
		self._current *= self._base


class FibonacciProgression(Progression):

	def __init__(self, first=0, second=1):
		super().__init__(first)
		self._prev = second - first

	def _advance(self):
		self._prev, self._current = self._current, self._prev + self._current

if __name__ == '__main__':
	# testing the progressions
	print('Default progression:')
	Progression().print_progression(10)

	print('\nArithmeric progression with incrememt 5:')
	ArithmeticProgression(5).print_progression(10)

	print('\nArithmetic progression with start 2 & increment 5:')
	ArithmeticProgression(5,2).print_progression(10)

	print('\nGeometric Progression with default base:')
	GeometricProgression().print_progression(10)

	print('\nGeometric progression with base 3:')
	GeometricProgression(3).print_progression(10)

	print('\nFibonacci progression with default values:')
	FibonacciProgression().print_progression(10)

	print('\nFibonacci progression with start values 4 & 6:')
	FibonacciProgression(4,6).print_progression(10)
