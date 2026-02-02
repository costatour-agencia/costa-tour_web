import streamlit as st
import pandas as pd

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="Costa-Tour | Agencia de Viajes", 
    layout="wide", 
    page_icon="✈️"
)

# 2. ESTILOS CSS PROFESIONALES (DISEÑO LIMPIO, SIN APIÑAMIENTOS)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&family=Lora:ital,wght@0,400;1,400&display=swap');

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
        width: 100%;
        font-weight: 600;
        text-transform: uppercase;
    }
    
    .stButton > button:hover {
        background-color: #A93226 !important;
        box-shadow: 0 4px 15px rgba(192, 57, 43, 0.2);
    }

    /* Hero Section */
    .hero-section {
        background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('https://images.unsplash.com/photo-1506929113675-b9299d39bb14?q=80&w=2070&auto=format&fit=crop');
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
        margin-bottom: 50px;
    }

    .hero-title {
        color: white !important;
        font-family: 'Lora', serif;
        font-size: 56px;
        font-weight: bold;
    }

    .essence-card {
        background: #FDFDFD;
        padding: 35px;
        border-radius: 15px;
        border: 1px solid #EEE;
        height: 100%;
        border-top: 5px solid #C0392B;
    }

    .section-title {
        text-align: center;
        margin: 60px 0 40px 0;
        color: #1A1A1A;
        font-size: 32px;
        font-family: 'Lora', serif;
        font-weight: bold;
    }

    /* Tabla Profesional con Espaciado */
    .styled-table {
        width: 100%;
        border-collapse: collapse;
        margin: 30px 0;
        font-size: 16px;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
    }
    .styled-table thead tr {
        background-color: #C0392B;
        color: #ffffff;
        text-align: left;
    }
    .styled-table th, .styled-table td {
        padding: 18px 25px;
        border-bottom: 1px solid #EEE;
    }
    .styled-table tbody tr:nth-of-type(even) {
        background-color: #F9F9F9;
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
    }

    /* FAQ - Menos apiñado, más aire */
    .stExpander {
        border: 1px solid #EEE !important;
        border-radius: 12px !important;
        margin-bottom: 25px !important;
        background-color: #FFFFFF !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.02);
    }

    .footer-container {
        background-color: #1A1A1A;
        color: #ECF0F1;
        padding: 60px 40px;
        margin-top: 100px;
        border-radius: 30px 30px 0 0;
    }

    .destinos-card {
        border-radius: 15px;
        overflow: hidden;
        background: white;
        border: 1px solid #EEE;
        margin-bottom: 25px;
        transition: 0.3s;
    }
    .destinos-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. HEADER (CORREO ÚNICO Y LOGO)
col_l, col_r = st.columns([2, 1])
with col_l:
    st.image("https://i.ibb.co/ds6F7b72/ve.png", width=200)
with col_r:
    st.markdown("""
        <div style='text-align:right; font-size:14px; margin-top:20px; color: #444;'>
            <b>Email Corporativo:</b> veronicaarangopedrozo@gmail.com<br>
            <b>Atención Directa:</b> +57 324 373 1661<br>
            <b>Sede Medellín:</b> El Poblado, Edificio Corporate
        </div>
    """, unsafe_allow_html=True)

# 4. NAVEGACIÓN
t_esencia, t_catalogo, t_atencion = st.tabs(["NUESTRA ESENCIA", "CATÁLOGO DE TOURS", "ATENCIÓN AL CLIENTE"])

# --- CONTENIDO: NUESTRA ESENCIA (TEXTO EN ESPAÑOL) ---
with t_esencia:
    st.markdown("""
        <div class="hero-section">
            <h1 class="hero-title">Costa-Tour</h1>
            <p style='font-size: 22px; font-weight: 300;'>Excelencia en experiencias turísticas por Colombia</p>
        </div>
        """, unsafe_allow_html=True)

    col_f1, col_f2 = st.columns(2)
    with col_f1:
        st.markdown("<div class='essence-card'>", unsafe_allow_html=True)
        st.subheader("Filosofía Institucional")
        st.write("""
        En Costa-Tour, concebimos el viaje como una oportunidad de conexión profunda con el entorno. 
        Nuestra labor va más allá de la logística; diseñamos itinerarios que respetan la integridad cultural 
        y natural de cada destino. Buscamos que cada pasajero viva una Colombia auténtica, segura y 
        memorable, respaldada por un equipo profesional comprometido con la calidad superior.
        """)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col_f2:
        st.markdown("<div class='essence-card'>", unsafe_allow_html=True)
        st.subheader("Diferenciales de Marca")
        st.write("""
        - **Conocimiento Local:** Expertos nativos en rutas del Caribe y el Pacífico.
        - **Selección Rigurosa:** Solo trabajamos con aliados que cumplen estándares internacionales.
        - **Atención Humana:** Priorizamos la cercanía y solución inmediata a sus necesidades.
        - **Sostenibilidad:** Programas de reducción de impacto ambiental en cada ruta.
        - **Seguridad Garantizada:** Seguros de cobertura total en todos nuestros planes.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<h2 class='section-title'>Destinos Destacados</h2>", unsafe_allow_html=True)
    d_c1, d_c2, d_c3 = st.columns(3)
    
    # Imágenes seleccionadas para que no carguen en blanco
    destinos_imgs = [
        {"nombre": "Archipiélago del Rosario", "img": "https://images.unsplash.com/photo-1590523741831-ab7e8b8f9c7f?q=80&w=600", "desc": "Paraíso de aguas turquesas y arrecifes."},
        {"nombre": "Selva y Mar en Nuquí", "img": "https://images.unsplash.com/photo-1544735030-c36173004944?q=80&w=600", "desc": "El encuentro místico entre la jungla y el Pacífico."},
        {"nombre": "Sierra Nevada y Tayrona", "img": "https://images.unsplash.com/photo-1596422846543-b5c64863e939?q=80&w=600", "desc": "Naturaleza virgen y herencia ancestral indígena."}
    ]
    
    for i, d in enumerate(destinos_imgs):
        with [d_c1, d_c2, d_c3][i]:
            st.markdown(f"""
                <div class="destinos-card">
                    <img src="{d['img']}" style="width:100%; height:250px; object-fit:cover;">
                    <div style="padding:20px; text-align:center;">
                        <h4 style="margin:0; color:#2C3E50;">{d['nombre']}</h4>
                        <p style="font-size:14px; color:#666; margin-top:10px;">{d['desc']}</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)

# --- CONTENIDO: CATÁLOGO DE TOURS (DOS LÍNEAS RESTAURADAS) ---
with t_catalogo:
    st.markdown("<h2 class='section-title'>Comparativa de Servicios</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    <table class="styled-table">
        <thead>
            <tr>
                <th>Categoría</th>
                <th>Línea Estándar</th>
                <th>Línea Premium</th>
            </tr>
        </thead>
        <tbody>
            <tr><td><b>Alojamiento</b></td><td>Hoteles 3* / Posadas con encanto</td><td>Resorts 5* / Hoteles Boutique</td></tr>
            <tr><td><b>Gastronomía</b></td><td>Desayunos locales incluidos</td><td>Plan de alimentación Gourmet</td></tr>
            <tr><td><b>Traslados</b></td><td>Transporte moderno compartido</td><td>Vehículos de lujo privados</td></tr>
            <tr><td><b>Atención</b></td><td>Asistencia vía chat 24/7</td><td>Concierge personal en destino</td></tr>
            <tr><td><b>Exclusividad</b></td><td>Grupos optimizados</td><td>Experiencia 100% privada</td></tr>
        </tbody>
    </table>
    """, unsafe_allow_html=True)

    # --- LÍNEA ESTÁNDAR ---
    st.markdown("<h3 style='color:#C0392B; margin-top:40px;'>Línea Estándar: Calidad y Confort</h3>", unsafe_allow_html=True)
    e_cols = st.columns(2)
    with e_cols[0]:
        st.image("https://images.unsplash.com/photo-1548574505-5e239809ee19?q=80&w=500")
        st.markdown("**Tour Caribe Alegre:** Cartagena e Islas del Rosario compartido. Ideal para parejas y amigos.")
    with e_cols[1]:
        st.image("https://images.unsplash.com/photo-1518732714860-b62714ce0c59?q=80&w=500")
        st.markdown("**Aventura Pacífico:** Nuquí en eco-posada. Avistamiento de ballenas y senderos naturales.")

    st.markdown("<br><hr style='opacity:0.2;'><br>", unsafe_allow_html=True)

    # --- LÍNEA PREMIUM ---
    st.markdown("<h3 style='color:#C0392B;'>Línea Premium: Exclusividad Elevada</h3>", unsafe_allow_html=True)
    p_cols = st.columns(4)
    premium_tours = [
        {"id": "p1", "name": "Pacífico Vivo VIP", "img": "https://images.unsplash.com/photo-1499793983690-e29da59ef1c2?q=80&w=400", "desc": "Eco-Lodge de lujo, vuelos privados y chef personal disponible."},
        {"id": "p2", "name": "Pacífico Místico Plus", "img": "https://images.unsplash.com/photo-1540541338287-41700207dee6?q=80&w=400", "desc": "Bahía Solano boutique, spa frente al mar y retiro de yoga privado."},
        {"id": "p3", "name": "Sol Caribe Luxury", "img": "https://images.unsplash.com/photo-1544124499-58912cbddaad?q=80&w=400", "desc": "Yate privado, resort VIP en islas y servicio de mayordomía."},
        {"id": "p4", "name": "Caribe Mágico Pro", "img": "https://images.unsplash.com/photo-1533105079780-92b9be482077?q=80&w=400", "desc": "Casa colonial exclusiva en el Centro Histórico con piscina privada."}
    ]

    for i, tour in enumerate(premium_tours):
        with p_cols[i]:
            st.image(tour['img'], use_container_width=True)
            st.markdown(f"<p style='text-align:center; font-weight:600; margin-bottom:5px;'>{tour['name']}</p>", unsafe_allow_html=True)
            if st.button("Detalles Premium", key=tour['id']):
                st.info(tour['desc'])

# --- CONTENIDO: ATENCIÓN AL CLIENTE ---
with t_atencion:
    st.markdown("<h2 class='section-title'>Canales de Atención</h2>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("<div class='essence-card' style='text-align:center;'><h4>Oficina Central</h4><p>Calle 10 #43E-21, El Poblado<br>Medellín, Antioquia</p></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='essence-card' style='text-align:center;'><h4>Correo Único</h4><p>veronicaarangopedrozo<br>@gmail.com</p></div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='essence-card' style='text-align:center;'><h4>Línea 24 Horas</h4><p>WhatsApp Corporativo:<br>+57 324 373 1661</p></div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    # Botones con enlaces reales e inventados útiles
    col_links1, col_links2 = st.columns(2)
    with col_links1:
        st.markdown("##### Gestión Administrativa")
        st.link_button("Portal de Peticiones y Reclamos (PQR)", "https://forms.office.com/pages/responsepage.aspx?id=IefhmYRxjkmK_7KtTlPBwmzEaoV6AVxMnWIMDnUV_6JUQjFRQVBCSEg5UldERzdTVkUxU1ZTRTFTMy4u")
    with col_links2:
        st.markdown("##### Guía del Viajero")
        st.link_button("Blog de Tips y Recomendaciones", "https://tipsdeviajeparalacostacolombiana.blogspot.com/")

    st.markdown("<h3 style='text-align:center; margin-top:50px;'>Preguntas Frecuentes (FAQ)</h3>", unsafe_allow_html=True)
    faqs = [
        ("¿Con cuánta anticipación debo reservar?", "Para la Línea Estándar recomendamos 15 días. Para la Línea Premium, al menos 30 días debido a la exclusividad de los alojamientos."),
        ("¿Qué documentos son requeridos para viajar?", "Es obligatorio portar el documento de identidad original (Cédula o Pasaporte). Para menores, registro civil original."),
        ("¿Los paquetes incluyen asistencia médica?", "Sí, todos nuestros servicios incluyen un seguro de viaje con cobertura total ante emergencias y accidentes nacionales."),
        ("¿Puedo personalizar un itinerario Premium?", "Totalmente. Los servicios Premium permiten ajustes de horarios, rutas y actividades según la preferencia del cliente."),
        ("¿Cuáles son los métodos de pago aceptados?", "Recibimos pagos vía PSE, transferencias directas a Bancolombia/Nequi y tarjetas de crédito internacionales."),
        ("¿Están incluidos los tiquetes aéreos?", "Nuestros planes base inician en destino. No obstante, ofrecemos el servicio de compra de vuelos como un opcional adicional."),
        ("¿Cuál es la política en caso de cancelación?", "Manejamos una política flexible que permite reprogramar sin costo avisando con 10 días de antelación según términos del hotel."),
        ("¿Cómo recibo mis vouchers de viaje?", "Se envían de forma digital vía Correo y WhatsApp 48 horas antes de iniciar la experiencia con el itinerario detallado.")
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
                <p>Líderes en turismo de experiencia en las costas colombianas. RNT vigente y compromiso con la sostenibilidad ambiental.</p>
            </div>
            <div>
                <h4>Enlaces de Interés</h4>
                <p><a href="https://www.colombia.travel" style="color:white; text-decoration:none;">• Turismo oficial Colombia</a><br>
                <a href="https://www.parquesnacionales.gov.co" style="color:white; text-decoration:none;">• Parques Nacionales</a><br>
                <a href="https://www.aerocivil.gov.co" style="color:white; text-decoration:none;">• Estado de vuelos</a></p>
            </div>
            <div>
                <h4>Contacto Directo</h4>
                <p>📍 Medellín, El Poblado<br>📞 +57 324 373 1661<br>✉️ veronicaarangopedrozo@gmail.com</p>
            </div>
        </div>
        <hr style="border-color: #333; margin: 40px 0;">
        <p style="text-align: center; font-size: 12px; opacity: 0.5;">© 2024 Costa-Tour Agencia de Viajes SAS. Todos los derechos reservados.</p>
    </div>
    """, unsafe_allow_html=True)

# 6. WHATSAPP FLOTANTE
st.markdown("""
    <a href="https://wa.me/573243731661" class="whatsapp-float" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="22"> 
        <span>Asesoría Directa</span>
    </a>
    """, unsafe_allow_html=True)