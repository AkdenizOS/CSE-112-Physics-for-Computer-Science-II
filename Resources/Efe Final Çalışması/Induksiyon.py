import numpy as np
import matplotlib.pyplot as plt

# Zaman aralığı ve adım sayısı
t = np.linspace(0, 2 * np.pi, 1000)
# Manyetik akı genliği ve açısal frekans
phi_0 = 1.0
omega = 1.0

# Manyetik akı (Phi_B)
phi_b = phi_0 * np.sin(omega * t)
# İndüklenen emk (E)
emk = -phi_0 * omega * np.cos(omega * t)

# Grafik çizimi
plt.figure(figsize=(12, 6))

# Manyetik akı grafiği
plt.subplot(2, 1, 1)
plt.plot(t, phi_b, label=r'$\Phi_B(t) = \Phi_0 \sin(\omega t)$')
plt.title('Manyetik Akı (Phi_B)')
plt.xlabel('Zaman (t)')
plt.ylabel('Manyetik Akı (Weber)')
plt.legend()
plt.grid(True)

# İndüklenen emk grafiği
plt.subplot(2, 1, 2)
plt.plot(t, emk, label=r'$\mathcal{E}(t) = -\Phi_0 \omega \cos(\omega t)$', color='r')
plt.title('İndüklenen EMK')
plt.xlabel('Zaman (t)')
plt.ylabel('EMK (Volt)')
plt.legend()
plt.grid(True)

# Grafik gösterimi
plt.tight_layout()
plt.show()
