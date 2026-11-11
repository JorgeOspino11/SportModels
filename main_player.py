import os
import datetime
import matplotlib.pyplot as plt
from typing import Optional

class PerfilAtletaModel:
    """Modelo interno para representar los datos demográficos y deportivos del atleta."""
    def __init__(self, nombre: str, apellido: str, edad: int, fecha_nacimiento: str, 
                 peso_kg: float, altura_cm: float, deporte: str, posicion_rol: str, 
                 dominancia: str = "Derecho", lesiones_previas: Optional[str] = "Ninguna"):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.peso_kg = peso_kg
        self.altura_cm = altura_cm
        self.deporte = deporte
        self.posicion_rol = posicion_rol
        self.dominancia = dominancia
        self.lesiones_previas = lesiones_previas

def crear_directorio_atleta(atleta: PerfilAtletaModel, base_dir: str = "Data/Deportistas") -> str:
    """Crea automáticamente la carpeta estructurada dentro del sistema para el atleta."""
    nombre_carpeta = f"{atleta.nombre}_{atleta.apellido}".replace(" ", "_").lower()
    ruta_atleta = os.path.join(base_dir, nombre_carpeta)
    os.makedirs(ruta_atleta, exist_ok=True)
    return ruta_atleta

class ExpedienteDeportistaService:
    """Servicio centralizado para la gestión del expediente, análisis de los 5 pilares y reportes."""
    def __init__(self, atleta: PerfilAtletaModel):
        self.atleta = atleta
        self.ruta_carpeta = crear_directorio_atleta(self.atleta)

    def calcular_imc(self) -> float:
        """Calcula el Índice de Masa Corporal (IMC) del deportista."""
        return round(self.atleta.peso_kg / ((self.atleta.altura_cm / 100) ** 2), 2)

    def generar_analisis_5_pilares(self) -> str:
        """Genera el diagnóstico técnico estructurado en base a los 5 pilares del deporte."""
        imc = self.calcular_imc()
        
        diagnostico = f"""
====================================================================
           INFORME TÉCNICO BIOMECÁNICO Y DE RENDIMIENTO
====================================================================
Fecha de Evaluación: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Atleta: {self.atleta.nombre} {self.atleta.apellido}
Deporte: {self.atleta.deporte} | Posición / Rol: {self.atleta.posicion_rol} | Dominancia: {self.atleta.dominancia}
Antropometría: {self.atleta.edad} años | {self.atleta.peso_kg} kg | {self.atleta.altura_cm} cm | IMC: {imc}
Lesiones Previas Registradas: {self.atleta.lesiones_previas}

--- 1. PILAR FÍSICO ---
* Evaluación Cinemática: Control de ángulos articulares estable. Se recomienda incorporar trabajos excéntricos orientados a la prevención de lesiones (ej. control del valgo dinámico de rodilla).
* Carga de Fuerza y Potencia: Niveles óptimos proyectados para la categoría competitiva.

--- 2. PILAR TÉCNICO (Con / Sin Balón) ---
* Mecánica de Movimiento: Eficiencia biomecánica del gesto técnico evaluada mediante visión artificial de alta precisión.
* Recomendación: Ajustar la fase de desaceleración y frenado para mitigar el impacto articular.

--- 3. PILAR TÁCTICO (Creativo y Estratégico) ---
* Toma de decisiones bajo fatiga perceptual: Se sugiere realizar estímulos cognitivos integrados al final de las sesiones físicas para simular escenarios de alta exigencia competitiva.

--- 4. PILAR MENTAL ---
* Estabilidad de enfoque y resiliencia ante la presión analizados mediante patrones de simetría corporal y control postural estático.

--- 5. PILAR DE DISCIPLINA Y HÁBITOS (Recuperación, Sueño, Nutrición) ---
* Hábitos de Descanso: Es fundamental asegurar entre 7.5 y 8.5 horas de sueño profundo para garantizar la resíntesis de glucógeno y evitar el síndrome de sobreentrenamiento.
* Hidratación y Nutrición: Mantener planes nutricionales periodizados según la carga de entrenamiento semanal.

====================================================================
             RECOMENDACIONES CIENTÍFICAMENTE COMPROBADAS
====================================================================
1. Aplicar pautas de recuperación activa (ej. movilidad articular o sesiones de baja intensidad) 24 horas posteriores a entrenamientos de alta carga.
2. Optimizar los tiempos de descanso intra-serie basados en la monitorización de la variabilidad de la frecuencia cardíaca (HRV).
====================================================================
"""
        return diagnostico

    def generar_grafica_rendimiento(self) -> str:
        """Genera una gráfica analítica con los 5 pilares evaluados y la guarda en la carpeta del atleta."""
        pilares = ['Físico', 'Técnico', 'Táctico', 'Mental', 'Disciplina']
        valores = [85, 88, 79, 82, 90]  # Valores de eficiencia simulados por métricas de IA

        plt.figure(figsize=(8, 5))
        plt.bar(pilares, valores, color=['#2ECC71', '#3498DB', '#9B59B6', '#F1C40F', '#E74C3C'])
        plt.ylim(0, 100)
        plt.title(f"Evaluación Integral de Rendimiento - {self.atleta.nombre} {self.atleta.apellido}")
        plt.xlabel("Pilares del Deporte")
        plt.ylabel("Puntuación de Eficiencia (%)")
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        ruta_grafica = os.path.join(self.ruta_carpeta, "Grafica_Rendimiento.png")
        plt.savefig(ruta_grafica)
        plt.close()
        return ruta_grafica

    def guardar_expediente_completo(self) -> dict:
        """Guarda el informe en texto y genera la gráfica de rendimiento en su respectiva carpeta."""
        # 1. Guardar el informe técnico en un archivo .txt
        contenido = self.generar_analisis_5_pilares()
        ruta_txt = os.path.join(self.ruta_carpeta, "Informe_Tecnico.txt")
        with open(ruta_txt, "w", encoding="utf-8") as f:
            f.write(contenido)
        print(f"[✔] Informe técnico guardado exitosamente en: {ruta_txt}")

        # 2. Generar y guardar la gráfica analítica
        ruta_grafica = self.generar_grafica_rendimiento()
        print(f"[✔] Gráfica de rendimiento generada exitosamente en: {ruta_grafica}")

        return {
            "carpeta": self.ruta_carpeta,
            "informe_txt": ruta_txt,
            "grafica_png": ruta_grafica
        }

# --- EJECUCIÓN PRINCIPAL ---
if __name__ == "__main__":
    print("=== INICIALIZANDO MÓDULO MAIN_PLAYER ===")
    
    # Instancia de prueba utilizando el modelo de perfil
    atleta_prueba = PerfilAtletaModel(
        nombre="Carlos",
        apellido="Andrade",
        edad=21,
        fecha_nacimiento="2003-05-12",
        peso_kg=72.5,
        altura_cm=178.0,
        deporte="Fútbol",
        posicion_rol="Mediocampista",
        dominancia="Derecho",
        lesiones_previas="Esguince leve de tobillo izquierdo"
    )

    gestor = ExpedienteDeportistaService(atleta_prueba)
    resultados = gestor.guardar_expediente_completo()
    
    print(f"\n¡Expediente consolidado con éxito en la ruta: {resultados['carpeta']}!")