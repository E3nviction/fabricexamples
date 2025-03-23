from fabric import Application
from fabric.widgets.box import Box
from fabric.widgets.button import Button
from fabric.widgets.wayland import WaylandWindow as Window
import subprocess

def get_random_quote():
	quote = subprocess.run(["fortune", "-s"], stdout=subprocess.PIPE)
	return quote.stdout.decode("utf-8")

class MyWindow(Window):
	def __init__(self, **kwargs):
		super().__init__(
			layer="bottom", # Sets the layer to bottom, so its behind windows
			anchor="bottom left", # Sets the window anchor to the top left
			exclusivity="none",
			margin=(5, 5, 5, 5), # Sets the margins from the screen edges
			all_visible=True,
			**kwargs
		)

		self.quote = Button(get_random_quote(), name="quote-widget-label", on_clicked=self.button_press, h_align="start")

		# Create the main box
		self.main_box = Box(
			orientation="v",
			name="main-box",
			children=[
				self.quote
			])

		self.add(self.main_box)

	def button_press(self, widget):
		self.quote.set_label(get_random_quote())

if __name__ == "__main__":
	desktop_widget = MyWindow()
	app = Application("quote-widget", desktop_widget)
	# Sets the CSS
	app.set_stylesheet_from_file("style.css")
	app.run()
