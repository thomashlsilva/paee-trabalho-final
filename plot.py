import numpy as np
import matplotlib.pyplot as plt

# Dados (exemplares do artigo)
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
y = np.array([0.000237, 0.000216, 0.000238, 0.000285, 0.000369, 0.001051, 
              0.004487, 0.017681, 0.170621, 1.428303, 14.474037, 180.8285, 2308.62])

plt.figure(figsize=(8,5))
plt.title("Tempo de execução - TSP Força Bruta")
plt.xlabel("Nº de cidades")
plt.ylabel("Tempo de execução (segundos)")
plt.plot(x, y, color="red", marker="o", label="Tempo Observado")

plt.xticks(ticks=x)
plt.xlim(1, 13)
plt.ylim(0, 2500)

plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

plt.savefig("grafico_tempo_execucao.png", dpi=300)
plt.show()
