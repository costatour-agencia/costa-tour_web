import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="Costa-Tour | Agencia de Viajes", 
    layout="wide", 
    page_icon="✈️"
)

# 2. ESTILOS CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&family=Lora:ital,wght@0,400;1,400&display=swap');

    html, body, [class*="st-emotion-cache"] {
        background-color: #FFFFFF;
        font-family: 'Poppins', sans-serif;
        color: #333333;
    }

    .top-bar {
        background-color: #8B4513;
        color: white;
        padding: 8px 50px;
        display: flex;
        justify-content: space-between;
        font-size: 13px;
    }

    .hero-section {
        background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=1200');
        background-size: cover;
        background-position: center;
        height: 450px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        text-align: center;
        flex-direction: column;
        border-radius: 0 0 40px 40px;
        margin-bottom: 30px;
    }

    .stButton>button {
        background-color: #C0392B !important;
        color: white !important;
        border-radius: 20px !important;
        border: none !important;
        transition: 0.3s !important;
    }

    .stButton>button:hover {
        background-color: #D35400 !important;
        transform: translateY(-2px);
    }

    .whatsapp-float {
        position: fixed;
        bottom: 25px;
        right: 25px;
        background-color: #25d366;
        color: white;
        padding: 15px 25px;
        border-radius: 50px;
        text-decoration: none;
        z-index: 100;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }

    .package-card {
        background-color: #FDFCF0;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #E6D5B8;
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. BARRA SUPERIOR
st.markdown("""
    <div class="top-bar">
        <div>📞 +57 324 373 1661 | ✉️ veronicaarangopedrozo@gmail.com</div>
        <div>📍 Medellín| Colombia </div>
    </div>
    """, unsafe_allow_html=True)

# 4. LOGO
col_logo, _ = st.columns([1, 4])
with col_logo:
    # Nuevo link del logo corregido
    st.image("https://i.ibb.co/ds6F7b72/ve.png", width=220)

# 5. MENÚ DE NAVEGACIÓN
tab_inicio, tab_tours, tab_formularios, tab_blog = st.tabs([
    "CONÓCENOS", "NUESTROS TOURS", "FORMULARIOS", "BLOG & NOTICIAS"
])

# --- SECCIÓN: CONÓCENOS ---
with tab_inicio:
    st.markdown("""
        <div class="hero-section">
            <h1 style='color: white !important; font-size: 55px;'>Costa-Tour</h1>
            <p style='font-size: 22px; font-family: "Lora", serif;'>Nuestra prioridad no es el destino, es tu experiencia.</p>
        </div>
        """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Conócenos")
        st.write("""
        En **Costa-Tour**, entendemos que el lujo y la comodidad no dependen del lugar donde te encuentres, 
        sino del servicio que recibes. Nos dedicamos a conectar a viajeros nacionales y extranjeros con 
        los rincones más hermosos de Colombia, garantizando estándares de calidad excepcionales.
        
        Nuestros destinos incluyen la magia del Caribe y la mística del Pacífico, pero lo que realmente 
        nos diferencia es el cuidado en cada detalle de nuestros paquetes Premium y Estándar.
        """)
    with col2:
        st.image("https://images.unsplash.com/photo-1589519160732-57fc498494f8?w=800", caption="Experiencias Costa-Tour")

# --- SECCIÓN: TOURS ---
with tab_tours:
    st.title("Portafolio de Paquetes Turísticos")
    st.info("💡 Nota: En Costa-Tour, el paquete define el nivel de servicio y exclusividad, independientemente del destino elegido.")
    
    # --- CATEGORÍA PREMIUM ---
    st.markdown("## Categoría Premium")
    st.write("Experiencias de élite con vuelos privados, hoteles de autor y atención bilingüe 24/7.")
    
    cp1, cp2, cp3, cp4 = st.columns(4)
    
    # Paquete 1: Caribe Mágico
    with cp1:
        st.image("https://images.unsplash.com/photo-1548574505-5e239809ee19?w=400")
        st.subheader("Caribe Mágico")
        if f"show_p1" not in st.session_state: st.session_state.show_p1 = False
        
        if not st.session_state.show_p1:
            if st.button("Ver más", key="btn_p1"):
                st.session_state.show_p1 = True
                st.rerun()
        else:
            st.write("""
            **Servicios VIP:**
            - Alojamiento en Suites presidenciales.
            - Traslados en yate privado.
            - Menú de degustación con chef privado.
            - Acceso exclusivo a playas vírgenes.
            """)
            if st.button("Ver menos", key="btn_p1_less"):
                st.session_state.show_p1 = False
                st.rerun()

    # Paquete 2: Pacífico Vivo
    with cp2:
        st.image("https://images.unsplash.com/photo-1516815231560-8f41ec531527?w=400")
        st.subheader("Pacífico Vivo")
        if f"show_p2" not in st.session_state: st.session_state.show_p2 = False
        
        if not st.session_state.show_p2:
            if st.button("Ver más", key="btn_p2"):
                st.session_state.show_p2 = True
                st.rerun()
        else:
            st.write("""
            **Inmersión Total:**
            - Eco-lodges boutique sostenibles.
            - Avistamiento de ballenas privado.
            - Expediciones con biólogos expertos.
            - Spa ancestral incluido.
            """)
            if st.button("Ver menos", key="btn_p2_less"):
                st.session_state.show_p2 = False
                st.rerun()

    # Paquete 3: Pacífico Místico
    with cp3:
        st.image("https://images.unsplash.com/photo-1554357475-acce8d059b4b?w=400")
        st.subheader("Pacífico Místico")
        if f"show_p3" not in st.session_state: st.session_state.show_p3 = False
        
        if not st.session_state.show_p3:
            if st.button("Ver más", key="btn_p3"):
                st.session_state.show_p3 = True
                st.rerun()
        else:
            st.write("""
            **Experiencia Espiritual:**
            - Retiros de bienestar en la selva.
            - Tours nocturnos de bioluminiscencia.
            - Fotografía profesional incluida.
            - Servicio de concierge bilingüe.
            """)
            if st.button("Ver menos", key="btn_p3_less"):
                st.session_state.show_p3 = False
                st.rerun()

    # Paquete 4: Sol Caribe
    with cp4:
        st.image("https://images.unsplash.com/photo-1506929197327-fb877276303b?w=400")
        st.subheader("Sol Caribe")
        if f"show_p4" not in st.session_state: st.session_state.show_p4 = False
        
        if not st.session_state.show_p4:
            if st.button("Ver más", key="btn_p4"):
                st.session_state.show_p4 = True
                st.rerun()
        else:
            st.write("""
            **Lujo Tropical:**
            - Club de playa privado.
            - Vuelos charter entre islas.
            - Equipamiento de deportes náuticos.
            - Open bar de bebidas Premium.
            """)
            if st.button("Ver menos", key="btn_p4_less"):
                st.session_state.show_p4 = False
                st.rerun()

    st.divider()

    # --- CATEGORÍA ESTÁNDAR ---
    st.markdown("## Categoría Estándar")
    st.write("La mejor relación calidad-precio para aventureros que aman la autenticidad.")
    
    ce1, ce2, ce3, ce4 = st.columns(4)
    
    # Estándar 1
    with ce1:
        st.image("https://images.unsplash.com/photo-1590523277543-a94d2e4eb00b?w=400")
        st.subheader("Nuestra Costa")
        if "show_e1" not in st.session_state: st.session_state.show_e1 = False
        if not st.session_state.show_e1:
            if st.button("Ver más", key="btn_e1"): st.session_state.show_e1 = True; st.rerun()
        else:
            st.write("Hoteles 3-4 estrellas, transporte cómodo y desayunos incluidos.")
            if st.button("Ver menos", key="btn_e1_less"): st.session_state.show_e1 = False; st.rerun()

    # Estándar 2
    with ce2:
        st.image("https://images.unsplash.com/photo-1580619305218-8423a7ef79b4?w=400")
        st.subheader("Marea")
        if "show_e2" not in st.session_state: st.session_state.show_e2 = False
        if not st.session_state.show_e2:
            if st.button("Ver más", key="btn_e2"): st.session_state.show_e2 = True; st.rerun()
        else:
            st.write("Tours grupales guiados, hidratación y actividades culturales.")
            if st.button("Ver menos", key="btn_e2_less"): st.session_state.show_e2 = False; st.rerun()

    # Estándar 3
    with ce3:
        st.image("https://images.unsplash.com/photo-1584132967334-10e028bd69f7?w=400")
        st.subheader("Ritmo Caribe")
        if "show_e3" not in st.session_state: st.session_state.show_e3 = False
        if not st.session_state.show_e3:
            if st.button("Ver más", key="btn_e3"): st.session_state.show_e3 = True; st.rerun()
        else:
            st.write("Ideal para familias. Incluye cenas temáticas y guías locales.")
            if st.button("Ver menos", key="btn_e3_less"): st.session_state.show_e3 = False; st.rerun()

    # Estándar 4 - RUTA MARINA
    with ce4:
        st.image("https://images.unsplash.com/photo-1590001158193-790179980bd3?w=400")
        st.subheader("Ruta Marina")
        if "show_e4" not in st.session_state: st.session_state.show_e4 = False
        if not st.session_state.show_e4:
            if st.button("Ver más", key="btn_e4"): st.session_state.show_e4 = True; st.rerun()
        else:
            st.write("Exploración costera, traslados en lanchas seguras y equipo de snorkel.")
            if st.button("Ver menos", key="btn_e4_less"): st.session_state.show_e4 = False; st.rerun()

# --- SECCIÓN: FORMULARIOS ---
with tab_formularios:
    st.subheader("Servicios y Atención")
    st.link_button("Abrir Formulario de Quejas y Reclamos", "https://forms.office.com/pages/responsepage.aspx?id=IefhmYRxjkmK_7KtTlPBwmzEaoV6AVxMnWIMDnUV_6JUQjFRQVBCSEg5UldERzdTVkUxU1ZTRTFTMy4u&route=shorturl")

# --- SECCIÓN: BLOG ---
with tab_blog:
    st.subheader("Noticias y Recomendaciones")
    st.markdown("### ¿Planeando tu próximo viaje?")
    st.write("Visita nuestro blog externo para encontrar tips exclusivos sobre equipaje, clima y cultura.")
    st.link_button("Ir al Blog Oficial", "https://tipsdeviajeparalacostacolombiana.blogspot.com/p/tips-de-viaje-para-la-costa-caribe-y-la.html")

# 6. WHATSAPP FLOTANTE
st.markdown("""
    <a href="https://wa.me/573243731661?text=Hola%20Costa-Tour!%20Quiero%20información%20sobre%20sus%20planes." class="whatsapp-float" target="_blank">
        💬 ¡Chatea con nosotros!
    </a>
    """, unsafe_allow_html=True)

