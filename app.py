import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="Costa-Tour | Agencia de Viajes", 
    layout="wide", 
    page_icon="✈️"
)

# 2. ESTILOS CSS AVANZADOS (Inspirado en la referencia de Protours)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&family=Lora:ital,wght@0,400;1,400&display=swap');

    /* Fondo y Fuente General */
    html, body, [class*="st-emotion-cache"] {
        background-color: #FFFFFF;
        font-family: 'Poppins', sans-serif;
        color: #333333;
    }

    /* Fuente Fina para párrafos */
    p, li {
        font-weight: 300;
        font-family: 'Poppins', sans-serif;
    }

    /* Encabezado Superior (Barra de Contacto) */
    .top-bar {
        background-color: #8B4513; /* Tierra */
        color: white;
        padding: 5px 50px;
        display: flex;
        justify-content: space-between;
        font-size: 12px;
    }

    /* Imagen Principal (Hero Section) */
    .hero-section {
        background-image: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), url('https://images.unsplash.com/photo-1548574505-5e239809ee19?w=1200');
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
        margin-bottom: 30px;
    }

    /* Botones Personalizados */
    .stButton>button {
        background-color: #C0392B !important; /* Rojo */
        color: white !important;
        border-radius: 25px !important;
        border: none !important;
        padding: 10px 30px !important;
        font-weight: 600 !important;
        transition: 0.3s !important;
    }

    .stButton>button:hover {
        background-color: #D35400 !important; /* Naranja */
        transform: scale(1.05);
    }

    /* Botón Flotante WhatsApp */
    .whatsapp-float {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background-color: #25d366;
        color: white;
        padding: 15px 25px;
        border-radius: 50px;
        text-decoration: none;
        z-index: 100;
        font-weight: bold;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
    }

    /* Navegación Superior (Tabs) */
    .stTabs [data-baseweb="tab-list"] {
        gap: 30px;
        justify-content: center;
        background-color: white;
        padding: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        position: sticky;
        top: 0;
        z-index: 99;
    }

    .stTabs [data-baseweb="tab"] {
        font-weight: 600;
        color: #8B4513;
    }
    
    /* Contenedores de Tours */
    .tour-card {
        background-color: #FDF5E6; /* Arena muy suave */
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #E6D5B8;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. BARRA DE CONTACTO SUPERIOR
st.markdown("""
    <div class="top-bar">
        <div>📞 +57 324 373 1661 | ✉️ veronicaarangopedrozo@gmail.com</div>
        <div>📍 Colombia / Caribe & Pacífico</div>
    </div>
    """, unsafe_allow_html=True)

# 4. LOGO Y ENCABEZADO
col_logo, col_espacio = st.columns([1, 4])
with col_logo:
    # URL de tu logo (IBB link ajustado a imagen directa)
    st.image("https://i.ibb.co/6R7m9g2C/ve.png", width=220)

# 5. MENÚ DE NAVEGACIÓN SUPERIOR
tab_inicio, tab_tours, tab_formularios, tab_blog = st.tabs([
    "NOSOTROS", "TOURS Y PLANES", "SERVICIOS", "BLOG & NOTICIAS"
])

# --- SECCIÓN: INICIO (CONÓCENOS) ---
with tab_inicio:
    st.markdown("""
        <div class="hero-section">
            <h1 style='font-size: 50px; color: white !important;'>¡Explora Colombia con Costa-Tour!</h1>
            <p style='font-size: 20px; font-family: "Lora", serif; font-style: italic;'>
                Experiencias inolvidables entre la selva y el mar.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("☀️ Conócenos")
        st.markdown("""
        <p style='text-align: justify;'>
        <b>Costa-Tour</b> es una agencia de viajes dedicada a mostrar la majestuosidad de Colombia 
        a extranjeros y nacionales. Nos especializamos en destinos donde la naturaleza y la cultura 
        se encuentran. <br><br>
        Desde las aguas cristalinas de <b>San Andrés</b> hasta la mística selva de <b>Bahía Solano</b>, 
        nuestro compromiso es ofrecerte un servicio de categoría mundial con el calor humano de nuestra tierra.
        </p>
        """, unsafe_allow_html=True)
    with c2:
        st.image("https://images.unsplash.com/photo-1590523277543-a94d2e4eb00b?w=800", caption="Costa-Tour: Tu aventura comienza aquí")

# --- SECCIÓN: TOURS ---
with tab_tours:
    st.title("🏝️ Nuestros Planes Turísticos")
    
    # Categoría Premium
    st.markdown("### ⭐ Categoría Premium")
    st.write("Planes con todo incluido, confort superior y experiencias exclusivas.")
    
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        with st.expander("✨ CARIBE MÁGICO / SOL CARIBE"):
            st.image("https://images.unsplash.com/photo-1548574505-5e239809ee19?w=600")
            st.write("**Destinos:** Cartagena, Santa Marta, San Andrés.")
            st.write("**Incluye:** Hoteles de lujo, tours privados y gastronomía de autor.")
            st.button("Consultar Caribe Premium", key="btn_p1")
    with col_p2:
        with st.expander("🐋 PACÍFICO VIVO / MÍSTICO"):
            st.image("https://images.unsplash.com/photo-1516815231560-8f41ec531527?w=600")
            st.write("**Destinos:** Nuquí, Bahía Solano.")
            st.write("**Incluye:** Avistamiento de ballenas, eco-lodges de lujo y guías expertos.")
            st.button("Consultar Pacífico Premium", key="btn_p2")

    st.divider()

    # Categoría Estándar
    st.markdown("### 🚢 Categoría Estándar")
    st.write("Aventura, cultura y paisajes increíbles al mejor precio.")
    
    col_e1, col_e2, col_e3, col_e4 = st.columns(4)
    estandar = [
        ("Nuestra Costa", "https://images.unsplash.com/photo-1580619305218-8423a7ef79b4?w=400"),
        ("Marea", "https://images.unsplash.com/photo-1590523741831-ab7e8b8f9c7f?w=400"),
        ("Ritmo Caribe", "https://images.unsplash.com/photo-1584132967334-10e028bd69f7?w=400"),
        ("Ruta Marina", "https://images.unsplash.com/photo-1590001158193-790179980bd3?w=400")
    ]
    
    cols = [col_e1, col_e2, col_e3, col_e4]
    for i, (nombre, img) in enumerate(estandar):
        with cols[i]:
            st.markdown(f"**{nombre}**")
            st.image(img)
            st.button("Ver más", key=f"est_{i}")

# --- SECCIÓN: FORMULARIOS ---
with tab_formularios:
    st.subheader("📋 Servicios al Cliente")
    st.write("En Costa-Tour nos importa tu opinión y seguridad.")
    
    st.markdown("""
    <div style='background-color: #f9f9f9; padding: 30px; border-radius: 20px; border: 1px solid #ddd;'>
        <h4>Formulario de Quejas, Sugerencias y Reclamos</h4>
        <p>Haz clic en el botón de abajo para ser redirigido a nuestra plataforma de atención oficial.</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Abrir Formulario de Quejas y Reclamos", "https://forms.office.com/pages/responsepage.aspx?id=IefhmYRxjkmK_7KtTlPBwmzEaoV6AVxMnWIMDnUV_6JUQjFRQVBCSEg5UldERzdTVkUxU1ZTRTFTMy4u&route=shorturl")

# --- SECCIÓN: BLOG ---
with tab_blog:
    st.subheader("📰 Noticias y Tips de Viaje")
    st.image("https://images.unsplash.com/photo-1516815231560-8f41ec531527?w=1000", caption="Aventuras en la Costa")
    st.markdown("""
    ### Tips de Viaje para la Costa Colombiana
    ¿Sabías que la mejor temporada para ver ballenas en el Pacífico es entre Julio y Octubre? 
    Encuentra estos y más consejos en nuestro blog especializado.
    """)
    st.link_button("Leer Blog Completo", "https://tipsdeviajeparalacostacolombiana.blogspot.com/p/tips-de-viaje-para-la-costa-caribe-y-la.html")

# 6. BOTÓN FLOTANTE DE WHATSAPP
st.markdown("""
    <a href="https://wa.me/573243731661?text=Hola%20Costa-Tour!%20Quiero%20información%20sobre%20sus%20planes." class="whatsapp-float" target="_blank">
        💬 Reserva aquí por WhatsApp
    </a>
    """, unsafe_allow_html=True)