#!/usr/bin/env python3

import os
import shutil
import subprocess
from pathlib import Path

def main():
    home = str(Path.home())
    pykrita_path = os.path.join(home, 'Library/Application Support/krita/pykrita')
    repo_path = os.getcwd()

    desktop_files = [f for f in os.listdir(repo_path) if f.endswith('.desktop')]
    if not desktop_files:
        print("❌ .desktop ファイルが見つかりません。")
        return

    for desktop_file in desktop_files:
        plugin_name = desktop_file.replace('.desktop', '')
        plugin_src_dir = os.path.join(repo_path, plugin_name)
        plugin_dst_dir = os.path.join(pykrita_path, plugin_name)

        if not os.path.exists(plugin_src_dir):
            print(f"❌ ディレクトリ {plugin_src_dir} が見つかりません。スキップします。")
            continue

        if os.path.exists(plugin_dst_dir):
            answer = input(f"⚠️ {plugin_dst_dir} は既に存在します。上書きしますか？ [y/N]: ")
            if answer.lower() != 'y':
                print("⏭ スキップしました。")
                continue
            shutil.rmtree(plugin_dst_dir)

        shutil.copytree(plugin_src_dir, plugin_dst_dir)
        shutil.copy2(os.path.join(repo_path, desktop_file), pykrita_path)

        print(f"✅ {plugin_name} を {pykrita_path} にコピーしました。")

    if not is_krita_running():
        print("🚀 Krita を起動します...")
        subprocess.Popen(["/Applications/krita.app/Contents/MacOS/krita"])
    else:
        print("🔄 Krita はすでに起動しています。")

def is_krita_running():
    try:
        output = subprocess.check_output(["pgrep", "-f", "krita"])
        return bool(output.strip())
    except subprocess.CalledProcessError:
        return False

if __name__ == "__main__":
    main()
