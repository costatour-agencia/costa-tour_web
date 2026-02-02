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
        background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('https://images.unsplash.com/photo-1544124499-58912cbddaad?q=80&w=2070&auto=format&fit=crop');
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
    }

    .hero-title {
        color: white !important;
        font-family: 'Lora', serif;
        font-size: 68px;
        font-weight: bold;
    }

    .essence-card {
        background: #FFFFFF;
        padding: 40px;
        border-radius: 15px;
        border: 1px solid #F0F0F0;
        height: 100%;
        border-top: 4px solid #C0392B;
    }

    .section-title {
        text-align: center;
        margin: 60px 0 40px 0;
        color: #1A1A1A;
        font-size: 36px;
        font-family: 'Lora', serif;
        font-weight: bold;
    }

    /* Tabla Profesional */
    .styled-table {
        width: 100%;
        border-collapse: collapse;
        margin: 25px 0;
        font-size: 0.9em;
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 0 20px rgba(0, 0, 0, 0.05);
    }
    .styled-table thead tr {
        background-color: #2C3E50;
        color: #ffffff;
        text-align: left;
    }
    .styled-table th, .styled-table td {
        padding: 15px 20px;
        border-bottom: 1px solid #dddddd;
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

    /* FAQ - Menos apiñado */
    .stExpander {
        border: 1px solid #EEE !important;
        border-radius: 12px !important;
        margin-bottom: 20px !important;
        background-color: #F9F9F9 !important;
        padding: 5px !important;
    }

    .footer-container {
        background-color: #1A1A1A;
        color: #ECF0F1;
        padding: 80px 40px;
        margin-top: 100px;
        border-radius: 30px 30px 0 0;
    }

    .destinos-card {
        border-radius: 15px;
        overflow: hidden;
        background: white;
        border: 1px solid #EEE;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. HEADER (CORREO ÚNICO)
col_l, col_r = st.columns([2, 1])
with col_l:
    # Usando el logo proporcionado
    st.image("https://i.ibb.co/ds6F7b72/ve.png", width=200)
with col_r:
    st.markdown("""
        <div style='text-align:right; font-size:15px; margin-top:15px; color: #555;'>
            <b>Email:</b> veronicaarangopedrozo@gmail.com<br>
            <b>Contacto:</b> +57 324 373 1661<br>
            <b>Medellín, El Poblado</b>
        </div>
    """, unsafe_allow_html=True)

# 4. NAVEGACIÓN
t_esencia, t_catalogo, t_atencion = st.tabs(["NUESTRA ESENCIA", "CATÁLOGO DE TOURS", "ATENCIÓN"])

# --- CONTENIDO: NUESTRA ESENCIA ---
with t_esencia:
    st.markdown("""
        <div class="hero-section">
            <h1 class="hero-title">Costa-Tour</h1>
            <p style='font-size: 24px;'>Tapeykue porãite Colombia yrembe'ýpe</p>
        </div>
        """, unsafe_allow_html=True)

    col_f1, col_f2 = st.columns(2)
    with col_f1:
        st.markdown("<div class='essence-card'>", unsafe_allow_html=True)
        st.subheader("Ore rembiapo rape")
        st.write("""
        Costa-Tour-pe rohecha tapeykue ñemoambue teéicha. Ndaha'éi logística añónte; roheka jaiko porãite 
        tapicha ha tekoha ndive. Roguerovia upéva ha'eha pe tape añetete omoĩ porãva ñande rekoha ha 
        umi táva oĩvape upépe. Ore rembipota ha'e rohechauka Colombia tee, jahecha hag̃ua tapichakuéra 
        reko porã ha py'aguapy.
        """)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col_f2:
        st.markdown("<div class='essence-card'>", unsafe_allow_html=True)
        st.subheader("Mba'érepa orembo'e")
        st.write("""
        - **Especialistas yrembe'ýpe:** Roikuaa porãite Caribe ha Pacífico colombiano.
        - **Tembiapo porã:** Roiporavo porã umi oipytyvõtava oréve roguereko hag̃ua servicio premium.
        - **Tapicha reko:** Nde ndaha'éi número de reserva; nde ha'e ore invitado de honor.
        - **Tekoha ñangareko:** Romba'apo ani hag̃ua ore rembiapo ombyai ñande rekoha.
        - **Py'aguapy:** Roguereko protocolo pytyvõrã opaite plan-pe.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<h2 class='section-title'>Destinos que te esperan</h2>", unsafe_allow_html=True)
    d_c1, d_c2, d_c3 = st.columns(3)
    
    # Imagenes con enlaces reales para evitar que salgan en blanco
    destinos_imgs = [
        {"nombre": "Archipiélago del Rosario", "img": "https://images.unsplash.com/photo-1544735030-c36173004944?q=80&w=600", "desc": "Y sakã ha coral-ita porãite."},
        {"nombre": "Nuquí - Pacífico", "img": "https://images.unsplash.com/photo-1596422846543-b5c64863e939?q=80&w=600", "desc": "Ka'aguy ha yguasu oñuguaitĩhápe."},
        {"nombre": "Parque Tayrona", "img": "https://images.unsplash.com/photo-1589394815804-964ed962eb33?q=80&w=600", "desc": "Yvyra ha yrembe'y porãite."}
    ]
    
    for i, d in enumerate(destinos_imgs):
        with [d_c1, d_c2, d_c3][i]:
            st.markdown(f"""
                <div class="destinos-card">
                    <img src="{d['img']}" style="width:100%; height:250px; object-fit:cover;">
                    <div style="padding:20px; text-align:center;">
                        <h4 style="margin:0;">{d['nombre']}</h4>
                        <p style="font-size:14px; color:#666;">{d['desc']}</p>
                    </div>
                </div>
            """, unsafe_allow_html=True)

# --- CONTENIDO: CATÁLOGO DE TOURS (MOKÕI LÍNEA) ---
with t_catalogo:
    st.markdown("<h2 class='section-title'>Líneas de Servicio</h2>", unsafe_allow_html=True)
    
    # Tabla mejorada visualmente
    st.markdown("""
    <table class="styled-table">
        <thead>
            <tr>
                <th>Atributo</th>
                <th>Línea Estándar</th>
                <th>Línea Premium</th>
            </tr>
        </thead>
        <tbody>
            <tr><td>Alojamiento</td><td>Hotel 3* / Posada</td><td>Resort 5* / Boutique</td></tr>
            <tr><td>Gastronomía</td><td>Desayuno Típico</td><td>Gourmet Completo</td></tr>
            <tr><td>Transporte</td><td>Compartido Moderno</td><td>Vehículo Lujo Privado</td></tr>
            <tr><td>Asistencia</td><td>Soporte Digital</td><td>Concierge Personalizado</td></tr>
            <tr><td>Exclusividad</td><td>Grupos Dinámicos</td><td>Privacidad Total</td></tr>
        </tbody>
    </table>
    """, unsafe_allow_html=True)

    # LÍNEA ESTÁNDAR
    st.markdown("### Línea Estándar: Calidad y Confort")
    e_cols = st.columns(2)
    with e_cols[0]:
        st.image("https://images.unsplash.com/photo-1533105079780-92b9be482077?q=80&w=500")
        st.write("**Tour Caribe Alegre:** Cartagena ha Islas del Rosario compartido. Confort ha diversión.")
    with e_cols[1]:
        st.image("https://images.unsplash.com/photo-1518732714860-b62714ce0c59?q=80&w=500")
        st.write("**Aventura Pacífico:** Nuquí eco-posada. Avistamiento de ballenas ha senderismo.")

    st.markdown("<br><hr><br>", unsafe_allow_html=True)

    # LÍNEA PREMIUM
    st.markdown("### Línea Premium: Exclusividad Elevada")
    p_cols = st.columns(4)
    premium_tours = [
        {"id": "p1", "name": "Pacífico Vivo VIP", "img": "https://images.unsplash.com/photo-1499793983690-e29da59ef1c2?q=80&w=500", "desc": "Eco-Lodge lujo, vuelos privados ha chef personal."},
        {"id": "p2", "name": "Pacífico Místico Plus", "img": "https://images.unsplash.com/photo-1540541338287-41700207dee6?q=80&w=500", "desc": "Bahía Solano boutique, spa ha retiro yoga."},
        {"id": "p3", "name": "Sol Caribe Luxury", "img": "https://images.unsplash.com/photo-1544124499-58912cbddaad?q=80&w=500", "desc": "Yate privado, resort VIP ha mayordomo."},
        {"id": "p4", "name": "Caribe Mágico Pro", "img": "https://images.unsplash.com/photo-1548574505-5e239809ee19?q=80&w=500", "desc": "Casa colonial exclusiva, piscina ha cena privada."}
    ]

    for i, tour in enumerate(premium_tours):
        with p_cols[i]:
            st.image(tour['img'], use_container_width=True)
            st.markdown(f"<p style='text-align:center; font-weight:600;'>{tour['name']}</p>", unsafe_allow_html=True)
            if st.button("Ver Detalles Premium", key=tour['id']):
                st.info(tour['desc'])

# --- CONTENIDO: ATENCIÓN ---
with t_atencion:
    st.markdown("<h2 class='section-title'>Atención al Viajero</h2>", unsafe_allow_html=True)
    
    # CANALES
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("<div class='essence-card' style='text-align:center;'><h4>Ubicación</h4><p>Calle 10 #43E-21, Medellín<br>El Poblado</p></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='essence-card' style='text-align:center;'><h4>Email Único</h4><p>veronicaarangopedrozo<br>@gmail.com</p></div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='essence-card' style='text-align:center;'><h4>Línea 24h</h4><p>WhatsApp:<br>+57 324 373 1661</p></div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    col_links1, col_links2 = st.columns(2)
    with col_links1:
        st.link_button("Ir al Portal de Servicio (PQR)", "https://forms.office.com/pages/responsepage.aspx?id=IefhmYRxjkmK_7KtTlPBwmzEaoV6AVxMnWIMDnUV_6JUQjFRQVBCSEg5UldERzdTVkUxU1ZTRTFTMy4u")
    with col_links2:
        st.link_button("Explorar Blog de Tips", "https://tipsdeviajeparalacostacolombiana.blogspot.com/")

    st.markdown("<h3 style='text-align:center; margin-top:40px;'>Porandu Jepi (FAQ)</h3>", unsafe_allow_html=True)
    faqs = [
        ("¿Mba'eichaitépa ambyaty va'erã che tour?", "Línea Estándar: 15 ára mboyve. Línea Premium: 30-45 ára mboyve."),
        ("¿Mba'e kuatia amoneĩ va'erã?", "Cédula original térã pasaporte ojeike hag̃ua Colombia-pe."),
        ("¿Oguereko seguro médico?", "Héẽ, opaite plan oguereko seguro asistencia médica nacional."),
        ("¿Ikatúpa amopyahu che itinerario Premium?", "Héẽ, Línea Premium-pe ikatu amoambue ojejapoháicha nde reipotaháicha."),
        ("¿Mba'éichapa ikatu apagá?", "PSE, transferencia Bancolombia/Nequi térã tarjeta de crédito."),
        ("¿Oguerekópa avión tiquete?", "Ndaha'éi, pero ikatu roguerohory ojehepyme'ẽvo adicional."),
        ("¿Mba'éichapa cancelación política?", "Roguereko política flexible reprogramación-rã."),
        ("¿Araka'épa aguerohory che voucher?", "WhatsApp térã email rupive 48h viaje mboyve.")
    ]
    for q, a in faqs:
        with st.expander(q):
            st.write(a)

# 5. FOOTER
st.markdown("""
    <div class="footer-container">
        <div style="display: flex; justify-content: space-around; flex-wrap: wrap; gap: 40px;">
            <div style="max-width: 350px;">
                <h3 style="color: #C0392B;">Costa-Tour</h3>
                <p>Agencia Líder en Experiencias de Costa en Colombia. Registro Nacional de Turismo vigente.</p>
            </div>
            <div>
                <h4>Enlaces Rápidos</h4>
                <p><a href="https://www.colombia.travel" style="color:white;">Turismo Colombia</a><br>
                <a href="https://www.parquesnacionales.gov.co" style="color:white;">Parques Nacionales</a></p>
            </div>
            <div>
                <h4>Contacto</h4>
                <p>📍 Medellín, Antioquia<br>📞 +57 324 373 1661<br>✉️ veronicaarangopedrozo@gmail.com</p>
            </div>
        </div>
        <hr style="border-color: #333; margin: 40px 0;">
        <p style="text-align: center; font-size: 13px; opacity: 0.6;">© 2024 Costa-Tour Agencia de Viajes SAS.</p>
    </div>
    """, unsafe_allow_html=True)

# 6. WHATSAPP
st.markdown("""
    <a href="https://wa.me/573243731661" class="whatsapp-float" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="22"> 
        <span>Eñe'ẽ ore ndive</span>
    </a>
    """, unsafe_allow_html=True)