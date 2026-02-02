import streamlit as st
import pandas as pd

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="Costa-Tour | Agencia de Viajes", 
    layout="wide", 
    page_icon="✈️"
)

# 2. ESTILOS CSS - REFINADOS PARA ELEGANCIA Y ORDEN
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&family=Lora:ital,wght@0,400;1,400&display=swap');

    /* Fondo general blanco */
    .stApp {
        background-color: #FFFFFF !important;
    }
    
    /* Botones Rojos Originales */
    .stButton > button {
        background-color: #C0392B !important;
        color: white !important;
        border: none !important;
        padding: 10px 20px !important;
        border-radius: 8px !important;
        transition: 0.3s;
        width: 100%;
        font-weight: 600;
    }
    
    .stButton > button:hover {
        background-color: #A93226 !important;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(192, 57, 43, 0.3);
    }

    /* Hero Section */
    .hero-section {
        background-image: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), url('https://images.unsplash.com/photo-1507525428034-b723cf961d3e?q=80&w=2073&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        height: 450px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        text-align: center;
        flex-direction: column;
        border-radius: 25px;
        margin-bottom: 40px;
    }

    .hero-title {
        color: white !important;
        font-family: 'Lora', serif;
        font-size: 72px;
        font-weight: bold;
        text-shadow: 2px 2px 15px rgba(0,0,0,0.6);
        margin-bottom: 10px;
    }

    /* Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 50px;
        justify-content: center;
        border-bottom: 2px solid #f0f0f0;
        margin-bottom: 30px;
    }

    .stTabs [data-baseweb="tab"] {
        font-weight: 600;
        color: #555;
        font-size: 18px;
    }

    .stTabs [aria-selected="true"] {
        color: #C0392B !important;
    }

    /* Card Styling for Packages */
    .package-card {
        background: white;
        padding: 0px;
        border-radius: 15px;
        transition: 0.3s;
        margin-bottom: 20px;
    }

    .package-description {
        font-family: 'Poppins', sans-serif;
        font-size: 14px;
        color: #444;
        padding: 20px;
        background: #F9F9F9;
        border-left: 4px solid #C0392B;
        border-radius: 0 12px 12px 0;
        margin-top: 10px;
        line-height: 1.6;
    }

    /* Testimonials */
    .testimonial-card {
        background: #FFF9F8;
        padding: 25px;
        border-radius: 20px;
        border: 1px solid #FFE4E1;
        text-align: center;
        height: 100%;
    }

    .testimonial-text {
        font-style: italic;
        color: #555;
        margin-bottom: 15px;
    }

    .testimonial-author {
        font-weight: bold;
        color: #C0392B;
    }

    /* FAQ Styling */
    .faq-container {
        background: #FFFFFF;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #EEE;
        margin-bottom: 10px;
    }

    /* WhatsApp Button */
    .whatsapp-float {
        position: fixed;
        bottom: 30px;
        right: 30px;
        background-color: #25d366;
        color: white !important;
        padding: 15px 30px;
        border-radius: 50px;
        text-decoration: none;
        z-index: 1000;
        font-weight: 600;
        box-shadow: 0 10px 30px rgba(37, 211, 102, 0.4);
        display: flex;
        align-items: center;
        gap: 10px;
    }

    h1, h2, h3, h4 {
        font-family: 'Lora', serif;
        color: #2C3E50;
    }

    .section-title {
        text-align: center;
        margin: 50px 0 30px 0;
        color: #8B4513;
        font-weight: bold;
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
tab_inicio, tab_tours, tab_atencion = st.tabs(["NUESTRA ESENCIA", "CATÁLOGO DE TOURS", "ATENCIÓN"])

# --- TAB INICIO ---
with tab_inicio:
    st.markdown("""
        <div class="hero-section">
            <h1 class="hero-title">Costa-Tour</h1>
            <p style='font-size: 26px; font-style: italic; font-weight: 300;'>
                "Nuestra prioridad no es el destino, es tu experiencia."
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<h2 class='section-title'>¿Quiénes somos?</h2>", unsafe_allow_html=True)
    st.write("""
    En Costa-Tour, redefinimos el concepto de viaje. Nacimos con la convicción de que el verdadero lujo no reside únicamente en un destino, sino en la calidad del servicio y la calidez humana que te acompaña en cada paso del camino.
    
    No somos solo una agencia de viajes; somos arquitectos de memorias. Nos especializamos en conectar el corazón indomable de Colombia con el mundo, ofreciendo experiencias que equilibran la riqueza natural de nuestras costas con un estándar de servicio impecable.
    """)

    st.markdown("<h2 class='section-title'>Destinos que te esperan</h2>", unsafe_allow_html=True)
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

    st.markdown("<br><br>", unsafe_allow_html=True)
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

    # SECCIÓN DE TESTIMONIOS
    st.markdown("<h2 class='section-title'>Lo que dicen nuestros viajeros</h2>", unsafe_allow_html=True)
    t_col1, t_col2, t_col3, t_col4 = st.columns(4)
    testimonials = [
        ("La atención al detalle fue impecable. Desde que aterrizamos hasta el regreso, nos sentimos como reyes. ¡Recomendado!", "Carlos Mendoza"),
        ("Costa-Tour hizo que nuestro viaje al Pacífico fuera mágico. Ver las ballenas con un guía privado fue otro nivel.", "Ana María Ruiz"),
        ("Buscábamos desconexión y recibimos paz absoluta. El hotel boutique superó mis expectativas de lujo y confort.", "Sebastián Gómez"),
        ("Excelente servicio al cliente. Hubo un pequeño cambio en mi vuelo y ellos lo resolvieron todo en minutos. ¡Geniales!", "Elena Torres")
    ]
    for i, (txt, author) in enumerate(testimonials):
        with [t_col1, t_col2, t_col3, t_col4][i]:
            st.markdown(f"""
                <div class="testimonial-card">
                    <p class="testimonial-text">"{txt}"</p>
                    <p class="testimonial-author">— {author}</p>
                </div>
            """, unsafe_allow_html=True)

# --- TAB TOURS ---
with tab_tours:
    # TABLA COMPARATIVA AL INICIO
    st.markdown("<h2 class='section-title'>Encuentra tu estilo de viaje</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Compara nuestras líneas de servicio para elegir la experiencia que mejor se adapte a ti.</p>", unsafe_allow_html=True)
    
    comparativa = {
        "Característica": ["Alojamiento", "Gastronomía", "Transporte", "Asistencia", "Exclusividad"],
        "Línea Estándar": ["Hoteles 3* / Posadas con encanto", "Desayuno buffet incluido", "Compartido en vans modernas", "Asistencia Virtual 24/7", "Grupos dinámicos y alegres"],
        "Línea Premium": ["Resorts 5* / Hoteles Boutique", "Plan Gastronómico Premium", "Privado en vehículos de lujo", "Asistencia Personalizada 24/7", "Experiencias privadas y exclusivas"]
    }
    df_comp = pd.DataFrame(comparativa)
    st.table(df_comp)

    st.markdown("<hr style='margin: 50px 0;'>", unsafe_allow_html=True)

    # PAQUETES PREMIUM
    st.markdown("<h2 style='text-align: center;'>Línea Premium: 'Exclusividad Elevada'</h2>", unsafe_allow_html=True)
    cp1, cp2, cp3, cp4 = st.columns(4)
    packs = [
        ("Caribe Mágico", "https://media-cdn.tripadvisor.com/media/photo-s/2f/59/25/75/caption.jpg", "p1", """
        **Experiencia de Lujo:**
        - **Alojamiento:** Suite de lujo frente al mar.
        - **Gastronomía:** Desayuno buffet y cena privada en la playa.
        - **Servicios:** Barra libre premium y acceso a zonas VIP.
        - **Extras:** Traslado privado aeropuerto-hotel.
        """),
        ("Pacífico Vivo", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRIeSN9RSQsxw_n-gbbbfOOsjBrcClZngt3DA&s", "p2", """
        **Aventura Exclusiva:**
        - **Alojamiento:** Eco-Lodge de alta gama con vista a la selva.
        - **Actividad:** Avistamiento de ballenas en bote privado.
        - **Gastronomía:** Menú de degustación ancestral.
        - **Servicios:** Guía bilingüe especializado 24/7.
        """),
        ("Pacífico Místico", "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2c/b0/c2/4f/private-beach-hotels.jpg?w=1200&h=-1&s=1", "p3", """
        **Retiro de Bienestar:**
        - **Alojamiento:** Hotel Boutique con spa privado.
        - **Actividad:** Ritual de sanación y meditación al amanecer.
        - **Gastronomía:** Plan de alimentación orgánico y personalizado.
        - **Servicios:** Masajes y terapias termales incluidos.
        """),
        ("Sol Caribe", "https://cdn2.paraty.es/landmar/images/865ffac6866fcba", "p4", """
        **Diversión Sin Límites:**
        - **Alojamiento:** Resort All-Inclusive categoría 5 estrellas.
        - **Actividad:** Tour privado en catamarán por las islas.
        - **Servicios:** Servicio de Concierge dedicado.
        - **Extras:** Kit de bienvenida premium.
        """)
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

    # PAQUETES ESTÁNDAR
    st.markdown("<hr style='margin: 40px 0;'>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Línea Estándar: 'Conexión Auténtica'</h2>", unsafe_allow_html=True)
    ce1, ce2, ce3, ce4 = st.columns(4)
    std_packs = [
        ("Nuestra Costa", "https://www.latamairlines.com/content/dam/latamxp/sites/vamos-latam/news-colombia/lista-latam/res_shutterstock_1312464929.jpg", "e1", """
        **Esencia Local:**
        - **Alojamiento:** Posadas nativas con encanto caribeño.
        - **Gastronomía:** Desayuno típico incluido.
        - **Actividad:** Tour caminando por el centro histórico.
        - **Servicios:** Seguro de viaje y asistencia básica.
        """),
        ("Marea", "https://plus.unsplash.com/premium_photo-1669748157617-a3a83cc8ea23?fm=jpg&q=60&w=3000&auto=format&fit=crop", "e2", """
        **Aventura Activa:**
        - **Alojamiento:** Hoteles modernos media gama.
        - **Actividad:** Clase grupal de surf o kayak.
        - **Servicios:** Traslados en lanchas compartidas.
        - **Extras:** Snack de hidratación incluido.
        """),
        ("Ritmo Caribe", "https://condominiovistamar.com/wp-content/uploads/2025/07/playas-en-caovenas.webp", "e3", """
        **Cultura y Sabor:**
        - **Alojamiento:** Hostales boutique con áreas sociales.
        - **Actividad:** Tour gastronómico por plazas locales.
        - **Gastronomía:** Almuerzo típico de playa.
        - **Servicios:** Guía local experto.
        """),
        ("Ruta Marina", "https://blog.gimlivingspaces.com/hubfs/Muelle%20r%C3%BAstico%20de%20madera%20con%20una%20palapa%20con%20vistas%20a%20las%20aguas%20turquesas%20cristalinas%20en%20Isla%20Mujeres%2C%20playa%20de%20M%C3%A9xico.webp", "e4", """
        **Ecoturismo:**
        - **Alojamiento:** Cabañas ecológicas sostenibles.
        - **Actividad:** Paseo en canoa por manglares.
        - **Servicios:** Educación ambiental durante el tour.
        - **Extras:** Entradas a parques nacionales.
        """)
    ]

    for i, (nombre, img, key, desc) in enumerate(std_packs):
        with [ce1, ce2, ce3, ce4][i]:
            st.image(img, use_container_width=True)
            st.markdown(f"<h5 style='text-align:center;'>{nombre}</h5>", unsafe_allow_html=True)
            if f"v_{key}" not in st.session_state: st.session_state[f"v_{key}"] = False
            if st.button("Ver Detalles", key=f"btn_{key}"): 
                st.session_state[f"v_{key}"] = not st.session_state[f"v_{key}"]
                st.rerun()
            if st.session_state[f"v_{key}"]:
                st.markdown(f"<div class='package-description'>{desc}</div>", unsafe_allow_html=True)

# --- TAB ATENCIÓN ---
with tab_atencion:
    st.markdown("<h2 class='section-title'>¿En qué podemos ayudarte?</h2>", unsafe_allow_html=True)
    
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        st.info("### 📝 Portal de PQR y Solicitudes\n\nRadique sus requerimientos, sugerencias o reclamos de manera formal.")
        st.link_button("Ir al Formulario", "https://forms.office.com/pages/responsepage.aspx?id=IefhmYRxjkmK_7KtTlPBwmzEaoV6AVxMnWIMDnUV_6JUQjFRQVBCSEg5UldERzdTVkUxU1ZTRTFTMy4u")
    
    with col_p2:
        st.success("### 📖 Blog del Viajero\n\nTips de viaje, guías de destinos y recomendaciones exclusivas.")
        st.link_button("Leer el Blog", "https://tipsdeviajeparalacostacolombiana.blogspot.com/")

    # SECCIÓN DE PREGUNTAS FRECUENTES (8)
    st.markdown("<br><hr>", unsafe_allow_html=True)
    st.markdown("<h2 class='section-title'>Preguntas Frecuentes</h2>", unsafe_allow_html=True)
    
    faqs = [
        ("¿Con cuánta anticipación debo reservar?", "Recomendamos reservar al menos con 30 días de antelación, especialmente para la Línea Premium."),
        ("¿Qué documentos necesito para viajar?", "Para destinos nacionales en Colombia, solo requieres tu documento de identidad original y vigente."),
        ("¿Los tours incluyen seguro médico?", "Sí, todos nuestros planes (Estándar y Premium) incluyen asistencia médica integral durante el viaje."),
        ("¿Puedo personalizar mi itinerario?", "¡Claro! Nuestra Línea Premium permite personalización total. Consulta con un asesor vía WhatsApp."),
        ("¿Qué métodos de pago aceptan?", "Aceptamos tarjetas de crédito, débito, transferencias bancarias y pagos a través de PSE."),
        ("¿Los vuelos están incluidos?", "Nuestros paquetes base se enfocan en la experiencia en destino. Los vuelos pueden añadirse como un extra a tu solicitud."),
        ("¿Tienen políticas de cancelación?", "Sí, contamos con políticas flexibles. Las cancelaciones con más de 15 días de antelación tienen reembolso parcial."),
        ("¿Tienen atención presencial?", "Atendemos en nuestra oficina en Medellín únicamente con cita previa gestionada por nuestros canales digitales.")
    ]

    for q, a in faqs:
        with st.expander(q):
            st.write(a)

# 5. FOOTER
st.markdown("""
    <div class="footer-white">
        <div style="display: flex; justify-content: space-between; flex-wrap: wrap; max-width: 1200px; margin: 0 auto;">
            <div style="flex: 1; min-width: 250px;">
                <h4 style="color:#C0392B">Costa-Tour</h4>
                <p>Tu puente a las mejores experiencias en Colombia. Redefiniendo el lujo y la autenticidad.</p>
            </div>
            <div style="flex: 1; min-width: 250px;">
                <h4 style="color:#C0392B">Contacto Directo</h4>
                <p>📲 +57 324 373 1661<br>📍 Medellín, Antioquia, Colombia</p>
            </div>
            <div style="flex: 1; min-width: 250px;">
                <h4 style="color:#C0392B">Redes Sociales</h4>
                <p>Instagram | Facebook | TikTok</p>
            </div>
        </div>
        <div style="text-align: center; margin-top: 30px; font-size: 13px; color: #aaa; border-top: 1px solid #eee; padding-top: 20px;">
            © 2024 Costa-Tour Agencia de Viajes. Todos los derechos reservados.
        </div>
    </div>
    """, unsafe_allow_html=True)

# 6. BOTÓN WHATSAPP
st.markdown("""
    <a href="https://wa.me/573243731661?text=Hola%20Costa-Tour!%20Deseo%20información%20sobre%20sus%20paquetes." class="whatsapp-float" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="25" height="25"> ¡Reserva con un Asesor!
    </a>
    """, unsafe_allow_html=True)