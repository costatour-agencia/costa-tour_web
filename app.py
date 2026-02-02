import streamlit as st

# --- CONFIGURACIÓN E IMAGEN DE MARCA ---
st.set_page_config(page_title="Costa-Tour | Expertos en Caribe y Pacífico", layout="wide", page_icon="🌴")

# Estilo personalizado con tus colores (Rojo, Naranja, Tierra)
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .st-emotion-cache-16idsys p { font-size: 1.1rem; }
    div.stButton > button {
        background-color: #C0392B;
        color: white;
        border-radius: 5px;
        height: 3em;
        width: 100%;
        border: none;
    }
    div.stButton > button:hover {
        background-color: #D35400;
        color: white;
        border: 1px solid #8B4513;
    }
    .destinos-card {
        background-color: #F4E7D3;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #D35400;
    }
    </style>
    """, unsafe_allow_html=True)

# --- FUNCIONES DE AYUDA ---
def boton_whatsapp(mensaje):
    # Reemplaza el número con el tuyo (formato internacional sin el +)
    numero = "573000000000" 
    url = f"https://wa.me/{numero}?text={mensaje.replace(' ', '%20')}"
    st.markdown(f'[@ Contactar a un asesor por WhatsApp]({url})', unsafe_allow_html=True)

# --- BARRA LATERAL ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/826/826070.png", width=120)
    st.title("Costa-Tour")
    menu = st.radio("Navegación", ["Conócenos", "Nuestros Tours", "Formularios", "Blog y Noticias"])
    st.divider()
    st.write("**Atención al Cliente:**")
    boton_whatsapp("Hola Costa-Tour, quiero información sobre un plan.")

# --- SECCIÓN 1: CONÓCENOS ---
if menu == "Conócenos":
    st.header("📍 Conócenos: Tu puerta al paraíso")
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.write("""
        ### ¿Quiénes somos?
        En **Costa-Tour**, no solo vendemos viajes; creamos memorias en los rincones más exóticos de Colombia. 
        Operamos en destinos emblemáticos tanto para el turista nacional como para el extranjero.
        
        **Nuestra especialidad:**
        Logística integral en 11 destinos mágicos: Bahía Solano, Cabo de la Vela, Cartagena, Coveñas, 
        Isla Múcura, Nuquí, Palomino, Riohacha, San Andrés, Santa Marta y Tolú.
        """)
    with col2:
        st.image("https://images.unsplash.com/photo-1590523277543-a94d2e4eb00b?w=800", caption="Atardecer en el Caribe colombiano")

# --- SECCIÓN 2: NUESTROS TOURS ---
elif menu == "Nuestros Tours":
    st.header("🏝️ Portafolio de Experiencias")
    
    tipo_plan = st.tabs(["⭐ Planes Premium", "🚢 Planes Estándar"])
    
    with tipo_plan[0]:
        st.subheader("Excelencia y Confort")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown('<div class="destinos-card"><h4>Caribe Mágico & Sol Caribe</h4><p>Incluye: Vuelos privados, hoteles boutique en Cartagena/San Andrés, tours de lujo y alimentación gourmet.</p></div>', unsafe_allow_html=True)
            if st.button("Cotizar Premium Caribe"):
                boton_whatsapp("Hola, me interesa el plan Premium Caribe Mágico")
        with c2:
            st.markdown('<div class="destinos-card"><h4>Pacífico Vivo & Místico</h4><p>Incluye: Eco-lodges premium en Nuquí/Bahía Solano, avistamiento privado de ballenas y guías bilingües.</p></div>', unsafe_allow_html=True)
            if st.button("Cotizar Premium Pacífico"):
                boton_whatsapp("Hola, me interesa el plan Premium Pacífico")

    with tipo_plan[1]:
        st.subheader("Aventura y Tradición")
        st.write("Nuestros planes **Nuestra Costa, Marea, Ritmo Caribe y Ruta Marina** ofrecen la mejor experiencia local.")
        c3, c4 = st.columns(2)
        with c3:
            st.write("✅ **Nuestra Costa / Marea:** Planes ideales para Tolú, Coveñas e Isla Múcura.")
        with c4:
            st.write("✅ **Ritmo Caribe / Ruta Marina:** Explora Palomino, Riohacha y el Cabo de la Vela.")

# --- SECCIÓN 3: FORMULARIOS ---
elif menu == "Formularios":
    st.header("📋 Gestión de Servicios")
    st.write("Selecciona el proceso que deseas realizar:")
    
    f1, f2, f3 = st.columns(3)
    with f1:
        st.info("### Registro de Viajero")
        st.write("Completa tus datos para el seguro de viaje.")
        st.link_button("Ir al Formulario", "https://tu-link-de-google-forms.com")
    with f2:
        st.error("### PQR y Sugerencias")
        st.write("Dinos cómo podemos mejorar tu experiencia.")
        st.link_button("Buzón de Sugerencias", "https://tu-link-de-pqr.com")
    with f3:
        st.success("### Encuesta de Satisfacción")
        st.write("¿Cómo te fue en tu viaje?")
        st.link_button("Llenar Encuesta", "https://tu-link-de-encuesta.com")

# --- SECCIÓN 4: BLOG ---
elif menu == "Blog y Noticias":
    st.header("📰 Blog Costa-Tour")
    st.image("https://images.unsplash.com/photo-1516815231560-8f41ec531527?w=1000", caption="Explora Colombia")
    st.markdown("""
    ### 5 Consejos para visitar el Cabo de la Vela
    1. **Lleva efectivo:** En la Alta Guajira no hay muchos cajeros.
    2. **Respeto cultural:** Aprende sobre la comunidad Wayuú.
    ...
    """)
    