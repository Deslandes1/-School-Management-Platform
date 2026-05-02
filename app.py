import streamlit as st
import pandas as pd
from datetime import datetime
import io

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="School Management System – Built by Gesner Deslandes",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- AUTHENTICATION ----------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "lang" not in st.session_state:
    st.session_state.lang = "en"

# ---------- LANGUAGE DICTIONARIES ----------
text = {
    "en": {
        "login_title": "🔐 School Management System Login",
        "login_password": "Password",
        "login_button": "Login",
        "login_error": "Incorrect password. Please try again.",
        "logout_button": "🚪 Logout",
        "welcome": "Welcome to the School Management Platform",
        "built_by": "Built by Gesner Deslandes – GlobalInternet.py",
        "nav_students": "📚 Students",
        "nav_grades": "📊 Grades",
        "nav_attendance": "📅 Attendance",
        "nav_parent": "👨‍👩‍👧 Parent Portal",
        "nav_fees": "💰 Fee Collection",
        "student_title": "Student Registration",
        "student_add": "➕ Add New Student",
        "student_name": "Full Name",
        "student_grade": "Grade Level",
        "student_parent": "Parent/Guardian Name",
        "student_contact": "Parent Contact",
        "student_add_btn": "Add Student",
        "student_edit": "✏️ Edit",
        "student_delete": "🗑️ Delete",
        "student_id": "ID",
        "student_list": "Student List",
        "grades_title": "Grades Management",
        "grades_select": "Select Student",
        "grades_subject": "Subject",
        "grades_score": "Score (0-100)",
        "grades_add": "Add Grade",
        "grades_list": "Grades History",
        "attendance_title": "Daily Attendance",
        "attendance_date": "Date",
        "attendance_mark": "Mark Attendance",
        "attendance_status": "Status",
        "attendance_present": "Present",
        "attendance_absent": "Absent",
        "attendance_save": "Save Attendance",
        "attendance_view": "View Attendance Records",
        "parent_title": "Parent Portal",
        "parent_student": "Select Student",
        "parent_grades": "Grades",
        "parent_attendance": "Attendance Summary",
        "fees_title": "Fee Collection",
        "fees_select": "Select Student",
        "fees_amount": "Amount (USD)",
        "fees_description": "Description (e.g., Tuition, Activity Fee)",
        "fees_record": "Record Payment",
        "fees_balance": "Balance",
        "fees_history": "Payment History",
        "fees_total_paid": "Total Paid",
        "fees_total_due": "Total Due",
        "report_title": "📄 Student Grade Report",
        "report_download": "Download Grade Report (CSV)",
        "back": "← Back",
        "edit": "Edit",
        "delete": "Delete",
        "save": "Save",
        "cancel": "Cancel",
        "sidebar_contact": "📞 Contact Us",
        "sidebar_email": "✉️ deslandes78@gmail.com",
        "sidebar_phone": "📱 (509)-47385663",
        "sidebar_pricing_title": "💰 Software Pricing",
        "sidebar_monthly": "📅 Monthly subscription: $99 USD / month",
        "sidebar_full": "💎 Full package (one‑time): $2,499 USD",
        "sidebar_note": "Includes source code, setup, and 1 year support",
    },
    "fr": {
        "login_title": "🔐 Connexion au Système de Gestion Scolaire",
        "login_password": "Mot de passe",
        "login_button": "Se connecter",
        "login_error": "Mot de passe incorrect. Veuillez réessayer.",
        "logout_button": "🚪 Déconnexion",
        "welcome": "Bienvenue sur la plateforme de gestion scolaire",
        "built_by": "Construit par Gesner Deslandes – GlobalInternet.py",
        "nav_students": "📚 Élèves",
        "nav_grades": "📊 Notes",
        "nav_attendance": "📅 Présence",
        "nav_parent": "👨‍👩‍👧 Portail Parents",
        "nav_fees": "💰 Frais de scolarité",
        "student_title": "Gestion des élèves",
        "student_add": "➕ Ajouter un élève",
        "student_name": "Nom complet",
        "student_grade": "Niveau",
        "student_parent": "Parent / Tuteur",
        "student_contact": "Contact du parent",
        "student_add_btn": "Ajouter",
        "student_edit": "✏️ Modifier",
        "student_delete": "🗑️ Supprimer",
        "student_id": "ID",
        "student_list": "Liste des élèves",
        "grades_title": "Gestion des notes",
        "grades_select": "Choisir un élève",
        "grades_subject": "Matière",
        "grades_score": "Note (0-100)",
        "grades_add": "Ajouter une note",
        "grades_list": "Historique des notes",
        "attendance_title": "Présence quotidienne",
        "attendance_date": "Date",
        "attendance_mark": "Marquer la présence",
        "attendance_status": "Statut",
        "attendance_present": "Présent",
        "attendance_absent": "Absent",
        "attendance_save": "Enregistrer",
        "attendance_view": "Voir les enregistrements",
        "parent_title": "Portail Parents",
        "parent_student": "Choisir un élève",
        "parent_grades": "Notes",
        "parent_attendance": "Résumé de présence",
        "fees_title": "Collecte des frais",
        "fees_select": "Choisir un élève",
        "fees_amount": "Montant (USD)",
        "fees_description": "Description",
        "fees_record": "Enregistrer le paiement",
        "fees_balance": "Solde",
        "fees_history": "Historique des paiements",
        "fees_total_paid": "Total payé",
        "fees_total_due": "Total dû",
        "report_title": "📄 Rapport de notes",
        "report_download": "Télécharger le rapport (CSV)",
        "back": "← Retour",
        "edit": "Modifier",
        "delete": "Supprimer",
        "save": "Enregistrer",
        "cancel": "Annuler",
        "sidebar_contact": "📞 Contactez‑nous",
        "sidebar_email": "✉️ deslandes78@gmail.com",
        "sidebar_phone": "📱 (509)-47385663",
        "sidebar_pricing_title": "💰 Tarifs du logiciel",
        "sidebar_monthly": "📅 Abonnement mensuel : 99 $US / mois",
        "sidebar_full": "💎 Licence complète (unique) : 2 499 $US",
        "sidebar_note": "Code source, installation et 1 an de support inclus",
    },
    "es": {
        "login_title": "🔐 Inicio de Sesión – Sistema de Gestión Escolar",
        "login_password": "Contraseña",
        "login_button": "Iniciar sesión",
        "login_error": "Contraseña incorrecta. Intente de nuevo.",
        "logout_button": "🚪 Cerrar sesión",
        "welcome": "Bienvenido a la plataforma de gestión escolar",
        "built_by": "Construido por Gesner Deslandes – GlobalInternet.py",
        "nav_students": "📚 Estudiantes",
        "nav_grades": "📊 Calificaciones",
        "nav_attendance": "📅 Asistencia",
        "nav_parent": "👨‍👩‍👧 Portal de padres",
        "nav_fees": "💰 Recaudación de cuotas",
        "student_title": "Registro de estudiantes",
        "student_add": "➕ Agregar estudiante",
        "student_name": "Nombre completo",
        "student_grade": "Grado",
        "student_parent": "Padre / tutor",
        "student_contact": "Contacto del padre",
        "student_add_btn": "Agregar",
        "student_edit": "✏️ Editar",
        "student_delete": "🗑️ Eliminar",
        "student_id": "ID",
        "student_list": "Lista de estudiantes",
        "grades_title": "Gestión de calificaciones",
        "grades_select": "Seleccionar estudiante",
        "grades_subject": "Asignatura",
        "grades_score": "Nota (0-100)",
        "grades_add": "Agregar calificación",
        "grades_list": "Historial de calificaciones",
        "attendance_title": "Asistencia diaria",
        "attendance_date": "Fecha",
        "attendance_mark": "Registrar asistencia",
        "attendance_status": "Estado",
        "attendance_present": "Presente",
        "attendance_absent": "Ausente",
        "attendance_save": "Guardar",
        "attendance_view": "Ver registros",
        "parent_title": "Portal de padres",
        "parent_student": "Seleccionar estudiante",
        "parent_grades": "Calificaciones",
        "parent_attendance": "Resumen de asistencia",
        "fees_title": "Recaudación de cuotas",
        "fees_select": "Seleccionar estudiante",
        "fees_amount": "Monto (USD)",
        "fees_description": "Descripción",
        "fees_record": "Registrar pago",
        "fees_balance": "Saldo",
        "fees_history": "Historial de pagos",
        "fees_total_paid": "Total pagado",
        "fees_total_due": "Total adeudado",
        "report_title": "📄 Informe de calificaciones",
        "report_download": "Descargar informe (CSV)",
        "back": "← Regresar",
        "edit": "Editar",
        "delete": "Eliminar",
        "save": "Guardar",
        "cancel": "Cancelar",
        "sidebar_contact": "📞 Contáctenos",
        "sidebar_email": "✉️ deslandes78@gmail.com",
        "sidebar_phone": "📱 (509)-47385663",
        "sidebar_pricing_title": "💰 Precios del software",
        "sidebar_monthly": "📅 Suscripción mensual: $99 USD / mes",
        "sidebar_full": "💎 Licencia completa (única): $2,499 USD",
        "sidebar_note": "Incluye código fuente, instalación y 1 año de soporte",
    }
}

def _(key):
    return text[st.session_state.lang].get(key, key)

# ---------- INITIALISE DATA STORES (in‑memory) ----------
if "students" not in st.session_state:
    st.session_state.students = {}
    st.session_state.next_student_id = 1
    # Demo students
    st.session_state.students[1] = {"name": "Marie Claire", "grade": "3rd Grade", "parent": "Jean Claire", "contact": "555-1234"}
    st.session_state.next_student_id = 2
    st.session_state.students[2] = {"name": "Jean Pierre", "grade": "5th Grade", "parent": "Marie Pierre", "contact": "555-5678"}
    st.session_state.next_student_id = 3

if "grades" not in st.session_state:
    st.session_state.grades = []  # list of dict: student_id, subject, score, date

if "attendance" not in st.session_state:
    st.session_state.attendance = []

if "payments" not in st.session_state:
    st.session_state.payments = []

# ---------- CUSTOM CSS (LIGHT BLUE BACKGROUND) ----------
st.markdown("""
<style>
    .stApp, [data-testid="stSidebar"] {
        background: linear-gradient(135deg, #e6f7ff 0%, #cceeff 100%) !important;
    }
    .main-header {
        background: linear-gradient(135deg, #1e3c72, #2a5298);
        padding: 1.5rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .footer {
        text-align: center;
        margin-top: 3rem;
        padding: 1rem;
        background-color: rgba(255,255,255,0.6);
        border-radius: 20px;
        color: #1e3c72;
    }
    .stButton button {
        background-color: #2a5298;
        color: white;
        border-radius: 30px;
        padding: 0.3rem 1.2rem;
        font-weight: bold;
    }
    .stButton button:hover {
        background-color: #1e3c72;
    }
    h1, h2, h3 {
        color: #1e3c72;
    }
</style>
""", unsafe_allow_html=True)

# ---------- LOGIN PAGE ----------
if not st.session_state.authenticated:
    st.markdown(f"<div class='main-header'><h1>{_('login_title')}</h1></div>", unsafe_allow_html=True)
    password = st.text_input(_("login_password"), type="password")
    if st.button(_("login_button")):
        if password == "20082010":
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error(_("login_error"))
    st.stop()

# ---------- LOGGED IN – MAIN INTERFACE ----------
# Language selector in sidebar
lang_options = {"English": "en", "Français": "fr", "Español": "es"}
selected_lang = st.sidebar.selectbox("🌐 Language", list(lang_options.keys()))
st.session_state.lang = lang_options[selected_lang]

# Sidebar navigation
page = st.sidebar.radio(
    "",
    [_("nav_students"), _("nav_grades"), _("nav_attendance"), _("nav_parent"), _("nav_fees"), _("report_title")]
)

# ---------- SIDEBAR CONTACT AND PRICING INFO ----------
st.sidebar.markdown("---")
st.sidebar.markdown(f"### {_('sidebar_contact')}")
st.sidebar.markdown(_("sidebar_email"))
st.sidebar.markdown(_("sidebar_phone"))
st.sidebar.markdown("---")
st.sidebar.markdown(f"### {_('sidebar_pricing_title')}")
st.sidebar.markdown(_("sidebar_monthly"))
st.sidebar.markdown(_("sidebar_full"))
st.sidebar.caption(_("sidebar_note"))
st.sidebar.markdown("---")

# Logout button
if st.sidebar.button(_("logout_button"), use_container_width=True):
    st.session_state.authenticated = False
    st.rerun()

st.sidebar.markdown("---")
st.sidebar.markdown(f"*{_('built_by')}*")

# Helper functions
def get_student_name(student_id):
    return st.session_state.students.get(student_id, {}).get("name", "Unknown")

# ---------- STUDENT REGISTRATION ----------
if page == _("nav_students"):
    st.markdown(f"<div class='main-header'><h1>{_('student_title')}</h1></div>", unsafe_allow_html=True)
    
    with st.expander(_("student_add")):
        with st.form("add_student"):
            name = st.text_input(_("student_name"))
            grade = st.text_input(_("student_grade"))
            parent = st.text_input(_("student_parent"))
            contact = st.text_input(_("student_contact"))
            if st.form_submit_button(_("student_add_btn")):
                if name:
                    new_id = st.session_state.next_student_id
                    st.session_state.students[new_id] = {"name": name, "grade": grade, "parent": parent, "contact": contact}
                    st.session_state.next_student_id += 1
                    st.rerun()
    
    st.subheader(_("student_list"))
    if st.session_state.students:
        for sid, data in st.session_state.students.items():
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                st.markdown(f"**ID {sid}:** {data['name']} – Grade {data['grade']} – Parent: {data['parent']} ({data['contact']})")
            with col2:
                if st.button(_("edit"), key=f"edit_{sid}"):
                    with st.form(key=f"edit_form_{sid}"):
                        new_name = st.text_input(_("student_name"), value=data["name"])
                        new_grade = st.text_input(_("student_grade"), value=data["grade"])
                        new_parent = st.text_input(_("student_parent"), value=data["parent"])
                        new_contact = st.text_input(_("student_contact"), value=data["contact"])
                        if st.form_submit_button(_("save")):
                            st.session_state.students[sid] = {"name": new_name, "grade": new_grade, "parent": new_parent, "contact": new_contact}
                            st.rerun()
            with col3:
                if st.button(_("delete"), key=f"del_{sid}"):
                    del st.session_state.students[sid]
                    st.rerun()
    else:
        st.info("No students yet.")

# ---------- GRADES MANAGEMENT ----------
elif page == _("nav_grades"):
    st.markdown(f"<div class='main-header'><h1>{_('grades_title')}</h1></div>", unsafe_allow_html=True)
    if not st.session_state.students:
        st.warning("Please add students first.")
    else:
        student_options = {sid: data["name"] for sid, data in st.session_state.students.items()}
        selected_sid = st.selectbox(_("grades_select"), list(student_options.keys()), format_func=lambda x: student_options[x])
        
        with st.form("add_grade"):
            subject = st.text_input(_("grades_subject"))
            score = st.number_input(_("grades_score"), 0.0, 100.0, step=0.5)
            if st.form_submit_button(_("grades_add")):
                if subject and score is not None:
                    st.session_state.grades.append({
                        "student_id": selected_sid,
                        "subject": subject,
                        "score": score,
                        "date": datetime.now().strftime("%Y-%m-%d")
                    })
                    st.rerun()
        
        st.subheader(_("grades_list"))
        student_grades = [g for g in st.session_state.grades if g["student_id"] == selected_sid]
        if student_grades:
            df = pd.DataFrame(student_grades)[["subject", "score", "date"]]
            st.dataframe(df, use_container_width=True)
        else:
            st.info("No grades recorded for this student.")

# ---------- ATTENDANCE (fixed duplicate key) ----------
elif page == _("nav_attendance"):
    st.markdown(f"<div class='main-header'><h1>{_('attendance_title')}</h1></div>", unsafe_allow_html=True)
    if not st.session_state.students:
        st.warning("Please add students first.")
    else:
        date_today = st.date_input(_("attendance_date"), datetime.today())
        date_str = date_today.strftime("%Y-%m-%d")
        
        with st.form(key="attendance_form"):
            st.subheader(_("attendance_mark"))
            attendance_dict = {}
            for sid, data in st.session_state.students.items():
                status = st.selectbox(
                    f"{data['name']}",
                    [_("attendance_present"), _("attendance_absent")],
                    key=f"att_{sid}_{date_str}"
                )
                attendance_dict[sid] = "Present" if status == _("attendance_present") else "Absent"
            if st.form_submit_button(_("attendance_save")):
                st.session_state.attendance = [a for a in st.session_state.attendance if a["date"] != date_str]
                for sid, status in attendance_dict.items():
                    st.session_state.attendance.append({"student_id": sid, "date": date_str, "status": status})
                st.rerun()
        
        st.subheader(_("attendance_view"))
        if st.session_state.attendance:
            df_att = pd.DataFrame(st.session_state.attendance)
            df_att["Student"] = df_att["student_id"].apply(get_student_name)
            st.dataframe(df_att[["Student", "date", "status"]], use_container_width=True)
        else:
            st.info("No attendance records yet.")

# ---------- PARENT PORTAL ----------
elif page == _("nav_parent"):
    st.markdown(f"<div class='main-header'><h1>{_('parent_title')}</h1></div>", unsafe_allow_html=True)
    if not st.session_state.students:
        st.warning("No students in the system.")
    else:
        student_options = {sid: data["name"] for sid, data in st.session_state.students.items()}
        selected_sid = st.selectbox(_("parent_student"), list(student_options.keys()), format_func=lambda x: student_options[x])
        data = st.session_state.students[selected_sid]
        st.markdown(f"**{data['name']}** – Grade {data['grade']}  \nParent: {data['parent']} – Contact: {data['contact']}")
        
        st.subheader(_("parent_grades"))
        grades = [g for g in st.session_state.grades if g["student_id"] == selected_sid]
        if grades:
            df_grades = pd.DataFrame(grades)[["subject", "score", "date"]]
            st.dataframe(df_grades, use_container_width=True)
        else:
            st.info("No grades available.")
        
        st.subheader(_("parent_attendance"))
        attendance = [a for a in st.session_state.attendance if a["student_id"] == selected_sid]
        if attendance:
            df_att = pd.DataFrame(attendance)[["date", "status"]]
            st.dataframe(df_att, use_container_width=True)
        else:
            st.info("No attendance records.")

# ---------- FEE COLLECTION ----------
elif page == _("nav_fees"):
    st.markdown(f"<div class='main-header'><h1>{_('fees_title')}</h1></div>", unsafe_allow_html=True)
    if not st.session_state.students:
        st.warning("Please add students first.")
    else:
        student_options = {sid: data["name"] for sid, data in st.session_state.students.items()}
        selected_sid = st.selectbox(_("fees_select"), list(student_options.keys()), format_func=lambda x: student_options[x])
        
        with st.form("add_payment"):
            amount = st.number_input(_("fees_amount"), min_value=0.0, step=10.0)
            desc = st.text_input(_("fees_description"))
            if st.form_submit_button(_("fees_record")):
                if amount > 0:
                    st.session_state.payments.append({
                        "student_id": selected_sid,
                        "amount": amount,
                        "description": desc,
                        "date": datetime.now().strftime("%Y-%m-%d")
                    })
                    st.rerun()
        
        total_due = 1000.0
        student_payments = [p for p in st.session_state.payments if p["student_id"] == selected_sid]
        total_paid = sum(p["amount"] for p in student_payments)
        balance = total_due - total_paid
        
        st.subheader(_("fees_balance"))
        st.metric(_("fees_total_due"), f"${total_due:.2f}")
        st.metric(_("fees_total_paid"), f"${total_paid:.2f}")
        st.metric(_("fees_balance"), f"${balance:.2f}")
        
        st.subheader(_("fees_history"))
        if student_payments:
            df_pay = pd.DataFrame(student_payments)[["date", "description", "amount"]]
            st.dataframe(df_pay, use_container_width=True)
        else:
            st.info("No payment history.")

# ---------- GRADE REPORT ----------
elif page == _("report_title"):
    st.markdown(f"<div class='main-header'><h1>{_('report_title')}</h1></div>", unsafe_allow_html=True)
    if not st.session_state.students:
        st.warning("No students in the system.")
    else:
        student_options = {sid: data["name"] for sid, data in st.session_state.students.items()}
        selected_sid = st.selectbox(_("grades_select"), list(student_options.keys()), format_func=lambda x: student_options[x])
        student_name = student_options[selected_sid]
        
        student_grades = [g for g in st.session_state.grades if g["student_id"] == selected_sid]
        if student_grades:
            df = pd.DataFrame(student_grades)[["subject", "score", "date"]]
            st.dataframe(df, use_container_width=True)
            
            csv_buffer = io.StringIO()
            df.to_csv(csv_buffer, index=False)
            csv_data = csv_buffer.getvalue()
            
            st.download_button(
                label=_("report_download"),
                data=csv_data,
                file_name=f"grades_report_{student_name.replace(' ', '_')}.csv",
                mime="text/csv",
                key="download_grades"
            )
        else:
            st.info("No grades recorded for this student.")

# ---------- FOOTER ----------
st.markdown(f"""
<div class="footer">
    <p>© {datetime.now().year} – {_('built_by')}</p>
</div>
""", unsafe_allow_html=True)
