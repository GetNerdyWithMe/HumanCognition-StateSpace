import numpy as np
import matplotlib.pyplot as plt

# Time horizon (days)
T = 30

# State variables
sleep_debt = np.zeros(T)
cognitive_capacity = np.zeros(T)
learning_efficiency = np.zeros(T)

sleep_debt[0] = 0
cognitive_capacity[0] = 1.0

sleep_loss_per_day = 0.3
recovery_rate = 0.2
noise_level = 0.05

for t in range(1, T):
    sleep+debt[t] = sleep_debt[t-1] + sleep_loss_per_day

  recovery=recovery_rate * np.exp(-sleep_debt[t])

  cognitive_capacity[t] = cognitive_capacity[t-1]-0.1 * sleep_debt[t] + recovery
  cognitive_capacity[t] + = np.random.normal(0,noise_level)

learning_efficiency[t] = np.clip(cognitive_capacity[t], 0, 1)
