import sublime, sublime_plugin
import cssABC

class CssabcCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        print("CSSABC Plugin")
        fullViewRegion = sublime.Region( 0, self.view.size() )
        fullContent = self.view.substr(fullViewRegion)
        sortedCSSContent = cssABC.main(fullContent)
        # print(sortedCSSContent)
        self.window = self.view.window()
        self.window.new_file().insert(edit, 0, sortedCSSContent)
        # sublime.Window.new_file()
        # self.view.insert(edit, 0, "Hello, World!")
        # print("Hello World")
