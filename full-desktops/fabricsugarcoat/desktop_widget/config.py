from fabric import Application
from fabric.widgets.box import Box
from fabric.widgets.datetime import DateTime
from fabric.widgets.wayland import WaylandWindow as Window
from fabric.utils import get_relative_path

class MyWindow(Window):
    def __init__(self, **kwargs):
        super().__init__(
            name="desktop-widget",
            layer="bottom",
            anchor="center",
            exclusivity="none",
            child=Box(
                orientation="v",
                children=[
                    DateTime(formatters=["%A. %d %B"], interval=10000, name="date"),
                    DateTime(formatters=["%I:%M"], name="clock"),
                ],
            ),
            all_visible=True,
            **kwargs
        )

if __name__ == "__main__":
    desktop_widget = MyWindow()

    app = Application("desktop-widget", desktop_widget)
    app.set_stylesheet_from_file(get_relative_path("./style.css"))

    app.run()
