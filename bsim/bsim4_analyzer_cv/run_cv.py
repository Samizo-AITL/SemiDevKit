"""
run_cv.py
---------

template_cv.cir を元に、ノード × (NMOS/PMOS) × 温度(LT/RT/HT) の
netlist を自動生成し、ngspice をバッチ実行して log ファイルを
results/<node>/ 以下に出力する。

生成物:
    results/<node>/
        nmos_<node>_<TEMP>.cir
        nmos_<node>_<TEMP>.log
        pmos_<node>_<TEMP>.cir
        pmos_<node>_<TEMP>.log
など
"""

from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Dict


# ------------------------------------------------------------
# パス設定
# ------------------------------------------------------------

ROOT = Path(__file__).resolve().parent
TEMPLATE = ROOT / "template_cv.cir"
MODELS = ROOT / "models"
RESULTS = ROOT / "results"

# ngspice 実行ファイル
NGSPICE_CMD = r"C:\Program Files\Spice64\bin\ngspice.exe"


# ------------------------------------------------------------
# 設定
# ------------------------------------------------------------

# プロセスノードの設定
NODES: Dict[str, Dict[str, object]] = {
    "130nm": {
        "vdd": 1.2,
        "nmos_model_file": "nmos130.sp",
        "pmos_model_file": "pmos130.sp",
        "nmos_model_name": "nmos130",
        "pmos_model_name": "pmos130",
        "lch": "0.13u",
        "wch": "1u",
        "toxe": "2e-9",
    },
}

# 温度条件
TEMPS: Dict[str, int] = {
    "LT": -40,
    "RT": 25,
    "HT": 125,
}

# VSB と VG ステップ
VSB_DEFAULT = 0.0
VG_STEP_DEFAULT = 0.01   # +方向 (NMOS)
VG_STEP_PMOS = -0.01     # -方向 (PMOS)


# ------------------------------------------------------------
# Netlist 生成
# ------------------------------------------------------------

def generate_netlist(
    node: str,
    device: str,
    temp_label: str,
) -> Path:
    cfg = NODES[node]
    vdd = float(cfg["vdd"])
    temp_value = TEMPS[temp_label]

    # NMOS / PMOS のスイープ方向
    if device == "nmos":
        model_file = cfg["nmos_model_file"]
        model_name = cfg["nmos_model_name"]
        vg_start = 0.0
        vg_stop = vdd
        vg_step = VG_STEP_DEFAULT
    elif device == "pmos":
        model_file = cfg["pmos_model_file"]
        model_name = cfg["pmos_model_name"]
        vg_start = vdd
        vg_stop = 0.0
        vg_step = VG_STEP_PMOS     # ★ 必須修正
    else:
        raise ValueError(f"Unknown device type: {device}")

    # 出力先フォルダ
    node_dir = RESULTS / node
    node_dir.mkdir(parents=True, exist_ok=True)

    # ファイル名
    netlist_name = f"{device}_{node}_{temp_label}.cir"
    netlist_path = node_dir / netlist_name

    # テンプレート読み込み
    if not TEMPLATE.exists():
        raise FileNotFoundError(f"template not found: {TEMPLATE}")

    text = TEMPLATE.read_text(encoding="utf-8")

    # 置換パラメータ
    params = {
        "MODEL_FILE": f"models/{model_file}",
        "MODEL_NAME": model_name,
        "LCH": cfg["lch"],
        "WCH": cfg["wch"],
        "TOXE": cfg["toxe"],
        "VSB": VSB_DEFAULT,
        "TEMP": temp_value,
        "VG_START": vg_start,
        "VG_STOP": vg_stop,
        "VG_STEP": vg_step,
    }

    # 埋め込み
    filled = text.format(**params)
    netlist_path.write_text(filled, encoding="utf-8")

    print(f"[GEN] {netlist_path.relative_to(ROOT)}")
    return netlist_path


# ------------------------------------------------------------
# ngspice 実行
# ------------------------------------------------------------

def run_ngspice(netlist_path: Path) -> Path:
    log_path = netlist_path.with_suffix(".log")

    cmd = [
        NGSPICE_CMD,
        "-b",
        "-o",
        str(log_path),
        str(netlist_path),
    ]
    print(f"[RUN] {' '.join(cmd)}")

    try:
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )
    except FileNotFoundError:
        raise SystemExit(
            "ngspice コマンドが見つかりません。\n"
            "PATH または NGSPICE_CMD を確認してください。"
        )

    if result.returncode != 0:
        print(f"[ERR] ngspice exited with code {result.returncode}")
        print("----- stdout -----")
        print(result.stdout)
        print("----- stderr -----")
        print(result.stderr)
    else:
        print(f"[OK ] log saved -> {log_path.relative_to(ROOT)}")

    return log_path


# ------------------------------------------------------------
# メイン処理
# ------------------------------------------------------------

def main() -> None:
    RESULTS.mkdir(exist_ok=True)

    for node in NODES:
        for device in ("nmos", "pmos"):
            for temp_label in TEMPS:
                print(f"\n=== {node} / {device.upper()} / {temp_label} ===")
                netlist = generate_netlist(node, device, temp_label)
                run_ngspice(netlist)


if __name__ == "__main__":
    main()
