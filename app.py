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

    /* Color de fondo global */
    .stApp {
        background-color: #FFFFFF !important;
    }
    
    /* Personalización de botones */
    div.stButton > button {
        background-color: #C0392B !important;
        color: white !important;
        border: none !important;
        border-radius: 8px;
        padding: 10px 25px !important;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    div.stButton > button:hover {
        background-color: #A93226 !important;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(192, 57, 43, 0.3);
    }

    /* Sección Hero Principal */
    .hero-section {
        background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('https://images.unsplash.com/photo-1616036740257-9449ea1f6605?q=80&w=1170&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        height: 480px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        text-align: center;
        flex-direction: column;
        border-radius: 0 0 50px 50px;
        margin-bottom: 50px;
        padding: 20px;
    }

    .hero-title {
        color: white !important;
        font-family: 'Lora', serif;
        font-size: 65px;
        font-weight: 700;
        margin-bottom: 10px;
    }

    /* Barra de contacto superior */
    .top-bar {
        background-color: #8B4513;
        color: white;
        padding: 12px 60px;
        display: flex;
        justify-content: space-between;
        font-size: 14px;
        font-family: 'Poppins', sans-serif;
    }

    /* Pestañas de Navegación */
    .stTabs [data-baseweb="tab-list"] {
        gap: 60px;
        justify-content: center;
        border-bottom: 2px solid #f0f0f0;
    }

    .stTabs [data-baseweb="tab"] {
        font-weight: 600;
        color: #8B4513;
        font-size: 16px;
    }

    /* Descripción de paquetes al expandir */
    .package-description {
        font-family: 'Poppins', sans-serif;
        font-size: 14px;
        color: #444;
        text-align: left;
        padding: 20px;
        background: #FDF5E6;
        border-left: 5px solid #8B4513;
        border-radius: 8px;
        margin-top: 15px;
        line-height: 1.6;
    }

    /* Botón flotante WhatsApp */
    .whatsapp-float {
        position: fixed;
        bottom: 40px;
        right: 40px;
        background-color: #25d366;
        color: white !important;
        padding: 18px 35px;
        border-radius: 50px;
        text-decoration: none;
        z-index: 1000;
        font-weight: 700;
        box-shadow: 0 10px 30px rgba(37, 211, 102, 0.4);
        transition: all 0.3s ease;
    }
    
    .whatsapp-float:hover {
        transform: scale(1.1);
        background-color: #128c7e;
    }
    
    h3, h2 {
        font-family: 'Lora', serif;
        color: #8B4513;
        margin-top: 30px;
    }

    /* Tabla comparativa */
    .comp-table {
        width: 100%;
        border-collapse: collapse;
        margin: 30px 0;
        font-family: 'Poppins', sans-serif;
    }
    .comp-table th {
        background-color: #8B4513;
        color: white;
        padding: 15px;
        text-align: center;
    }
    .comp-table td {
        padding: 15px;
        border-bottom: 1px solid #eee;
        text-align: center;
    }

    /* Tarjetas de Testimonios/Reseñas */
    .testimonial-card {
        background: #ffffff;
        border: 1px solid #f0f0f0;
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        margin-top: 20px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.05);
        height: 100%;
    }
    .testimonial-avatar {
        width: 80px;
        height: 80px;
        border-radius: 50%;
        object-fit: cover;
        margin-bottom: 15px;
        border: 3px solid #8B4513;
    }
    .testimonial-name {
        font-weight: 600;
        color: #8B4513;
        font-size: 18px;
    }
    .testimonial-text {
        font-style: italic;
        font-size: 15px;
        color: #666;
        margin-top: 15px;
        line-height: 1.5;
    }
    .stars {
        color: #F1C40F;
        font-size: 20px;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. BARRA SUPERIOR DE CONTACTO
st.markdown("""
    <div class="top-bar">
        <div>📞 +57 324 373 1661 | ✉️ veronicaarangopedrozo@gmail.com</div>
        <div>📍 Medellín | Colombia</div>
    </div>
    """, unsafe_allow_html=True)

# 4. LOGOTIPO
col_l, _ = st.columns([1, 3])
with col_l:
    # Usando el logo proporcionado
    st.image("https://i.ibb.co/ds6F7b72/ve.png", width=280)

# 5. MENÚ PRINCIPAL (TABS)
tab_inicio, tab_tours, tab_formularios, tab_blog = st.tabs([
    "🏠 CONÓCENOS", "🌊 NUESTROS TOURS", "📋 SERVICIOS / PQR", "✍️ BLOG"
])

# --- PESTAÑA: CONÓCENOS ---
with tab_inicio:
    st.markdown("""
        <div class="hero-section">
            <h1 class="hero-title">Costa-Tour</h1>
            <p style='font-size: 24px; font-style: italic; font-weight: 300;'>
                "El viaje es el servicio, y el destino es tu felicidad."
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("### ¿Quiénes somos?")
    st.write("""
    En **Costa-Tour**, redefinimos el concepto de viaje. Nacimos con la convicción de que el verdadero lujo no reside únicamente en un destino, sino en la calidad del servicio y la calidez humana que te acompaña en cada paso del camino.
    
    No somos solo una agencia de viajes; somos **arquitectos de memorias**. Nos especializamos en conectar el corazón indomable de Colombia con el mundo, ofreciendo experiencias que equilibran la riqueza natural de nuestras costas con un estándar de servicio impecable.
    """)
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### Nuestra Filosofía")
        st.write("""
        Creemos que un viaje se vive tres veces: al soñarlo, al vivirlo y al recordarlo.
        * **Autenticidad:** Respetamos la cultura local del Caribe y el Pacífico.
        * **Excelencia:** Atención personalizada en cada una de nuestras líneas.
        * **Pasión:** Cuidamos desde el guía hasta el transporte para tu tranquilidad.
        """)
    with c2:
        st.markdown("### ¿Por qué elegirnos?")
        st.write("""
        * **Flexibilidad:** Tú eliges el destino, nosotros el nivel de confort.
        * **Turismo Sostenible:** Apoyamos directamente a las comunidades locales.
        * **Seguridad:** Protocolos estrictos y asistencia médica incluida.
        """)

    # --- SECCIÓN DE RESEÑAS ---
    st.markdown("<br><hr><h2 style='text-align: center;'>Voces de nuestros Viajeros</h2>", unsafe_allow_html=True)
    
    rev_col1, rev_col2, rev_col3 = st.columns(3)
    
    testimonios = [
        {
            "nombre": "Carolina Méndez",
            "foto": "https://randomuser.me/api/portraits/women/44.jpg",
            "estrellas": "★★★★★",
            "comentario": "La línea Premium es increíble. El Pacífico Místico superó mis expectativas; el hotel boutique era un sueño y el guía bilingüe fue súper atento."
        },
        {
            "nombre": "Andrés Felipe Ruiz",
            "foto": "https://randomuser.me/api/portraits/men/32.jpg",
            "estrellas": "★★★★★",
            "comentario": "Viajé con mi familia a Nuquí. Todo muy bien organizado, seguro y auténtico. ¡Costa-Tour es confianza total para viajar en Colombia!"
        },
        {
            "nombre": "Mariana Gómez",
            "foto": "https://randomuser.me/api/portraits/women/68.jpg",
            "estrellas": "★★★★★",
            "comentario": "Excelente servicio. Tuve un cambio de última hora y lo resolvieron por WhatsApp en minutos. Muy recomendados para planes de playa."
        }
    ]
    
    for i, col_r in enumerate([rev_col1, rev_col2, rev_col3]):
        with col_r:
            t = testimonios[i]
            st.markdown(f"""
            <div class="testimonial-card">
                <img src="{t['foto']}" class="testimonial-avatar">
                <div class="stars">{t['estrellas']}</div>
                <div class="testimonial-name">{t['nombre']}</div>
                <div class="testimonial-text">"{t['comentario']}"</div>
            </div>
            """, unsafe_allow_html=True)

# --- PESTAÑA: NUESTROS TOURS ---
with tab_tours:
    st.markdown("<h1 style='text-align: center;'>Portafolio de Experiencias</h1>", unsafe_allow_html=True)
    
    st.markdown("### Comparativa de Líneas de Servicio")
    st.markdown("""
    <table class="comp-table">
        <tr>
            <th>Característica</th>
            <th>Línea Estándar</th>
            <th>Línea Premium</th>
        </tr>
        <tr>
            <td><b>Transporte</b></td>
            <td>Vans de turismo compartidas</td>
            <td>Camionetas o lanchas privadas</td>
        </tr>
        <tr>
            <td><b>Hospedaje</b></td>
            <td>Hoteles 3-4 estrellas seleccionados</td>
            <td>Resorts de lujo o Hoteles Boutique</td>
        </tr>
        <tr>
            <td><b>Alimentación</b></td>
            <td>Desayunos incluidos / Menú del día</td>
            <td>Todo incluido / Platos a la carta</td>
        </tr>
        <tr>
            <td><b>Asistencia</b></td>
            <td>Guía local grupal</td>
            <td>Concierge privado 24/7</td>
        </tr>
    </table>
    """, unsafe_allow_html=True)

    # LÍNEA PREMIUM
    st.markdown("## ✨ Línea Premium: Exclusividad Sin Límites")
    
    pcol1, pcol2, pcol3, pcol4 = st.columns(4)
    paquetes_p = [
        ("Caribe Mágico", "https://media-cdn.tripadvisor.com/media/photo-s/2f/59/25/75/caption.jpg", "p1", 
         "<b>Escapada VIP al Caribe.</b><br>Hospedaje en suites frente al mar.<br>Incluye cena romántica privada y transporte en yate."),
        ("Pacífico Vivo", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRIeSN9RSQsxw_n-gbbbfOOsjBrcClZngt3DA&s", "p2", 
         "<b>Aventura y confort.</b><br>Avistamiento de ballenas privado con expertos.<br>Hospedaje en Eco-Lodge boutique de lujo."),
        ("Pacífico Místico", "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2c/b0/c2/4f/private-beach-hotels.jpg?w=1200&h=-1&s=1", "p3", 
         "<b>Conexión espiritual.</b><br>Retiros de yoga y spa frente al océano.<br>Vuelos chárter incluidos y alimentación orgánica."),
        ("Sol Caribe", "https://cdn2.paraty.es/landmar/images/865ffac6866fcba", "p4", 
         "<b>Diversión Premium.</b><br>Acceso a clubes de playa exclusivos.<br>Transporte privado y tours personalizados por la ciudad.")
    ]

    for i, (nom, img, k, d) in enumerate(paquetes_p):
        with [pcol1, pcol2, pcol3, pcol4][i]:
            st.image(img, use_container_width=True)
            st.markdown(f"<h4 style='text-align: center;'>{nom}</h4>", unsafe_allow_html=True)
            if f"st_{k}" not in st.session_state: st.session_state[f"st_{k}"] = False
            if st.button("Detalles VIP", key=f"btn_{k}"):
                st.session_state[f"st_{k}"] = not st.session_state[f"st_{k}"]
            if st.session_state[f"st_{k}"]:
                st.markdown(f"<div class='package-description'>{d}</div>", unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # LÍNEA ESTÁNDAR
    st.markdown("## 🏖️ Línea Estándar: Calidad y Tradición")
    
    ecol1, ecol2, ecol3, ecol4 = st.columns(4)
    paquetes_e = [
        ("Nuestra Costa", "https://www.latamairlines.com/content/dam/latamxp/sites/vamos-latam/news-colombia/lista-latam/res_shutterstock_1312464929.jpg", "e1", 
         "<b>Esencia Caribeña.</b><br>Visita las playas más icónicas con guías locales.<br>Hospedaje cómodo y seguro."),
        ("Marea", "https://plus.unsplash.com/premium_photo-1669748157617-a3a83cc8ea23?fm=jpg&q=60&w=3000&auto=format&fit=crop", "e2", 
         "<b>Diversión asegurada.</b><br>Planes grupales con actividades náuticas.<br>Ideal para jóvenes y grupos de amigos."),
        ("Ritmo Caribe", "https://condominiovistamar.com/wp-content/uploads/2025/07/playas-en-caovenas.webp", "e3", 
         "<b>Cultura y Sabor.</b><br>Tours gastronómicos y clases de baile local.<br>Hoteles céntricos con fácil acceso."),
        ("Ruta Marina", "https://blog.gimlivingspaces.com/hubfs/Muelle%20r%C3%BAstico%20de%20madera%20con%20una%20palapa%20con%20vistas%20a%20las%20aguas%20turquesas%20cristalinas%20en%20Isla%20Mujeres%2C%20playa%20de%20M%C3%A9xico.webp", "e4", 
         "<b>Exploración Costera.</b><br>Senderismo y visitas a manglares protegidos.<br>Un plan perfecto para la familia.")
    ]

    for i, (nom, img, k, d) in enumerate(paquetes_e):
        with [ecol1, ecol2, ecol3, ecol4][i]:
            st.image(img, use_container_width=True)
            st.markdown(f"<h4 style='text-align: center;'>{nom}</h4>", unsafe_allow_html=True)
            if f"st_{k}" not in st.session_state: st.session_state[f"st_{k}"] = False
            if st.button("Saber más", key=f"btn_{k}"):
                st.session_state[f"st_{k}"] = not st.session_state[f"st_{k}"]
            if st.session_state[f"st_{k}"]:
                st.markdown(f"<div class='package-description'>{d}</div>", unsafe_allow_html=True)

# --- PESTAÑA: SERVICIOS / PQR ---
with tab_formularios:
    st.markdown("### Atención al Cliente y Soporte")
    st.write("Tu tranquilidad es nuestra prioridad. Si tienes alguna solicitud, queja, reclamo o sugerencia, utiliza nuestro portal oficial.")
    st.info("Al hacer clic serás redirigido a nuestro formulario de atención de Microsoft Forms.")
    st.link_button("Ir al Portal de PQR", "https://forms.office.com/pages/responsepage.aspx?id=IefhmYRxjkmK_7KtTlPBwmzEaoV6AVxMnWIMDnUV_6JUQjFRQVBCSEg5UldERzdTVkUxU1ZTRTFTMy4u&route=shorturl")

# --- PESTAÑA: BLOG ---
with tab_blog:
    st.markdown("### ✍️ Costa-Tour Blog: Inspiración para tu Viaje")
    st.write("¿No sabes qué empacar? ¿Buscas la mejor época para ver ballenas? Nuestro blog está lleno de consejos expertos para viajeros.")
    st.link_button("Leer el Blog de Costa-Tour", "https://tipsdeviajeparalacostacolombiana.blogspot.com/p/tips-de-viaje-para-la-costa-caribe-y-la.html")

# 6. BOTÓN FLOTANTE WHATSAPP
st.markdown("""
    <a href="https://wa.me/573243731661?text=Hola%20Costa-Tour!%20Me%20gustaría%20recibir%20asesoría%20para%20mi%20próximo%20viaje." class="whatsapp-float" target="_blank">
         📲 Hablar con un Asesor
    </a>
    """, unsafe_allow_html=True)