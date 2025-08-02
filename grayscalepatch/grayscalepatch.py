from krita import Extension, Krita, Filter

class GrayscaleOverlayExtension(Extension):
    def __init__(self, parent):
        super().__init__(parent)

    def setup(self):
        pass

    def createActions(self, window):
        action = window.createAction(
            "add_non_destructive_grayscale", 
            "Add Grayscale Filter Layer (Lightness)", 
            "tools/scripts"
        )
        action.triggered.connect(self.add_grayscale_filter_layer)

    def add_grayscale_filter_layer(self):
        try:
            app = Krita.instance()
            doc = app.activeDocument()
            if not doc:
                print("No active document.")
                return

            node = doc.activeNode()
            if not node:
                print("No active node.")
                return

            grayscale_filter = Krita.instance().filter("desaturate")
            if not grayscale_filter:
                print("Desaturate filter not found.")
                return

            config = grayscale_filter.configuration()
            config.setProperty("desaturationType", "lightness")
            grayscale_filter.setConfiguration(config)

            filter_mask = doc.createFilterMask("Grayscale_Filter", grayscale_filter, node)

            node.addChildNode(filter_mask, None)

            doc.refreshProjection()
            print("グレースケールのフィルターマスクを追加しました。")

        except Exception as e:
            print(f"Error: {e}")



app = Krita.instance()
app.addExtension(GrayscaleOverlayExtension(app))
