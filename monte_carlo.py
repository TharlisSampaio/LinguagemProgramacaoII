import random
import time

def monte_carlo_pi(num_samples):
    inside_circle = 0
    total_samples = num_samples

    start_time = time.time()  # Início da contagem de tempo

    for _ in range(num_samples):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            inside_circle += 1

    pi_estimate = 4 * (inside_circle / total_samples)

    end_time = time.time()  # Fim da contagem de tempo
    elapsed_time = end_time - start_time

    return pi_estimate, elapsed_time

# Número de amostras (aumente para maior precisão)
num_samples = 800000000

# Calcula o valor estimado de Pi e o tempo de execução
pi_value, execution_time = monte_carlo_pi(num_samples)

print(f"Valor estimado de Pi usando {num_samples} amostras: {pi_value:.6f}")
print(f"Tempo de execução: {execution_time:.6f} segundos")
