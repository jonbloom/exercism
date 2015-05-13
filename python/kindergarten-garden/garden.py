class Garden(object):

	_default_students = ['Alice', 'Bob', 'Charlie', 'David',
				'Eve', 'Fred', 'Ginny', 'Harriet',
				'Ileana', 'Joseph', 'Kincaid', 'Larry']
	_row1 = None
	_row2 = None
	_students = None

	def __init__(self, diagram, students=_default_students):
		self._row1 = diagram.split('\n')[0]
		self._row2 = diagram.split('\n')[1]
		self._students = sorted(students)

	def _get_long_name(self,initial):
		if initial == 'G':
			return 'Grass'
		elif initial == 'C':
			return 'Clover'
		elif initial == 'R':
			return 'Radishes'
		elif initial == 'V':
			return 'Violets'
		else:
			return None
			
	def plants(self, student):
		rtn = list()
		index = self._students.index(student)*2
		for plant in self._row1[index:index+2]:
			rtn.append(self._get_long_name(plant))
		for plant in self._row2[index:index+2]:
			rtn.append(self._get_long_name(plant))
		return rtn