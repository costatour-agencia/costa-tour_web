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

    .destination-card {
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
        background: white;
        margin-bottom: 20px;
    }
    .destination-card:hover {
        transform: translateY(-5px);
    }

    .stats-container {
        background-color: #8B4513;
        color: white;
        padding: 40px;
        border-radius: 20px;
        text-align: center;
        margin: 40px 0;
    }

    .stat-box h2 {
        color: #FDF5E6 !important;
        font-size: 40px;
        margin: 0;
    }

    .stat-box p {
        font-size: 16px;
        font-weight: 300;
    }

    .comp-table {
        width: 100%;
        border-collapse: collapse;
        margin: 30px 0;
        font-family: 'Poppins', sans-serif;
        background-color: white;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
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
        color: #333;
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

    .instagram-feed img {
        width: 100%;
        height: 200px;
        object-fit: cover;
        border-radius: 10px;
        transition: opacity 0.3s;
    }
    .instagram-feed img:hover {
        opacity: 0.8;
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
    
    col_intro1, col_intro2 = st.columns([2, 1])
    
    with col_intro1:
        st.markdown("### Nuestra Historia")
        st.write("""
        En **Costa-Tour**, redefinimos el concepto de viaje. Nacimos con la convicción de que el verdadero lujo no reside únicamente en un destino, sino en la calidad del servicio y la calidez humana que te acompaña en cada paso del camino.
        
        Nuestra misión es transformar cada travesía en una historia inolvidable, donde tú eres el protagonista y nosotros los arquitectos de tu bienestar. Nos especializamos en conectar a nuestros viajeros con la esencia más pura de las costas colombianas, ofreciendo experiencias que van desde la inmersión cultural profunda hasta el confort más sofisticado.
        """)
        
        st.markdown("#### Nuestros Valores")
        st.markdown("- **Hospitalidad Genuina:** Tratamos a cada viajero como parte de nuestra familia.")
        st.markdown("- **Compromiso Local:** Trabajamos mano a mano con comunidades costeras.")
        st.markdown("- **Excelencia en el Detalle:** Porque lo pequeño hace la diferencia.")
    
    with col_intro2:
        # Añadimos un pequeño indicador de impacto
        st.markdown("""
            <div class="stats-container">
                <div class="stat-box">
                    <h2>+500</h2>
                    <p>Viajeros Felices</p>
                </div>
                <div class="stat-box" style="margin-top:20px;">
                    <h2>15</h2>
                    <p>Comunidades Apoyadas</p>
                </div>
            </div>
        """, unsafe_allow_html=True)

    # --- GALERÍA INDIVIDUAL DE DESTINOS ---
    st.markdown("### Destinos que te esperan")
    st.write("Explora la belleza de nuestras costas a través de estos destinos seleccionados:")
    
    destinos_info = [
        {"url": "https://www.vivecolombia.es/rep/37ce/imagenes/1309902/9/cabo-san-juan-tayronajpg.jpg", "caption": "Cabo San Juan, Parque Tayrona"},
        {"url": "https://www.vivecolombia.es/rep/0c5a/imagenes/1310002/9/isla-majagua-archipielago-de-islas-del-rosariojpg.jpg", "caption": "Islas del Rosario, Cartagena"},
        {"url": "https://www.vivecolombia.es/rep/91cf/imagenes/1309802/9/cabo-de-la-vela-guajirajpg.jpg", "caption": "Cabo de la Vela, La Guajira"},
        {"url": "https://www.vivecolombia.es/rep/3d52/imagenes/1310202/9/playa-nuqui-chocojpg.jpg", "caption": "Playa Nuquí, Chocó"},
        {"url": "https://images.unsplash.com/photo-1575388107541-520c8c3e48ac?q=80&w=1170&auto=format&fit=crop", "caption": "Atardeceres en el Caribe"},
        {"url": "https://images.unsplash.com/photo-1625505825515-c2f8db4a29b5?q=80&w=1230&auto=format&fit=crop", "caption": "San Andrés Islas"}
    ]

    cols_destinos = st.columns(3)
    for i, destino in enumerate(destinos_info):
        with cols_destinos[i % 3]:
            st.markdown('<div class="destination-card">', unsafe_allow_html=True)
            st.image(destino["url"], use_container_width=True)
            st.markdown(f"<p style='text-align: center; font-weight: 600; color: #8B4513; padding: 5px;'>{destino['caption']}</p>", unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    # --- SECCIÓN INSTAGRAM MOMENTS ---
    st.markdown("<br>### Síguenos en @CostaTour")
    st.write("Comparte tus momentos usando nuestro hashtag #MiCostaTour")
    insta_cols = st.columns(6)
    insta_imgs = [
        "https://images.unsplash.com/photo-1519046904884-53103b34b206?q=80&w=1170&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1590523277543-a94d2e4eb00b?q=80&w=1230&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?q=80&w=1173&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1520483844508-8c731fc6ff4f?q=80&w=1170&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1544124499-58912cbddaad?q=80&w=1230&auto=format&fit=crop",
        "https://images.unsplash.com/photo-1471922694854-ff1b63b20054?q=80&w=1172&auto=format&fit=crop"
    ]
    for i, img_url in enumerate(insta_imgs):
        with insta_cols[i]:
            st.markdown(f'<div class="instagram-feed"><img src="{img_url}"></div>', unsafe_allow_html=True)

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
         """<b>"Siéntete un local más."</b><br>Este paquete es para quienes creen que viajar es conocer a la gente.<br><br>
         <b>Alojamiento:</b> Hoteles boutique tipo posada.<br>
         <b>Servicios:</b> Desayunos típicos, traslados cómodos y guía local.<br>
         <b>Ideal para:</b> Viajeros solitarios y parejas."""),
        ("Marea", "https://plus.unsplash.com/premium_photo-1669748157617-a3a83cc8ea23?fm=jpg&q=60&w=3000&auto=format&fit=crop", "e2", 
         """<b>"Siente la fuerza del océano."</b><br>Marea es adrenalina y contacto directo con el agua.<br><br>
         <b>Alojamiento:</b> Hoteles modernos con piscina.<br>
         <b>Servicios:</b> Deportes acuáticos incluidos y seguro médico.<br>
         <b>Ideal para:</b> Grupos de amigos."""),
        ("Ritmo Caribe", "https://condominiovistamar.com/wp-content/uploads/2025/07/playas-en-caovenas.webp", "e3", 
         """<b>"El alma de la fiesta."</b><br>Este plan celebra la música, el baile y la vida nocturna.<br><br>
         <b>Alojamiento:</b> Hoteles céntricos.<br>
         <b>Servicios:</b> City Tour nocturno y cóctel VIP.<br>
         <b>Ideal para:</b> Graduaciones y amigos."""),
        ("Ruta Marina", "https://blog.gimlivingspaces.com/hubfs/Muelle%20r%C3%BAstico%20de%20madera%20con%20una%20palapa%20con%20vistas%20a%20las%20aguas%20turquesas%20cristalinas%20en%20Isla%20Mujeres%2C%20playa%20de%20M%C3%A9xico.webp", "e4", 
         """<b>"Naturaleza pura."</b><br>Un viaje educativo y consciente enfocado en el ecosistema.<br><br>
         <b>Alojamiento:</b> Eco-hoteles sostenibles.<br>
         <b>Servicios:</b> Expedición a manglares y charlas biológicas.<br>
         <b>Ideal para:</b> Familias.""")
    ]

    for i, (nom, img, k, d) in enumerate(paquetes_e):
        with [ecol1, ecol2, ecol3, ecol4][i]:
            st.image(img, use_container_width=True)
            st.markdown(f"<h4 style='text-align: center;'>{nom}</h4>", unsafe_allow_html=True)
            if f"st_{k}" not in st.session_state: st.session_state[f"st_{k}"] = False
            
            label = "Cerrar" if st.session_state[f"st_{k}"] else "Ver Plan"
            if st.button(label, key=f"btn_{k}"):
                st.session_state[f"st_{k}"] = not st.session_state[f"st_{k}"]
                st.rerun()
            
            if st.session_state[f"st_{k}"]:
                st.markdown(f"<div class='package-description'>{d}</div>", unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # LÍNEA PREMIUM
    st.markdown("## LÍNEA PREMIUM: Exclusividad Elevada")
    st.write("El lujo no es solo un hotel, es que no tengas que preocuparte por absolutamente nada.")
    
    pcol1, pcol2, pcol3, pcol4 = st.columns(4)
    paquetes_p = [
        ("Caribe Mágico", "https://media-cdn.tripadvisor.com/media/photo-s/2f/59/25/75/caption.jpg", "p1", 
         """<b>"Cena bajo las estrellas."</b><br>Suite de lujo, cena privada en la playa y open bar premium."""),
        ("Pacífico Vivo", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRIeSN9RSQsxw_n-gbbbfOOsjBrcClZngt3DA&s", "p2", 
         """<b>"Ballenas y Yates."</b><br>Avistamiento privado en yate con catering de lujo y guía experto."""),
        ("Pacífico Místico", "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2c/b0/c2/4f/private-beach-hotels.jpg?w=1200&h=-1&s=1", "p3", 
         """<b>"Bienestar Total."</b><br>Villas privadas, spa termal y menú Farm-to-Table."""),
        ("Sol Caribe", "https://cdn2.paraty.es/landmar/images/865ffac6866fcba", "p4", 
         """<b>"All-Inclusive VIP."</b><br>Resorts de gran lujo, concierge 24/7 y traslados blindados.""")
    ]

    for i, (nom, img, k, d) in enumerate(paquetes_p):
        with [pcol1, pcol2, pcol3, pcol4][i]:
            st.image(img, use_container_width=True)
            st.markdown(f"<h4 style='text-align: center;'>{nom}</h4>", unsafe_allow_html=True)
            if f"st_{k}" not in st.session_state: st.session_state[f"st_{k}"] = False
            
            label = "Cerrar" if st.session_state[f"st_{k}"] else "Detalles VIP"
            if st.button(label, key=f"btn_{k}"):
                st.session_state[f"st_{k}"] = not st.session_state[f"st_{k}"]
                st.rerun()
                
            if st.session_state[f"st_{k}"]:
                st.markdown(f"<div class='package-description'>{d}</div>", unsafe_allow_html=True)

# --- PESTAÑA: INFORMACIÓN, BLOG Y FAQ ---
with tab_info_blog:
    col_info1, col_info2 = st.columns([1, 1])
    
    with col_info1:
        st.markdown("### Centro de Ayuda")
        st.write("Planifica tu viaje con tranquilidad.")
        st.link_button("Portal de PQR", "https://forms.office.com/pages/responsepage.aspx?id=IefhmYRxjkmK_7KtTlPBwmzEaoV6AVxMnWIMDnUV_6JUQjFRQVBCSEg5UldERzdTVkUxU1ZTRTFTMy4u&route=shorturl")
        st.link_button("Blog: Tips de Viaje", "https://tipsdeviajeparalacostacolombiana.blogspot.com/p/tips-de-viaje-para-la-costa-caribe-y-la.html")
        
        st.markdown("<br>#### Suscríbete a Ofertas", unsafe_allow_html=True)
        email = st.text_input("Ingresa tu email para recibir descuentos VIP")
        if st.button("Suscribirme"):
            st.success("¡Bienvenido a la familia Costa-Tour! Revisa tu correo.")
    
    with col_info2:
        st.markdown("### Contacto Directo")
        st.write("📍 Oficina Principal: Medellín, Colombia")
        st.write("📞 WhatsApp: +57 324 373 1661")
        st.write("✉️ Correo: veronicaarangopedrozo@gmail.com")
        
        # Mapa Simulado de Zonas
        st.markdown("#### Nuestras Zonas de Cobertura")
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Mapa_de_Colombia_%28regiones_naturales%29.svg/1200px-Mapa_de_Colombia_%28regiones_naturales%29.svg.png", caption="Operamos en toda la Costa Caribe y Pacífico", width=250)

    st.markdown("<br><hr>", unsafe_allow_html=True)
    st.markdown("### Preguntas Frecuentes (FAQ)")
    
    faq_items = [
        ("1. ¿Qué incluye el seguro?", "Cobertura para accidentes y enfermedades repentinas."),
        ("2. ¿Puedo cambiar la fecha?", "Sí, hasta 15 días antes del viaje."),
        ("3. ¿Métodos de pago?", "PSE, Tarjetas de Crédito y Transferencias."),
        ("4. ¿Vouchers?", "Digitales vía WhatsApp y Correo 48h tras el pago.")
    ]
    
    for q, a in faq_items:
        with st.expander(q):
            st.write(a)

# 6. BOTÓN FLOTANTE
st.markdown("""
    <a href="https://wa.me/573243731661?text=Hola%20Costa-Tour!%20Me%20gustaría%20recibir%20asesoría." class="whatsapp-float" target="_blank">
         📲 Hablar con un Asesor
    </a>
    """, unsafe_allow_html=True)


