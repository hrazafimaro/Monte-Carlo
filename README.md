# Monte Carlo Integration - Vectorized Python

Ce projet montre une **estimation de l'intégrale** de la fonction :
f(x) = 0.5*exp(x) + 1

sur l'intervalle [0.5, 1.5] **avec la méthode Monte Carlo vectorisée** en Python.

## Features

- Monte Carlo vectorisé (pas de boucle Python)  
- Calcul de l'erreur relative par rapport à la valeur exacte  
- Seed pour reproductibilité  
- Exemple de notebook avec graphique

## Installation

```bash
pip install numpy matplotlib
```

## Exécution du script

```bash
python monte_carlo.py
```

## Exécution du notebook

```bash
jupyter notebook notebooks/demo.ipynb
```

## Exemple de sortie

```text
Monte Carlo estimate: 2.649234
Exact integral      : 2.648721
Relative error      : 0.019%
```
