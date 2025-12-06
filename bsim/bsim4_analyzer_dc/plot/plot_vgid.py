from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def load_dat(path):
    data = np.loadtxt(path, comments=["*"])
    V = data[:, 0]
    Id = data[:, 3]

    # PMOS の符号反転
    if "pmos" in path.name:
        Id = -Id

    return V, Id


def plot_vgid(tech="130nm"):

    temps = ["LT", "RT", "HT"]
    devices = ["nmos", "pmos"]

    for device in devices:

        # --- Linear plot ---
        plt.figure(figsize=(12, 8))

        for tag in temps:
            dat = Path(f"results/{tech}/vgid/{tech}_{device}_vgid_{tag}.dat")
            V, Id = load_dat(dat)
            plt.plot(V, Id, label=tag)

        plt.title(f"VGID – {tech.upper()} – {device.upper()} (Linear)")
        plt.xlabel("Vgs [V]")
        plt.ylabel("Id [A]")
        plt.grid(True)
        plt.legend()

        out_png = f"results/{tech}/vgid/{tech}_{device}_vgid_lin.png"
        plt.savefig(out_png, dpi=300)
        print("[saved]", out_png)

        # --- Log plot ---
        plt.figure(figsize=(12, 8))

        for tag in temps:
            dat = Path(f"results/{tech}/vgid/{tech}_{device}_vgid_{tag}.dat")
            V, Id = load_dat(dat)
            plt.semilogy(V, np.abs(Id), label=tag)

        plt.title(f"VGID – {tech.upper()} – {device.upper()} (Log)")
        plt.xlabel("Vgs [V]")
        plt.ylabel("Id [A] (log)")
        plt.grid(True)
        plt.legend()

        out_png = f"results/{tech}/vgid/{tech}_{device}_vgid_log.png"
        plt.savefig(out_png, dpi=300)
        print("[saved]", out_png)


if __name__ == "__main__":
    plot_vgid()
