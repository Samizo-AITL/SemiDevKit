"""
plot_cv.py
----------

results/<node>/ 以下の *.log を走査し、
Cgg–Vg カーブのみを抽出して PNG を出力する。

出力:
    results/<node>/<same_basename>.png
    例: nmos_130nm_RT.log -> nmos_130nm_RT.png
"""

from __future__ import annotations

from pathlib import Path
from typing import List, Tuple

import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"


def parse_cgg_from_log(log_path: Path) -> Tuple[List[float], List[float]]:
    if not log_path.exists():
        raise FileNotFoundError(log_path)

    lines = log_path.read_text(encoding="utf-8", errors="ignore").splitlines()

    # ---- "Index ..." を探す ----
    header_line = None
    header_index = None
    for i, line in enumerate(lines):
        if line.strip().startswith("Index"):
            header_line = line.strip()
            header_index = i
            break

    if header_line is None:
        raise RuntimeError(f"Header line 'Index ...' not found in {log_path}")

    headers = header_line.split()

    # v(g)
    try:
        idx_v = next(i for i, h in enumerate(headers) if h.lower().startswith("v("))
    except StopIteration:
        raise RuntimeError(f"Gate voltage column not found in {log_path}")

    # cgg
    try:
        idx_cgg = next(i for i, h in enumerate(headers) if "cgg" in h.lower())
    except StopIteration:
        raise RuntimeError(f"Cgg column not found in {log_path}")

    vg_list: List[float] = []
    cgg_list: List[float] = []

    # ---- データ行の解析 ----
    for line in lines[header_index + 1 :]:
        if not line.strip():
            continue

        parts = line.split()

        # Index チェック
        try:
            int(parts[0])
        except Exception:
            continue

        if len(parts) <= max(idx_v, idx_cgg):
            continue

        try:
            vg = float(parts[idx_v])
            cgg = float(parts[idx_cgg])
        except Exception:
            continue

        vg_list.append(vg)
        cgg_list.append(cgg)

    if not vg_list:
        raise RuntimeError(f"No numeric data parsed from {log_path}")

    return vg_list, cgg_list


def plot_one(log_path: Path) -> Path:
    vg, cgg = parse_cgg_from_log(log_path)

    # -----------------------------------------------------
    # ★ 不正な点の除外処理（重要）
    #     1) Index=0 除外
    #     2) Cgg <= 0 の点を除外（初期収束不安定）
    # -----------------------------------------------------

    # (1) 先頭点除外
    if len(vg) > 1:
        vg = vg[1:]
        cgg = cgg[1:]

    # (2) Cgg <= 0 を除外
    vg_filtered = []
    cgg_filtered = []
    for v, c in zip(vg, cgg):
        if c > 0:
            vg_filtered.append(v)
            cgg_filtered.append(c)

    vg = vg_filtered
    cgg = cgg_filtered

    # -----------------------------------------------------
    # プロット
    # -----------------------------------------------------
    png_path = log_path.with_suffix(".png")

    plt.figure()
    plt.plot(vg, cgg)
    plt.xlabel("Gate Voltage Vg [V]")
    plt.ylabel("Cgg [F]")
    plt.title(png_path.name.replace(".png", ""))
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(png_path, dpi=300)
    plt.close()

    print(f"[PNG] {png_path.relative_to(ROOT)}")
    return png_path


def main() -> None:
    if not RESULTS.exists():
        print("results/ ディレクトリがありません。先に run_cv.py を実行してください。")
        return

    for node_dir in sorted(RESULTS.iterdir()):
        if not node_dir.is_dir():
            continue
        for log_path in sorted(node_dir.glob("*.log")):
            try:
                plot_one(log_path)
            except Exception as e:
                print(f"[WARN] failed to plot {log_path}: {e}")


if __name__ == "__main__":
    main()
