import sublime
import sublime_plugin

#view.run_command('wiregock')
class WiregockCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		wiregock_validate(self.view.substr(sublime.Region(0, self.view.size())))

def wiregock_validate(text):
	from json import loads
	from json.decoder import JSONDecodeError
	from logging import getLogger
	logger = getLogger(__name__)
	js = None
	try:
		js = loads(text)
	except JSONDecodeError as e:
		logger.error("Error while parsing JSON:\n{0}\n{1}".format(text, str(e)))
		return False
	return True