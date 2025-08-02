from krita import Extension, Krita, Filter

class GrayscaleOverlayExtension(Extension):
    def __init__(self, parent):
        super().__init__(parent)

    def setup(self):
        pass

    def createActions(self, window):
        action = window.createAction(
            "add_grayscale_overlay", 
            "Add Grayscale Overlay (Lightness)", 
            "tools/scripts"
        )
        action.triggered.connect(self.add_grayscale_overlay)

    def add_grayscale_overlay(self):
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

            duplicated = node.duplicate()
            duplicated.setName(node.name() + "_Grayscale")

            parent = node.parentNode()
            try:
                parent.addChildNode(duplicated, node)
            except Exception as e:
                print(f"Failed to insert duplicated layer above node: {e}")
                root = doc.rootNode()
                children = root.childNodes()
                root.addChildNode(duplicated, children[0] if children else None)

            grayscale_filter = Filter.filter("desaturate")
            if not grayscale_filter:
                print("Desaturate filter not found.")
                return

            config = grayscale_filter.configuration()
            config.setProperty("desaturationType", "lightness")  
            grayscale_filter.setConfiguration(config)

            rect = duplicated.bounds()
            grayscale_filter.apply(duplicated, rect)

            doc.refreshProjection()
            print("Grayscale overlay added successfully.")

        except Exception as e:
            print(f"Error in add_grayscale_overlay: {e}")

app = Krita.instance()
app.addExtension(GrayscaleOverlayExtension(app))
