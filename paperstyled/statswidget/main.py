from fabric import Application
from fabric.widgets.box import Box
from fabric.widgets.datetime import DateTime
from fabric.widgets.scale import Scale
from fabric.widgets.image import Image
from fabric.widgets.label import Label
from fabric.widgets.wayland import WaylandWindow as Window
from fabric.audio import Audio
import psutil
import time
import threading

from gi.repository import GLib # type: ignore

class MyWindow(Window):
	def __init__(self, **kwargs):
		super().__init__(
			layer="bottom", # Sets the layer to bottom, so its behind windows
			anchor="top left", # Sets the window anchor to the top left
			exclusivity="none",
			margin=(10, 10, 10, 10), # Sets the margins from the screen edges
			all_visible=True,
			**kwargs
		)

		# Window size
		self.set_size_request(250, 350)

		# Connect to the audio service
		self.audio = Audio()
		# Everytime audio changes call the volume_changed function
		self.audio.connect("changed", self.volume_changed)

		self.mac_image = Image(
			image_file="imac.png",
		)

		self.volume_scale = Scale(value=0, min_value=0, max_value=100, increments=(5, 5), name="volume-widget-slider", size=50, h_expand=True)
		self.volume = Box(
			orientation="h",
			children=[
				Label("vol", name="volume-widget-label", h_align="start"),
				self.volume_scale
			])

		self.cpu_scale = Scale(value=0, min_value=0, max_value=100, increments=(5, 5), name="cpu-widget-slider", size=30, h_expand=True)
		self.cpu = Box(
			orientation="h",
			children=[
				Label("cpu", name="cpu-widget-label", h_align="start"),
				self.cpu_scale
			])

		self.memory_scale = Scale(value=0, min_value=0, max_value=100, increments=(5, 5), name="memory-widget-slider", size=30, h_expand=True)
		self.memory = Box(
			orientation="h",
			children=[
				Label("ram", name="memory-widget-label", h_align="start"),
				self.memory_scale
			])

		# Create the main box
		self.main_box = Box(
			orientation="v",
			name="main-box",
			children=[
				self.mac_image,
				DateTime(formatters=["%I:%M %p"], name="clock"),
				self.volume,
				self.cpu,
				self.memory
			])

		self.add(self.main_box)

		threading.Thread(target=self.update_stats, daemon=True).start()

	def volume_changed(self, audio):
		# Checks if a speaker is connected
		if not audio.speaker: return
		# Sets the volume
		GLib.idle_add(lambda: self.volume_scale.set_value(audio.speaker.volume))

	def update_stats(self):
		while True:
			# Updates the stats
			GLib.idle_add(lambda: self.cpu_scale.set_value(psutil.cpu_percent()))
			GLib.idle_add(lambda: self.memory_scale.set_value(psutil.virtual_memory().percent))
			time.sleep(1)

if __name__ == "__main__":
	desktop_widget = MyWindow()
	app = Application("desktop-widget", desktop_widget)
	# Sets the CSS
	app.set_stylesheet_from_file("style.css")
	app.run()
