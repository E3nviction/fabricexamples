from fabric.utils import get_relative_path
from quotewidget.main import MyWindow as QuoteWindow
from statswidget.main import MyWindow as StatsWindow
from toppanel.main import MyWindow as TopPanelWindow

from fabric import Application

if __name__ == "__main__":
	app = Application("papershell", QuoteWindow(), StatsWindow(), TopPanelWindow())
	# Sets the CSS
	app.set_stylesheet_from_file(get_relative_path("style.css"))
	app.run()