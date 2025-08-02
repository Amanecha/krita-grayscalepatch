from krita import *

class TemplateCreatorExtension(Extension):
    def __init__(self, parent):
        super().__init__(parent)

    def setup(self):
        pass

    def createActions(self, window):
        print("createActions called")
        action = window.createAction("create_template_canvas", "create_template", "tools/scripts")
        action.triggered.connect(self.create_template)

    def create_template(self):
        print("Creating template...")
        doc = Krita.instance().createDocument(1920, 1080, "New Template", "RGBA", "U8", "", 300.0)
        Krita.instance().activeWindow().addView(doc)

# Register the extension
Krita.instance().addExtension(TemplateCreatorExtension(Krita.instance()))
