import argparse
import json
from pathlib import Path

from physical.poisson import run_poisson
from physical.iv import generate_iv_data
from physical.extract import extract_core_params
from physical.mapping import map_to_bsim_params
from modelcard.build import build_modelcard


PRESET_DIR = Path(__file__).parent / "presets"


def load_preset(node: str, dev_type: str) -> dict:
    """プリセット JSON を読み込む。例: node="130nm", dev_type="nmos"."""
    fname = f"{dev_type}_{node}.json"
    path = PRESET_DIR / fname
    if not path.exists():
        raise FileNotFoundError(f"Preset not found: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def override_physical_params(base: dict, args: argparse.Namespace) -> dict:
    """CLI で指定された物理パラメータでプリセットを上書き。"""
    p = base.copy()
    if args.tox is not None:
        p["tox_m"] = float(args.tox)
    if args.na is not None:
        p["na_m3"] = float(args.na)
    if args.vfb is not None:
        p["vfb"] = float(args.vfb)
    if args.u0 is not None:
        p["mu0"] = float(args.u0)
    if args.L is not None:
        p["L_m"] = float(args.L)
    if args.W is not None:
        p["W_m"] = float(args.W)
    return p


def build_argparser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Paramus Physical Edition: 5 parameters -> BSIM4 modelcard"
    )
    p.add_argument("--node", type=str, default="130nm", help="process node (e.g. 130nm, 90nm)")
    p.add_argument("--type", type=str, default="nmos", choices=["nmos", "pmos"], help="device type")
    p.add_argument("--out", type=str, default="model.sp", help="output SPICE file path")

    # 物理パラメータの上書き用オプション（任意）
    p.add_argument("--tox", type=float, help="oxide thickness [m]")
    p.add_argument("--na", type=float, help="channel doping [1/m^3]")
    p.add_argument("--vfb", type=float, help="flat-band voltage [V]")
    p.add_argument("--u0", type=float, help="mobility [m^2/Vs]")
    p.add_argument("--L", type=float, help="channel length [m]")
    p.add_argument("--W", type=float, help="channel width [m]")

    return p


def main() -> None:
    parser = build_argparser()
    args = parser.parse_args()

    # 1) プリセット読み込み
    preset = load_preset(args.node, args.type)

    # JSON では nm, cm^-3 等なので SI 単位に変換したフィールドを追加済み想定
    # （ファイル側で tox_m, na_m3 などを持たせている）
    phys = override_physical_params(preset, args)

    # 2) Poisson 近似
    pois = run_poisson(phys)

    # 3) 擬似 IV データ生成
    iv_data = generate_iv_data(phys, pois)

    # 4) VTH0 / U0 / PCLM など抽出
    core_params = extract_core_params(phys, pois, iv_data)

    # 5) BSIM4 パラメータセットへ変換
    bsim_params = map_to_bsim_params(phys, pois, core_params)

    # 6) テンプレートに流し込み modelcard 出力
    out_path = Path(args.out)
    build_modelcard(bsim_params, out_path)
    print(f"[Paramus] generated BSIM4 modelcard -> {out_path}")


if __name__ == "__main__":
    main()
