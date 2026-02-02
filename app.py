import streamlit as st
import time

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

    .top-bar {
        background-color: #8B4513;
        color: white;
        padding: 12px 60px;
        display: flex;
        justify-content: space-between;
        font-size: 14px;
        font-family: 'Poppins', sans-serif;
    }

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
    }
    
    h3, h2 {
        font-family: 'Lora', serif;
        color: #8B4513;
        margin-top: 30px;
    }

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
    }
    .testimonial-text {
        font-style: italic;
        font-size: 15px;
        color: #666;
        margin-top: 15px;
    }
    .stars {
        color: #F1C40F;
        font-size: 20px;
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

# 4. LOGOTIPO
col_l, _ = st.columns([1, 3])
with col_l:
    st.image("https://i.ibb.co/ds6F7b72/ve.png", width=280)

# 5. MENÚ PRINCIPAL
tab_inicio, tab_tours, tab_info_blog = st.tabs([
    "🏠 CONÓCENOS", "🌊 NUESTROS TOURS", "📋 INFORMACIÓN Y BLOG"
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
    """)
    
    # --- GALERÍA DINÁMICA DE DESTINOS ---
    st.markdown("### Destinos que te esperan")
    destinos_imgs = [
        "https://www.vivecolombia.es/rep/37ce/imagenes/1309902/9/cabo-san-juan-tayronajpg.jpg",
        "https://www.vivecolombia.es/rep/0c5a/imagenes/1310002/9/isla-majagua-archipielago-de-islas-del-rosariojpg.jpg",
        "https://www.vivecolombia.es/rep/91cf/imagenes/1309802/9/cabo-de-la-vela-guajirajpg.jpg",
        "https://www.vivecolombia.es/rep/3d52/imagenes/1310202/9/playa-nuqui-chocojpg.jpg",
        "https://plus.unsplash.com/premium_photo-1664116928361-2972cf5d6848?q=80&w=687&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1575388107541-520c8c3e48ac?q=80&w=1170&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1625505825515-c2f8db4a29b5?q=80&w=1230&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1594342436424-dda50df715d9?q=80&w=1171&auto=format&fit=crop"
    ]
    
    # Manejo de estado para la galería (simulando rotación)
    if 'img_idx' not in st.session_state:
        st.session_state.img_idx = 0
    
    # Mostrar imagen actual
    st.image(destinos_imgs[st.session_state.img_idx], use_container_width=True, caption="Nuestros paraísos seleccionados")
    
    col_prev, col_next = st.columns([1, 1])
    with col_prev:
        if st.button("Anterior"):
            st.session_state.img_idx = (st.session_state.img_idx - 1) % len(destinos_imgs)
            st.rerun()
    with col_next:
        if st.button("Siguiente"):
            st.session_state.img_idx = (st.session_state.img_idx + 1) % len(destinos_imgs)
            st.rerun()

    # --- SECCIÓN DE RESEÑAS ---
    st.markdown("<br><hr><h2 style='text-align: center;'>Voces de nuestros Viajeros</h2>", unsafe_allow_html=True)
    rev_col1, rev_col2, rev_col3 = st.columns(3)
    testimonios = [
        {"nombre": "Carolina Méndez", "foto": "https://randomuser.me/api/portraits/women/44.jpg", "estrellas": "★★★★★", "comentario": "La línea Premium es increíble. El Pacífico Místico superó mis expectativas."},
        {"nombre": "Andrés Felipe Ruiz", "foto": "https://randomuser.me/api/portraits/men/32.jpg", "estrellas": "★★★★★", "comentario": "Viajé con mi familia a Nuquí. Todo muy bien organizado, seguro y auténtico."},
        {"nombre": "Mariana Gómez", "foto": "https://randomuser.me/api/portraits/women/68.jpg", "estrellas": "★★★★★", "comentario": "Excelente servicio. Tuve un cambio de última hora y lo resolvieron por WhatsApp."}
    ]
    for i, col_r in enumerate([rev_col1, rev_col2, rev_col3]):
        with col_r:
            t = testimonios[i]
            st.markdown(f'<div class="testimonial-card"><img src="{t["foto"]}" class="testimonial-avatar"><div class="stars">{t["estrellas"]}</div><div class="testimonial-name">{t["nombre"]}</div><div class="testimonial-text">"{t["comentario"]}"</div></div>', unsafe_allow_html=True)

# --- PESTAÑA: NUESTROS TOURS ---
with tab_tours:
    st.markdown("<h1 style='text-align: center;'>Portafolio de Experiencias</h1>", unsafe_allow_html=True)
    
    # LÍNEA ESTÁNDAR
    st.markdown("## LÍNEA ESTÁNDAR: Conexión Auténtica")
    st.write("Diseñada para viajeros que buscan comodidad, seguridad y vivir el destino de forma real.")
    
    ecol1, ecol2, ecol3, ecol4 = st.columns(4)
    paquetes_e = [
        ("Nuestra Costa", "https://www.latamairlines.com/content/dam/latamxp/sites/vamos-latam/news-colombia/lista-latam/res_shutterstock_1312464929.jpg", "e1", 
         """<b>"Siéntete un local más."</b><br>Este paquete es para quienes creen que viajar es conocer a la gente. Nos alejamos de los grandes resorts para llevarte al corazón de la cultura costera.<br><br>
         <b>Alojamiento:</b> Hoteles boutique tipo posada con encanto local.<br>
         <b>Experiencia destacada:</b> Recorrido a pie por pueblos pesqueros y clases de cocina tradicional.<br>
         <b>Servicios:</b> Desayunos típicos incluidos, traslados en transporte regional cómodo y guía local certificado.<br>
         <b>Ideal para:</b> Viajeros solitarios, parejas jóvenes y estudiantes."""),
        ("Marea", "https://plus.unsplash.com/premium_photo-1669748157617-a3a83cc8ea23?fm=jpg&q=60&w=3000&auto=format&fit=crop", "e2", 
         """<b>"Siente la fuerza del océano."</b><br>Para los que no van a la playa a quedarse sentados. Marea es adrenalina y contacto directo con el agua.<br><br>
         <b>Alojamiento:</b> Hoteles modernos con zonas sociales vibrantes y piscina.<br>
         <b>Experiencia destacada:</b> Un día de deportes acuáticos (clase de surf en el Pacífico o Paddle Board en el Caribe).<br>
         <b>Servicios:</b> Almuerzo tipo "box lunch" para días de playa y seguro de asistencia médica con cobertura para deportes.<br>
         <b>Ideal para:</b> Grupos de amigos y amantes de la actividad física."""),
        ("Ritmo Caribe", "https://condominiovistamar.com/wp-content/uploads/2025/07/playas-en-caovenas.webp", "e3", 
         """<b>"El alma de la fiesta y el color."</b><br>No importa si eliges el Pacífico, aquí el espíritu es alegre. Este plan celebra la música, el baile y la vida nocturna.<br><br>
         <b>Alojamiento:</b> Hoteles cercanos a las zonas de entretenimiento y comercio.<br>
         <b>Experiencia destacada:</b> City Tour nocturno con ingreso a los clubes más icónicos y cóctel de bienvenida.<br>
         <b>Servicios:</b> Traslados grupales nocturnos seguros y desayunos tipo buffet.<br>
         <b>Ideal para:</b> Viajes de graduación o despedidas de solteros/as."""),
        ("Ruta Marina", "https://blog.gimlivingspaces.com/hubfs/Muelle%20r%C3%BAstico%20de%20madera%20con%20una%20palapa%20con%20vistas%20a%20las%20aguas%20turquesas%20cristalinas%20en%20Isla%20Mujeres%2C%20playa%20de%20M%C3%A9xico.webp", "e4", 
         """<b>"Naturaleza en su estado puro."</b><br>Un viaje educativo y consciente. Nos enfocamos en el avistamiento y la protección del ecosistema.<br><br>
         <b>Alojamiento:</b> Eco-hoteles con políticas de sostenibilidad y ahorro de agua.<br>
         <b>Experiencia destacada:</b> Expedición a manglares o santuarios de fauna protegida.<br>
         <b>Servicios:</b> Charla con biólogos locales y transporte en lanchas con motores ecológicos.<br>
         <b>Ideal para:</b> Familias con niños y amantes de la fotografía de naturaleza.""")
    ]

    for i, (nom, img, k, d) in enumerate(paquetes_e):
        with [ecol1, ecol2, ecol3, ecol4][i]:
            st.image(img, use_container_width=True)
            st.markdown(f"<h4 style='text-align: center;'>{nom}</h4>", unsafe_allow_html=True)
            if f"st_{k}" not in st.session_state: st.session_state[f"st_{k}"] = False
            if st.button("Ver Plan", key=f"btn_{k}"):
                st.session_state[f"st_{k}"] = not st.session_state[f"st_{k}"]
            if st.session_state[f"st_{k}"]:
                st.markdown(f"<div class='package-description'>{d}</div>", unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # LÍNEA PREMIUM
    st.markdown("## LÍNEA PREMIUM: Exclusividad Elevada")
    st.write("El lujo no es solo un hotel, es que no tengas que preocuparte por absolutamente nada.")
    
    pcol1, pcol2, pcol3, pcol4 = st.columns(4)
    paquetes_p = [
        ("Caribe Mágico", "https://media-cdn.tripadvisor.com/media/photo-s/2f/59/25/75/caption.jpg", "p1", 
         """<b>"Donde el tiempo se detiene."</b><br>Una experiencia sensorial diseñada para el descanso absoluto en escenarios de película.<br><br>
         <b>Alojamiento:</b> Suites de lujo con vista frontal al mar y jacuzzi privado.<br>
         <b>Servicio VIP:</b> Cena privada de 3 pasos en la playa con mesero personal.<br>
         <b>Incluye:</b> Open bar de licores premium y acceso a zonas privadas del hotel."""),
        ("Pacífico Vivo", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRIeSN9RSQsxw_n-gbbbfOOsjBrcClZngt3DA&s", "p2", 
         """<b>"La majestad de la vida salvaje."</b><br>Una aventura de alto nivel para presenciar los milagros de la naturaleza con total confort.<br><br>
         <b>Alojamiento:</b> Glamping de lujo o Eco-Lodges boutique en medio de la selva frente al mar.<br>
         <b>Servicio VIP:</b> Avistamiento privado de ballenas o delfines con catering a bordo de un yate.<br>
         <b>Incluye:</b> Equipamiento profesional de observación y guía experto bilingüe."""),
        ("Pacífico Místico", "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2c/b0/c2/4f/private-beach-hotels.jpg?w=1200&h=-1&s=1", "p3", 
         """<b>"Sanación para el alma."</b><br>Un retiro de bienestar en los lugares más remotos y energéticos de la costa.<br><br>
         <b>Alojamiento:</b> Villas privadas con arquitectura bioclimática y total privacidad.<br>
         <b>Servicio VIP:</b> Circuito de Spa termal o de lodo y sesión privada de meditación al amanecer.<br>
         <b>Incluye:</b> Menú de alimentación orgánica "Farm to table" diseñado por chefs."""),
        ("Sol Caribe", "https://cdn2.paraty.es/landmar/images/865ffac6866fcba", "p4", 
         """<b>"El privilegio del sol eterno."</b><br>Para quienes buscan el estándar más alto del turismo internacional.<br><br>
         <b>Alojamiento:</b> Resorts de gran lujo con sistema All-Inclusive Premium.<br>
         <b>Servicio VIP:</b> Concierge personal para gestionar todas tus reservas y traslados en vehículo blindado o lancha de alta velocidad.<br>
         <b>Incluye:</b> Pases "Fast Pass" para las atracciones turísticas locales y amenidades de bienvenida de marcas de lujo.""")
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

# --- PESTAÑA: INFORMACIÓN, BLOG Y FAQ ---
with tab_info_blog:
    col_info1, col_info2 = st.columns([1, 1])
    
    with col_info1:
        st.markdown("### Centro de Ayuda y Blog")
        st.write("Accede a nuestros recursos digitales para planificar tu viaje.")
        st.link_button("Portal de PQR (Quejas y Reclamos)", "https://forms.office.com/pages/responsepage.aspx?id=IefhmYRxjkmK_7KtTlPBwmzEaoV6AVxMnWIMDnUV_6JUQjFRQVBCSEg5UldERzdTVkUxU1ZTRTFTMy4u&route=shorturl")
        st.link_button("Blog Costa-Tour: Tips de Viaje", "https://tipsdeviajeparalacostacolombiana.blogspot.com/p/tips-de-viaje-para-la-costa-caribe-y-la.html")
    
    with col_info2:
        st.markdown("### Contacto Directo")
        st.write("Si prefieres atención inmediata, nuestro equipo está listo para ayudarte.")
        st.write("📞 WhatsApp: +57 324 373 1661")
        st.write("✉️ Correo: veronicaarangopedrozo@gmail.com")

    st.markdown("<br><hr>", unsafe_allow_html=True)
    st.markdown("### Preguntas Frecuentes (FAQ)")
    
    with st.expander("1. ¿Qué incluye el seguro de asistencia médica?"):
        st.write("Incluye cobertura para accidentes, enfermedades repentinas y, en la Línea Marea, cobertura especial para deportes acuáticos.")
    
    with st.expander("2. ¿Puedo cambiar la fecha de mi viaje después de reservar?"):
        st.write("Sí, permitimos un cambio sin penalidad hasta 15 días antes del viaje, sujeto a disponibilidad y ajuste de tarifas.")
    
    with st.expander("3. ¿Cuáles son los métodos de pago aceptados?"):
        st.write("Aceptamos transferencias bancarias, tarjetas de crédito (Visa, Mastercard, Amex) y pagos vía PSE.")
    
    with st.expander("4. ¿Los tours incluyen propinas para los guías?"):
        st.write("Las propinas son voluntarias y no están incluidas en el precio del paquete.")
    
    with st.expander("5. ¿Ofrecen planes para niños pequeños?"):
        st.write("Sí, la Ruta Marina es ideal para familias. Niños menores de 2 años viajan gratis en la mayoría de destinos (sujeto a aerolínea).")
    
    with st.expander("6. ¿Es seguro viajar al Pacífico colombiano?"):
        st.write("Absolutamente. Operamos en zonas turísticas seguras y siempre contamos con guías locales que conocen perfectamente el territorio.")
    
    with st.expander("7. ¿Qué debo empacar para un retiro místico?"):
        st.write("Ropa cómoda de algodón, protector solar biodegradable, repelente natural y calzado para senderismo suave.")
    
    with st.expander("8. ¿La Línea Premium incluye transporte desde el aeropuerto?"):
        st.write("Sí, incluye traslados privados en vehículos blindados o de alta gama desde y hacia el aeropuerto.")
    
    with st.expander("9. ¿Puedo personalizar un tour Estándar con servicios Premium?"):
        st.write("¡Claro! Podemos añadir servicios adicionales 'a la carta' a cualquier paquete estándar.")
    
    with st.expander("10. ¿Cómo recibo mis vouchers de viaje?"):
        st.write("Se envían de forma digital a tu correo electrónico y WhatsApp 48 horas después de confirmado el pago total.")

# 6. BOTÓN FLOTANTE
st.markdown("""
    <a href="https://wa.me/573243731661?text=Hola%20Costa-Tour!%20Me%20gustaría%20recibir%20asesoría." class="whatsapp-float" target="_blank">
         📲 Hablar con un Asesor
    </a>
    """, unsafe_allow_html=True)