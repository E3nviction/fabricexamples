from fabric import Application
from fabric.widgets.centerbox import CenterBox
from fabric.widgets.button import Button
from fabric.widgets.datetime import DateTime
from fabric.widgets.label import Label
from fabric.widgets.svg import Svg
from fabric.hyprland.widgets import ActiveWindow
from fabric.utils import FormattedString
from fabric.widgets.wayland import WaylandWindow as Window

class MyWindow(Window):
	def __init__(self, **kwargs):
		super().__init__(
			layer="overlay", # Sets the layer to bottom, so its behind windows
			anchor="top left right", # Sets the window anchor to the top left
			exclusivity="auto",
			margin=(10, 10, 10, 10), # Sets the margins from the screen edges
			all_visible=True,
			**kwargs
		)

		self.icon = Button(image=Svg("icon.svg", size=24), name="icon-button", h_align="start")

		self.active = ActiveWindow(formatter=FormattedString("{'Desktop' if not win_title else win_title}"))

		self.title = Label("Title", name="title-label", h_align="start")
		self.clock = DateTime(formatters=["%a %b %d  %H:%M %p"], name="clock-label", h_align="end")

		# Create the main box
		self.main_box = CenterBox(
			orientation="h",
			name="main-box",
			start_children=[
				self.icon,
			],
			center_children=[
				self.active
			],
			end_children=[
				self.clock
			]
		)

		self.add(self.main_box)

if __name__ == "__main__":
	desktop_widget = MyWindow()
	app = Application("quote-widget", desktop_widget)
	# Sets the CSS
	app.set_stylesheet_from_file("style.css")
	app.run()
