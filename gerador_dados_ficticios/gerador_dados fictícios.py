import pandas as pd
import numpy as np

np.random.seed(42)

data = {
    "Data da Entrega": pd.date_range(start="2024-01-01", periods=50, freq="D"),
    "Número de Entregas": np.random.randint(5, 50, size=50),
    "Região": np.random.choice(["Norte", "Sul", "Centro-Oeste", "Sudeste", "Nordeste"], size=50),
    "Tempo de Entrega (Horas)": np.random.randint(2, 24, size=50),
    "Status da Entrega": np.random.choice(["No prazo", "Atrasada", "Pendente"], size=50),
    "Tipo de Carga": np.random.choice(["Alimentos", "Eletrônicos", "Vestuário", "Medicamentos", "Móveis"], size=50),
    "Distância Percorrida (Km)": np.random.randint(10, 1000, size=50),
}

df_entregas_operacoes = pd.DataFrame(data)

print(df_entregas_operacoes.head())

df_entregas_operacoes.to_csv("dados_entregas_operacoes.csv", index=False, encoding='utf-8')