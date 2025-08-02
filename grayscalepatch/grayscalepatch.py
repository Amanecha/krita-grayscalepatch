from krita import Extension, Krita, Filter
from PyQt5.QtWidgets import QMessageBox, QApplication

class GrayscaleOverlayExtension(Extension):
    def __init__(self, parent):
        super().__init__(parent)

    def setup(self):
        pass

    def createActions(self, window):
        print("createActions called")
        try:
            action = window.createAction(
                "add_non_destructive_grayscale", 
                "Add Grayscale Filter Layer (Lightness)", 
                "tools/scripts"
            )
            action.triggered.connect(self.add_grayscale_filter_layer)
            print("✅ アクションが正常に追加されました")
        except Exception as e:
            print(f"❌ createActions 中に例外: {e}")

    def add_grayscale_filter_layer(self):
        try:
            app = Krita.instance()
            doc = app.activeDocument()
            if not doc:
                print("No active document.")
                return

            # モード選択ダイアログを表示
            mode = self.ask_user_mode()
            if mode is None:
                print("キャンセルされました。")
                return

            if mode == "merge":
                # 全レイヤーをマージ
                merged = doc.rootNode().clone()
                merged.setName("Merged_Layers")
                doc.rootNode().addChildNode(merged, None)
                node = merged
            else:
                node = doc.activeNode()

            # フィルター取得
            grayscale_filter = Krita.instance().filter("desaturate")
            if not grayscale_filter:
                print("Desaturate filter not found.")
                return

            config = grayscale_filter.configuration()
            config.setProperty("desaturationType", "lightness")
            grayscale_filter.setConfiguration(config)

            # フィルターマスク作成
            filter_mask = doc.createFilterMask("Grayscale_Filter", grayscale_filter, node)
            node.addChildNode(filter_mask, None)

            doc.refreshProjection()
            print("✅ グレースケールのフィルターマスクを追加しました。")

        except Exception as e:
            print(f"❌ Error: {e}")

    def ask_user_mode(self):
        parent_window = QApplication.activeWindow()

        msg = QMessageBox(parent_window)
        msg.setWindowTitle("グレースケール適用対象")
        msg.setText("どのレイヤーに適用しますか？")
        merge_button = msg.addButton("全レイヤーをマージして適用", QMessageBox.AcceptRole)
        active_button = msg.addButton("現在のレイヤーに適用", QMessageBox.YesRole)
        cancel_button = msg.addButton("キャンセル", QMessageBox.RejectRole)

        msg.exec_()

        clicked = msg.clickedButton()
        if clicked == merge_button:
            return "merge"
        elif clicked == active_button:
            return "active"
        else:
            return None

# Krita に拡張機能を登録
app = Krita.instance()
app.addExtension(GrayscaleOverlayExtension(app))
