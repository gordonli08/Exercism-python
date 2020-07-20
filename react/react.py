class Observable():
	def __init__(self):
		self.observers = []

	def register_observer(self, observer):
		self.observers.append(observer)

	def notify_observers(self):
		for o in self.observers:
			o.update()

#The Observable
class InputCell(Observable):
	def __init__(self, initial_value):
		super().__init__()
		self._value = initial_value
	
	@property
	def value(self):
		return self._value

	@value.setter
	def value(self, new_value):
		if self._value != new_value:
			self._value = new_value
			self.notify_observers()


#The Observer which is also an Observable sometimes
class ComputeCell(Observable):
	def __init__(self, inputs, compute_function):
		super().__init__()
		self.observables = inputs
		self.comp_f = compute_function
		self.callbacks = []

		self._value = self.comp_f([cell.value for cell in inputs])

		for cell in inputs:
			cell.register_observer(self)


	def add_callback(self, callback):
		self.callbacks.append(callback)

	def remove_callback(self, callback):
		if callback in self.callbacks:
			self.callbacks.remove(callback)

	@property
	def value(self):
		return self.update()

	def update(self):
		new_value = self.comp_f([cell.value for cell in self.observables])

		if self._value != new_value:
			self._value = new_value

			for cb in self.callbacks:
				cb(new_value)

			self.notify_observers()

		return self._value
