from dataclasses import dataclass
from typing import Dict
import numpy as np

from .poisson import PoissonResult


@dataclass
class IVData:
    vg: np.ndarray        # Vg sweep
    id_lin: np.ndarray    # Id–Vg (linear region Vd_small)
    vd: np.ndarray        # Vd sweep at high Vg
    id_vd: np.ndarray     # Id–Vd at fixed high Vg
    vd_lin: float
    vg_high: float
    vd_max: float


def generate_iv_data(phys: Dict, pois: PoissonResult) -> IVData:
    """
    Poisson 結果と物理パラメータから、簡易な Id–Vg / Id–Vd を生成する。

    モデル:
        Id_lin = mu0 * Cox * (W/L) * (Vg - Vth) * Vd_lin （Vg > Vth のとき）
        Id_sat = 0.5 * mu0 * Cox * (W/L) * (Vg - Vth)^2 * (1 + λ Vd)
    """
    vg_th = pois.vth
    cox = pois.cox

    mu0 = float(phys["mu0"])        # [m^2/Vs]
    L = float(phys["L_m"])
    W = float(phys["W_m"])
    ratio = W / L

    # Vg スイープ
    vg_min = 0.0
    vg_max = vg_th + 0.8
    vg = np.linspace(vg_min, vg_max, 81)

    vd_lin = 0.05  # 線形領域 Vd
    vd_max = 1.2   # 飽和領域 Vd

    # Id–Vg（線形領域）
    overdrive = np.maximum(vg - vg_th, 0.0)
    id_lin = mu0 * cox * ratio * overdrive * vd_lin

    # Id–Vd（高 Vg でのチャネル長変調を見るため）
    vg_high = vg_th + 0.6
    vd = np.linspace(0.05, vd_max, 40)
    overdrive_high = max(vg_high - vg_th, 0.0)
    lambda0 = 0.1  # 仮のチャネル長変調係数
    id_vd = 0.5 * mu0 * cox * ratio * overdrive_high ** 2 * (1.0 + lambda0 * vd)

    return IVData(
        vg=vg,
        id_lin=id_lin,
        vd=vd,
        id_vd=id_vd,
        vd_lin=vd_lin,
        vg_high=vg_high,
        vd_max=vd_max,
    )
