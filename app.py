import streamlit as st
import pandas as pd

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="Costa-Tour | Agencia de Viajes", 
    layout="wide", 
    page_icon="✈️"
)

# 2. ESTILOS CSS - REFINADOS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&family=Lora:ital,wght@0,400;1,400&display=swap');

    .stApp { background-color: #FFFFFF !important; }
    
    /* Botones Rojos - Estilo unificado */
    .stButton > button {
        background-color: #C0392B !important;
        color: white !important;
        border: none !important;
        padding: 10px 20px !important;
        border-radius: 8px !important;
        transition: 0.3s;
        width: 100%;
        font-weight: 600;
        font-family: 'Poppins', sans-serif;
    }
    
    .stButton > button:hover {
        background-color: #A93226 !important;
        transform: translateY(-2px);
    }

    /* Tabla Estilizada Personalizada */
    [data-testid="stTable"] {
        background-color: white;
        border-radius: 12px;
        overflow: hidden;
    }
    
    /* Hero Section */
    .hero-section {
        background-image: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), url('https://images.unsplash.com/photo-1507525428034-b723cf961d3e?q=80&w=2073&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        height: 400px;
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
        font-size: 64px;
        font-weight: bold;
        margin-bottom: 10px;
    }

    /* Package Description Box */
    .package-description {
        font-family: 'Poppins', sans-serif;
        font-size: 15px;
        color: #333;
        padding: 20px;
        background: #FDFDFD;
        border: 1px solid #F0F0F0;
        border-left: 5px solid #C0392B;
        border-radius: 8px;
        margin-top: 15px;
        line-height: 1.7;
    }

    /* Testimonial Card */
    .testimonial-card {
        background: #FFFFFF;
        padding: 25px;
        border-radius: 20px;
        border: 1px solid #F0F0F0;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.02);
    }

    .section-title {
        text-align: center;
        margin: 50px 0 30px 0;
        color: #2C3E50;
        font-weight: bold;
        font-family: 'Lora', serif;
    }

    /* WhatsApp Button */
    .whatsapp-float {
        position: fixed;
        bottom: 30px;
        right: 30px;
        background-color: #25d366;
        color: white !important;
        padding: 15px 25px;
        border-radius: 50px;
        text-decoration: none;
        z-index: 1000;
        font-weight: 600;
        box-shadow: 0 10px 25px rgba(37, 211, 102, 0.3);
        display: flex;
        align-items: center;
        gap: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. CABECERA
t_col1, t_col2 = st.columns([2, 1])
with t_col1:
    st.image("https://i.ibb.co/ds6F7b72/ve.png", width=200)
with t_col2:
    st.markdown("<p style='text-align:right; color:#888; font-size:14px; margin-top:20px;'>📲 +57 324 373 1661<br>📍 Medellín, Colombia</p>", unsafe_allow_html=True)

# 4. TABS
tab_inicio, tab_tours, tab_atencion = st.tabs(["NUESTRA ESENCIA", "CATÁLOGO DE TOURS", "ATENCIÓN"])

# --- TAB INICIO ---
with tab_inicio:
    st.markdown("""
        <div class="hero-section">
            <h1 class="hero-title">Costa-Tour</h1>
            <p style='font-size: 22px; font-style: italic;'>Explora la belleza indomable de Colombia con expertos.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<h2 class='section-title'>Nuestra Historia</h2>", unsafe_allow_html=True)
    st.write("En Costa-Tour, redefinimos el viaje. Nos especializamos en conectar el corazón de Colombia con el mundo, ofreciendo experiencias que equilibran la riqueza natural con un estándar de servicio impecable.")

    # TESTIMONIOS
    st.markdown("<h2 class='section-title'>Lo que dicen nuestros viajeros</h2>", unsafe_allow_html=True)
    t_col1, t_col2, t_col3, t_col4 = st.columns(4)
    testimonials = [
        ("La atención al detalle fue impecable. Todo estuvo perfecto.", "Carlos Mendoza"),
        ("El Pacífico con Costa-Tour es otra experiencia. Mágico.", "Ana María Ruiz"),
        ("Paz absoluta y hoteles de primera. Volveré sin duda.", "Sebastián Gómez"),
        ("Resolvieron mis dudas al instante. Gran equipo.", "Elena Torres")
    ]
    for i, (txt, author) in enumerate(testimonials):
        with [t_col1, t_col2, t_col3, t_col4][i]:
            st.markdown(f"""
                <div class="testimonial-card">
                    <p style='font-style: italic; color: #555;'>"{txt}"</p>
                    <p style='font-weight: bold; color: #C0392B; margin-top:10px;'>{author}</p>
                </div>
            """, unsafe_allow_html=True)

# --- TAB TOURS ---
with tab_tours:
    st.markdown("<h2 class='section-title'>Encuentra tu estilo de viaje</h2>", unsafe_allow_html=True)
    
    # TABLA COMPARATIVA MEJORADA
    df_data = {
        "Servicio": ["🏨 Alojamiento", "🍽️ Gastronomía", "🚐 Transporte", "🛎️ Asistencia", "⭐ Exclusividad"],
        "Línea Estándar": ["Hoteles 3* / Posadas", "Desayuno buffet", "Vans compartidas", "Virtual 24/7", "Grupos dinámicos"],
        "Línea Premium": ["Resorts 5* / Boutique", "Plan Gastronómico Pro", "Vehículos de lujo", "Personalizada 24/7", "Privacidad Total"]
    }
    st.table(pd.DataFrame(df_data))

    st.markdown("<hr style='margin: 40px 0;'>", unsafe_allow_html=True)

    # FUNCIÓN PARA RENDERIZAR PAQUETES
    def render_packages(package_list, title):
        st.markdown(f"<h2 style='text-align: center; color:#2C3E50;'>{title}</h2>", unsafe_allow_html=True)
        cols = st.columns(4)
        for i, (name, img, key, desc) in enumerate(package_list):
            with cols[i]:
                st.image(img, use_container_width=True)
                st.markdown(f"<h5 style='text-align:center;'>{name}</h5>", unsafe_allow_html=True)
                
                # Lógica de botón Ver más / Ver menos
                state_key = f"v_{key}"
                if state_key not in st.session_state: st.session_state[state_key] = False
                
                label = "Cerrar detalles" if st.session_state[state_key] else "Ver más detalles"
                
                if st.button(label, key=f"btn_{key}"):
                    st.session_state[state_key] = not st.session_state[state_key]
                    st.rerun()
                
                if st.session_state[state_key]:
                    st.markdown(f"<div class='package-description'>{desc}</div>", unsafe_allow_html=True)

    # PREMIUM
    premium_packs = [
        ("Caribe Mágico", "https://media-cdn.tripadvisor.com/media/photo-s/2f/59/25/75/caption.jpg", "p1", "• <b>Alojamiento:</b> Suite de lujo frente al mar.<br>• <b>Comida:</b> Cena privada en la playa.<br>• <b>Servicios:</b> Barra libre premium."),
        ("Pacífico Vivo", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRIeSN9RSQsxw_n-gbbbfOOsjBrcClZngt3DA&s", "p2", "• <b>Actividad:</b> Avistamiento privado de ballenas.<br>• <b>Lodge:</b> Alta gama en medio de la selva.<br>• <b>Guía:</b> Bilingüe dedicado."),
        ("Pacífico Místico", "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2c/b0/c2/4f/private-beach-hotels.jpg?w=1200&h=-1&s=1", "p3", "• <b>Spa:</b> Terapias termales incluidas.<br>• <b>Retiro:</b> Hotel boutique exclusivo.<br>• <b>Dieta:</b> Menú orgánico personalizado."),
        ("Sol Caribe", "https://cdn2.paraty.es/landmar/images/865ffac6866fcba", "p4", "• <b>All-Inclusive:</b> Resort 5 estrellas.<br>• <b>Tour:</b> Catamarán privado por las islas.<br>• <b>Plus:</b> Concierge las 24 horas.")
    ]
    render_packages(premium_packs, "Línea Premium")

    st.markdown("<br>", unsafe_allow_html=True)

    # ESTÁNDAR
    standard_packs = [
        ("Nuestra Costa", "https://www.latamairlines.com/content/dam/latamxp/sites/vamos-latam/news-colombia/lista-latam/res_shutterstock_1312464929.jpg", "e1", "• <b>Posadas:</b> Encanto local y confort.<br>• <b>Tour:</b> Caminata histórica guiada.<br>• <b>Seguro:</b> Cobertura médica completa."),
        ("Marea", "https://plus.unsplash.com/premium_photo-1669748157617-a3a83cc8ea23?fm=jpg&q=60&w=3000&auto=format&fit=crop", "e2", "• <b>Hotel:</b> Moderno media gama.<br>• <b>Acción:</b> Clase de surf grupal.<br>• <b>Transporte:</b> Lanchas compartidas."),
        ("Ritmo Caribe", "https://condominiovistamar.com/wp-content/uploads/2025/07/playas-en-caovenas.webp", "e3", "• <b>Social:</b> Hostales de diseño boutique.<br>• <b>Sabor:</b> Almuerzo típico incluido.<br>• <b>Guía:</b> Experto local."),
        ("Ruta Marina", "https://blog.gimlivingspaces.com/hubfs/Muelle%20r%C3%BAstico%20de%20madera%20con%20una%20palapa%20con%20vistas%20a%20las%20aguas%20turquesas%20cristalinas%20en%20Isla%20Mujeres%2C%20playa%20de%20M%C3%A9xico.webp", "e4", "• <b>Eco:</b> Cabañas sostenibles.<br>• <b>Canoa:</b> Paseo por los manglares.<br>• <b>Parques:</b> Entradas incluidas.")
    ]
    render_packages(standard_packs, "Línea Estándar")

# --- TAB ATENCIÓN ---
with tab_atencion:
    st.markdown("<h2 class='section-title'>Centro de Ayuda</h2>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.info("### PQR y Solicitudes\nRadique sus requerimientos aquí.")
        st.link_button("Abrir Formulario", "https://forms.office.com/...")
    with c2:
        st.success("### Blog del Viajero\nConsejos y guías para tu próximo viaje.")
        st.link_button("Ver Consejos", "https://tipsdeviaje...")

    st.markdown("<br><h4>Preguntas Frecuentes</h4>", unsafe_allow_html=True)
    faqs = [
        ("¿Antelación de reserva?", "Recomendamos 30 días antes."),
        ("¿Documentos?", "Cédula original vigente."),
        ("¿Seguro médico?", "Incluido en todos los planes."),
        ("¿Personalización?", "Disponible en Línea Premium."),
        ("¿Métodos de pago?", "PSE, tarjetas y transferencia."),
        ("¿Vuelos?", "Se pueden añadir como extra."),
        ("¿Cancelaciones?", "Flexibles hasta 15 días antes."),
        ("¿Atención presencial?", "Cita previa en Medellín.")
    ]
    for q, a in faqs:
        with st.expander(q):
            st.write(a)

# 5. FOOTER & WHATSAPP
st.markdown("<div style='text-align:center; padding:40px; color:#999; font-size:12px;'>© 2024 Costa-Tour. Medellín, Colombia.</div>", unsafe_allow_html=True)
st.markdown("""
    <a href="https://wa.me/573243731661" class="whatsapp-float" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="20"> ¡Habla con un asesor!
    </a>
    """, unsafe_allow_html=True)