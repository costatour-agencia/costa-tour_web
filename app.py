import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="Costa-Tour | Agencia de Viajes", 
    layout="wide", 
    page_icon="✈️"
)

# 2. ESTILOS CSS AVANZADOS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&family=Lora:ital,wght@0,400;1,400&display=swap');

    .stApp {
        background-color: #FFFFFF !important;
    }
    
    /* Limpieza total de botones */
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
        padding: 8px 20px !important;
        transition: 0.3s;
    }
    
    .stButton > button:hover {
        background-color: #A93226 !important;
        transform: translateY(-2px);
    }

    .stButton > button p {
        background-color: transparent !important;
        color: white !important;
        margin: 0 !important;
    }

    .hero-section {
        background-image: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), url('https://images.unsplash.com/photo-1616036740257-9449ea1f6605?q=80&w=1170&auto=format&fit=crop');
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
        margin-bottom: 40px;
    }

    .hero-title {
        background: transparent !important;
        color: white !important;
        font-family: 'Lora', serif;
        font-size: 60px;
        margin: 0;
    }

    .top-bar {
        background-color: #8B4513;
        color: white;
        padding: 10px 60px;
        display: flex;
        justify-content: space-between;
        font-size: 14px;
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 50px;
        justify-content: center;
    }

    .stTabs [data-baseweb="tab"] {
        font-weight: 600;
        color: #8B4513;
    }

    .package-description {
        font-family: 'Poppins', sans-serif;
        font-size: 13px;
        color: #444;
        text-align: left;
        padding: 15px;
        background: #f9f9f9;
        border-radius: 10px;
        margin-top: 10px;
        line-height: 1.5;
    }

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
    
    h3, h2 {
        font-family: 'Lora', serif;
        color: #8B4513;
    }

    .comp-table {
        width: 100%;
        border-collapse: collapse;
        margin: 25px 0;
        font-size: 15px;
        text-align: left;
    }
    .comp-table th {
        background-color: #8B4513;
        color: white;
        padding: 12px;
    }
    .comp-table td {
        padding: 12px;
        border-bottom: 1px solid #eee;
    }

    .testimonial-card {
        background: #fdf2e9;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #8B4513;
        margin-bottom: 20px;
    }

    /* Tarjetas de Contacto */
    .contact-card {
        background: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        text-align: center;
        border: 1px solid #eee;
        transition: 0.3s;
    }
    .contact-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(139, 69, 19, 0.1);
    }

    .footer {
        background-color: #2C3E50;
        color: #ECF0F1;
        padding: 40px 60px;
        margin-top: 50px;
        border-radius: 40px 40px 0 0;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. BARRA SUPERIOR
st.markdown("""
    <div class="top-bar">
        <div>📞 +57 324 373 1661 | ✉️ veronicaarangopedrozo@gmail.com</div>
        <div>📍 Medellín | Colombia</div>
    </div>
    """, unsafe_allow_html=True)

# 4. HEADER CON LOGO
col_logo, _ = st.columns([1, 3])
with col_logo:
    st.image("https://i.ibb.co/ds6F7b72/ve.png", width=250)

# 5. NAVEGACIÓN
tab_inicio, tab_tours, tab_faq, tab_formularios, tab_blog = st.tabs([
    "CONÓCENOS", "NUESTROS TOURS", "PREGUNTAS", "SERVICIOS", "BLOG"
])

# --- SECCIÓN: CONÓCENOS ---
with tab_inicio:
    st.markdown("""
        <div class="hero-section">
            <h1 class="hero-title">Costa-Tour</h1>
            <p style='font-size: 22px; font-style: italic; font-weight: 300; background: transparent;'>
                "El viaje es el servicio, y el destino es tu felicidad."
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("### ¿Quiénes somos?")
    st.write("""
    En Costa-Tour, redefinimos el concepto de viaje. Nacimos con la convicción de que el verdadero lujo no reside únicamente en un destino, sino en la calidad del servicio y la calidez humana que te acompaña en cada paso del camino.
    
    No somos solo una agencia de viajes; somos arquitectos de memorias. Nos especializamos en conectar el corazón indomable de Colombia con el mundo, ofreciendo experiencias que equilibran la riqueza natural de nuestras costas con un estándar de servicio impecable.
    """)
    
    # Galería de Destinos Actualizada con tus fotos
    st.markdown("### Destinos que te esperan")
    g1, g2, g3, g4 = st.columns(4)
    with g1:
        st.image("https://images.unsplash.com/photo-1610045058619-8c37e8913c55?q=80&w=735&auto=format&fit=crop", caption="Magia Natural")
    with g2:
        st.image("https://images.unsplash.com/photo-1561571994-3c61c554181a?q=80&w=686&auto=format&fit=crop", caption="Paraíso Escondido")
    with g3:
        st.image("https://images.unsplash.com/photo-1514890084135-f16d926f4d03?q=80&w=1170&auto=format&fit=crop", caption="Atardeceres Únicos")
    with g4:
        st.image("https://plus.unsplash.com/premium_photo-1664116928361-2972cf5d6848?q=80&w=687&auto=format&fit=crop", caption="Refugios de Lujo")

    col_fil, col_pq = st.columns(2)
    with col_fil:
        st.markdown("### Nuestra Filosofía")
        st.write("""
        Creemos que un viaje se vive tres veces: al soñarlo, al vivirlo y al recordarlo.
        - **Autenticidad:** Respetamos y celebramos la cultura local del Caribe y el Pacífico.
        - **Excelencia Adaptativa:** Atención personalizada y sin contratiempos en cualquier línea.
        - **Pasión por el Detalle:** Desde la elección de la almohada hasta el conocimiento del guía.
        """)
    with col_pq:
        st.markdown("### ¿Por qué elegirnos?")
        st.write("""
        - **Flexibilidad Única:** Tú eliges el horizonte, nosotros diseñamos el nivel de confort.
        - **Compromiso Local:** Turismo sostenible que beneficia directamente a nuestras tierras.
        - **Seguridad y Confianza:** Altos estándares en transporte y asistencia médica.
        """)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.info("Nuestra Visión: Ser el puente principal entre la biodiversidad colombiana y viajeros que buscan una transformación real.")

    # Testimonios
    st.markdown("### Lo que dicen nuestros viajeros")
    t1, t2 = st.columns(2)
    with t1:
        st.markdown("""<div class='testimonial-card'>"La mejor experiencia en el Pacífico. El servicio premium realmente vale la pena, no nos preocupamos por nada."<br><b>- Familia Restrepo</b></div>""", unsafe_allow_html=True)
    with t2:
        st.markdown("""<div class='testimonial-card'>"Costa-Tour hizo que mi luna de miel fuera mágica. Los guías bilingües fueron muy amables."<br><b>- Juan & Elena</b></div>""", unsafe_allow_html=True)

    # NUEVA SECCIÓN DE CONTACTO BONITA
    st.markdown("<br><h3 style='text-align: center;'>Conecta con Nosotros</h3>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""<div class='contact-card'><h4>📍 Ubicación</h4><p>Medellín, Colombia<br>Atención Presencial (Cita previa)</p></div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class='contact-card'><h4>📧 Email</h4><p>veronicaarangopedrozo<br>@gmail.com</p></div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""<div class='contact-card'><h4>📞 Teléfono</h4><p>+57 324 373 1661<br>Atención 24/7 Clientes</p></div>""", unsafe_allow_html=True)

# --- SECCIÓN: TOURS ---
with tab_tours:
    st.markdown("<h1 style='text-align: center;'>Portafolio de Experiencias</h1>", unsafe_allow_html=True)
    
    st.markdown("### Tabla Comparativa de Servicios")
    st.markdown("""
    <table class="comp-table">
        <tr><th>Beneficio</th><th>Línea Estándar</th><th>Línea Premium</th></tr>
        <tr><td>Transporte</td><td>Vans compartidas de turismo</td><td>Camionetas o lanchas privadas</td></tr>
        <tr><td>Alimentación</td><td>Solo desayunos / Menú fijo</td><td>Todo incluido / A la carta</td></tr>
        <tr><td>Guías</td><td>Guías locales grupales</td><td>Expertos privados y bilingües</td></tr>
        <tr><td>Flexibilidad</td><td>Horarios programados</td><td>Itinerario personalizado 100%</td></tr>
    </table>
    """, unsafe_allow_html=True)

    # LÍNEA PREMIUM
    st.markdown("## Línea Premium: 'Exclusividad Elevada'")
    st.write("El lujo no es solo un hotel, es que no tengas que preocuparte por absolutamente nada.")
    
    cp1, cp2, cp3, cp4 = st.columns(4)
    paquetes_premium = [
        ("Caribe Mágico", "https://media-cdn.tripadvisor.com/media/photo-s/2f/59/25/75/caption.jpg", "p1", "<b>Donde el tiempo se detiene.</b><br>Descanso absoluto en escenarios de película.<br><br><b>Alojamiento:</b> Suites con vista al mar y jacuzzi.<br><b>Servicio VIP:</b> Cena privada de 3 pasos en la playa.<br><b>Incluye:</b> Open bar premium y zonas privadas."),
        ("Pacífico Vivo", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRIeSN9RSQsxw_n-gbbbfOOsjBrcClZngt3DA&s", "p2", "<b>La majestad de la vida salvaje.</b><br>Aventura de alto nivel con total confort.<br><br><b>Alojamiento:</b> Glamping de lujo o Eco-Lodges boutique.<br><b>Servicio VIP:</b> Avistamiento privado en yate con catering.<br><b>Incluye:</b> Guía experto bilingüe."),
        ("Pacífico Místico", "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2c/b0/c2/4f/private-beach-hotels.jpg?w=1200&h=-1&s=1", "p3", "<b>Sanación para el alma.</b><br>Retiro de bienestar en lugares remotos y energéticos.<br><br><b>Alojamiento:</b> Villas privadas bioclimáticas.<br><b>Servicio VIP:</b> Spa termal y meditación privada.<br><b>Incluye:</b> Menú orgánico Farm to table."),
        ("Sol Caribe", "https://cdn2.paraty.es/landmar/images/865ffac6866fcba", "p4", "<b>El privilegio del sol eterno.</b><br>El estándar más alto del turismo internacional.<br><br><b>Alojamiento:</b> Resorts All-Inclusive Premium.<br><b>Servicio VIP:</b> Concierge personal y transporte blindado.<br><b>Incluye:</b> Fast Pass y amenidades de lujo.")
    ]

    for i, (nombre, img, key, desc) in enumerate(paquetes_premium):
        with [cp1, cp2, cp3, cp4][i]:
            st.image(img, use_container_width=True)
            st.markdown(f"<h4 style='text-align: center;'>{nombre}</h4>", unsafe_allow_html=True)
            if f"show_{key}" not in st.session_state: st.session_state[f"show_{key}"] = False
            if not st.session_state[f"show_{key}"]:
                if st.button("Detalles Premium", key=f"btn_{key}"): st.session_state[f"show_{key}"] = True; st.rerun()
            else:
                st.markdown(f"<div class='package-description'>{desc}</div>", unsafe_allow_html=True)
                if st.button("Cerrar", key=f"btn_{key}_less"): st.session_state[f"show_{key}"] = False; st.rerun()

    st.markdown("<br><hr>", unsafe_allow_html=True)

    # LÍNEA ESTÁNDAR
    st.markdown("## Línea Estándar: 'Conexión Auténtica'")
    st.write("Comodidad y seguridad para vivir el destino de forma real.")
    
    ce1, ce2, ce3, ce4 = st.columns(4)
    paquetes_estandar = [
        ("Nuestra Costa", "https://www.latamairlines.com/content/dam/latamxp/sites/vamos-latam/news-colombia/lista-latam/res_shutterstock_1312464929.jpg", "e1", "<b>Siéntete un local más.</b><br>Conoce el corazón de la cultura costera.<br><br><b>Alojamiento:</b> Posadas boutique con encanto.<br><b>Exp. destacada:</b> Clases de cocina tradicional.<br><b>Ideal para:</b> Parejas y viajeros."),
        ("Marea", "https://plus.unsplash.com/premium_photo-1669748157617-a3a83cc8ea23?fm=jpg&q=60&w=3000&auto=format&fit=crop", "e2", "<b>Siente la fuerza del océano.</b><br>Adrenalina y contacto directo con el agua.<br><br><b>Alojamiento:</b> Hoteles modernos con piscina.<br><b>Exp. destacada:</b> Surf o Paddle Board."),
        ("Ritmo Caribe", "https://condominiovistamar.com/wp-content/uploads/2025/07/playas-en-caovenas.webp", "e3", "<b>El alma de la fiesta.</b><br>Celebra la música, el baile y la vida nocturna.<br><br><b>Alojamiento:</b> Céntrico cerca de zonas de ocio.<br><b>Exp. destacada:</b> City Tour nocturno VIP."),
        ("Ruta Marina", "https://blog.gimlivingspaces.com/hubfs/Muelle%20r%C3%BAstico%20de%20madera%20con%20una%20palapa%20con%20vistas%20a%20las%20aguas%20turquesas%20cristalinas%20en%20Isla%20Mujeres%2C%20playa%20de%20M%C3%A9xico.webp", "e4", "<b>Naturaleza pura.</b><br>Viaje educativo enfocado en la protección ambiental.<br><br><b>Alojamiento:</b> Eco-hoteles sostenibles.<br><b>Exp. destacada:</b> Expedición a manglares.")
    ]

    for i, (nombre, img, key, desc) in enumerate(paquetes_estandar):
        with [ce1, ce2, ce3, ce4][i]:
            st.image(img, use_container_width=True)
            st.markdown(f"<h4 style='text-align: center;'>{nombre}</h4>", unsafe_allow_html=True)
            if f"show_{key}" not in st.session_state: st.session_state[f"show_{key}"] = False
            if not st.session_state[f"show_{key}"]:
                if st.button("Ver más", key=f"btn_{key}"): st.session_state[f"show_{key}"] = True; st.rerun()
            else:
                st.markdown(f"<div class='package-description'>{desc}</div>", unsafe_allow_html=True)
                if st.button("Cerrar", key=f"btn_{key}_less"): st.session_state[f"show_{key}"] = False; st.rerun()

# --- SECCIÓN: PREGUNTAS FRECUENTES ---
with tab_faq:
    st.markdown("### Preguntas Frecuentes")
    with st.expander("¿Qué métodos de pago aceptan?"):
        st.write("Aceptamos transferencias bancarias, tarjetas de crédito (Visa, Mastercard, Amex) y pagos a través de PSE.")
    with st.expander("¿Incluyen seguros de viaje?"):
        st.write("Sí, todos nuestros planes (Estándar y Premium) incluyen asistencia médica básica y seguro de viaje para tu tranquilidad.")
    with st.expander("¿Con cuánto tiempo debo reservar?"):
        st.write("Recomendamos reservar con al menos 15 días de antelación para la línea Estándar y 30 días para la línea Premium.")

# --- SECCIÓN: FORMULARIOS ---
with tab_formularios:
    st.markdown("### Atención al Cliente")
    st.write("Radica tus solicitudes, quejas o reclamos a través de nuestro canal oficial.")
    st.link_button("Portal de PQR", "https://forms.office.com/pages/responsepage.aspx?id=IefhmYRxjkmK_7KtTlPBwmzEaoV6AVxMnWIMDnUV_6JUQjFRQVBCSEg5UldERzdTVkUxU1ZTRTFTMy4u&route=shorturl")

# --- SECCIÓN: BLOG ---
with tab_blog:
    st.markdown("### Costa-Tour Blog")
    st.write("Encuentra tips de viaje, consejos de equipaje y las mejores fechas para visitar las costas colombianas en nuestro blog externo.")
    st.link_button("Ir al Blog Oficial", "https://tipsdeviajeparalacostacolombiana.blogspot.com/p/tips-de-viaje-para-la-costa-caribe-y-la.html")

# 6. FOOTER
st.markdown("""
    <div class="footer">
        <div style="display: flex; justify-content: space-between;">
            <div>
                <h4>Costa-Tour</h4>
                <p>Tu puente a las mejores experiencias en Colombia.</p>
            </div>
            <div>
                <h4>Contacto Directo</h4>
                <p>📲 +57 324 373 1661<br>📍 Medellín, Antioquia</p>
            </div>
            <div>
                <h4>Síguenos</h4>
                <p>Instagram | Facebook | TikTok</p>
            </div>
        </div>
        <hr style="border-color: #555;">
        <p style="text-align: center; font-size: 12px; color: #bdc3c7;">© 2024 Costa-Tour Agencia de Viajes. Todos los derechos reservados.</p>
    </div>
    """, unsafe_allow_html=True)

# 7. WHATSAPP FLOTANTE
st.markdown("""
    <a href="https://wa.me/573243731661?text=Hola%20Costa-Tour!%20Deseo%20información%20sobre%20un%20paquete." class="whatsapp-float" target="_blank">
        💬 ¡Reserva con un Asesor!
    </a>
    """, unsafe_allow_html=True)