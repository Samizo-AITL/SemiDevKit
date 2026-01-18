---
layout: default
title: install
---

---

# 🧰 Installation Guide — SemiDevKit

本ドキュメントでは、**SemiDevKit** を利用するための  
**環境構築・必須ソフトウェア・初期セットアップ手順** を解説します。

対象ツール：
- 🧪 TCAD Playground  
- 📐 BSIM4 Analyzer  
- 🏗 OpenLane-Lite（RTL → GDSII）

---

## 🖥 1. System Requirements

### 1.1 Supported OS

| OS | 対応状況 | 備考 |
|----|---------|------|
| 🐧 Linux | ✅ 推奨 | Ubuntu 20.04 / 22.04 |
| 🪟 Windows | ✅ 推奨 | **WSL2 + Ubuntu** |
| 🍎 macOS | ✅ 対応 | Intel / Apple Silicon |

> 💡 **Windows 環境では WSL2 の使用を強く推奨**します。

---

## 📦 2. Required Software

### 🐍 2.1 Python

SemiDevKit では以下の Python バージョンを使用します。

- **Python 3.9 – 3.12**

#### ✔ バージョン確認
```bash
python3 --version
```

#### ✔ 基本パッケージのインストール
```bash
pip install numpy scipy matplotlib pandas pyyaml
```

📌 モジュールによっては `numpy + matplotlib` のみで動作しますが、  
解析系（BSIM / Paramus）では `pandas` を使用します。

---

### ⚡ 2.2 ngspice

SemiDevKit は **ngspice** を用いた SPICE シミュレーションを行います。

#### 🐧 Linux (Ubuntu)
```bash
sudo apt update
sudo apt install -y ngspice
```

#### 🍎 macOS
```bash
brew install ngspice
```

#### 🪟 Windows
- ✅ **推奨**：WSL2 Ubuntu 上で Linux 版 ngspice を使用  
- ⚠ 代替：Windows バイナリ  
  https://ngspice.sourceforge.io/

#### ✔ 動作確認
```bash
ngspice --version
```

---

## 🧩 3. Recommended Tools

### 🪟 3.1 WSL2（Windows のみ）

Windows での安定動作のため **必須級** です。

```powershell
wsl --install
```

Ubuntu を Microsoft Store から導入後：

```bash
sudo apt update && sudo apt upgrade -y
```

---

### 🐳 3.2 Docker（OpenLane-Lite 用）

RTL → GDSII の最小フロー実行に使用します。

- インストール  
  https://www.docker.com/products/docker-desktop/

#### ✔ 設定項目
- ✅ WSL2 backend
- ✅ Linux containers mode

---

### 📝 3.3 Visual Studio Code

推奨エディタ環境です。

#### 推奨拡張
- 🐍 Python  
- 🪟 Remote – WSL（Windows）  
- 🧾 Markdown All in One  

---

## 📥 4. Clone the Repository

### 🔐 HTTPS
```bash
git clone https://github.com/Samizo-AITL/SemiDevKit.git
cd SemiDevKit
```

### 🔑 SSH
```bash
git clone git@github.com:Samizo-AITL/SemiDevKit.git
cd SemiDevKit
```

---

## 🐍 5. Python Environment（venv）

SemiDevKit には複数のツール群が含まれます。

📌 **ツール単位で venv を分ける運用を推奨**します。

---

### 5.1 venv 作成・有効化（Linux / WSL2 / macOS）

```bash
cd SemiDevKit
python3 -m venv .venv
source .venv/bin/activate
```

---

### 5.2 venv 作成・有効化（Windows PowerShell）

```powershell
cd SemiDevKit
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

---

### 5.3 Python パッケージ導入

```bash
pip install -r requirements.txt
```

※ 初期リリース等で `requirements.txt` が無い場合：

```bash
pip install numpy scipy matplotlib pandas pyyaml
```

---

## 🧭 6. ngspice Path 設定（Windows ネイティブ）

```powershell
setx PATH "$env:PATH;C:\Program Files\Spice64\bin"
```

```bash
ngspice
```

---

## 📁 7. Directory Overview

```
SemiDevKit/
 ├ bsim/        # BSIM4 analyzers（DC / CV / DIM / Reliability / Paramus）
 ├ tcad/        # TCAD playgrounds（MOSFET / PZT）
 ├ openlane/    # OpenLane-Lite（RTL → GDSII）
 ├ docs/        # Documentation
 ├ assets/      # GitHub Pages assets
 ├ README.md
 └ ChangeLog.md
```

---

## 🚀 8. Quick Test

### ✔ ngspice + BSIM Analyzer
```bash
cd bsim/analyzer_dc
python run/run_vgid.py
```

### ✔ Python Plot Test
```bash
python - <<EOF
import numpy as np
import matplotlib.pyplot as plt
plt.plot([0,1],[0,1])
plt.savefig("test.png")
print("OK")
EOF
```

---

## 🛠 9. Troubleshooting

### ❌ ngspice not found
- インストール確認
- PATH 設定確認
- 🪟 Windows では **WSL2 使用を推奨**

### ❌ venv activation permission error（Windows）
```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

---

## 📜 10. License Notes

SemiDevKit は **ハイブリッドライセンス** を採用しています。

| 対象 | ライセンス |
|----|----|
| 💻 Source Code | MIT License |
| 📘 Docs / Diagrams | CC BY 4.0 |

---

## 📬 11. Contact

| 項目 | 内容 |
|----|----|
| 👤 Name | **Shinichi Samizo** |
| 🧑‍💻 GitHub | [Samizo-AITL](https://github.com/Samizo-AITL) |

---

🎉 **Installation 完了後は `docs/UsageGuide` へ進んでください！**
