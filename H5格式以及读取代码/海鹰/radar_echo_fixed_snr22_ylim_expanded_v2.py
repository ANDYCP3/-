
import numpy as np
import matplotlib.pyplot as plt
import os

fc = 15e6
c = 3e8
prf = 100
pulse_width = 300e-6
fs = 1e6
duration = 2 / prf
t = np.arange(0, duration, 1 / fs)

R = 10e3
tau = 2 * R / c

time_labels = ["09_00", "13_00", "17_00", "21_00", "01_00", "05_00"]

Pr_table = {
    "无目标": [1.958e-12, 5.192e-13, 3.656e-12, 7.833e-12, 0, 0],
    "23dB":  [1.963e-12, 6.477e-13, 7.375e-12, 3.253e-12, 0, 0],
    "22dB":  [1.958e-12, 6.459e-13, 7.355e-12, 3.242e-12, 0, 0],
    "17dB":  [1.944e-12, 6.413e-13, 7.301e-12, 3.214e-12, 0, 0],
    "27dB":  [2.003e-12, 6.605e-13, 7.523e-12, 3.331e-12, 0, 0]
}

snr_db = 22
snr_linear = 10 ** (snr_db / 10)

os.makedirs("fixed_noise_outputs", exist_ok=True)

for target_label, Pr_list in Pr_table.items():
    fig, axes = plt.subplots(2, 3, figsize=(15, 8))
    axes = axes.flatten()

    for i, Pr_signal in enumerate(Pr_list):
        ax = axes[i]
        if Pr_signal == 0:
            ax.set_title(f"{time_labels[i]}: 无数据")
            ax.axis("off")
            continue

        Pr_noise = Pr_signal / snr_linear
        signal_amplitude = np.sqrt(Pr_signal)

        carrier = np.exp(1j * 2 * np.pi * fc * t)
        pulse = ((t >= tau) & (t <= tau + pulse_width)).astype(float)
        iq_signal = signal_amplitude * pulse * carrier

        noise = np.sqrt(Pr_noise / 2) * (np.random.randn(len(t)) + 1j * np.random.randn(len(t)))
        received_signal = iq_signal + noise
        amplitude = np.abs(received_signal)

        ax.plot(t * 1e3, amplitude)
        ax.set_ylim(0, 3.10e-06)
        ax.set_title(f"{time_labels[i]}")
        ax.set_xlabel("Time (ms)")
        ax.set_ylabel("Amplitude")
        ax.grid(True)

    plt.suptitle(f"Radar Echo — {target_label} (fixed SNR = 22 dB)")
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig(f"fixed_noise_outputs/Radar_Echo_{target_label}.png")
    plt.close()

print("图像已更新，Y轴范围进一步扩大。")
