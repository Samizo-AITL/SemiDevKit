from dataclasses import dataclass
from typing import Dict
import numpy as np

from .poisson import PoissonResult
from .iv import IVData


@dataclass
class CoreParams:
    vth0: float
    u0: float
    pclm: float


def _estimate_vth0_from_gmmax(iv: IVData) -> float:
    """gmmax 法で VTH0 を推定。"""
    vg = iv.vg
    id_lin = iv.id_lin

    dvg = np.gradient(vg)
    did = np.gradient(id_lin)
    gm = did / np.where(dvg == 0, np.nan, dvg)
    idx = np.nanargmax(gm)
    return float(vg[idx])


def _estimate_u0(iv: IVData, pois: PoissonResult, phys: Dict, vth0: float) -> float:
    """線形領域の式から μ0 を推定。Id ≈ μ Cox (W/L) (Vg − Vth) Vd"""
    vg = iv.vg
    id_lin = iv.id_lin
    cox = pois.cox
    L = float(phys["L_m"])
    W = float(phys["W_m"])
    ratio = W / L
    vd = iv.vd_lin

    mask = vg > (vth0 + 0.1)
    if mask.sum() < 3:
        return float(phys["mu0"])  # うまく取れなければプリセット値

    x = (vg[mask] - vth0)
    y = id_lin[mask]

    # y ≒ μ Cox (W/L) Vd * x
    k, _ = np.polyfit(x, y, 1)
    mu_est = k / (cox * ratio * vd)
    return float(mu_est)


def _estimate_pclm(iv: IVData) -> float:
    """
    Id–Vd の線形フィットから λ を求め、PCLM の初期値を作る。
    モデル: Id ≒ Id0 (1 + λ Vd)
    """
    vd = iv.vd
    id_vd = iv.id_vd

    # 直線フィット
    k, b = np.polyfit(vd, id_vd, 1)  # Id ≒ k*Vd + b
    id0 = b
    if id0 <= 0:
        return 0.1
    lam = k / id0  # dId/dVd / Id0

    pclm = max(lam, 0.01)  # 極端な値を避けて下限を設ける
    return float(pclm)


def extract_core_params(phys: Dict, pois: PoissonResult, iv: IVData) -> CoreParams:
    """Poisson + IV データから VTH0, U0, PCLM を抽出する高レベル関数。"""
    vth0 = _estimate_vth0_from_gmmax(iv)
    u0 = _estimate_u0(iv, pois, phys, vth0)
    pclm = _estimate_pclm(iv)

    return CoreParams(vth0=vth0, u0=u0, pclm=pclm)
