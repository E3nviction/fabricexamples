from side_panel.config import SidePanel
from desktop_widget.config import MyWindow
from bar.config import StatusBar
from notifications.config import MyWindow as NotificationWindow

from fabric import Application
from fabric.utils import get_relative_path

if __name__ == "__main__":
    app = Application("fabricsugarcoatshell", SidePanel(), MyWindow(), StatusBar(), NotificationWindow())
    app.set_stylesheet_from_string("* {all: unset;}")
    app.set_stylesheet_from_file(get_relative_path("./side_panel/style.css"), append=True)
    app.set_stylesheet_from_file(get_relative_path("./desktop_widget/style.css"), append=True)
    app.set_stylesheet_from_file(get_relative_path("./bar/style.css"), append=True)
    app.set_stylesheet_from_file(get_relative_path("./notifications/style.css"), append=True)

    app.run()