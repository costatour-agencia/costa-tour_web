import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="Costa-Tour | Agencia de Viajes", 
    layout="wide", 
    page_icon="✈️"
)

# 2. ESTILOS CSS - ENFOCADO EN BLANCO Y ELEGANCIA
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&family=Lora:ital,wght@0,400;1,400&display=swap');

    /* Fondo general blanco */
    .stApp {
        background-color: #FFFFFF !important;
    }
    
    /* Botones limpios */
    .stButton > button {
        background-color: #C0392B !important;
        color: white !important;
        border: none !important;
        padding: 8px 25px !important;
        border-radius: 8px !important;
        transition: 0.3s;
    }
    
    .stButton > button:hover {
        background-color: #A93226 !important;
        transform: translateY(-2px);
    }

    /* Hero Section con mejor contraste */
    .hero-section {
        background-image: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.3)), url('https://images.unsplash.com/photo-1507525428034-b723cf961d3e?q=80&w=2073&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        height: 400px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        text-align: center;
        flex-direction: column;
        border-radius: 20px;
        margin: 20px;
    }

    .hero-title {
        color: white !important;
        font-family: 'Lora', serif;
        font-size: 65px;
        font-weight: bold;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.5);
    }

    /* Barra de navegación de pestañas */
    .stTabs [data-baseweb="tab-list"] {
        gap: 40px;
        justify-content: center;
        border-bottom: 1px solid #eee;
    }

    .stTabs [data-baseweb="tab"] {
        font-weight: 600;
        color: #5D4037;
    }

    /* Tarjetas de contacto Blancas (Premium) */
    .contact-card {
        background: white;
        padding: 35px 20px;
        border-radius: 20px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.06);
        text-align: center;
        border: 1px solid #f0f0f0;
        margin-bottom: 20px;
    }
    
    .contact-icon {
        font-size: 24px;
        margin-bottom: 15px;
    }

    /* Footer Blanco Elegante */
    .footer-white {
        background-color: #fcfcfc;
        border-top: 1px solid #eee;
        padding: 60px 40px 30px 40px;
        margin-top: 80px;
        color: #555;
    }

    .package-description {
        font-family: 'Poppins', sans-serif;
        font-size: 13.5px;
        color: #444;
        padding: 20px;
        background: #fdfdfd;
        border: 1px solid #eee;
        border-radius: 12px;
        margin-top: 15px;
    }

    .whatsapp-float {
        position: fixed;
        bottom: 30px;
        right: 30px;
        background-color: #25d366;
        color: white !important;
        padding: 15px 25px;
        border-radius: 50px;
        text-decoration: none;
        z-index: 1000;
        font-weight: 600;
        box-shadow: 0 10px 30px rgba(37, 211, 102, 0.4);
    }
    
    h1, h2, h3 {
        font-family: 'Lora', serif;
        color: #5D4037;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. CABECERA
t_col1, t_col2 = st.columns([2, 1])
with t_col1:
    st.image("https://i.ibb.co/ds6F7b72/ve.png", width=220)
with t_col2:
    st.markdown("<p style='text-align:right; color:#888; font-size:14px; margin-top:20px;'>📞 +57 324 373 1661<br>✉️ veronicaarangopedrozo@gmail.com</p>", unsafe_allow_html=True)

# 4. TABS
tab_inicio, tab_tours, tab_servicios = st.tabs(["NUESTRA ESENCIA", "CATÁLOGO DE TOURS", "ATENCIÓN"])

# --- TAB INICIO ---
with tab_inicio:
    st.markdown("""
        <div class="hero-section">
            <h1 class="hero-title">Costa-Tour</h1>
            <p style='font-size: 24px; font-style: italic; font-weight: 300;'>
                "Nuestra prioridad no es el destino, es tu experiencia."
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Texto de Introducción
    st.markdown("### ¿Quiénes somos?")
    st.write("""
    En Costa-Tour, redefinimos el concepto de viaje. Nacimos con la convicción de que el verdadero lujo no reside únicamente en un destino, sino en la calidad del servicio y la calidez humana que te acompaña en cada paso del camino.
    
    No somos solo una agencia de viajes; somos arquitectos de memorias. Nos especializamos en conectar el corazón indomable de Colombia con el mundo, ofreciendo experiencias que equilibran la riqueza natural de nuestras costas con un estándar de servicio impecable.
    """)

    # Galería de Destinos (Tus imágenes de Unsplash)
    st.markdown("### Destinos que te esperan")
    img_cols = st.columns(4)
    urls = [
        "https://images.unsplash.com/photo-1610045058619-8c37e8913c55?q=80&w=735&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1561571994-3c61c554181a?q=80&w=686&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1514890084135-f16d926f4d03?q=80&w=1170&auto=format&fit=crop",
        "https://plus.unsplash.com/premium_photo-1664116928361-2972cf5d6848?q=80&w=687&auto=format&fit=crop"
    ]
    captions = ["Magia Natural", "Paraíso Turquesa", "Horizonte Infinito", "Refugio Exclusivo"]
    for i, col in enumerate(img_cols):
        with col:
            st.image(urls[i], caption=captions[i], use_container_width=True)

    # Filosofía
    st.markdown("<br>", unsafe_allow_html=True)
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("#### Nuestra Filosofía")
        st.write("""
        - **Autenticidad:** Respetamos y celebramos la cultura local del Caribe y el Pacífico.
        - **Excelencia:** Atención personalizada en cada detalle del trayecto.
        - **Sostenibilidad:** Viajes conscientes que protegen nuestro entorno.
        """)
    with col_b:
        st.markdown("#### ¿Por qué Costa-Tour?")
        st.write("""
        - **Flexibilidad:** Itinerarios que se adaptan a tu ritmo de vida.
        - **Seguridad:** Acompañamiento 24/7 y asistencia médica integral.
        - **Conexión Real:** Guías que aman su tierra y te la muestran de verdad.
        """)

    # CONTACTO (La parte más bonita)
    st.markdown("<br><h3 style='text-align: center;'>Canales de Atención</h3>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""<div class='contact-card'><div class='contact-icon'>📍</div><h4>Ubicación</h4><p>Medellín, Colombia<br>Atención Presencial (Cita previa)</p></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class='contact-card'><div class='contact-icon'>✉️</div><h4>Email</h4><p>veronicaarangopedrozo<br>@gmail.com</p></div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""<div class='contact-card'><div class='contact-icon'>📞</div><h4>Teléfono</h4><p>+57 324 373 1661<br>Atención 24/7 Clientes</p></div>""", unsafe_allow_html=True)

# --- TAB TOURS ---
with tab_tours:
    st.markdown("<h2 style='text-align: center;'>Línea Premium: 'Exclusividad Elevada'</h2>", unsafe_allow_html=True)
    
    cp1, cp2, cp3, cp4 = st.columns(4)
    # Paquetes Premium
    packs = [
        ("Caribe Mágico", "https://images.unsplash.com/photo-1548574505-5e239809ee19?q=80&w=600", "p1", "<b>Suite frente al mar.</b> Cena privada en la playa y barra libre premium."),
        ("Pacífico Vivo", "https://images.unsplash.com/photo-1544551763-47a0159f963f?q=80&w=600", "p2", "<b>Avistamiento privado.</b> Yate exclusivo y Eco-Lodge de alta gama."),
        ("Pacífico Místico", "https://images.unsplash.com/photo-1506929199039-b05275fa5352?q=80&w=600", "p3", "<b>Sanación y Spa.</b> Retiro boutique con menú orgánico personalizado."),
        ("Sol Caribe", "https://images.unsplash.com/photo-1520483601560-389dff54adcd?q=80&w=600", "p4", "<b>Resort All-Inclusive.</b> Servicio de Concierge y traslados VIP.")
    ]

    for i, (nombre, img, key, desc) in enumerate(packs):
        with [cp1, cp2, cp3, cp4][i]:
            st.image(img, use_container_width=True)
            st.markdown(f"<h5 style='text-align:center;'>{nombre}</h5>", unsafe_allow_html=True)
            if f"v_{key}" not in st.session_state: st.session_state[f"v_{key}"] = False
            if st.button("Detalles Premium", key=f"btn_{key}"): 
                st.session_state[f"v_{key}"] = not st.session_state[f"v_{key}"]
                st.rerun()
            if st.session_state[f"v_{key}"]:
                st.markdown(f"<div class='package-description'>{desc}</div>", unsafe_allow_html=True)

    st.markdown("<hr style='margin: 40px 0;'>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Línea Estándar: 'Conexión Auténtica'</h2>", unsafe_allow_html=True)
    
    ce1, ce2, ce3, ce4 = st.columns(4)
    std_packs = [
        ("Nuestra Costa", "https://images.unsplash.com/photo-1590523277543-a94d2e4eb00b?q=80&w=600", "e1", "<b>Posadas con encanto.</b> Vive la cultura como un local."),
        ("Marea", "https://images.unsplash.com/photo-1519046904884-53103b34b206?q=80&w=600", "e2", "<b>Aventura marina.</b> Hoteles modernos y clases de surf."),
        ("Ritmo Caribe", "https://images.unsplash.com/photo-1533174072545-7a4b6ad7a6c3?q=80&w=600", "e3", "<b>Noche y sabor.</b> Tour de bares y música en vivo."),
        ("Ruta Marina", "https://images.unsplash.com/photo-1500614922032-b6dd337b1313?q=80&w=600", "e4", "<b>Ecoturismo.</b> Avistamiento en manglares y hoteles sostenibles.")
    ]

    for i, (nombre, img, key, desc) in enumerate(std_packs):
        with [ce1, ce2, ce3, ce4][i]:
            st.image(img, use_container_width=True)
            st.markdown(f"<h5 style='text-align:center;'>{nombre}</h5>", unsafe_allow_html=True)
            if f"v_{key}" not in st.session_state: st.session_state[f"v_{key}"] = False
            if st.button("Ver más", key=f"btn_{key}"): 
                st.session_state[f"v_{key}"] = not st.session_state[f"v_{key}"]
                st.rerun()
            if st.session_state[f"v_{key}"]:
                st.markdown(f"<div class='package-description'>{desc}</div>", unsafe_allow_html=True)

# --- TAB ATENCIÓN ---
with tab_servicios:
    st.markdown("### ¿En qué podemos ayudarte?")
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        st.info("**PQR y Solicitudes**\n\nSi necesitas radicar un requerimiento formal, usa nuestro enlace seguro.")
        st.link_button("Portal de Servicio", "https://forms.office.com/pages/responsepage.aspx?id=IefhmYRxjkmK_7KtTlPBwmzEaoV6AVxMnWIMDnUV_6JUQjFRQVBCSEg5UldERzdTVkUxU1ZTRTFTMy4u")
    with col_p2:
        st.success("**Blog de Viajero**\n\nConsejos de equipaje, mejores temporadas y guías de viaje.")
        st.link_button("Visitar el Blog", "https://tipsdeviajeparalacostacolombiana.blogspot.com/")

# 5. FOOTER BLANCO
st.markdown("""
    <div class="footer-white">
        <div style="display: flex; justify-content: space-between; flex-wrap: wrap;">
            <div style="flex: 1; min-width: 250px;">
                <h4 style="color:#8B4513">Costa-Tour</h4>
                <p>Tu aliado en experiencias inolvidables por las costas de Colombia.</p>
            </div>
            <div style="flex: 1; min-width: 250px;">
                <h4 style="color:#8B4513">Contacto Directo</h4>
                <p>📲 +57 324 373 1661<br>📍 Medellín, Antioquia</p>
            </div>
            <div style="flex: 1; min-width: 250px;">
                <h4 style="color:#8B4513">Redes Sociales</h4>
                <p>Instagram | Facebook | TikTok</p>
            </div>
        </div>
        <div style="text-align: center; margin-top: 40px; font-size: 13px; color: #aaa;">
            © 2024 Costa-Tour Agencia de Viajes. Todos los derechos reservados.
        </div>
    </div>
    """, unsafe_allow_html=True)

# 6. BOTÓN WHATSAPP
st.markdown("""
    <a href="https://wa.me/573243731661?text=Hola%20Costa-Tour!" class="whatsapp-float" target="_blank">
        💬 Reserva con un Asesor
    </a>
    """, unsafe_allow_html=True)