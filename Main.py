from Model import InfectionModel
from Data_analysis import get_column_data
import matplotlib
matplotlib.use("TkAgg")  # Para permitir gráficos interactivos en Manjaro
import matplotlib.pyplot as plt


# Parámetros
pop = 100  
steps = 50  

# Ejecutar simulación
model = InfectionModel(pop, 20, 20, ptrans=0.5)
for i in range(steps):
    model.step()

# Obtener datos
data = get_column_data(model)

# Graficar resultados
plt.figure(figsize=(10, 5))
for col in data.columns:
    plt.plot(data.index, data[col], label=col)
plt.xlabel("Step")
plt.ylabel("Número de Agentes")
plt.legend()
plt.title("Evolución de la epidemia")
plt.show()
