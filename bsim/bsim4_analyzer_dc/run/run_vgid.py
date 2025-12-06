from __future__ import annotations
from pathlib import Path
import subprocess
import numpy as np
import csv

# ngspice 実行ファイルパス
NGSPICE_EXE = r"C:\Program Files\Spice64\bin\ngspice_con.exe"


def run_vgid(
    model_include: str,
    model_name: str,
    tech: str,
    device: str,     # "nmos" / "pmos"
    temp_tag: str,   # "LT" / "RT" / "HT"
    temp: float,
    Lch: float,
    Wch: float,
    vdd: float,
    raw_dir: Path,
) -> dict:

    prefix = f"{tech}_{device}_vgid_{temp_tag}"
    raw_dir.mkdir(parents=True, exist_ok=True)

    cir_path = (raw_dir / f"{prefix}.cir").resolve()
    dat_path = (raw_dir / f"{prefix}.dat").resolve()   # VX, IY を書き出す生データ
    csv_path = (raw_dir / f"{prefix}.csv").resolve()   # 抽出パラメータまとめ
    log_path = (raw_dir / f"{prefix}.log").resolve()
    out_path = (raw_dir / f"{prefix}_bsim4.out").resolve()

    # -------------------------------------------------
    #  テンプレート展開
    #  ※ template_vgid.cir 側では必ず
    #      wrdata {{CSV_PATH}} VX IY
    #    のように VX(=Vgs), IY(=Id>0) を出すこと
    # -------------------------------------------------
    tpl = Path("templates/template_vgid.cir").read_text(encoding="utf-8")
    include_str = model_include.replace("\\", "/")

    # NMOS / PMOS のバイアス条件
    if device == "nmos":
        D, S, B = vdd, 0.0, 0.0
        VG_START, VG_STOP, VG_STEP = 0.0, vdd, 0.05
    else:
        D, S, B = 0.0, vdd, vdd
        VG_START, VG_STOP, VG_STEP = 0.0, -vdd, -0.05

    content = (
        tpl.replace("{{MODEL_INCLUDE}}", f'.include "{include_str}"')
           .replace("{{MODEL_NAME}}", model_name)
           .replace("{{TEMP}}", str(temp))
           .replace("{{LCH}}", str(Lch))
           .replace("{{WCH}}", str(Wch))
           .replace("{{D_VOLT}}", str(D))
           .replace("{{S_VOLT}}", str(S))
           .replace("{{B_VOLT}}", str(B))
           .replace("{{VG_START}}", str(VG_START))
           .replace("{{VG_STOP}}", str(VG_STOP))
           .replace("{{VG_STEP}}", str(VG_STEP))
           # テンプレ側では {{CSV_PATH}} を使って VX, IY を出力
           .replace("{{CSV_PATH}}", dat_path.as_posix())
    )

    cir_path.write_text(content, encoding="utf-8")

    # -------------------------------------------------
    #  ngspice 実行
    # -------------------------------------------------
    print(f"[VGID] Running ngspice → {cir_path}")

    result = subprocess.run(
        [NGSPICE_EXE, "-b", str(cir_path)],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )

    # ログ保存
    log_path.write_text(result.stdout)

    # bsim4.out / sim.log が吐かれていればリネーム
    tmp_bsim = raw_dir / "bsim4.out"
    tmp_log = raw_dir / "sim.log"
    if tmp_bsim.exists():
        tmp_bsim.rename(out_path)
    if tmp_log.exists():
        tmp_log.rename(log_path)

    if result.returncode != 0:
        print("=== NGSPICE ERROR (VGID) ===")
        raise RuntimeError(f"ngspice failed: {cir_path}")

    # -------------------------------------------------
    #  データ読み込み（Vgs, Id）
    #  template_vgid.cir の wrdata で
    #     wrdata {{CSV_PATH}} VX IY
    #  としている前提です。
    # -------------------------------------------------
    data = np.loadtxt(dat_path)
    if data.ndim == 1:
        data = data.reshape(1, -1)

    Vgs = data[:, 0]
    Id = data[:, 1]   # NMOS / PMOS とも Id > 0 になるように wrdata 側で調整済み

    # -------------------------------------------------
    #  パラメータ抽出
    # -------------------------------------------------
    # gm 計算
    gm = np.gradient(Id, Vgs)

    # gm が最大となる点
    idx_gm = int(np.nanargmax(np.abs(gm)))
    gmmax = float(np.abs(gm[idx_gm]))
    Vth_gmmax = float(Vgs[idx_gm])

    # -------------------------------------------------
    #  summary CSV 出力
    # -------------------------------------------------
    rows = [
        ["param", "value"],
        ["Vth_gmmax", Vth_gmmax],
        ["gmmax", gmmax],
    ]

    with open(csv_path, "w", newline="") as f:
        csv.writer(f).writerows(rows)

    return {
        "dat": dat_path,
        "csv": csv_path,
        "cir": cir_path,
        "log": log_path,
        "bsim4": out_path,
    }


# ======================================================
# MAIN：NMOS / PMOS × LT / RT / HT すべて実行
# ======================================================
if __name__ == "__main__":
    tech = "130nm"
    temps = {"LT": -40.0, "RT": 25.0, "HT": 125.0}

    for device in ["nmos", "pmos"]:
        for tag, T in temps.items():
            model = Path(f"models/{device}130.sp").resolve()
            print(f"===== VGID RUN {device.upper()} {tag} =====")
            out = run_vgid(
                model_include=str(model),
                model_name=f"{device}130",
                tech=tech,
                device=device,
                temp_tag=tag,
                temp=T,
                Lch=0.13e-6,
                Wch=1e-6,
                vdd=1.2,
                raw_dir=Path(f"results/{tech}/vgid"),
            )
            print(out)
