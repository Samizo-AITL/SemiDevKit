from pathlib import Path
from typing import Dict


def build_modelcard(params: Dict[str, float], out_path: Path) -> None:
    """
    template_bsim4.tpl を読み込み、params を埋め込んで .sp を出力する。
    """
    here = Path(__file__).parent
    tpl_path = here / "template_bsim4.tpl"
    tpl = tpl_path.read_text(encoding="utf-8")

    # テンプレートで使う追加パラメータ
    dev_type = params.get("DEVICE_TYPE", "nmos")
    model_name = params.get("MODEL_NAME", "paramus_nmos")

    fmt_params = {
        "MODEL_NAME": model_name,
        "DEVICE_TYPE": dev_type,
        **params,
    }

    text = tpl.format(**fmt_params)
    out_path.write_text(text, encoding="utf-8")
