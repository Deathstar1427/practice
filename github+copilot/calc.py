"""
Simple calculator GUI using Tkinter.
Supports digits 0-9, +, -, *, /, and equals.
"""

import tkinter as tk


class CalculatorApp:
	def __init__(self, root):
		self.root = root
		root.title("Calculator")

		self.display_var = tk.StringVar(value="0")
		self.current_input = ""
		self.stored_value = None
		self.operator = None

		display = tk.Entry(
			root,
			textvariable=self.display_var,
			font=("Segoe UI", 16),
			justify="right",
			bd=4,
			relief=tk.RIDGE,
			state="readonly",
			readonlybackground="white",
		)
		display.grid(row=0, column=0, columnspan=4, padx=8, pady=8, sticky="nsew")

		buttons = [
			("7", self.press_digit), ("8", self.press_digit), ("9", self.press_digit), ("/", self.set_operator),
			("4", self.press_digit), ("5", self.press_digit), ("6", self.press_digit), ("*", self.set_operator),
			("1", self.press_digit), ("2", self.press_digit), ("3", self.press_digit), ("-", self.set_operator),
			("0", self.press_digit), ("C", self.clear), ("=", self.calculate), ("+", self.set_operator),
		]

		for idx, (text, handler) in enumerate(buttons):
			row = 1 + idx // 4
			col = idx % 4
			btn = tk.Button(root, text=text, width=5, height=2, command=lambda t=text, h=handler: h(t))
			btn.grid(row=row, column=col, padx=4, pady=4, sticky="nsew")

		for i in range(4):
			root.grid_columnconfigure(i, weight=1)
		for i in range(5):
			root.grid_rowconfigure(i, weight=1)

	def press_digit(self, digit):
		if self.current_input == "0":
			self.current_input = digit
		else:
			self.current_input += digit
		self.display_var.set(self.current_input)

	def set_operator(self, op):
		if self.current_input:
			self._store_current()
		self.operator = op
		self.current_input = ""

	def calculate(self, _=None):
		if self.operator is None or not self.current_input:
			return
		try:
			right = float(self.current_input)
		except ValueError:
			self.display_var.set("Error")
			self.current_input = ""
			return

		if self.stored_value is None:
			return

		try:
			result = self._apply_operator(self.stored_value, right, self.operator)
		except ZeroDivisionError:
			self.display_var.set("Divide by 0")
			self._reset_state()
			return

		self.display_var.set(self._format_number(result))
		self.stored_value = result
		self.current_input = ""
		self.operator = None

	def clear(self, _=None):
		self.display_var.set("0")
		self._reset_state()

	def _store_current(self):
		try:
			value = float(self.current_input)
		except ValueError:
			self.display_var.set("Error")
			self.current_input = ""
			return
		if self.stored_value is None:
			self.stored_value = value
		elif self.operator:
			try:
				self.stored_value = self._apply_operator(self.stored_value, value, self.operator)
			except ZeroDivisionError:
				self.display_var.set("Divide by 0")
				self._reset_state()
				return
		self.display_var.set(self._format_number(self.stored_value))

	@staticmethod
	def _apply_operator(left, right, op):
		if op == "+":
			return left + right
		if op == "-":
			return left - right
		if op == "*":
			return left * right
		if op == "/":
			if right == 0:
				raise ZeroDivisionError
        
			return left / right
		raise ValueError("Unknown operator")

	@staticmethod
	def _format_number(value):
		if value.is_integer():
			return str(int(value))
		return str(value)

	def _reset_state(self):
		self.current_input = ""
		self.stored_value = None
		self.operator = None


def main():
	root = tk.Tk()
	CalculatorApp(root)
	root.mainloop()


if __name__ == "__main__":
	main()
