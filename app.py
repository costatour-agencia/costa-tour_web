import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="Costa-Tour | Agencia de Viajes", 
    layout="wide", 
    page_icon="✈️"
)

# 2. ESTILOS CSS AVANZADOS (Limpieza total de recuadros e incrustaciones)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&family=Lora:ital,wght@0,400;1,400&display=swap');

    /* Reset total de fondos de Streamlit */
    .stApp {
        background-color: #FFFFFF !important;
    }
    
    /* Eliminar el recuadro blanco que aparece en los botones (Captura image_2d6de3.jpg) */
    div.stButton > button > div > border {
        display: none !important;
    }
    
    .stButton > button {
        background-color: #C0392B !important;
        color: white !important;
        border: none !important;
        outline: none !important;
        box-shadow: none !important;
        width: auto;
        display: block;
        margin: 0 auto;
    }

    /* Estilo específico para el texto dentro del botón para evitar el recuadro blanco */
    .stButton > button p {
        background-color: transparent !important;
        color: white !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    /* Limpieza del Hero Section (Captura image_2d5eff.jpg) */
    .hero-section {
        background-image: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), url('https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=1400');
        background-size: cover;
        background-position: center;
        height: 500px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        text-align: center;
        flex-direction: column;
        border-radius: 0 0 50px 50px;
        margin-bottom: 40px;
    }

    /* Forzar que el título no tenga fondo blanco */
    .hero-title {
        background: transparent !important;
        background-color: transparent !important;
        color: white !important;
        font-family: 'Lora', serif;
        font-size: 70px;
        margin: 0;
        padding: 0;
        border: none !important;
    }

    /* Quitar bordes de enfoque en botones */
    .stButton > button:focus, .stButton > button:active {
        background-color: #8B4513 !important;
        color: white !important;
        border: none !important;
        box-shadow: none !important;
    }

    /* Barra superior */
    .top-bar {
        background-color: #8B4513;
        color: white;
        padding: 10px 60px;
        display: flex;
        justify-content: space-between;
        font-size: 14px;
        font-weight: 300;
    }

    /* Tabs estéticos */
    .stTabs [data-baseweb="tab-list"] {
        gap: 50px;
        justify-content: center;
    }

    .stTabs [data-baseweb="tab"] {
        font-weight: 600;
        color: #8B4513;
        background-color: transparent !important;
    }

    /* Descripciones de paquetes */
    .package-description {
        font-family: 'Poppins', sans-serif;
        font-size: 14px;
        color: #555;
        text-align: center;
        padding: 10px;
        background: transparent !important;
    }

    /* WhatsApp Flotante */
    .whatsapp-float {
        position: fixed;
        bottom: 30px;
        right: 30px;
        background-color: #25d366;
        color: white;
        padding: 15px 30px;
        border-radius: 50px;
        text-decoration: none;
        z-index: 1000;
        font-weight: 600;
        box-shadow: 0 8px 25px rgba(37, 211, 102, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. BARRA SUPERIOR
st.markdown("""
    <div class="top-bar">
        <div>📞 +57 324 373 1661 | ✉️ veronicaarangopedrozo@gmail.com</div>
        <div>📍 Bahía Solano | Cartagena | Nuquí | San Andrés | Santa Marta</div>
    </div>
    """, unsafe_allow_html=True)

# 4. HEADER CON LOGO
col_logo, _ = st.columns([1, 3])
with col_logo:
    # Usando el logo proporcionado ve.png
    st.image("https://i.ibb.co/ds6F7b72/ve.png", width=250)

# 5. NAVEGACIÓN
tab_inicio, tab_tours, tab_formularios, tab_blog = st.tabs([
    "CONÓCENOS", "NUESTROS TOURS", "SERVICIOS", "BLOG"
])

# --- SECCIÓN: CONÓCENOS ---
with tab_inicio:
    st.markdown("""
        <div class="hero-section">
            <h1 class="hero-title">Costa-Tour</h1>
            <p style='font-size: 24px; font-style: italic; font-weight: 300; background: transparent;'>
                Nuestra prioridad no es el destino, es tu experiencia.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    c1, c2 = st.columns([1, 1])
    with c1:
        st.markdown("<h2 style='color: #8B4513; font-family: \"Lora\", serif;'>Conócenos</h2>", unsafe_allow_html=True)
        st.markdown("""
        <p style='text-align: justify; font-size: 16px; line-height: 1.8;'>
        En <b>Costa-Tour</b>, redefinimos el concepto de viaje. Creemos firmemente que el lujo no es un lugar, 
        es la calidad del servicio que te acompaña en el camino. Nos especializamos en conectar el corazón de 
        Colombia con el mundo.
        </p>
        """, unsafe_allow_html=True)
    with c2:
        st.image("https://images.unsplash.com/photo-1590523277543-a94d2e4eb00b?w=800")

# --- SECCIÓN: TOURS ---
with tab_tours:
    st.markdown("<h1 style='text-align: center; font-family: \"Lora\", serif; color: #8B4513;'>Portafolio de Experiencias</h1>", unsafe_allow_html=True)
    
    # --- PREMIUM ---
    st.markdown("<h2 style='border-left: 5px solid #C0392B; padding-left: 15px; margin-top: 40px;'>⭐ Categoría Premium</h2>", unsafe_allow_html=True)
    
    cp1, cp2, cp3, cp4 = st.columns(4)
    paquetes_premium = [
        ("Caribe Mágico", "https://images.unsplash.com/photo-1548574505-5e239809ee19?w=400", "p1", "Suite presidencial, traslados en yate privado y playas exclusivas."),
        ("Pacífico Vivo", "https://images.unsplash.com/photo-1516815231560-8f41ec531527?w=400", "p2", "Eco-lodges boutique y avistamiento privado de ballenas."),
        ("Pacífico Místico", "https://images.unsplash.com/photo-1554357475-acce8d059b4b?w=400", "p3", "Retiros de bienestar y tours nocturnos VIP."),
        ("Sol Caribe", "https://images.unsplash.com/photo-1506929197327-fb877276303b?w=400", "p4", "Vuelos charter y club de playa privado.")
    ]

    cols_p = [cp1, cp2, cp3, cp4]
    for i, (nombre, img, key, desc) in enumerate(paquetes_premium):
        with cols_p[i]:
            st.image(img)
            st.markdown(f"<h4 style='text-align: center; margin-top: 10px;'>{nombre}</h4>", unsafe_allow_html=True)
            
            if f"show_{key}" not in st.session_state: st.session_state[f"show_{key}"] = False
            
            if not st.session_state[f"show_{key}"]:
                if st.button("Ver más detalles", key=f"btn_{key}"):
                    st.session_state[f"show_{key}"] = True
                    st.rerun()
            else:
                st.markdown(f"<div class='package-description'>{desc}</div>", unsafe_allow_html=True)
                if st.button("Ver menos", key=f"btn_{key}_less"):
                    st.session_state[f"show_{key}"] = False
                    st.rerun()

    # --- ESTÁNDAR ---
    st.markdown("<h2 style='border-left: 5px solid #8B4513; padding-left: 15px; margin-top: 40px;'>🚢 Categoría Estándar</h2>", unsafe_allow_html=True)
    ce1, ce2, ce3, ce4 = st.columns(4)
    paquetes_estandar = [
        ("Nuestra Costa", "https://images.unsplash.com/photo-1590523277543-a94d2e4eb00b?w=400", "e1", "Hoteles seleccionados y tours grupales de calidad."),
        ("Marea", "https://images.unsplash.com/photo-1580619305218-8423a7ef79b4?w=400", "e2", "Experiencias culturales con guías locales expertos."),
        ("Ritmo Caribe", "https://images.unsplash.com/photo-1584132967334-10e028bd69f7?w=400", "e3", "Plan familiar con cenas temáticas incluidas."),
        ("Ruta Marina", "https://images.unsplash.com/photo-1590001158193-790179980bd3?w=400", "e4", "Exploración de arrecifes y equipo de snorkel.")
    ]

    cols_e = [ce1, ce2, ce3, ce4]
    for i, (nombre, img, key, desc) in enumerate(paquetes_estandar):
        with cols_e[i]:
            st.image(img)
            st.markdown(f"<h4 style='text-align: center; margin-top: 10px;'>{nombre}</h4>", unsafe_allow_html=True)
            
            if f"show_{key}" not in st.session_state: st.session_state[f"show_{key}"] = False
            
            if not st.session_state[f"show_{key}"]:
                if st.button("Ver más", key=f"btn_{key}"):
                    st.session_state[f"show_{key}"] = True
                    st.rerun()
            else:
                st.markdown(f"<div class='package-description'>{desc}</div>", unsafe_allow_html=True)
                if st.button("Ver menos", key=f"btn_{key}_less"):
                    st.session_state[f"show_{key}"] = False
                    st.rerun()

# --- SECCIÓN: FORMULARIOS ---
with tab_formularios:
    st.markdown("<h2 style='color: #8B4513; font-family: \"Lora\", serif;'>Atención al Cliente</h2>", unsafe_allow_html=True)
    st.link_button("Radicar Queja o Reclamo (PQR)", "https://forms.office.com/pages/responsepage.aspx?id=IefhmYRxjkmK_7KtTlPBwmzEaoV6AVxMnWIMDnUV_6JUQjFRQVBCSEg5UldERzdTVkUxU1ZTRTFTMy4u&route=shorturl")

# --- SECCIÓN: BLOG ---
with tab_blog:
    st.markdown("<h2 style='color: #8B4513; font-family: \"Lora\", serif;'>Costa-Tour Blog</h2>", unsafe_allow_html=True)
    st.link_button("Explorar Blog", "https://tipsdeviajeparalacostacolombiana.blogspot.com/p/tips-de-viaje-para-la-costa-caribe-y-la.html")

# 6. WHATSAPP FLOTANTE
st.markdown("""
    <a href="https://wa.me/573243731661?text=Hola%20Costa-Tour!" class="whatsapp-float" target="_blank">
        💬 ¡Reserva con un Asesor!
    </a>
    """, unsafe_allow_html=True)