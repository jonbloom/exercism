class Garden(object):

	_default_students = ['Alice', 'Bob', 'Charlie', 'David',
				'Eve', 'Fred', 'Ginny', 'Harriet',
				'Ileana', 'Joseph', 'Kincaid', 'Larry']
	_plants = {'G': 'Grass', 'C': 'Clover', 'R': 'Radishes', 'V': 'Violets'}

	def __init__(self, diagram, students=_default_students):
		self._row1 = diagram.split('\n')[0]
		self._row2 = diagram.split('\n')[1]
		self._students = sorted(students)
			
	def plants(self, student):
		rtn = list()
		i = self._students.index(student)*2
		for plant in self._row1[i:i+2]:
			rtn.append(self._plants[plant])
		for plant in self._row2[i:i+2]:
			rtn.append(self._plants[plant])
		return rtn