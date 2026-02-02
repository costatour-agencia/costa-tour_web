import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="Costa-Tour | Agencia de Viajes", 
    layout="wide", 
    page_icon="✈️"
)

# 2. ESTILOS CSS AVANZADOS (Eliminando recuadros y mejorando estética)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&family=Lora:ital,wght@0,400;1,400&display=swap');

    /* Fondo general limpio */
    .main {
        background-color: #FFFFFF;
    }
    
    html, body, [class*="st-emotion-cache"] {
        background-color: #FFFFFF;
        font-family: 'Poppins', sans-serif;
        color: #333333;
    }

    /* Barra superior de contacto */
    .top-bar {
        background-color: #8B4513;
        color: white;
        padding: 10px 60px;
        display: flex;
        justify-content: space-between;
        font-size: 14px;
        font-weight: 300;
    }

    /* Hero Section - Inspirado en Protours */
    .hero-section {
        background-image: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.3)), url('https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=1400');
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
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }

    /* Estilo de Tarjetas de Paquetes (Sin recuadros feos) */
    .package-card {
        background: white;
        padding: 0px;
        border-radius: 20px;
        transition: 0.3s;
        text-align: center;
    }
    
    .package-description {
        font-family: 'Poppins', sans-serif;
        font-size: 14px;
        color: #666;
        line-height: 1.6;
        padding: 10px;
        background: transparent !important;
    }

    /* Botones personalizados */
    .stButton>button {
        background-color: #C0392B !important;
        color: white !important;
        border-radius: 30px !important;
        border: none !important;
        padding: 8px 25px !important;
        font-size: 14px !important;
        font-weight: 500 !important;
        transition: 0.4s !important;
        box-shadow: 0 4px 15px rgba(192, 57, 43, 0.2) !important;
    }

    .stButton>button:hover {
        background-color: #8B4513 !important;
        transform: translateY(-3px) !important;
        box-shadow: 0 6px 20px rgba(0,0,0,0.15) !important;
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
        box-shadow: 0 8px 25px rgba(37, 211, 102, 0.4);
        transition: 0.3s;
    }
    
    .whatsapp-float:hover {
        transform: scale(1.05);
        color: white;
    }

    /* Tabs (Menú de navegación) */
    .stTabs [data-baseweb="tab-list"] {
        gap: 50px;
        justify-content: center;
        background-color: transparent;
    }

    .stTabs [data-baseweb="tab"] {
        height: 50px;
        font-weight: 600;
        font-size: 16px;
        color: #8B4513;
        border-bottom: 2px solid transparent;
    }

    .stTabs [data-baseweb="tab"]:hover {
        color: #C0392B;
    }

    /* Quitar bordes de imágenes */
    img {
        border-radius: 15px;
    }
    
    /* Eliminar el padding extra de las columnas de Streamlit */
    [data-testid="column"] {
        background-color: transparent !important;
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
    # Logo oficial de Costa-Tour (limpio y sin recuadros)
    st.image("https://i.ibb.co/ds6F7b72/ve.png", width=250)

# 5. NAVEGACIÓN
tab_inicio, tab_tours, tab_formularios, tab_blog = st.tabs([
    "CONÓCENOS", "NUESTROS TOURS", "SERVICIOS", "BLOG"
])

# --- SECCIÓN: CONÓCENOS ---
with tab_inicio:
    st.markdown("""
        <div class="hero-section">
            <h1 style='color: white !important; font-size: 65px; font-family: "Lora", serif; margin-bottom: 10px;'>Costa-Tour</h1>
            <p style='font-size: 24px; font-style: italic; font-weight: 300;'>Nuestra prioridad no es el destino, es tu experiencia.</p>
        </div>
        """, unsafe_allow_html=True)
    
    c1, c2 = st.columns([1, 1])
    with c1:
        st.markdown("<h2 style='color: #8B4513; font-family: \"Lora\", serif;'>Conócenos</h2>", unsafe_allow_html=True)
        st.markdown("""
        <p style='text-align: justify; font-size: 16px; line-height: 1.8;'>
        En <b>Costa-Tour</b>, redefinimos el concepto de viaje. Creemos firmemente que el lujo no es un lugar, 
        es la calidad del servicio que te acompaña en el camino. Nos especializamos en conectar el corazón de 
        Colombia con el mundo, ofreciendo experiencias exclusivas tanto en la Costa Caribe como en el Pacífico Colombiano.
        <br><br>
        Nuestro enfoque se centra en la personalización. No importa si eliges la selva profunda de Bahía Solano o el 
        brillo de Cartagena; lo que garantiza tu satisfacción es el nivel de paquete que selecciones, diseñado 
        cuidadosamente para superar cualquier expectativa.
        </p>
        """, unsafe_allow_html=True)
    with c2:
        st.image("https://images.unsplash.com/photo-1590523277543-a94d2e4eb00b?w=800")

# --- SECCIÓN: TOURS ---
with tab_tours:
    st.markdown("<h1 style='text-align: center; font-family: \"Lora\", serif; color: #8B4513;'>Portafolio de Experiencias</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666;'>La excelencia de tu viaje depende del servicio contratado, disponible en todos nuestros destinos.</p>", unsafe_allow_html=True)
    
    # --- PREMIUM ---
    st.markdown("<h2 style='border-left: 5px solid #C0392B; padding-left: 15px;'>⭐ Categoría Premium</h2>", unsafe_allow_html=True)
    st.write("Servicios VIP: Vuelos privados, suites de lujo, atención bilingüe y gastronomía gourmet.")
    
    cp1, cp2, cp3, cp4 = st.columns(4)
    
    paquetes_premium = [
        ("Caribe Mágico", "https://images.unsplash.com/photo-1548574505-5e239809ee19?w=400", "p1", 
         "Suite presidencial, traslados en yate privado, chef exclusivo y playas privadas."),
        ("Pacífico Vivo", "https://images.unsplash.com/photo-1516815231560-8f41ec531527?w=400", "p2", 
         "Eco-lodges boutique, avistamiento privado de ballenas y spa ancestral incluido."),
        ("Pacífico Místico", "https://images.unsplash.com/photo-1554357475-acce8d059b4b?w=400", "p3", 
         "Retiros de bienestar, tours nocturnos VIP y fotografía profesional incluida."),
        ("Sol Caribe", "https://images.unsplash.com/photo-1506929197327-fb877276303b?w=400", "p4", 
         "Vuelos charter entre islas, club de playa privado y bar de bebidas premium.")
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

    st.markdown("<br><hr><br>", unsafe_allow_html=True)

    # --- ESTÁNDAR ---
    st.markdown("<h2 style='border-left: 5px solid #8B4513; padding-left: 15px;'>🚢 Categoría Estándar</h2>", unsafe_allow_html=True)
    st.write("Calidad y aventura garantizada al mejor precio del mercado.")
    
    ce1, ce2, ce3, ce4 = st.columns(4)
    paquetes_estandar = [
        ("Nuestra Costa", "https://images.unsplash.com/photo-1590523277543-a94d2e4eb00b?w=400", "e1", 
         "Hoteles 3-4 estrellas seleccionados, transporte puntual y tours grupales."),
        ("Marea", "https://images.unsplash.com/photo-1580619305218-8423a7ef79b4?w=400", "e2", 
         "Experiencias culturales, hidratación constante y guías locales expertos."),
        ("Ritmo Caribe", "https://images.unsplash.com/photo-1584132967334-10e028bd69f7?w=400", "e3", 
         "Plan familiar con cenas temáticas y actividades recreativas incluidas."),
        ("Ruta Marina", "https://images.unsplash.com/photo-1590001158193-790179980bd3?w=400", "e4", 
         "Exploración de arrecifes, lanchas seguras y equipo de snorkel completo.")
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
    st.write("Para Costa-Tour, tu seguridad y satisfacción son la base de nuestro negocio.")
    st.link_button("Radicar Queja o Reclamo (PQR)", "https://forms.office.com/pages/responsepage.aspx?id=IefhmYRxjkmK_7KtTlPBwmzEaoV6AVxMnWIMDnUV_6JUQjFRQVBCSEg5UldERzdTVkUxU1ZTRTFTMy4u&route=shorturl")

# --- SECCIÓN: BLOG ---
with tab_blog:
    st.markdown("<h2 style='color: #8B4513; font-family: \"Lora\", serif;'>Costa-Tour Blog</h2>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1516815231560-8f41ec531527?w=1200", caption="Descubre los secretos de Colombia")
    st.write("Aprende sobre climas, qué empacar y las mejores fechas para viajar en nuestro blog oficial.")
    st.link_button("Explorar Blog", "https://tipsdeviajeparalacostacolombiana.blogspot.com/p/tips-de-viaje-para-la-costa-caribe-y-la.html")

# 6. WHATSAPP FLOTANTE
st.markdown("""
    <a href="https://wa.me/573243731661?text=Hola%20Costa-Tour!%20Deseo%20información%20sobre%20un%20paquete%20Premium." class="whatsapp-float" target="_blank">
        💬 ¡Reserva con un Asesor!
    </a>
    """, unsafe_allow_html=True)