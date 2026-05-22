import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer
from sklearn.decomposition import PCA


# caricamento dataset
dataset = load_breast_cancer()

# dati
X = dataset.data

# target
y = dataset.target


# PCA con 2 componenti
pca = PCA(n_components=2)

# trasformazione dati
X_pca = pca.fit_transform(X)


# grafico tumori benigni
plt.scatter(
    X_pca[y == 1, 0],
    X_pca[y == 1, 1],
    label="Tumore benigno")


# grafico tumori maligni
plt.scatter(
    X_pca[y == 0, 0],
    X_pca[y == 0, 1],
    label="Tumore maligno")


# nomi assi
plt.xlabel("Informazioni principali")

plt.ylabel("Informazioni secondarie")

# titolo
plt.title("Analisi PCA Tumore al Seno")

# legenda
plt.legend()

# mostra grafico
plt.show()