import streamlit as st
import pandas as pd
from datetime import datetime

# ==========================================
# PAGE CONFIGURATION & FOOTBALL DARK THEME
# ==========================================
st.set_page_config(
    page_title="ШИГШЭЭ 2026 // FIFA World Cup",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Injecting clean developer CSS directly into Streamlit to control look and feel
st.markdown("""
    <style>
    .main .block-container { padding-top: 1rem; }
    
    /* Live Top Ticker Row */
    .ticker-container {
        background-color: #0d1117;
        padding: 12px;
        border-bottom: 2px solid #10b981;
        margin-bottom: 25px;
        border-radius: 6px;
    }
    .ticker-text {
        color: #f1f5f9;
        font-family: 'Segoe UI', monospace;
        font-size: 13px;
    }
    .live-dot {
        background-color: #ef4444;
        color: white;
        padding: 2px 6px;
        font-weight: bold;
        border-radius: 4px;
        font-size: 11px;
    }
    
    /* Custom Match and News Cards */
    .match-card {
        background-color: #161b22;
        border: 1px solid #21262d;
        border-radius: 8px;
        padding: 18px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
    }
    .news-card {
        background-color: #111827;
        border: 1px solid #1f2937;
        border-radius: 10px;
        padding: 20px;
        height: 100%;
    }
    
    /* Badges */
    .tag-badge {
        background-color: #d97706;
        color: white;
        padding: 3px 8px;
        border-radius: 4px;
        font-size: 11px;
        font-weight: bold;
        text-transform: uppercase;
    }
    .group-sub {
        color: #10b981;
        font-size: 12px;
        font-weight: bold;
        margin-top: 4px;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# UPPER LIVE MATCH TICKER
# ==========================================
st.markdown("""
<div class="ticker-container">
    <span class="ticker-text">
        <span class="live-dot">ШУУД ОНОО</span> 
        &nbsp;&nbsp; Саудын Араб vs Уругвай | <span style="color:#ef4444; font-weight:bold;">1:1 (Нэгдүгээр үе 81')</span> 
        &nbsp;&nbsp;•&nbsp;&nbsp; БНСУ vs Чех | <span style="color:#10b981;">2:1 (FT)</span> 
        &nbsp;&nbsp;•&nbsp;&nbsp; Канад vs Босни Герцеговин | <span style="color:#10b981;">1:1 (FT)</span> 
        &nbsp;&nbsp;•&nbsp;&nbsp; АНУ vs Парагвай | <span style="color:#10b981;">4:1 (FT)</span> 
        &nbsp;&nbsp;•&nbsp;&nbsp; Испани vs Кабо-Верде | <span style="color:#8b949e;">0:0 (FT)</span>
    </span>
</div>
""", unsafe_allow_html=True)

# ==========================================
# SIDEBAR NAVIGATION CONTROLS
# ==========================================
st.sidebar.title("🟢 ШИГШЭЭ 2026")
st.sidebar.markdown("---")
navigation = st.sidebar.radio(
    "Үндсэн цэс", 
    ["📊 НҮҮР (Эргэн тойронд)", "📰 МЭДЭЭ (FIFA Сурвалжлага)", "🔮 ТОГЛОЛТЫН ТААМАГЛАЛ"]
)
st.sidebar.markdown("---")
st.sidebar.caption(f"Синхрончлогдсон хугацаа: {datetime.now().strftime('%H:%M:%S')}")

# ==========================================
# VIEW ROUTING
# ==========================================

if navigation == "📊 НҮҮР (Эргэн тойронд)":
    st.caption("ОНЦЛОХ МЭДЭЭЛЛИЙН ТӨВ")
    st.title("FIFA ДАШТ 2026 — Монгол Хөгжөөн Дэмжигчдийн Төв")
    
    st.markdown("### 🔴 Өнөөдрийн Тоглолтууд")
    
    # Grid columns matching the original layout parameters
    m1, m2, m3, m4 = st.columns(4)
    
    with m1:
        st.markdown("""
        <div class="match-card" style="border-left: 4px solid #ef4444;">
            <p style="color:#ef4444; font-size:12px; font-weight:bold; margin:0;">● LIVE 81'</p>
            <h4 style="margin:12px 0; color:#ffffff;">Саудын Араб <span style="color:#ef4444;">1 - 1</span> Уругвай</h4>
            <p style="color:#9ca3af; font-size:12px; margin:0;">Н Бүлэг • Хүчтэй тулаан</p>
        </div>
        """, unsafe_allow_html=True)
        
    with m2:
        st.markdown("""
        <div class="match-card" style="border-left: 4px solid #8b949e;">
            <p style="color:#8b949e; font-size:12px; font-weight:bold; margin:0;">FT</p>
            <h4 style="margin:12px 0; color:#ffffff;">Испани <span style="color:#8b949e;">0 - 0</span> Кабо-Верде</h4>
            <p style="color:#9ca3af; font-size:12px; margin:0;">Н Бүлэг • Тэнцээ</p>
        </div>
        """, unsafe_allow_html=True)
        
    with m3:
        st.markdown("""
        <div class="match-card" style="border-left: 4px solid #d97706;">
            <p style="color:#d97706; font-size:12px; font-weight:bold; margin:0;">МАГАДЛАЛТАЙ</p>
            <h4 style="margin:12px 0; color:#ffffff;">Иран <span style="color:#d97706;">vs</span> Шинэ Зеланд</h4>
            <p style="color:#9ca3af; font-size:12px; margin:0;">G Бүлэг • Орой 18:00 цагт</p>
        </div>
        """, unsafe_allow_html=True)
        
    with m4:
        st.markdown("""
        <div class="match-card" style="border-left: 4px solid #d97706;">
            <p style="color:#d97706; font-size:12px; font-weight:bold; margin:0;">МАГАДЛАЛТАЙ</p>
            <h4 style="margin:12px 0; color:#ffffff;">Франц <span style="color:#d97706;">vs</span> Сенегал</h4>
            <p style="color:#9ca3af; font-size:12px; margin:0;">I Бүлэг • Шөнө 21:00 цагт</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    
    st.markdown("""
    <div style="background-color:#161b22; padding:25px; border-radius:10px; border:1px solid #21262d;">
        <span class="tag-badge">НЭЭЛТИЙН ТОГЛОЛТ — А БҮЛЭГ</span>
        <h2 style="margin-top:12px; color:#ffffff;">Ацтека цэнгэлдэхэд түүхэн нээлт — Мексик хүчирхэг эхлэлийг тавилаа</h2>
        <p style="color:#c9d1d9; font-size:15px; line-height:1.6; margin-bottom:0;">
            Домогт Ацтека цэнгэлдэх хүрээлэнд явагдсан нээлтийн тоглолтод талбайн эзэд Өмнөд Африкийн багийг 2:0 харьцаатайгаар 
            итгэл төгс буулган авч, бүлгээ тэргүүлж эхэллээ. Түүхэн нээлтийн уур амьсгал цэнгэлдэх даяар гайхалтай байлаа.
        </p>
    </div>
    """, unsafe_allow_html=True)

elif navigation == "📰 МЭДЭЭ (FIFA Сурвалжлага)":
    st.title("Мэдээ мэдээлэл — ДАШТ 2026")
    
    n1, n2, n3 = st.columns(3)
    
    with n1:
        st.markdown("""
        <div class="news-card">
            <span class="tag-badge">ОНЦЛОХ МЭДЭЭ</span>
            <p class="group-sub">С БҮЛЭГ</p>
            <h3 style="color:#ffffff; margin-top:10px;">Лионель Месси ДАШТ 2026-ын бэлтгэлээ бүрэн хангаж, гараанд гарахад бэлэн болжээ</h3>
            <p style="color:#8b949e; font-size:14px; line-height:1.5;">
                Аргентины шилдэг багийн ахлагч өөрийн сүүлийн ДАШТ-ий тактик бэлтгэлдээ ямар нэгэн бэртэлгүй оролцлоо. 
                Тэрээр өөрийн сүүлийн тэмцээнийг албан ёсоор ялалтаар эхлүүлэхийг зорьж байна.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    with n2:
        st.markdown("""
        <div class="news-card">
            <span class="tag-badge">ТАЛБАЙН ЭЗЭД</span>
            <p class="group-sub">А БҮЛЭГ</p>
            <h3 style="color:#ffffff; margin-top:10px;">Ацтека цэнгэлдэх хөдөлгөөнд дарагдав: Мексикийн довтолгоо Өмнөд Африкийг сандаргав</h3>
            <p style="color:#8b949e; font-size:14px; line-height:1.5;">
                Хөгжөөн дэмжигчдийн нүргээн дунд Хулиан Киньонес болон Рауль Хименес нарын гайхалтай довтолгоо 
                талбайн эзэд эхний 3 оноо авахад голлох үүргийг гүйцэтгэж, багийн тактикийг амжилттай болголоо.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    with n3:
        st.markdown("""
        <div class="news-card">
            <span class="tag-badge">ТАКТИК ШИНЖИЛГЭЭ</span>
            <p class="group-sub">D БҮЛЭГ</p>
            <h3 style="color:#ffffff; margin-top:10px;">Кристиан Пулишичийн тактик дуулиан тарив: АНУ-ын шигшээ Парагвайг 4-1 бут ниргэлээ</h3>
            <p style="color:#8b949e; font-size:14px; line-height:1.5;">
                SoFi Stadium-д явагдсан тоглолтод Пулишич тоглолтыг бүрэн удирдаж, 1 гол, 2 оновчтой дамжуулалт өгснөөр 
                тоглолтын шилдэг тоглогч болсон бөгөөд Парагвайн хамгаалалтыг бүрэн эвдэж чадлаа.
            </p>
        </div>
        """, unsafe_allow_html=True)

elif navigation == "🔮 ТОГЛОЛТЫН ТААМАГЛАЛ":
    st.title("🔮 Тэмцээний Үр Дүн Тааварлах")
    st.markdown("Удахгүй болох тоглолтуудын оноог тааж системд бүртгүүлээрэй.")
    
    with st.form("prediction_engine"):
        st.subheader("Иран vs Шинэ Зеланд")
        score_iran = st.number_input("Иран Улсын Оноо", min_value=0, max_value=15, step=1, value=0)
        score_nz = st.number_input("Шинэ Зеланд Улсын Оноо", min_value=0, max_value=15, step=1, value=0)
        
        submit_btn = st.form_submit_button("Таамаглалыг Илгээх", type="primary")
        if submit_btn:
            st.success(f"Таны таамаглал амжилттай хадгалагдлаа: Иран {score_iran} - {score_nz} Шинэ Зеланд")
