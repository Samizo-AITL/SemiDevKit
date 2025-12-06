from dataclasses import dataclass
from typing import Dict
import numpy as np

# 物理定数
Q = 1.602176634e-19  # [C]
K_B = 1.380649e-23   # [J/K]
EPS0 = 8.8541878128e-12  # [F/m]
EPS_SI = 11.7 * EPS0
EPS_OX = 3.9 * EPS0

# シリコンの固有キャリア密度（約 300 K）
NI_M3 = 1.0e16  # [1/m^3] ≒ 1e10 [1/cm^3]


@dataclass
class PoissonResult:
    vth: float
    cox: float
    phi_f: float
    gamma: float


def _ensure_si_units(phys: Dict) -> Dict:
    """
    プリセット JSON では:
      - tox_nm
      - na_cm3
      - L_nm
      - W_um
    等を持たせておき、ここで SI 単位に変換して tox_m, na_m3, L_m, W_m を補完する。
    """
    p = phys.copy()

    if "tox_m" not in p and "tox_nm" in p:
        p["tox_m"] = p["tox_nm"] * 1e-9
    if "na_m3" not in p and "na_cm3" in p:
        p["na_m3"] = p["na_cm3"] * 1e6
    if "L_m" not in p and "L_nm" in p:
        p["L_m"] = p["L_nm"] * 1e-9
    if "W_m" not in p and "W_um" in p:
        p["W_m"] = p["W_um"] * 1e-6

    return p


def run_poisson(phys: Dict, temperature: float = 300.0) -> PoissonResult:
    """
    MOSCAP の長チャネル近似を用いて Vth, Cox を計算する簡易 Poisson モデル。

    - NMOS の場合:
        Vth = Vfb + 2phiF + (sqrt(2*q*eps_si*Na*2phiF))/Cox
    - PMOS の場合は符号が反転（ここでは単純な近似）

    戻り値:
        PoissonResult(vth, cox, phi_f, gamma)
    """
    p = _ensure_si_units(phys)
    dev_type = p.get("device_type", "nmos")

    tox = float(p["tox_m"])
    na = float(p["na_m3"])
    vfb = float(p["vfb"])
    t = temperature

    cox = EPS_OX / tox  # 単位面積あたり [F/m^2]

    phi_f = (K_B * t / Q) * np.log(na / NI_M3)  # フェルミポテンシャル
    gamma = np.sqrt(2.0 * Q * EPS_SI * na) / cox

    if dev_type == "nmos":
        vth = vfb + 2.0 * phi_f + gamma * np.sqrt(2.0 * phi_f)
    else:  # pMOS（簡易近似）
        # 絶対値のみを合わせる単純モデル
        vth_mag = abs(vfb) + 2.0 * abs(phi_f) + gamma * np.sqrt(2.0 * abs(phi_f))
        vth = -vth_mag

    return PoissonResult(vth=vth, cox=cox, phi_f=phi_f, gamma=gamma)
