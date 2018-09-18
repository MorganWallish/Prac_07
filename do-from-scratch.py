from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class DoFromScratch(App):
    def build(self):
        Window.size = (400, 200)
        self.title = 'Do from scratch'
        self.root = Builder.load_file('do-from-scratch.kv')
        return self.root
    def convert_miles_to_kilometres(self, value):
        result = value * 1.60934
        self.root.ids.output_label.text = str(result)

DoFromScratch().run()
