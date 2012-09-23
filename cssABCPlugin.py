import sublime, sublime_plugin
import cssABC

class CssabcCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        print("CSSABC")
        fullViewRegion = sublime.Region( 0, self.view.size() )
        fullContent = self.view.substr(fullViewRegion)
        cssABC.main(fullContent)

        # self.view.insert(edit, 0, "Hello, World!")
        # print("Hello World")
