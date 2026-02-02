import streamlit as st

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Costa-Tour | Agencia de Viajes", layout="wide", page_icon="🌴")

# 2. DISEÑO Y COLORES (Arena, Rojo, Naranja, Tierra y Fuente Fina)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Lora:wght@400;500&display=swap');

    html, body, [class*="st-emotion-cache"] {
        background-color: #F5E6D3; /* Color Arena */
        font-family: 'Lora', serif; /* Fuente Fina y Elegante */
        color: #4A3728; /* Color Tierra para el texto */
    }

    .stButton>button {
        background-color: #C0392B; /* Rojo */
        color: white;
        border-radius: 20px;
        border: none;
        transition: 0.3s;
    }

    .stButton>button:hover {
        background-color: #D35400; /* Naranja al pasar el mouse */
        color: white;
    }

    /* Estilo para los títulos */
    h1, h2, h3 {
        color: #8B4513 !important; /* Tierra Profundo */
        font-weight: 500;
    }
    
    /* Barra de navegación superior */
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
        justify-content: center;
        background-color: #ffffff66;
        padding: 10px;
        border-radius: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. ENCABEZADO Y LOGO
col_logo, col_vacio = st.columns([1, 4])
with col_logo:
    # REEMPLAZA ESTE LINK POR EL LINK DE TU LOGO REAL
    st.image("https://cdn-icons-png.flaticon.com/512/826/826070.png", width=150)

# 4. NAVEGACIÓN SUPERIOR
menu = st.tabs(["🏠 Conócenos", "🏝️ Nuestros Tours", "📋 Formularios", "📰 Blog y Noticias"])

# --- SECCIÓN: CONÓCENOS ---
with menu[0]:
    st.title("Descubre el alma de Colombia con Costa-Tour")
    st.image("https://images.unsplash.com/photo-1589519160732-57fc498494f8?w=1200", use_container_width=True)
    
    c1, c2 = st.columns(2)
    with c1:
        st.write("### Nuestra Esencia")
        st.write("""
        En **Costa-Tour**, creamos puentes entre tus sueños y los destinos más indómitos de nuestra costa. 
        Especialistas en turismo de alto nivel para nacionales y extranjeros.
        """)
    with c2:
        st.write("### Contacto Directo")
        st.write("📧 **Correo:** veronicaarangopedrozo@gmail.com")
        st.write("📞 **WhatsApp:** +57 3243731661")
        st.link_button("Chatear con un asesor", "https://wa.me/573243731661")

# --- SECCIÓN: NUESTROS TOURS ---
with menu[1]:
    st.title("Portafolio de Experiencias")
    
    # --- CATEGORÍA PREMIUM ---
    st.header("⭐ Categoría Premium")
    
    with st.expander("✨ CARIBE MÁGICO"):
        col1, col2 = st.columns(2)
        with col1:
            st.image(["https://images.unsplash.com/photo-1548574505-5e239809ee19?w=500", 
                      "https://images.unsplash.com/photo-1590001158193-790179980bd3?w=500"], caption=["Cartagena", "San Andrés"])
        with col2:
            st.write("### Un paraíso exclusivo")
            st.write("Disfruta de hoteles boutique, cenas frente al mar y transporte privado en Cartagena y San Andrés.")
            st.button("Cotizar Caribe Mágico", key="p1")

    with st.expander("🐋 PACÍFICO VIVO"):
        col1, col2 = st.columns(2)
        with col1:
            st.image(["https://images.unsplash.com/photo-1554357475-acce8d059b4b?w=500", 
                      "https://images.unsplash.com/photo-1516815231560-8f41ec531527?w=500"], caption=["Nuquí", "Ballenas"])
        with col2:
            st.write("### Conexión Natural")
            st.write("Avistamiento de ballenas en Nuquí y Bahía Solano con la mejor logística de la región.")
            st.button("Cotizar Pacífico Vivo", key="p2")

    # --- CATEGORÍA ESTÁNDAR ---
    st.header("🚢 Categoría Estándar")
    
    st.subheader("Nuestra Costa / Marea / Ritmo Caribe / Ruta Marina")
    st.write("Destinos: Tolú, Coveñas, Palomino, Riohacha y Cabo de la Vela.")
    
    # Galería de fotos que se mueven (usando columnas)
    st.image(["https://images.unsplash.com/photo-1590523741831-ab7e8b8f9c7f?w=400", 
              "https://images.unsplash.com/photo-1580619305218-8423a7ef79b4?w=400",
              "https://images.unsplash.com/photo-1516815231560-8f41ec531527?w=400"], width=300)

# --- SECCIÓN: FORMULARIOS ---
with menu[2]:
    st.title("Gestión y Documentación")
    st.write("Utiliza nuestro formulario oficial para reportar cualquier novedad:")
    st.link_button("📝 Formulario de Quejas, Sugerencias y Reclamos", "https://forms.office.com/pages/responsepage.aspx?id=IefhmYRxjkmK_7KtTlPBwmzEaoV6AVxMnWIMDnUV_6JUQjFRQVBCSEg5UldERzdTVkUxU1ZTRTFTMy4u&route=shorturl")

# --- SECCIÓN: BLOG ---
with menu[3]:
    st.title("Actualidad y Tips de Viaje")
    st.image("https://images.unsplash.com/photo-1516815231560-8f41ec531527?w=1000", use_container_width=True)
    st.write("### ¡Infórmate antes de viajar!")
    st.write("Te recomendamos leer nuestro blog externo con los mejores tips para la Costa Colombiana.")
    st.link_button("📖 Leer Blog de Noticias", "https://tipsdeviajeparalacostacolombiana.blogspot.com/p/tips-de-viaje-para-la-costa-caribe-y-la.html")
    
