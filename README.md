# 🧹 Limpieza y Análisis Exploratorio de Datos — Incidencia Delictiva en México (2026)

> Pipeline de limpieza, transformación y análisis exploratorio de datos (EDA) sobre la incidencia delictiva estatal reportada en el **Registro Nacional de Incidencias de Delitos (RNID)**, enero–abril 2026.

---

## 📋 Tabla de Contenidos

- [Descripción del Proyecto](#-descripción-del-proyecto)
- [Dataset](#-dataset)
- [Pipeline de Procesamiento](#-pipeline-de-procesamiento)
- [Hallazgos Clave](#-hallazgos-clave)
- [Tecnologías Utilizadas](#-tecnologías-utilizadas)
- [Requisitos](#-requisitos)
- [Cómo Ejecutar](#-cómo-ejecutar)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Licencia](#-licencia)

---

## 📖 Descripción del Proyecto

Este proyecto implementa un flujo completo de **ciencia de datos** en un Jupyter Notebook:

1. **Carga e inspección** del dataset crudo de incidencia delictiva estatal.
2. **Diagnóstico de calidad**: detección de valores nulos, tipos de datos incorrectos y columnas vacías.
3. **Estandarización**: renombrado de columnas a `snake_case` y normalización de texto.
4. **Tratamiento de columnas vacías**: eliminación de meses sin datos (mayo–diciembre).
5. **Transformación a Tidy Data**: pivoteo de columnas de meses a filas con `pd.melt`.
6. **Enriquecimiento**: creación de columnas auxiliares (número de mes, fecha completa).
7. **Visualización**: gráficos descriptivos de tendencias, rankings y distribuciones.
8. **EDA avanzado**: análisis por bien jurídico, entidad federativa, tipo de homicidio, tendencias temporales y modalidades de robo.

---

## 📁 Dataset

| Campo | Detalle |
|---|---|
| **Fuente** | Registro Nacional de Incidencias de Delitos (RNID) — Datos abiertos del Gobierno de México |
| **Archivo** | `data/RNID-Delitos_Estatal-2026-abr2026.csv` |
| **Codificación** | `latin1` |
| **Registros** | ~3,648 filas × 19 columnas |
| **Periodo** | Enero – Abril 2026 |
| **Granularidad** | Estatal (32 entidades federativas) |

### Columnas originales

| Columna | Descripción |
|---|---|
| `Año` | Año de registro (2026) |
| `Clave_Ent` | Clave numérica de la entidad federativa |
| `Entidad` | Nombre de la entidad federativa |
| `Bien jurídico afectado` | Categoría del bien jurídico (patrimonio, vida, libertad, etc.) |
| `Tipo de delito` | Tipo de delito (homicidio, robo, fraude, etc.) |
| `Subtipo de delito` | Subtipo específico del delito |
| `Modalidad` | Modalidad del delito (con violencia, con arma de fuego, etc.) |
| `Enero` – `Diciembre` | Cantidad de carpetas de investigación por mes |

---

## ⚙️ Pipeline de Procesamiento

```
CSV crudo (19 cols, formato ancho)
  │
  ├─ 1. Carga con encoding latin1
  ├─ 2. Diagnóstico de calidad (nulos, dtypes, duplicados)
  ├─ 3. Estandarización (snake_case, normalización de texto)
  ├─ 4. Eliminación de columnas vacías (mayo–diciembre)
  ├─ 5. Pivot a formato Tidy Data (melt → filas por mes)
  ├─ 6. Enriquecimiento (mes numérico, fecha)
  ├─ 7. Visualización descriptiva
  └─ 8. EDA avanzado y conclusiones
          │
          ▼
  DataFrame limpio y enriquecido (formato largo)
```

---

## 📊 Hallazgos Clave

1. **Predominio de delitos patrimoniales** — El patrimonio concentra la mayoría de las carpetas de investigación, impulsado por las diversas modalidades de robo.
2. **Distribución asimétrica** — Unas pocas entidades concentran un volumen desproporcionado de delitos, evidenciando la necesidad de estrategias regionalizadas.
3. **Homicidios y violencia armada** — Un porcentaje muy elevado de homicidios dolosos se perpetran con arma de fuego.
4. **Estabilidad temporal** — Los delitos más frecuentes muestran tendencias mensuales estables en el primer cuatrimestre, sugiriendo patrones estructurales.
5. **Diversificación del robo** — Robo a transeúnte, a comercio, de vehículos y a casa habitación son las variantes principales.

---

## 🛠️ Tecnologías Utilizadas

| Herramienta | Uso |
|---|---|
| **Python 3** | Lenguaje principal |
| **Pandas** | Manipulación y limpieza de datos |
| **NumPy** | Operaciones numéricas |
| **Matplotlib** | Gráficos estáticos |
| **Seaborn** | Visualizaciones estadísticas |
| **Jupyter Notebook** | Entorno interactivo de análisis |

---

## 📦 Requisitos

- Python ≥ 3.8
- Jupyter Notebook o JupyterLab

Instala las dependencias con:

```bash
pip install pandas numpy matplotlib seaborn jupyter
```

---

## 🚀 Cómo Ejecutar

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/mendiolaleonel2002-debug/limpieza_datos_pd.git
   cd limpieza_datos_pd
   ```

2. **Instalar dependencias:**

   ```bash
   pip install pandas numpy matplotlib seaborn jupyter
   ```

3. **Abrir el notebook:**

   ```bash
   jupyter notebook limpieza_datos.ipynb
   ```

4. **Ejecutar todas las celdas** (`Kernel → Restart & Run All`) para reproducir el análisis completo.

---

## 📂 Estructura del Proyecto

```
limpieza_datos_pd/
├── data/
│   └── RNID-Delitos_Estatal-2026-abr2026.csv   # Dataset original (RNID)
├── limpieza_datos.ipynb                          # Notebook con pipeline completo
├── LICENSE                                       # Licencia MIT
└── README.md                                     # Este archivo
```

---

## 📄 Licencia

Este proyecto está bajo la [Licencia MIT](LICENSE). © 2026 Leonel Mendiola.
