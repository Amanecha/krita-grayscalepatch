# Krita Grayscale Overlay Plugin

A Krita plugin that adds a non-destructive grayscale filter layer above the selected layer.  
Useful for checking values and brightness levels while painting.

---

## ✨ Features

- Adds a grayscale (lightness-based) filter mask above the selected layer
- Non-destructive: original artwork remains untouched
- Designed for digital painting and illustration workflows

---

## 🖥️ Requirements

- **Krita 5.x** or later
- Python 3 (bundled with Krita)
- Tested on **macOS**; should also work on **Windows** and **Linux**

---

## 📦 Installation

1. Locate Krita's Python plugin folder:

    - **macOS**:  
      `~/Library/Application Support/krita/pykrita/`

    - **Windows**:  
      `%APPDATA%\krita\pykrita\`

    - **Linux**:  
      `~/.local/share/krita/pykrita/`

2. Clone or copy this plugin into the `pykrita` folder:

    ```bash
    cd ~/Library/Application\ Support/krita/pykrita/
    git clone https://github.com/Amanecha/krita-grayscalepatch.git grayscalepatch
    ```

3. Restart Krita

4. Enable the plugin:

    - Open Krita
    - Go to `Preference` → `Python plugin manager`
    - Find and enable `grayscalepatch`
    - Restart Krita again

---

## 🚀 Usage

1. Select a **paint layer** in your Layers panel
2. Run the plugin via:
    - `Tools` → `Scripts` → `Add Grayscale Overlay`
3. A grayscale **filter mask** will be applied above the selected layer
4. Toggle the filter mask visibility to compare color vs grayscale

---

## 📁 File Structure
pykrita/
├── grayscalepatch/
│   ├── __init__.py
│   ├── create_template.py
│   ├── grayscale.py
│   ├── grayscalepatch.py
│   ├── LICENSE
│   └── README.md
└── grayscalepatch.desktop

---

## 🧪 Development

If you're modifying or expanding the plugin:

- Use Krita's built-in **Scripter** tool to test Python snippets
- Refer to the [Krita Python API docs](https://docs.krita.org/en/user_manual/python.html)
- For filter masks, work with `Filter`, `FilterMask`, and `Node` classes

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋 Author

**Amane**  
Feedback, issues, or feature requests are welcome.  
Feel free to open an [Issue](https://github.com/Amanecha/krita-grayscalepatch/issues) or pull request!

---

## ⭐️ Support

If you find this plugin useful, consider starring the repo or sharing it with fellow artists.  
Happy painting!
