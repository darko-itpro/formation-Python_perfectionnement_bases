"""
Données  -->  Entraînement d'un modèle  -->  Prédiction  -->  Évaluation
"""

from sklearn.linear_model import LinearRegression

model = LinearRegression()

# Données d'entrée (surface)
X = [[30], [40], [50], [60]]

# Valeurs à prédire (prix)
y = [100, 150, 200, 250]

model.fit(X, y)


print(model.predict([[45]]))
