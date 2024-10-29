import sublime
import sublime_plugin
from json import loads
from json.decoder import JSONDecodeError
from logging import getLogger
logger = getLogger(__name__)

#view.run_command('wiregock')
class WiregockCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		wiregock_validate(self.view.substr(sublime.Region(0, self.view.size())))

def wiregock_error(msg):
	logger.error(msg)
	sublime.error_message(msg)
	return False

def wiregock_info(msg):
	logger.info(msg)
	sublime.status_message(msg)
	sublime.message_dialog(msg)
	return True

def wiregock_validate(text):
	jsData = None
	try:
		jsData = loads(text)
	except JSONDecodeError as e:
		return wiregock_error("Error while parsing JSON:\n{0}\n{1}".format(text, str(e)))
	if jsData is None:
		return False
	if not isinstance(jsData, list):
		jsData = [jsData]
	for js in jsData:
		if 'request' not in js:
			return wiregock_error("Provided JSON doesn't contain 'request' object")
		request = js['request']
		if 'urlPath' not in request and 'urlPattern' not in request:
			return wiregock_error("Provided JSON 'request' object doesn't contain 'urlPath' or 'urlPattern'")
	return wiregock_info("Wiregock validation passed. Everything is OK")