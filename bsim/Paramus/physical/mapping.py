from typing import Dict

from .poisson import PoissonResult
from .extract import CoreParams


def map_to_bsim_params(phys: Dict, pois: PoissonResult, core: CoreParams) -> Dict[str, float]:
    """
    物理量＋抽出パラメータを BSIM4 の主要パラメータにマッピングする。
    あくまで「初期推定」であり、実務向けの厳密モデルではない。
    """
    params: Dict[str, float] = {}

    # コアパラメータ
    params["VTH0"] = core.vth0
    params["U0"] = core.u0
    params["PCLM"] = core.pclm

    # 酸化膜厚
    params["TOXM"] = float(phys["tox_m"])

    # 表面制御係数など（簡易な固定値／ヒューリスティク）
    params["NFACTOR"] = 1.5
    params["ETA0"] = 0.05      # DIBL の初期値
    params["DVT0"] = 1.0
    params["DVT1"] = 0.5

    # ソース/ドレイン
    params["RDSW"] = 200.0     # [ohm*µm] 的なニュアンスの固定値
    params["VSAT"] = 1.0e5     # [m/s] オーダーの値

    # 本来はドーピング・Vth ロールオフから決めるが、ここでは固定 or 緩い依存に留める
    params["K1"] = 0.6
    params["K2"] = -0.02

    # 端子容量（かなりラフな固定値）
    params["CGSO"] = 1.0e-10
    params["CGDO"] = 1.0e-10

    return params
