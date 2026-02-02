import streamlit as st
import pandas as pd

# 1. CONFIGURACIÓN DE PÁGINA (PUNTAL PARA EL DISEÑO)
st.set_page_config(
    page_title="Costa-Tour | Agencia de Viajes", 
    layout="wide", 
    page_icon="✈️"
)

# 2. ESTILOS CSS PERSONALIZADOS (LÓGICA VISUAL EXTENSA)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&family=Lora:ital,wght@0,400;1,400&display=swap');

    /* Fondo general */
    .stApp { background-color: #FFFFFF !important; }
    
    /* Tipografía y Textos */
    html, body, [class*="st-"] {
        font-family: 'Poppins', sans-serif;
    }

    /* Botones Rojos Estilo Costa-Tour */
    .stButton > button {
        background-color: #C0392B !important;
        color: white !important;
        border: none !important;
        padding: 12px 24px !important;
        border-radius: 10px !important;
        transition: all 0.3s ease;
        width: 100%;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .stButton > button:hover {
        background-color: #A93226 !important;
        transform: translateY(-3px);
        box-shadow: 0 5px 15px rgba(192, 57, 43, 0.3);
    }

    /* Diseño de Tabla Comparativa */
    [data-testid="stTable"] {
        background-color: white;
        border-radius: 15px;
        overflow: hidden;
        border: 1px solid #EEE;
        box-shadow: 0 4px 20px rgba(0,0,0,0.05);
    }
    
    [data-testid="stTable"] td {
        padding: 15px !important;
        color: #444;
    }

    /* Sección Hero */
    .hero-section {
        background-image: linear-gradient(rgba(0,0,0,0.45), rgba(0,0,0,0.45)), url('https://images.unsplash.com/photo-1507525428034-b723cf961d3e?q=80&w=2073&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        height: 450px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        text-align: center;
        flex-direction: column;
        border-radius: 30px;
        margin-bottom: 50px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.15);
    }

    .hero-title {
        color: white !important;
        font-family: 'Lora', serif;
        font-size: 72px;
        font-weight: bold;
        margin-bottom: 15px;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.5);
    }

    /* Cuadros de Descripción de Paquetes */
    .package-description {
        font-family: 'Poppins', sans-serif;
        font-size: 14px;
        color: #444;
        padding: 25px;
        background: #F9F9F9;
        border-left: 6px solid #C0392B;
        border-radius: 12px;
        margin-top: 15px;
        line-height: 1.8;
        box-shadow: inset 0 0 10px rgba(0,0,0,0.02);
    }

    /* Tarjetas de Testimonios */
    .testimonial-card {
        background: #FFFFFF;
        padding: 30px;
        border-radius: 25px;
        border: 1px solid #F0F0F0;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.03);
        height: 100%;
        transition: 0.3s;
    }
    
    .testimonial-card:hover {
        transform: scale(1.02);
    }

    .section-title {
        text-align: center;
        margin: 60px 0 40px 0;
        color: #2C3E50;
        font-size: 32px;
        font-weight: bold;
        font-family: 'Lora', serif;
    }

    /* Botón Flotante WhatsApp */
    .whatsapp-float {
        position: fixed;
        bottom: 40px;
        right: 40px;
        background-color: #25d366;
        color: white !important;
        padding: 18px 28px;
        border-radius: 50px;
        text-decoration: none;
        z-index: 1000;
        font-weight: 600;
        box-shadow: 0 12px 30px rgba(37, 211, 102, 0.4);
        display: flex;
        align-items: center;
        gap: 12px;
        transition: 0.3s;
    }
    
    .whatsapp-float:hover {
        transform: scale(1.1);
        background-color: #20ba5a;
    }

    /* Cuadros de Contacto */
    .contact-info-card {
        padding: 30px;
        border-radius: 20px;
        background-color: #FDFDFD;
        border: 1px solid #F0F0F0;
        margin-bottom: 20px;
    }

    /* Estilo de Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
        justify-content: center;
    }

    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: #F8F9FA;
        border-radius: 10px 10px 0 0;
        padding: 0 30px;
        font-weight: 600;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. HEADER (LOGOTIPO Y DATOS RÁPIDOS)
head_col1, head_col2 = st.columns([2, 1])
with head_col1:
    st.image("https://i.ibb.co/ds6F7b72/ve.png", width=220)
with head_col2:
    st.markdown("""
        <div style='text-align:right; color:#777; font-size:15px; margin-top:15px;'>
            <b>Llámanos:</b> +57 324 373 1661<br>
            <b>Ubicación:</b> El Poblado, Medellín
        </div>
    """, unsafe_allow_html=True)

# 4. SISTEMA DE NAVEGACIÓN (TABS)
tab_inicio, tab_tours, tab_atencion = st.tabs(["✨ NUESTRA ESENCIA", "🌴 CATÁLOGO COMPLETO", "🛎️ SOPORTE Y CONTACTO"])

# --- CONTENIDO: NUESTRA ESENCIA ---
with tab_inicio:
    st.markdown("""
        <div class="hero-section">
            <h1 class="hero-title">Costa-Tour</h1>
            <p style='font-size: 26px; font-style: italic; opacity: 0.9;'>Donde el lujo y la naturaleza se encuentran.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<h2 class='section-title'>Una Trayectoria de Excelencia</h2>", unsafe_allow_html=True)
    col_hist1, col_hist2 = st.columns([1, 1])
    with col_hist1:
        st.write("""
        Costa-Tour nació de la pasión por los paisajes inexplorados de Colombia. 
        Lo que comenzó como una pequeña agencia local en Medellín, hoy es el referente 
        nacional para viajeros que buscan algo más que un simple hotel: buscan historias.
        """)
    with col_hist2:
        st.write("""
        Nos especializamos en dos mundos: la **Línea Estándar**, diseñada para la aventura 
        social y auténtica, y la **Línea Premium**, enfocada en la exclusividad, el confort 
        máximo y el servicio de guante blanco.
        """)

    # TESTIMONIOS (RESEÑAS COMPLETAS)
    st.markdown("<h2 class='section-title'>Experiencias de nuestros Clientes</h2>", unsafe_allow_html=True)
    t_col1, t_col2, t_col3, t_col4 = st.columns(4)
    
    testimonials = [
        {
            "user": "Carlos Mendoza",
            "text": "La atención al detalle fue impecable. Desde la recogida en el aeropuerto hasta los tours privados, todo estuvo perfecto. Superó mis expectativas.",
            "stars": "★★★★★"
        },
        {
            "user": "Ana María Ruiz",
            "text": "El Pacífico con Costa-Tour es otra experiencia. El avistamiento de ballenas fue mágico y muy respetuoso con la naturaleza. ¡Increíble!",
            "stars": "★★★★★"
        },
        {
            "user": "Sebastián Gómez",
            "text": "Paz absoluta y hoteles de primera. Es la primera vez que viajo y no tengo que preocuparme por nada. Volveré sin duda el próximo año.",
            "stars": "★★★★★"
        },
        {
            "user": "Elena Torres",
            "text": "Resolvieron mis dudas al instante por WhatsApp. El equipo es muy profesional y los guías locales conocen cada rincón del Caribe.",
            "stars": "★★★★★"
        }
    ]
    
    for i, t in enumerate(testimonials):
        with [t_col1, t_col2, t_col3, t_col4][i]:
            st.markdown(f"""
                <div class="testimonial-card">
                    <p style='font-style: italic; color: #555; font-size: 14px;'>"{t['text']}"</p>
                    <p style='font-weight: bold; color: #C0392B; margin-top:15px; margin-bottom:0;'>{t['user']}</p>
                    <p style='color: #F1C40F; font-size: 18px;'>{t['stars']}</p>
                </div>
            """, unsafe_allow_html=True)

# --- CONTENIDO: CATÁLOGO DE TOURS ---
with tab_tours:
    st.markdown("<h2 class='section-title'>Compara Nuestras Experiencias</h2>", unsafe_allow_html=True)
    
    # TABLA COMPARATIVA MEJORADA
    df_compare = pd.DataFrame({
        "Beneficios": ["🏨 Alojamiento", "🍽️ Gastronomía", "🚐 Transporte", "🛎️ Asistencia", "⭐ Exclusividad", "🎒 Actividades"],
        "Línea Estándar": [
            "Hoteles 3* / Posadas con encanto local", 
            "Desayuno buffet incluido y cocina típica", 
            "Vans modernas con aire compartido", 
            "Soporte Virtual 24/7 vía WhatsApp", 
            "Grupos dinámicos (10-15 personas)",
            "Itinerarios grupales predefinidos"
        ],
        "Línea Premium": [
            "Resorts 5* / Hoteles Boutique Privados", 
            "Plan Gourmet Pro (Chef en vivo)", 
            "Vehículos de lujo / Traslados Privados", 
            "Concierge Personalizado 24/7", 
            "Privacidad Total / Grupos VIP",
            "Actividades a la medida y horarios flexibles"
        ]
    })
    st.table(df_compare)

    st.markdown("<hr style='margin: 50px 0; border: 0.5px solid #EEE;'>", unsafe_allow_html=True)

    # FUNCIÓN PARA RENDERIZAR BLOQUES DE PAQUETES
    def render_tour_grid(packages, title):
        st.markdown(f"<h2 style='text-align: center; color:#2C3E50; margin-bottom:30px;'>{title}</h2>", unsafe_allow_html=True)
        cols = st.columns(4)
        for idx, p in enumerate(packages):
            with cols[idx]:
                st.image(p['img'], use_container_width=True)
                st.markdown(f"<h4 style='text-align:center;'>{p['name']}</h4>", unsafe_allow_html=True)
                
                # Estado del botón
                key_state = f"state_{p['id']}"
                if key_state not in st.session_state:
                    st.session_state[key_state] = False
                
                btn_label = "Cerrar detalles" if st.session_state[key_state] else "Ver más detalles"
                
                if st.button(btn_label, key=f"btn_{p['id']}"):
                    st.session_state[key_state] = not st.session_state[key_state]
                    st.rerun()
                
                if st.session_state[key_state]:
                    st.markdown(f"""
                        <div class="package-description">
                            {p['desc']}
                        </div>
                    """, unsafe_allow_html=True)

    # DATOS DE PAQUETES PREMIUM
    premium_data = [
        {
            "id": "p_caribe", "name": "Caribe Mágico", 
            "img": "https://media-cdn.tripadvisor.com/media/photo-s/2f/59/25/75/caption.jpg",
            "desc": "<b>Alojamiento:</b> Suite Presidencial frente al mar.<br><b>Comida:</b> Cena privada de 5 tiempos en la playa.<br><b>Extras:</b> Acceso a Club de Playa privado y Open Bar premium."
        },
        {
            "id": "p_pacifico", "name": "Pacífico Vivo", 
            "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRIeSN9RSQsxw_n-gbbbfOOsjBrcClZngt3DA&s",
            "desc": "<b>Alojamiento:</b> Eco-Lodge de lujo en Nuquí.<br><b>Actividad:</b> Lancha privada para avistamiento de ballenas.<br><b>Guía:</b> Biólogo marino especializado bilingüe."
        },
        {
            "id": "p_mistico", "name": "Pacífico Místico", 
            "img": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2c/b0/c2/4f/private-beach-hotels.jpg?w=1200&h=-1&s=1",
            "desc": "<b>Experiencia:</b> Retiro espiritual y Spa de lodo ancestral.<br><b>Comida:</b> Dieta orgánica personalizada por nutricionista.<br><b>Lugar:</b> Bahía Solano en hotel boutique exclusivo."
        },
        {
            "id": "p_sol", "name": "Sol Caribe VIP", 
            "img": "https://cdn2.paraty.es/landmar/images/865ffac6866fcba",
            "desc": "<b>Transporte:</b> Catamarán privado a Islas del Rosario.<br><b>Stay:</b> Resort 5 estrellas en Barú.<br><b>Plus:</b> Mayordomo asignado 24 horas."
        }
    ]
    render_tour_grid(premium_data, "💎 Línea Premium")

    st.markdown("<br><br>", unsafe_allow_html=True)

    # DATOS DE PAQUETES ESTÁNDAR
    standard_data = [
        {
            "id": "e_costa", "name": "Nuestra Costa", 
            "img": "https://www.latamairlines.com/content/dam/latamxp/sites/vamos-latam/news-colombia/lista-latam/res_shutterstock_1312464929.jpg",
            "desc": "<b>Alojamiento:</b> Posadas coloniales confortables.<br><b>Actividad:</b> City tour histórico por el Centro Amurallado.<br><b>Seguro:</b> Cobertura total de viaje nacional."
        },
        {
            "id": "e_marea", "name": "Marea y Aventura", 
            "img": "https://plus.unsplash.com/premium_photo-1669748157617-a3a83cc8ea23?fm=jpg&q=60&w=3000&auto=format&fit=crop",
            "desc": "<b>Perfil:</b> Ideal para jóvenes y aventureros.<br><b>Action:</b> Clases de surf grupal en Castillogrande.<br><b>Stay:</b> Hotel moderno en Bocagrande."
        },
        {
            "id": "e_ritmo", "name": "Ritmo Caribe", 
            "img": "https://condominiovistamar.com/wp-content/uploads/2025/07/playas-en-caovenas.webp",
            "desc": "<b>Cultura:</b> Inmersión en música y baile local.<br><b>Sabor:</b> Taller de cocina de arepa e' huevo.<br><b>Stay:</b> Hostal Boutique con piscina social."
        },
        {
            "id": "e_ruta", "name": "Ruta Marina Eco", 
            "img": "https://blog.gimlivingspaces.com/hubfs/Muelle%20r%C3%BAstico%20de%20madera%20con%20una%20palapa%20con%20vistas%20a%20las%20aguas%20turquesas%20cristalinas%20en%20Isla%20Mujeres%2C%20playa%20de%20M%C3%A9xico.webp",
            "desc": "<b>Naturaleza:</b> Visita guiada a los manglares en canoa.<br><b>Eco:</b> Cabañas sostenibles en el Parque Tayrona.<br><b>Check:</b> Guía local certificado."
        }
    ]
    render_tour_grid(standard_data, "🎒 Línea Estándar")

# --- CONTENIDO: ATENCIÓN Y CONTACTO ---
with tab_atencion:
    st.markdown("<h2 class='section-title'>Canales de Atención Directa</h2>", unsafe_allow_html=True)
    
    # SECCIÓN DE DATOS DE CONTACTO (EXPANDIDA)
    c_info1, c_info2 = st.columns(2)
    with c_info1:
        st.markdown("""
        <div class="contact-info-card">
            <h4 style='color:#C0392B;'>📍 Oficina Central</h4>
            <p>Calle 10 #43E-21, Barrio El Poblado<br>Edificio Square, Piso 5<br>Medellín, Colombia</p>
            <h4 style='color:#C0392B;'>⏰ Horarios Operativos</h4>
            <p><b>Lunes a Viernes:</b> 8:30 AM - 6:30 PM<br><b>Sábados:</b> 9:00 AM - 2:00 PM</p>
        </div>
        """, unsafe_allow_html=True)
    
    with c_info2:
        st.markdown("""
        <div class="contact-info-card">
            <h4 style='color:#C0392B;'>📧 Canales Digitales</h4>
            <p><b>Información:</b> veronicaarangopedrozo@gmail.com<br><b>Reservas:</b> ventas@costatour.co<br><b>PQR:</b> atencion@costatour.co</p>
            <h4 style='color:#C0392B;'>📞 Líneas de Soporte</h4>
            <p><b>WhatsApp:</b> +57 324 373 1661<br><b>PBX Medellín:</b> (604) 444 00 00</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    # ENLACES EXTERNOS
    c_btn1, c_btn2 = st.columns(2)
    with c_btn1:
        st.info("### 📝 Radicar PQR\nFormalice sus solicitudes, reclamos o sugerencias a través de nuestro portal oficial.")
        st.link_button("Ir al Formulario de PQR", "https://forms.office.com/pages/responsepage.aspx?id=IefhmYRxjkmK_7KtTlPBwmzEaoV6AVxMnWIMDnUV_6JUQjFRQVBCSEg5UldERzdTVkUxU1ZTRTFTMy4u")
    with c_btn2:
        st.success("### 📚 Blog Costa-Tips\nEncuentra las mejores recomendaciones de equipaje y clima para tu viaje.")
        st.link_button("Leer el Blog del Viajero", "https://tipsdeviajeparalacostacolombiana.blogspot.com/")

    # PREGUNTAS FRECUENTES (8 PUNTOS)
    st.markdown("<br><h3 style='text-align:center;'>Preguntas Frecuentes (FAQ)</h3>", unsafe_allow_html=True)
    faq_list = [
        ("¿Con cuánta anticipación debo reservar mi tour?", "Recomendamos un mínimo de 30 días para asegurar disponibilidad hotelera, especialmente en Línea Premium."),
        ("¿Qué documentos necesito para viajar?", "Solo tu documento de identidad original. Para extranjeros, pasaporte con sello de entrada vigente."),
        ("¿Los planes incluyen seguro médico?", "Sí, todos los tours incluyen tarjeta de asistencia médica integral durante toda la estancia."),
        ("¿Puedo personalizar un tour para mi grupo?", "¡Claro! Nuestra Línea Premium ofrece diseño de itinerarios 100% personalizados según sus gustos."),
        ("¿Cuáles son los métodos de pago?", "Recibimos PSE, tarjetas de crédito nacionales e internacionales, y transferencias Bancolombia."),
        ("¿El precio base incluye los tiquetes aéreos?", "Nuestros planes se enfocan en la experiencia local. Podemos añadir los vuelos como un servicio extra."),
        ("¿Hay políticas de reembolso por cancelación?", "Sí, manejamos reembolsos parciales notificando con al menos 15 días de antelación al viaje."),
        ("¿Cómo recibo mis comprobantes de reserva?", "Se envían vía correo electrónico y WhatsApp 48 horas después de confirmar el pago total.")
    ]
    for q, a in faq_list:
        with st.expander(q):
            st.write(a)

# 5. FOOTER FINAL
st.markdown("""
    <div style='text-align:center; padding:50px; color:#aaa; font-size:13px; border-top: 1px solid #F0F0F0; margin-top:50px;'>
        © 2024 Costa-Tour Agencia de Viajes S.A.S | RNT: 98765 | Medellín, Antioquia.<br>
        <i>Inspiramos historias en cada kilómetro.</i>
    </div>
""", unsafe_allow_html=True)

# 6. BOTÓN FLOTANTE WHATSAPP (ESTÁTICO)
st.markdown("""
    <a href="https://wa.me/573243731661" class="whatsapp-float" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="22"> 
        <span>Habla con un Asesor VIP</span>
    </a>
    """, unsafe_allow_html=True)