from __future__ import annotations
from pathlib import Path

# ============================================================
# 基本設定
# ============================================================

TECH = "130nm"

L_LIST = [
    0.10e-6,
    0.13e-6,
    0.16e-6,
    0.20e-6,
    0.50e-6,
    1.00e-6,
]

W_LIST = [
    0.50e-6,
    1.00e-6,
    10.0e-6,
]

L_REF = 1.00e-6
W_REF = 1.00e-6

BASE_DIR = Path(__file__).resolve().parent
TEMPLATE_NMOS = BASE_DIR / "nmos130_base.tpl"
TEMPLATE_PMOS = BASE_DIR / "pmos130_base.tpl"


# ============================================================
# ロングチャネル基準パラメータ
# ============================================================

NMOS_BASE = dict(
    VTH0=0.40,
    K1=0.50,
    K2=-0.03,
    VOFF=-0.05,
    NFACTOR=1.3,
    U0=1.35e-2,
    UA=2e-9,
    UB=5e-19,
    UC=0.1,
    VSAT=1.5e6,
    DVT0=0.70,
    DVT1=0.30,
    DVT2=0.00,
    DVT1W=5e6,
    W0=1e-7,
    ETA0=0.10,
    ETAB=-0.05,
    PCLM=0.25,
    PDIBLC1=0.02,
    PDIBLC2=0.005,
    RDSW=80.0,
    WR=1.0,
    CGSO=2.5e-10,
    CGDO=2.5e-10,
    CGBO=1.0e-10,
    XPART=0,
)

PMOS_BASE = dict(
    VTH0=-0.40,
    K1=0.50,
    K2=-0.03,
    VOFF=0.05,
    NFACTOR=1.3,
    U0=1.0e-2,
    UA=2e-9,
    UB=5e-19,
    UC=0.1,
    VSAT=1.5e6,
    DVT0=0.70,
    DVT1=0.30,
    DVT2=0.00,
    DVT1W=5e6,
    W0=1e-7,
    ETA0=0.10,
    ETAB=-0.05,
    PCLM=0.25,
    PDIBLC1=0.02,
    PDIBLC2=0.005,
    RDSW=90.0,
    WR=1.0,
    CGSO=2.5e-10,
    CGDO=2.5e-10,
    CGBO=1.0e-10,
    XPART=0,
)


# ============================================================
# スケーリングモデル（SCE / NCE）
# ============================================================

def scale_params_for_L(base: dict, L: float, device: str) -> dict:
    p = base.copy()
    ratio = L_REF / L

    dvth = 0.03 * (ratio - 1.0)
    if device == "nmos":
        p["VTH0"] = base["VTH0"] - dvth
    else:
        p["VTH0"] = base["VTH0"] + dvth

    p["ETA0"] = base["ETA0"] * (1 + 0.5 * (ratio - 1))
    p["PDIBLC1"] = base["PDIBLC1"] * (1 + 0.7 * (ratio - 1))
    p["PDIBLC2"] = base["PDIBLC2"] * (1 + 0.7 * (ratio - 1))

    p["U0"] = base["U0"] * (1 + 0.1 * (ratio - 1))
    p["VSAT"] = base["VSAT"] * (1 + 0.1 * (ratio - 1))

    p["DVT0"] = base["DVT0"] * (1 + 0.3 * (ratio - 1))
    p["DVT1"] = base["DVT1"] * (1 + 0.3 * (ratio - 1))

    return p


def scale_params_for_W(base: dict, W: float, device: str) -> dict:
    p = base.copy()
    ratio = W_REF / W

    dvth = 0.02 * (ratio - 1.0)
    if device == "nmos":
        p["VTH0"] = base["VTH0"] + dvth
    else:
        p["VTH0"] = base["VTH0"] - dvth

    p["U0"] = base["U0"] * (1 - 0.05 * (ratio - 1))
    p["RDSW"] = base["RDSW"] * (1 + 0.2 * (ratio - 1))

    return p


# ============================================================
# Lモデル生成
# ============================================================

def generate_L_models(device: str):
    tpl_path = TEMPLATE_NMOS if device == "nmos" else TEMPLATE_PMOS
    tpl = tpl_path.read_text(encoding="utf-8")

    base_params = NMOS_BASE if device == "nmos" else PMOS_BASE

    for L in L_LIST:
        Lum = L * 1e6
        code = int(round(Lum * 100))
        code_str = f"{code:03d}"

        params = scale_params_for_L(base_params, L, device)
        params["CODE"] = f"l{code_str}"

        text = tpl.format(**params)

        out_path = BASE_DIR / f"{TECH}_{device}_l{code_str}.sp"
        out_path.write_text(text, encoding="utf-8")

        print(f"[L-model] {TECH}_{device}_l{code_str}.sp 生成")


# ============================================================
# Wモデル生成
# ============================================================

def generate_W_models(device: str):
    tpl_path = TEMPLATE_NMOS if device == "nmos" else TEMPLATE_PMOS
    tpl = tpl_path.read_text(encoding="utf-8")

    base_params = NMOS_BASE if device == "nmos" else PMOS_BASE

    for W in W_LIST:
        Wum = W * 1e6
        code = int(round(Wum * 100))
        code_str = f"{code:03d}"

        params = scale_params_for_W(base_params, W, device)
        params["CODE"] = f"w{code_str}"

        text = tpl.format(**params)

        out_path = BASE_DIR / f"{TECH}_{device}_w{code_str}.sp"
        out_path.write_text(text, encoding="utf-8")

        print(f"[W-model] {TECH}_{device}_w{code_str}.sp 生成")


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    print("=== generate_dim_models.py START ===")
    for dev in ["nmos", "pmos"]:
        generate_L_models(dev)
        generate_W_models(dev)
    print("=== generate_dim_models.py DONE ===")
