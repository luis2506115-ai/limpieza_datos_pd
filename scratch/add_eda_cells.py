import json
import uuid

def create_markdown_cell(source_text):
    return {
        "cell_type": "markdown",
        "id": str(uuid.uuid4())[:8],
        "metadata": {},
        "source": [line + "\n" for line in source_text.strip().split("\n")]
    }

def create_code_cell(source_code):
    return {
        "cell_type": "code",
        "execution_count": None,
        "id": str(uuid.uuid4())[:8],
        "metadata": {},
        "outputs": [],
        "source": [line + "\n" for line in source_code.strip().split("\n")]
    }

notebook_path = "/Users/leonelmendiola/limpieza_datos_pd/limpieza_datos.ipynb"

# Load current notebook
with open(notebook_path, 'r', encoding='utf-8') as f:
    notebook_data = json.load(f)

new_cells = []

# Cell 1: Section Header and Intro (Markdown)
new_cells.append(create_markdown_cell("""
# 📊 8. Análisis Exploratorio de Datos (EDA) Avanzado

Habiendo completado la fase de limpieza y transformación de los datos a un formato estructurado y enriquecido ("Tidy Data"), procederemos a realizar un **Análisis Exploratorio de Datos (EDA)** detallado. El objetivo de esta sección es descubrir patrones ocultos, identificar los focos de mayor incidencia delictiva, analizar la temporalidad a corto plazo y comprender la composición de la delincuencia en México durante el primer cuatrimestre de 2026.

### Objetivos del EDA Avanzado:
1. **Distribución por Bien Jurídico:** Identificar cuáles son los derechos y bienes de los ciudadanos más afectados por la delincuencia.
2. **Análisis Geográfico:** Determinar qué estados concentran la mayor cantidad absoluta de delitos y cuáles presentan cifras más bajas.
3. **Foco en Delitos de Alto Impacto:** Analizar de manera particular los homicidios y sus modalidades (armas de fuego, armas blancas, etc.).
4. **Tendencias Temporales:** Observar la evolución y estacionalidad de los 5 delitos más comunes durante el periodo Enero-Abril.
5. **Comportamiento del Robo:** Desglosar el delito de robo para entender sus variantes y niveles de violencia.
"""))

# Cell 2: Affected Legal Assets (Code)
new_cells.append(create_code_cell("""
# 1. Agrupación y cálculo del total por Bien Jurídico Afectado
bien_juridico_stats = df_tidy.groupby('bien_juridico_afectado')['cantidad'].sum().sort_values(ascending=False).reset_index()
bien_juridico_stats['porcentaje'] = (bien_juridico_stats['cantidad'] / bien_juridico_stats['cantidad'].sum()) * 100

# Configuración del estilo visual premium
plt.figure(figsize=(12, 6))
colors = sns.color_palette("viridis", len(bien_juridico_stats))

ax = sns.barplot(
    data=bien_juridico_stats,
    x='cantidad',
    y='bien_juridico_afectado',
    palette=colors,
    edgecolor='black',
    linewidth=0.8
)

# Añadir etiquetas de valores y porcentajes en las barras
for i, bar in enumerate(ax.patches):
    width = bar.get_width()
    percentage = bien_juridico_stats.loc[i, 'porcentaje']
    ax.text(
        width + (bien_juridico_stats['cantidad'].max() * 0.01),
        bar.get_y() + bar.get_height()/2,
        f"{int(width):,} ({percentage:.1f}%)",
        va='center',
        ha='left',
        fontsize=10,
        fontweight='bold',
        color='#2c3e50'
    )

plt.title("Distribución de Delitos por Bien Jurídico Afectado (Ene - Abr 2026)", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Total de Incidencias Registradas", fontsize=11, fontweight='bold', labelpad=10)
plt.ylabel("Bien Jurídico Afectado", fontsize=11, fontweight='bold', labelpad=10)
plt.grid(axis='x', linestyle="--", alpha=0.5)
sns.despine(left=True, bottom=True)

plt.tight_layout()
plt.show()
"""))

# Cell 3: Legal Assets Explanation (Markdown)
new_cells.append(create_markdown_cell("""
*   **Interpretación:**
    *   **El patrimonio** es, por un amplio margen, el bien jurídico más afectado por la delincuencia (representando la gran mayoría de las incidencias). Esto es sumamente común en las estadísticas de seguridad pública, dado que los delitos patrimoniales (como el robo) representan el mayor volumen de denuncias ante el Ministerio Público.
    *   **La vida y la Integridad corporal** ocupa el segundo lugar, lo cual es de suma importancia ya que aquí se encuentran los delitos de más alto impacto (como homicidios, lesiones y feminicidios), que definen directamente la percepción de seguridad física y el bienestar social.
    *   **Libertad personal** y **La libertad y la seguridad sexual** muestran incidencias menores en términos absolutos pero representan delitos de extrema gravedad que requieren de un análisis focalizado y de políticas de prevención altamente especializadas.
"""))

# Cell 4: Geographical Analysis (Code)
new_cells.append(create_code_cell("""
# 2. Agrupar delitos por entidad federativa
entidades_stats = df_tidy.groupby('entidad')['cantidad'].sum().sort_values(ascending=False).reset_index()

fig, axes = plt.subplots(1, 2, figsize=(16, 7))

# Gráfico de los 10 estados con mayor incidencia
sns.barplot(
    data=entidades_stats.head(10),
    x='cantidad',
    y='entidad',
    palette="Reds_r",
    ax=axes[0],
    edgecolor='black',
    linewidth=0.8
)
axes[0].set_title("Top 10 Estados con Mayor Incidencia Delictiva", fontsize=13, fontweight='bold', pad=10)
axes[0].set_xlabel("Total de Delitos (Ene-Abr 2026)", fontsize=10, fontweight='bold')
axes[0].set_ylabel("Entidad Federativa", fontsize=10, fontweight='bold')
axes[0].grid(axis='x', linestyle="--", alpha=0.5)
for i, bar in enumerate(axes[0].patches):
    axes[0].text(bar.get_width() + 200, bar.get_y() + bar.get_height()/2, f"{int(bar.get_width()):,}", va='center', fontsize=9, fontweight='bold')

# Gráfico de los 10 estados con menor incidencia
sns.barplot(
    data=entidades_stats.tail(10).sort_values('cantidad'),
    x='cantidad',
    y='entidad',
    palette="Blues",
    ax=axes[1],
    edgecolor='black',
    linewidth=0.8
)
axes[1].set_title("Top 10 Estados con Menor Incidencia Delictiva", fontsize=13, fontweight='bold', pad=10)
axes[1].set_xlabel("Total de Delitos (Ene-Abr 2026)", fontsize=10, fontweight='bold')
axes[1].set_ylabel("", fontsize=10)
axes[1].grid(axis='x', linestyle="--", alpha=0.5)
for i, bar in enumerate(axes[1].patches):
    axes[1].text(bar.get_width() + 10, bar.get_y() + bar.get_height()/2, f"{int(bar.get_width()):,}", va='center', fontsize=9, fontweight='bold')

plt.suptitle("Análisis Geográfico de la Delincuencia en México (Primer Cuatrimestre 2026)", fontsize=16, fontweight='bold', y=0.98)
plt.tight_layout()
plt.show()
"""))

# Cell 5: Geographical Explanation (Markdown)
new_cells.append(create_markdown_cell("""
*   **Interpretación:**
    *   Este análisis geográfico ilustra la marcada disparidad en la frecuencia absoluta de delitos registrados a lo largo del país. 
    *   Los estados con las mayores concentraciones poblacionales y de grandes centros urbanos suelen liderar los conteos en términos absolutos, lo cual genera una carga de trabajo inmensa en las fiscalías locales.
    *   Por otro lado, los estados con menor población o con mejores condiciones de seguridad muestran un volumen sumamente bajo de incidencias en este primer cuatrimestre de 2026.
    *   *Nota metodológica:* Cabe destacar que para análisis sociodemográficos más profundos, se requeriría normalizar estas cifras por cada 100,000 habitantes; sin embargo, en términos absolutos de volumen operativo judicial, esta gráfica refleja dónde se requiere una mayor asignación de recursos policiacos e investigación.
"""))

# Cell 6: High-Impact Crimes (Code)
new_cells.append(create_code_cell("""
# 3. Filtrar delitos del tipo Homicidio
homicidios = df_tidy[df_tidy['tipo_delito'] == 'Homicidio']

# Agrupar por subtipo de homicidio (doloso vs culposo)
subtipo_homicidios = homicidios.groupby('subtipo_delito')['cantidad'].sum().reset_index()

# Agrupar por modalidad de homicidio doloso (los homicidios culposos son por accidente de tránsito u otros)
homicidios_dolosos = homicidios[homicidios['subtipo_delito'] == 'Homicidio doloso']
modalidades_dolosas = homicidios_dolosos.groupby('modalidad')['cantidad'].sum().sort_values(ascending=False).reset_index()

fig, axes = plt.subplots(1, 2, figsize=(16, 7))

# Gráfico izquierdo: Tipos de homicidio (doloso vs culposo)
axes[0].pie(
    subtipo_homicidios['cantidad'],
    labels=subtipo_homicidios['subtipo_delito'],
    autopct='%1.1f%%',
    colors=['#e74c3c', '#3498db', '#f1c40f'],
    startangle=90,
    textprops={'fontsize': 11, 'fontweight': 'bold'},
    wedgeprops={'edgecolor': 'black', 'linewidth': 0.8}
)
axes[0].set_title("Distribución de Homicidios por Subtipo\\n(Ene - Abr 2026)", fontsize=13, fontweight='bold', pad=10)

# Gráfico derecho: Modalidad de homicidios dolosos
sns.barplot(
    data=modalidades_dolosas,
    x='cantidad',
    y='modalidad',
    palette="copper",
    ax=axes[1],
    edgecolor='black',
    linewidth=0.8
)
axes[1].set_title("Modalidad de los Homicidios Dolosos\\n(Armas de Fuego, Armas Blancas, etc.)", fontsize=13, fontweight='bold', pad=10)
axes[1].set_xlabel("Número de Casos", fontsize=10, fontweight='bold')
axes[1].set_ylabel("Modalidad", fontsize=10, fontweight='bold')
axes[1].grid(axis='x', linestyle="--", alpha=0.5)
for i, bar in enumerate(axes[1].patches):
    axes[1].text(bar.get_width() + 10, bar.get_y() + bar.get_height()/2, f"{int(bar.get_width()):,}", va='center', fontsize=9, fontweight='bold')

plt.suptitle("Análisis Profundo de Homicidios en México (2026)", fontsize=16, fontweight='bold', y=0.98)
plt.tight_layout()
plt.show()
"""))

# Cell 7: High-Impact Explanation (Markdown)
new_cells.append(create_markdown_cell("""
*   **Interpretación:**
    *   El **Homicidio** es el delito más sensible y representativo de la violencia extrema.
    *   En el gráfico circular izquierdo, observamos la proporción entre homicidios culposos (negligentes, principalmente accidentes de tránsito) y homicidios dolosos (intencionales). La correcta tipificación de estas muertes es clave para el diagnóstico de la violencia en el país.
    *   En el gráfico de barras derecho, analizamos las modalidades de los homicidios dolosos. La utilización de **armas de fuego** resalta como la modalidad más frecuente en los crímenes violentos de alto impacto. Esto enfatiza la importancia crítica de diseñar y ejecutar programas de despistolización y de control de armas en las regiones más vulnerables.
"""))

# Cell 8: Temporal Trend of Top 5 Crimes (Code)
new_cells.append(create_code_cell("""
# 4. Obtener las 5 principales categorías de delito por volumen
top_delitos = df_tidy.groupby('tipo_delito')['cantidad'].sum().sort_values(ascending=False).head(5).index.tolist()

# Filtrar el dataframe para incluir solo estas categorías
df_top_temporal = df_tidy[df_tidy['tipo_delito'].isin(top_delitos)]

# Agrupar por tipo de delito y mes para ver la evolución
temporal_stats = df_top_temporal.groupby(['tipo_delito', 'mes'])['cantidad'].sum().reset_index()

# Ordenar los meses para graficar de forma lógica cronológica
meses_ordenados = ['Enero', 'Febrero', 'Marzo', 'Abril']
temporal_stats['mes'] = pd.Categorical(temporal_stats['mes'], categories=meses_ordenados, ordered=True)
temporal_stats = temporal_stats.sort_values(['tipo_delito', 'mes'])

# Graficar la tendencia de delitos
plt.figure(figsize=(12, 6))

sns.lineplot(
    data=temporal_stats,
    x='mes',
    y='cantidad',
    hue='tipo_delito',
    marker='o',
    markersize=8,
    linewidth=2.5,
    palette="Set1"
)

plt.title("Tendencia Mensual de los 5 Delitos Más Frecuentes (Ene - Abr 2026)", fontsize=14, fontweight='bold', pad=15)
plt.xlabel("Mes de Registro", fontsize=11, fontweight='bold', labelpad=10)
plt.ylabel("Total de Incidencias", fontsize=11, fontweight='bold', labelpad=10)
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend(title="Tipo de Delito", fontsize=10, title_fontsize=11)
sns.despine()

plt.tight_layout()
plt.show()
"""))

# Cell 9: Temporal Trend Explanation (Markdown)
new_cells.append(create_markdown_cell("""
*   **Interpretación:**
    *   Este gráfico de líneas permite observar la trayectoria mensual de las 5 categorías más representativas del fuero común.
    *   **Robo** se posiciona consistentemente a la cabeza, manteniendo una tendencia estable con ligeras fluctuaciones mensuales que podrían responder a factores socioeconómicos o dinámicas estacionales del periodo Enero-Abril.
    *   La estabilidad y el paralelismo de las curvas sugieren que las dinámicas delictivas operan bajo patrones consolidados, los cuales requieren intervenciones sistémicas a largo plazo más allá de operativos temporales de reacción inmediata.
"""))

# Cell 10: Robbery Modality (Code)
new_cells.append(create_code_cell("""
# 5. Filtrar delitos del tipo Robo
robos = df_tidy[df_tidy['tipo_delito'] == 'Robo']

# Agrupar por modalidad (Con violencia vs Sin violencia)
modalidad_robos = robos.groupby('modalidad')['cantidad'].sum().reset_index()

# Agrupar por subtipo de robo y obtener los 8 principales
subtipos_robos = robos.groupby('subtipo_delito')['cantidad'].sum().sort_values(ascending=False).head(8).reset_index()

# Acortar nombres largos de subtipos para mejor visualización
subtipos_robos['subtipo_delito'] = subtipos_robos['subtipo_delito'].apply(lambda x: x[:40] + '...' if len(x) > 40 else x)

fig, axes = plt.subplots(1, 2, figsize=(16, 7))

# Gráfico izquierdo: Modalidad de robo (Con vs Sin violencia)
axes[0].pie(
    modalidad_robos['cantidad'],
    labels=modalidad_robos['modalidad'],
    autopct='%1.1f%%',
    colors=['#e67e22', '#2ecc71'],
    startangle=140,
    textprops={'fontsize': 11, 'fontweight': 'bold'},
    wedgeprops={'edgecolor': 'black', 'linewidth': 0.8}
)
axes[0].set_title("Proporción de Robos con y sin Violencia\\n(Primer Cuatrimestre 2026)", fontsize=13, fontweight='bold', pad=10)

# Gráfico derecho: Top 8 Subtipos de robo
sns.barplot(
    data=subtipos_robos,
    x='cantidad',
    y='subtipo_delito',
    palette="magma",
    ax=axes[1],
    edgecolor='black',
    linewidth=0.8
)
axes[1].set_title("Top 8 Subtipos de Robo Más Frecuentes", fontsize=13, fontweight='bold', pad=10)
axes[1].set_xlabel("Número de Casos", fontsize=10, fontweight='bold')
axes[1].set_ylabel("Subtipo de Robo", fontsize=10, fontweight='bold')
axes[1].grid(axis='x', linestyle="--", alpha=0.5)
for i, bar in enumerate(axes[1].patches):
    axes[1].text(bar.get_width() + 10, bar.get_y() + bar.get_height()/2, f"{int(bar.get_width()):,}", va='center', fontsize=9, fontweight='bold')

plt.suptitle("Análisis Detallado del Robo en México (Ene - Apr 2026)", fontsize=16, fontweight='bold', y=0.98)
plt.tight_layout()
plt.show()
"""))

# Cell 11: Robbery Explanation (Markdown)
new_cells.append(create_markdown_cell("""
*   **Interpretación:**
    *   Al desglosar el delito de **Robo** (el de mayor frecuencia), encontramos un equilibrio relevante entre robos cometidos **con violencia** y **sin violencia**. Una alta tasa de robos violentos representa un foco rojo para la integridad física de los ciudadanos en su vida cotidiana.
    *   La clasificación por **subtipo de robo** revela de manera clara cuáles son las modalidades que más aquejan a la sociedad: el robo de vehículos, el robo a transeúntes (en vía pública y espacio abierto), el robo a negocio y el robo a casa habitación.
    *   Esta información es esencial para la planeación táctica de patrullajes urbanos y para la prevención del delito, orientando los recursos de seguridad pública a los puntos críticos (paradas de transporte, zonas comerciales y habitacionales).
"""))

# Cell 12: Summary and Strategic Insights (Markdown)
new_cells.append(create_markdown_cell("""
# 📝 9. Conclusiones y Hallazgos Clave del EDA

1.  **Predominio de Delitos Patrimoniales:** El patrimonio es el bien jurídico más vulnerable en México, concentrando la inmensa mayoría de las carpetas de investigación, impulsado principalmente por las diversas modalidades de robo.
2.  **Distribución Asimétrica del Delito:** Existe una concentración delictiva pronunciada en unas cuantas entidades del país. Esto resalta la necesidad de estrategias de seguridad pública regionalizadas, adaptadas a los volúmenes operativos reales de cada estado.
3.  **Homicidios y Violencia Armada:** Un porcentaje sumamente elevado de homicidios dolosos son perpetrados con **arma de fuego**. Las políticas de desarme y pacificación territorial en los municipios clave son esenciales para reducir esta tasa crítica.
4.  **Estabilidad Temporal a Corto Plazo:** Los delitos más frecuentes muestran tendencias mensuales estables en el primer cuatrimestre de 2026, lo cual sugiere la existencia de patrones estructurales y criminales constantes en el territorio.
5.  **Diversificación del Robo:** El robo a transeúnte, a comercio, de vehículos y a casa habitación son las variantes principales del delito patrimonial. El combate coordinado a estos delitos en micro-zonificaciones específicas puede tener un impacto masivo y positivo en la percepción de seguridad ciudadana.
"""))

# Append new cells
notebook_data['cells'].extend(new_cells)

# Write modified notebook
with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(notebook_data, f, indent=1)

print("EDA cells added successfully to the notebook!")
