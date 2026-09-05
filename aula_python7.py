import math
import matplotlib.pyplot as plt
import numpy as np

#Pede o ângulo em graus ao utilizador
angulo_graus = float(input("Entre com o valor do ângulo em graus: "))

#Converte para radianos antes de calcular
angulo_radianos = math.radians(angulo_graus)
seno = math.sin(angulo_radianos)
coss = math.cos(angulo_radianos)

#Mostra o resultado formatado com 2 casas decimais
print(f"Seno = {seno:.2f}, Cosseno = {coss:.2f}")


# Gerar pontos de 0 a 360 graus para desenhar as ondas estruturadas
graus_onda = np.linspace(0, 360, 500)
radianos_onda = np.radians(graus_onda)

seno_onda = np.sin(radianos_onda)
coss_onda = np.cos(radianos_onda)

plt.figure(figsize=(10, 5))

plt.plot(graus_onda, seno_onda, label="Seno", color="blue", linewidth=2)
plt.plot(graus_onda, coss_onda, label="Cosseno", color="orange", linewidth=2)

plt.scatter([angulo_graus], [seno], color="darkblue", zorder=5, label=f"meu Seno ({seno:.2f})")
plt.scatter([angulo_graus], [coss], color="darkorange", zorder=5, label=f"meu Cosseno ({coss:.2f})")

# Customizar o gráfico
plt.title(f"Ondas Trigonométricas e o Ângulo de {angulo_graus}°")
plt.xlabel("Ângulo (Graus)")
plt.ylabel("Valor")
plt.axhline(0, color='black', linewidth=0.5, linestyle='--') # Linha central
plt.xticks(np.arange(0, 361, 45)) # Marcadores no eixo X de 45 em 45 graus
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend()

# Exibir o gráfico
plt.show()
