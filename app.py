import streamlit as st
import pandas as pd

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="Costa-Tour | Agencia de Viajes", 
    layout="wide", 
    page_icon="✈️"
)

# 2. ESTILOS CSS PROFESIONALES (DISEÑO LIMPIO Y CORPORATIVO)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&family=Lora:ital,wght@0,400;1,400&display=swap');

    /* Variables de color y fuentes */
    :root {
        --primary-red: #C0392B;
        --dark-blue: #2C3E50;
        --light-gray: #F8F9FA;
    }

    .stApp { background-color: #FFFFFF !important; }
    
    html, body, [class*="st-"] {
        font-family: 'Poppins', sans-serif;
        color: #2C3E50;
        line-height: 1.6;
    }

    /* Botones de Acción */
    .stButton > button {
        background-color: #C0392B !important;
        color: white !important;
        border: none !important;
        padding: 12px 24px !important;
        border-radius: 8px !important;
        transition: all 0.3s ease;
        width: 100%;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .stButton > button:hover {
        background-color: #A93226 !important;
        box-shadow: 0 4px 15px rgba(192, 57, 43, 0.2);
        transform: translateY(-2px);
    }

    /* Hero Section Impactante */
    .hero-section {
        background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('https://images.unsplash.com/photo-1507525428034-b723cf961d3e?q=80&w=2073&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        height: 450px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        text-align: center;
        flex-direction: column;
        border-radius: 20px;
        margin-bottom: 50px;
        box-shadow: 0 15px 30px rgba(0,0,0,0.1);
    }

    .hero-title {
        color: white !important;
        font-family: 'Lora', serif;
        font-size: 68px;
        font-weight: bold;
        margin-bottom: 10px;
    }

    /* Tarjetas de Información de Nuestra Esencia */
    .essence-card {
        background: #FFFFFF;
        padding: 40px;
        border-radius: 15px;
        border: 1px solid #F0F0F0;
        box-shadow: 0 5px 20px rgba(0,0,0,0.02);
        height: 100%;
        border-top: 4px solid #C0392B;
    }

    .section-title {
        text-align: center;
        margin: 70px 0 40px 0;
        color: #1A1A1A;
        font-size: 36px;
        font-family: 'Lora', serif;
        font-weight: bold;
    }

    /* Tabla Comparativa */
    [data-testid="stTable"] {
        border-radius: 12px;
        overflow: hidden;
        border: 1px solid #EEE;
    }

    /* WhatsApp Flotante */
    .whatsapp-float {
        position: fixed;
        bottom: 35px;
        right: 35px;
        background-color: #25d366;
        color: white !important;
        padding: 16px 28px;
        border-radius: 50px;
        text-decoration: none;
        z-index: 1000;
        font-weight: 600;
        box-shadow: 0 10px 30px rgba(37, 211, 102, 0.3);
        display: flex;
        align-items: center;
        gap: 12px;
        transition: 0.3s;
    }
    
    .whatsapp-float:hover {
        transform: scale(1.05);
    }

    /* Preguntas Frecuentes */
    .stExpander {
        border: 1px solid #F0F0F0 !important;
        border-radius: 10px !important;
        margin-bottom: 12px !important;
        background-color: #FCFCFC !important;
    }

    /* Footer */
    .footer-container {
        background-color: #1A1A1A;
        color: #ECF0F1;
        padding: 80px 40px;
        margin-top: 100px;
        border-radius: 30px 30px 0 0;
    }

    .destinos-card {
        transition: 0.3s;
        border-radius: 15px;
        overflow: hidden;
        background: white;
        border: 1px solid #EEE;
    }
    .destinos-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 15px 30px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. HEADER (SIN EMOJIS, MÁS LIMPIO)
col_l, col_r = st.columns([2, 1])
with col_l:
    st.image("https://i.ibb.co/ds6F7b72/ve.png", width=200)
with col_r:
    st.markdown("""
        <div style='text-align:right; font-size:15px; margin-top:15px; color: #555;'>
            <b>Atención al Cliente:</b> +57 324 373 1661<br>
            <b>Sede Principal:</b> Medellín, El Poblado
        </div>
    """, unsafe_allow_html=True)

# 4. NAVEGACIÓN PRINCIPAL
t_esencia, t_catalogo, t_atencion = st.tabs(["NUESTRA ESENCIA", "CATÁLOGO DE TOURS", "ATENCIÓN"])

# --- CONTENIDO: NUESTRA ESENCIA ---
with t_esencia:
    st.markdown("""
        <div class="hero-section">
            <h1 class="hero-title">Costa-Tour</h1>
            <p style='font-size: 24px; font-weight: 300; letter-spacing: 1px;'>Excelencia Turística en el Corazón de Colombia</p>
        </div>
        """, unsafe_allow_html=True)

    # BLOQUE DE FILOSOFÍA Y VALORES (TEXTO LARGO Y SUSTANCIOSO)
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        st.markdown("<div class='essence-card'>", unsafe_allow_html=True)
        st.subheader("Nuestra Filosofía")
        st.write("""
        En Costa-Tour, entendemos el viaje como una herramienta de transformación personal. No nos limitamos a la logística; 
        buscamos la armonía entre el viajero y el entorno. Creemos firmemente en el turismo responsable, aquel que 
        beneficia a las comunidades locales y preserva la integridad de nuestros paisajes naturales. 
        Nuestra pasión es mostrar una Colombia auténtica, lejos de los clichés, enfocándonos en la calidad humana 
        y la seguridad operativa. Cada itinerario es revisado minuciosamente para que su única preocupación sea 
        disfrutar del momento.
        """)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col_f2:
        st.markdown("<div class='essence-card'>", unsafe_allow_html=True)
        st.subheader("¿Por qué elegirnos?")
        st.write("""
        - **Especialistas en la Costa:** Conocemos cada rincón del Caribe y el Pacífico colombiano de primera mano.
        - **Compromiso con la Calidad:** Seleccionamos aliados estratégicos bajo estándares internacionales de servicio.
        - **Atención Personalizada:** Usted no es un número de reserva; es nuestro invitado de honor.
        - **Sostenibilidad:** Trabajamos activamente en reducir la huella de carbono de nuestras operaciones.
        - **Seguridad Integral:** Contamos con protocolos de emergencia y seguros de cobertura total en todos los planes.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

    # GALERÍA DE DESTINOS DETALLADA
    st.markdown("<h2 class='section-title'>Destinos que te esperan</h2>", unsafe_allow_html=True)
    d_c1, d_c2, d_c3 = st.columns(3)
    destinos = [
        {
            "nombre": "Archipiélago del Rosario", 
            "img": "https://images.unsplash.com/photo-1589394815804-964ed962eb33?q=80&w=600",
            "desc": "Aguas cristalinas y arrecifes de coral. El destino perfecto para el descanso y el buceo de alta categoría."
        },
        {
            "nombre": "Selva de Nuquí", 
            "img": "https://images.unsplash.com/photo-1590523741831-ab7e8b8f9c7f?q=80&w=600",
            "desc": "Donde la selva toca el mar. Ideal para el avistamiento de ballenas jorobadas y el ecoturismo místico."
        },
        {
            "nombre": "Santuario Tayrona", 
            "img": "https://images.unsplash.com/photo-1596422846543-b5c64863e939?q=80&w=600",
            "desc": "Cunas de la civilización indígena. Un recorrido entre montañas de la Sierra Nevada y playas vírgenes."
        }
    ]
    for i, d in enumerate(destinos):
        with [d_c1, d_c2, d_c3][i]:
            st.markdown(f"""
                <div class="destinos-card">
                    <img src="{d['img']}" style="width:100%; height:250px; object-fit:cover;">
                    <div style="padding:20px;">
                        <h4 style="margin:0;">{d['nombre']}</h4>
                        <p style="font-size:14px; color:#666; margin-top:10px;">{d['desc']}</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)

# --- CONTENIDO: CATÁLOGO DE TOURS ---
with t_catalogo:
    st.markdown("<h2 class='section-title'>Líneas de Servicio</h2>", unsafe_allow_html=True)
    
    # TABLA COMPARATIVA TÉCNICA
    df_comp = pd.DataFrame({
        "Atributo del Servicio": ["Alojamiento", "Gastronomía", "Transporte", "Asistencia", "Exclusividad", "Flexibilidad"],
        "Línea Estándar": [
            "Hoteles 3* / Posadas Rurales", 
            "Desayuno Típico Incluido", 
            "Transporte Terrestre Compartido", 
            "Soporte Digital 24/7", 
            "Grupos de hasta 15 personas",
            "Itinerario Fijo"
        ],
        "Línea Premium": [
            "Resorts 5* / Hoteles Boutique", 
            "Plan Gastronómico Gourmet Completo", 
            "Vehículos Privados de Lujo", 
            "Concierge Personalizado In-Situ", 
            "Privacidad Máxima (Solo su grupo)",
            "Personalización de Horarios"
        ]
    })
    st.table(df_comp)

    st.markdown("<br><hr style='border:0.5px solid #EEE;'><br>", unsafe_allow_html=True)

    # SECCIÓN PREMIUM DETALLADA
    st.markdown("<h2 style='text-align:center;'>Línea Premium: Exclusividad Elevada</h2>", unsafe_allow_html=True)
    st.write("<p style='text-align:center;'>Diseñado para quienes el tiempo y el confort son el mayor lujo.</p>", unsafe_allow_html=True)
    
    p_cols = st.columns(4)
    premium_tours = [
        {
            "id": "p1", "name": "Pacífico Vivo VIP", 
            "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRIeSN9RSQsxw_n-gbbbfOOsjBrcClZngt3DA&s",
            "desc": "<b>Experiencia Nuquí:</b> Estancia en Eco-Lodge de lujo con spa privado. Incluye vuelos charters privados, expediciones exclusivas de avistamiento y chef de comida fusión del mar solo para usted."
        },
        {
            "id": "p2", "name": "Pacífico Místico Plus", 
            "img": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2c/b0/c2/4f/private-beach-hotels.jpg?w=1200&h=-1&s=1",
            "desc": "<b>Bienestar Total:</b> Retiro en Bahía Solano. Yoga frente al mar, terapias de barro volcánico y caminatas por senderos privados. Alojamiento en bungalows de diseño arquitectónico sostenible."
        },
        {
            "id": "p3", "name": "Sol Caribe Luxury", 
            "img": "https://cdn2.paraty.es/landmar/images/865ffac6866fcba",
            "desc": "<b>Islas VIP:</b> Navegación en yate privado por el archipiélago. Almuerzo en isla privada. Suite nupcial o familiar en resort de cadena internacional con servicio de mayordomía."
        },
        {
            "id": "p4", "name": "Caribe Mágico Pro", 
            "img": "https://media-cdn.tripadvisor.com/media/photo-s/2f/59/25/75/caption.jpg",
            "desc": "<b>Historia y Lujo:</b> Cartagena desde otra perspectiva. Cena en baluartes históricos, tour privado por las murallas y estancia en casa colonial restaurada con piscina privada y personal de servicio."
        }
    ]

    for i, tour in enumerate(premium_tours):
        with p_cols[i]:
            st.image(tour['img'], use_container_width=True)
            st.markdown(f"<p style='text-align:center; font-weight:600; font-size:18px;'>{tour['name']}</p>", unsafe_allow_html=True)
            
            state_key = f"st_{tour['id']}"
            if state_key not in st.session_state: st.session_state[state_key] = False
            
            label = "Cerrar Detalles" if st.session_state[state_key] else "Ver Detalles Premium"
            if st.button(label, key=tour['id']):
                st.session_state[state_key] = not st.session_state[state_key]
                st.rerun()
            
            if st.session_state[state_key]:
                st.markdown(f"<div style='background:#F9F9F9; padding:15px; border-left:4px solid #C0392B; font-size:14px;'>{tour['desc']}</div>", unsafe_allow_html=True)

# --- CONTENIDO: ATENCIÓN ---
with t_atencion:
    st.markdown("<h2 class='section-title'>Atención al Viajero</h2>", unsafe_allow_html=True)
    
    # CANALES DE CONTACTO (REORGANIZADO)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        <div style='background:white; padding:30px; border:1px solid #EEE; border-radius:15px; text-align:center;'>
            <h4 style='color:#C0392B;'>Sede Administrativa</h4>
            <p>Calle 10 #43E-21, El Poblado<br>Edificio Corporate Medellín<br>Antioquia, Colombia</p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div style='background:white; padding:30px; border:1px solid #EEE; border-radius:15px; text-align:center;'>
            <h4 style='color:#C0392B;'>Correos Directos</h4>
            <p><b>General:</b> veronicaarangopedrozo@gmail.com<br><b>Ventas:</b> reservas@costatour.com</p>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div style='background:white; padding:30px; border:1px solid #EEE; border-radius:15px; text-align:center;'>
            <h4 style='color:#C0392B;'>Línea de Emergencia</h4>
            <p><b>WhatsApp:</b> +57 324 373 1661<br>Disponibilidad 24 horas para pasajeros en tránsito.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # BOTONES DE ACCIÓN (SOLO PORTAL Y BLOG)
    col_b1, col_b2 = st.columns(2)
    with col_b1:
        st.info("### Gestión de Solicitudes\nUtilice nuestro portal oficial para radicar cualquier requerimiento, consulta de reserva o trámite administrativo.")
        st.link_button("Ir al Portal de Servicio", "https://forms.office.com/pages/responsepage.aspx?id=IefhmYRxjkmK_7KtTlPBwmzEaoV6AVxMnWIMDnUV_6JUQjFRQVBCSEg5UldERzdTVkUxU1ZTRTFTMy4u")
    with col_b2:
        st.success("### Tips del Viajero\n¿Qué llevar a la selva? ¿Cuál es la mejor época para el Caribe? Encuentre todas las respuestas en nuestro blog.")
        st.link_button("Explorar el Blog de Tips", "https://tipsdeviajeparalacostacolombiana.blogspot.com/")

    # PREGUNTAS FRECUENTES (8 PREGUNTAS LIMPIAS)
    st.markdown("<h3 style='text-align:center; margin-top:50px;'>Preguntas Frecuentes</h3>", unsafe_allow_html=True)
    faqs = [
        ("¿Con cuánta anticipación debo reservar mi tour?", "Para la Línea Estándar, recomendamos 15 días. Para la Línea Premium, al menos 30 a 45 días debido a la alta demanda de hoteles boutique."),
        ("¿Qué documentos son obligatorios para el viaje?", "Ciudadanos colombianos requieren cédula original vigente. Extranjeros deben portar pasaporte con el sello de ingreso al país."),
        ("¿La asistencia médica está incluida en el precio?", "Sí, todos nuestros planes incluyen un seguro de viaje con cobertura nacional para accidentes y emergencias médicas."),
        ("¿Puedo solicitar cambios en el itinerario de un tour Premium?", "Totalmente. Los planes Premium son flexibles. Usted puede coordinar con su concierge cambios de horarios o actividades adicionales."),
        ("¿Cuáles son los métodos de pago habilitados?", "Aceptamos pagos electrónicos vía PSE, transferencias directas Bancolombia/Nequi y tarjetas de crédito internacionales."),
        ("¿Los vuelos nacionales están dentro del paquete?", "Por defecto, el precio cubre la experiencia en destino. No obstante, ofrecemos el servicio de gestión de tiquetes aéreos como opcional."),
        ("¿Cuál es la política en caso de cancelación por fuerza mayor?", "Contamos con una política flexible que permite reprogramar o solicitar reembolsos parciales según la antelación de la cancelación."),
        ("¿Cuándo recibiré la confirmación final de mi reserva?", "Recibirá sus vouchers digitales y el itinerario minuto a minuto a través de correo electrónico y WhatsApp 48 horas antes de su salida.")
    ]
    for q, a in faqs:
        with st.expander(q):
            st.write(a)

# 5. FOOTER CORPORATIVO
st.markdown("""
    <div class="footer-container">
        <div style="display: flex; justify-content: space-around; flex-wrap: wrap; gap: 40px;">
            <div style="max-width: 350px;">
                <h3 style="color: #C0392B;">Costa-Tour</h3>
                <p>Agencia Líder en Experiencias de Costa en Colombia. Registro Nacional de Turismo vigente. Comprometidos con el desarrollo regional.</p>
            </div>
            <div>
                <h4>Enlaces de Interés</h4>
                <ul style="list-style: none; padding: 0;">
                    <li>Política de Privacidad</li>
                    <li>Términos y Condiciones</li>
                    <li>Sostenibilidad Ambiental</li>
                </ul>
            </div>
            <div>
                <h4>Contacto Directo</h4>
                <p>📍 Calle 10 #43E-21, Medellín<br>📞 +57 324 373 1661<br>✉️ info@costatour.com</p>
            </div>
        </div>
        <hr style="border-color: #333; margin: 40px 0;">
        <p style="text-align: center; font-size: 13px; opacity: 0.6;">© 2024 Costa-Tour Agencia de Viajes SAS. Todos los derechos reservados.</p>
    </div>
    """, unsafe_allow_html=True)

# 6. WHATSAPP FLOTANTE
st.markdown("""
    <a href="https://wa.me/573243731661" class="whatsapp-float" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="22"> 
        <span>Asesoría en Línea</span>
    </a>
    """, unsafe_allow_html=True)