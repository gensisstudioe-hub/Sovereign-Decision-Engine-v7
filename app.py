import streamlit as st
from openai import OpenAI
import re
import os
import base64

# 1. إعدادات الواجهة السيادية (Sovereign UI v7.0)
st.set_page_config(page_title="Sovereign OS | Protocol 07", layout="wide")

# دالة تحويل الصورة لليقين البصري (Base64) لضمان الاستقرار التشغيلي
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except Exception:
        return None

st.markdown("""
    <style>
    .main { background-color: #0c0c0c; color: #d4af37; font-family: 'Segoe UI', sans-serif; }
    
    /* أيقونة الزيتا - رمز الجدارة الرياضية والمعادلة */
    .sovereign-logo {
        width: 80px; height: 80px; border: 2px solid #d4af37;
        margin-bottom: 20px; display: flex; align-items: center;
        justify-content: center; font-weight: bold; font-size: 32px;
        color: #d4af37; background: linear-gradient(45deg, #1a1a1a, #0c0c0c);
        box-shadow: 0 0 15px rgba(212, 175, 55, 0.2);
    }
    
    .stButton>button { 
        background-color: #d4af37; color: #0c0c0c; 
        border-radius: 0px; border: none; font-weight: bold; width: 100%; 
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #ffffff; color: #0c0c0c;
        box-shadow: 0 0 20px rgba(212, 175, 55, 0.4);
    }
    .report-box { 
        border-left: 5px solid #d4af37; padding: 30px; 
        background-color: #1a1a1a; color: #ffffff; 
        line-height: 1.8; font-family: 'Courier New', Courier, monospace;
    }
    .metric-value { font-size: 2.5rem; font-weight: bold; color: #d4af37; }
    h1, h2, h3 { color: #d4af37 !important; }
    .stTextArea textarea { background-color: #1a1a1a; color: #ffffff; border: 1px solid #333; }
    
    .signature-seal {
        display: flex; align-items: center; justify-content: flex-end;
        gap: 15px; margin-top: 50px; color: #d4af37; font-size: 0.95rem;
        border-top: 1px solid #1a1a1a; padding-top: 20px;
    }
    .sovereign-icon-img {
        filter: drop-shadow(0 0 5px #d4af37);
        border-radius: 4px;
    }
    </style>
    """, unsafe_allow_html=True)

# استعادة الهيبة الرياضية بالزيتا (Σ)
st.markdown('<div class="sovereign-logo">Σ</div>', unsafe_allow_html=True)
st.title("Sovereign Engine | v7.0")
st.subheader("Architectural Validation & Decision Logic")

# إعداد العميل (Hugging Face / OpenAI)
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=st.secrets.get("HF_TOKEN")
)

STABLE_MODEL = "meta-llama/Llama-3.3-70B-Instruct"

strategic_context = st.text_area("Input Strategic Context (Expansion, Risk, or Asset):", 
                                 placeholder="e.g., 40% Factory Expansion in Dubai...",
                                 height=150)

if st.button("CALCULATE SOVEREIGN CERTAINTY"):
    if not strategic_context:
        st.error("Protocol Error: Strategic Context is required.")
    else:
        with st.spinner("Decoding Structural Failures..."):
            try:
                # المرحلة 1: استخراج القيم بناءً على الورقة رقم 07
                estimation_prompt = f"Analyze: '{strategic_context}'. Return strictly as: IA:value, SRF:value, RE:value. (Values 1-10)"
                
                est_response = client.chat.completions.create(
                    model=STABLE_MODEL,
                    messages=[{"role": "system", "content": "You are the Sovereign OS Logic Engine. Extract numerical values for risk architecture."},
                              {"role": "user", "content": estimation_prompt}]
                )
                
                raw_val = est_response.choices[0].message.content
                values = {k: float(v) for k, v in re.findall(r'(\w+)\s*[:=]\s*(\d+\.?\d*)', raw_val)}
                
                IA = values.get('IA', 5.0)
                SRF = values.get('SRF', 1.0)
                RE = values.get('RE', 3.0)
                
                # تطبيق معادلة الجاهزية السيادية: SR = (IA * SRF) / RE
                SR = (IA * SRF) / RE

                # المرحلة 2: توليد التقرير الحاسم بلغة "البساطة الحاسمة"
                report_prompt = f"Context: {strategic_context}. SR: {SR:.2f}. Generate: Threat Vector, Risk Clause, Action Protocols, Exit Criteria."
                
                final_report = client.chat.completions.create(
                    model=STABLE_MODEL,
                    messages=[{"role": "system", "content": "Architect of Sovereign OS. Minimalist tone."},
                              {"role": "user", "content": report_prompt}]
                )

                content = final_report.choices[0].message.content

                st.markdown("---")
                col1, col2 = st.columns([1, 3])
                with col1:
                    st.markdown("### Sovereign Ratio")
                    st.markdown(f'<p class="metric-value">{SR:.2f}</p>', unsafe_allow_html=True)
                    if SR >= 1.5:
                        st.success("STATUS: SOVEREIGN")
                    else:
                        st.warning("STATUS: FRAGILE")

                with col2:
                    st.markdown(f'<div class="report-box">{content}</div>', unsafe_allow_html=True)
                
                st.download_button(label="DOWNLOAD ARCHITECTURAL VERDICT", data=content, file_name="Sovereign_OS_Report.txt")
                
            except Exception as e:
                st.error(f"Structural Integrity Compromised: {str(e)}")

# التوقيع النهائي المدعوم بـ "اليقين البصري"
st.markdown("---")
icon_path = "sovereign_icon.png"
img_base64 = get_base64_image(icon_path)

if img_base64:
    st.markdown(f"""
        <div class="signature-seal">
            <div style="text-align: right;">
                <span style="display: block; font-weight: bold;">Eman El Shafie</span>
                <span style="display: block; font-size: 0.8rem; opacity: 0.8;">Founder & Sovereign OS Architect</span>
                <span style="display: block; font-size: 0.8rem; opacity: 0.8;">Genesis Logic Lab</span>
            </div>
            <img src="data:image/png;base64,{img_base64}" class="sovereign-icon-img" width="50">
        </div>
        """, unsafe_allow_html=True)
else:
    # حل احتياطي في حال عدم العثور على الصورة (Fallback)
    st.markdown(f"""
        <div class="signature-seal">
            <div style="text-align: right;">
                <span style="display: block; font-weight: bold;">Eman El Shafie</span>
                <span style="display: block; font-size: 0.8rem; opacity: 0.8;">Founder & Sovereign OS Architect</span>
                <span style="display: block; font-size: 0.8rem; opacity: 0.8;">Genesis Logic Lab</span>
            </div>
            <span style="font-size: 30px; filter: drop-shadow(0 0 5px #d4af37);">⚙️🦋</span>
        </div>
        """, unsafe_allow_html=True)
