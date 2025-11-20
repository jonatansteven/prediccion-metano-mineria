# Predicción de Metano en Minería Subterránea - Boyacá

**Universidad ECCI – Electiva DevOps 2025**  
**Grupo 10 ANL**  
Jonatan Steven Gómez · Nicolás David González · Nicolás Palomino

[![CI/CD](https://github.com/jonatansteven/prediccion-metano-mineria/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/jonatansteven/prediccion-metano-mineria/actions)

## Descripción del proyecto
Modelo de **Regresión Lineal** para predecir niveles de metano (CH₄) en tiempo real en una mina de carbón de Boyacá, utilizando datos reales de un multidetector ambiental.

**Resultados del modelo (500 registros reales):**
- R² = **70.83%**
- MAE = **0.23**
- RMSE = **0.35**

¡Excelente rendimiento con solo 6 variables ambientales!

## Tecnologías y prácticas MLOps implementadas
| Componente               | Tecnología usada                 |
|---------------------------|-------------------------------------|
| Limpieza y EDA            | Pandas, Seaborn, Matplotlib         |
| Modelado                  | Scikit-learn (Regresión Lineal)     |
| Serialización            | joblib                              |
| API REST                  | Flask                               |
| Contenedorización         | Docker                              |
| CI/CD automático          | GitHub Actions                      |
| Versionado                | Git + GitHub                        |

## Estructura del repositorio
prediccion-metano-mineria/
├── modelo_final/              ← Modelo, scaler y métricas
├── datos_limpios_mina.csv     ← Dataset procesado
├── app.py                     ← API Flask
├── Dockerfile                 ← Imagen Docker lista para producción
├── requirements.txt
├── .github/workflows/ci-cd.yml ← Pipeline automático
└── README.md                  ← Este archivo
