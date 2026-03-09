import streamlit as st
from openai import OpenAI
import re

# 1. إعدادات الواجهة السيادية المحدثة (Sovereign UI v7)
st.set_page_config(page_title="Sovereign Decision Engine v7", layout="wide")

st.markdown("""
    <style>
    /* التنسيق اللوني: فحمي، ذهبي، أبيض */
    .main { background-color: #0c0c0c; color: #ffffff; font-family: 'Segoe UI', sans-serif; }
    
    /* شعار المحرك الاحترافي - محاكاة لهوية جيت هب السيادية */
    .engine-seal {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 15px;
        padding: 20px;
        background: linear-gradient(145deg, #1a1a1a, #0c0c0c);
        border: 1px solid #d4af37;
        border-radius: 12px;
        margin-bottom: 30px;
        box-shadow: 0 4px 15px rgba(212, 175, 55, 0.1);
    }
    .seal-icon { font-size: 50px; color: #d4af37; }
    .seal-text { color: #d4af37; font-weight: bold; font-size: 1.5rem; letter-spacing: 2px; }

    /* أزرار التنفيذ */
    .stButton>button { 
        background-color: #d4af37; color: #0c0c0c; 
        border-radius: 4px; border: none; font-weight: bold; 
        height: 3em; transition: 0.4s;
    }
    .stButton>button:hover {
        background-color: #ffffff;
        box-shadow: 0 0 20px rgba(212, 175, 55, 0.4);
    }

    /* صندوق التقرير الحاسم */
    .report-box { 
        border: 1px solid #333;
        border-left: 4px solid #d4af37;
        padding: 25px; 
        background-color: #111111; color: #f0f0f0; 
        line-height: 1.6;
    }
    
    .signature-area {
        margin-top: 50px;
        padding-top: 20px;
        border-top: 1px solid #333;
        display: flex;
        align-items: center;
        justify-content: space-between;
        color: #888;
    }
    </style>
    """, unsafe_allow_html=True)

# هيدر المحرك (الختم السيادي الجديد)
st.markdown("""
    <div class="engine-seal">
        <div class="seal-icon">⚙️🦋</div>
        <div class="seal-text">SOVEREIGN ENGINE v7</div>
    </div>
    """, unsafe_allow_html=True)

st.title("Architectural Validation | Protocol 07")

# إعداد العميل
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=st.secrets.get("HF_TOKEN")
)

STABLE_MODEL = "meta-llama/Llama-3.3-70B-Instruct"

# إدخال السياق الاستراتيجي
strategic_context = st.text_area("Input Strategic Context:", 
                                 placeholder="Enter expansion details or risk vectors...", 
                                 height=150)

if st.button("EXECUTE SOVEREIGN ANALYSIS"):
    if not strategic_context:
        st.error("Protocol Error: Strategic Context missing.")
    else:
        with st.spinner("Analyzing Structural Gaps..."):
            try:
                # منطق استخراج الأرقام (IA, SRF, RE) بناءً على الورقة رقم 07
                estimation_prompt = f"Analyze: '{strategic_context}'. Extract strictly: IA:val, SRF:val, RE:val."
                est_res = client.chat.completions.create(
                    model=STABLE_MODEL,
                    messages=[{"role": "user", "content": estimation_prompt}]
                )
                
                raw_val = est_res.choices[0].message.content
                values = {k: float(v) for k, v in re.findall(r'(\w+)\s*[:=]\s*(\d+\.?\d*)', raw_val)}
                
                IA = values.get('IA', 5.0)
                SRF = values.get('SRF', 1.0)
                RE = values.get('RE', 3.0)
                SR = (IA * SRF) / RE # معادلة الجاهزية السيادية

                # توليد التقرير النهائي
                report_prompt = f"Context: {strategic_context}. SR: {SR:.2f}. Generate: Threat Vector, Risk Clause, Action Protocols, Exit Criteria. Tone: Decisive Simplicity."
                final_res = client.chat.completions.create(
                    model=STABLE_MODEL,
                    messages=[{"role": "system", "content": "You are the Sovereign OS Architect."}, {"role": "user", "content": report_prompt}]
                )

                # عرض النتائج
                st.markdown(f"### Sovereign Ratio: `{SR:.2f}`")
                st.markdown(f'<div class="report-box">{final_res.choices[0].message.content}</div>', unsafe_allow_html=True)
                
                st.download_button("Download Report", final_res.choices[0].message.content, "Sovereign_Report.txt")

            except Exception as e:
                st.error(f"Integrity Error: {str(e)}")

# التوقيع النهائي مع الختم المطلوب (الفراشة والترس)
st.markdown(f"""
    <div class="signature-area">
        <div>Eman El Shafie | Eudaimonics Theory Founder</div>
        <div style="font-size: 24px;">🦋⚙️</div>
    </div>
    """, unsafe_allow_html=True)
