import streamlit as st

def calcular_riesgo_metastasis(tamano, profundidad, grado, invasion_perineural, invasion_linfovascular, ubicacion, recurrencia, inmunosupresion):
    """
    Calculadora de riesgo de metástasis nodal en carcinoma escamoso cutáneo (cSCC)
    Parámetros:
    - tamano: Tamaño del tumor en cm
    - profundidad: Profundidad del tumor en mm
    - grado: 'bien diferenciado', 'moderadamente diferenciado', 'pobremente diferenciado'
    - invasion_perineural: True o False
    - invasion_linfovascular: True o False
    - ubicacion: 'bajo riesgo' (tronco/extremidades), 'alto riesgo' (cabeza, cuello, periocular, periauricular, cuero cabelludo)
    - recurrencia: True o False
    - inmunosupresion: True o False
    
    Retorna:
    - Riesgo estimado en porcentaje de metástasis nodal
    """
    
    # Factores de riesgo y su peso en el cálculo
    riesgo = 0
    
    # Tamaño del tumor
    if tamano > 2:
        riesgo += 10  # Aumenta riesgo si >2 cm
    if tamano > 5:
        riesgo += 15  # Aumenta aún más si >5 cm
    
    # Profundidad de invasión
    if profundidad > 4:
        riesgo += 15  # Alto riesgo si >4 mm
    if profundidad > 6:
        riesgo += 20  # Aumenta aún más si >6 mm
    
    # Grado histológico
    if grado == 'pobremente diferenciado':
        riesgo += 15
    elif grado == 'moderadamente diferenciado':
        riesgo += 10
    
    # Invasión perineural y linfovascular
    if invasion_perineural:
        riesgo += 15
    if invasion_linfovascular:
        riesgo += 10
    
    # Ubicación del tumor
    if ubicacion == 'alto riesgo':
        riesgo += 10
    
    # Recurrencia
    if recurrencia:
        riesgo += 15
    
    # Inmunosupresión
    if inmunosupresion:
        riesgo += 20  # Alto riesgo en pacientes inmunosuprimidos
    
    # Máximo riesgo teórico 100%
    return min(riesgo, 100)

# Interfaz de usuario con Streamlit
st.title("Calculadora de Riesgo de Metástasis Nodal en cSCC")

tamano = st.number_input("Tamaño del tumor (cm)", min_value=0.0, max_value=10.0, step=0.1)
profundidad = st.number_input("Profundidad del tumor (mm)", min_value=0.0, max_value=20.0, step=0.1)
grados = ['bien diferenciado', 'moderadamente diferenciado', 'pobremente diferenciado']
grados_seleccion = st.selectbox("Grado histológico", grados)
invasion_perineural = st.checkbox("Invasión perineural")
invasion_linfovascular = st.checkbox("Invasión linfovascular")
ubicaciones = ['bajo riesgo', 'alto riesgo']
ubicacion_seleccion = st.selectbox("Ubicación del tumor", ubicaciones)
recurrencia = st.checkbox("Recurrencia previa")
inmunosupresion = st.checkbox("Inmunosupresión")

if st.button("Calcular Riesgo"):
    riesgo = calcular_riesgo_metastasis(tamano, profundidad, grados_seleccion, invasion_perineural, invasion_linfovascular, ubicacion_seleccion, recurrencia, inmunosupresion)
    st.write(f"El riesgo estimado de metástasis nodal es: {riesgo}%")

# Guardar como ejecutable con PyInstaller (instrucciones)
# Ejecutar en terminal o consola: 
# pyinstaller --onefile --windowed --name "Calculadora_cSCC" calculadora_cSCC.py
