import streamlit as st
from openai import OpenAI
import re

# 1. إعدادات الواجهة السيادية (Sovereign UI)
st.set_page_config(page_title="Sovereign OS | Protocol 07", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0c0c0c; color: #d4af37; font-family: 'Segoe UI', sans-serif; }
    .sovereign-logo {
        width: 80px; height: 80px; border: 2px solid #d4af37;
        margin-bottom: 20px; display: flex; align-items: center;
        justify-content: center; font-weight: bold; font-size: 24px;
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
        line-height: 1.8; height: auto; overflow: visible; white-space: pre-wrap;
        font-family: 'Courier New', Courier, monospace;
    }
    .metric-value { font-size: 2.5rem; font-weight: bold; color: #d4af37; }
    h1, h2, h3 { color: #d4af37 !important; }
    .stTextArea textarea { background-color: #1a1a1a; color: #ffffff; border: 1px solid #333; }
    .signature-seal {
        display: flex; align-items: center; justify-content: flex-end;
        gap: 10px; margin-top: 40px; color: #d4af37; font-size: 0.9rem;
    }
    </style>
    """, unsafe_allow_html=True)

# أيقونة السيادة Σ
st.markdown('<div class="sovereign-logo">Σ</div>', unsafe_allow_html=True)
st.title("Sovereign Engine | v7.0")
st.subheader("Architectural Validation & Sovereign Certainty System")

# إعداد العميل (Hugging Face Interface)
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=st.secrets.get("HF_TOKEN")
)

STABLE_MODEL = "meta-llama/Llama-3.3-70B-Instruct"

# المدخلات الاستراتيجية
strategic_context = st.text_area("Input Strategic Context (Expansion, Risk, or Asset):", 
                                 placeholder="e.g., 40% Factory Expansion in Dubai with Indian/Iranian supply chains...",
                                 height=150)

if st.button("CALCULATE SOVEREIGN CERTAINTY"):
    if not strategic_context:
        st.error("Protocol Error: Strategic Context is required to bridge structural gaps.")
    else:
        with st.spinner("Decoding Invisible Assets & Stress-Testing Systems..."):
            try:
                # المرحلة 1: استخراج القيم (Protocol 07 Logic)
                # IA = Invisible Assets, SRF = Structural Reflection Factor, RE = Risk Exposure
                estimation_prompt = f"Analyze: '{strategic_context}'. Identify Invisible Assets and Structural Fragility. Return strictly as: IA:value, SRF:value, RE:value. (Values 1-10)"
                
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
                
                # معادلة السيادة (Sovereign Ratio)
                # SR = (IA * SRF) / RE
                SR = (IA * SRF) / RE

                # المرحلة 2: توليد التقرير الحاسم (Decisive Report)
                report_prompt = f"""
                Context: {strategic_context}
                Sovereign Ratio (SR): {SR:.2f}
                Task: Generate a 'Sovereign Certainty Report'. 
                Sections: 
                1. Structural Gap Analysis (Where the system is fragile).
                2. Invisible Asset Activation (How to leverage unseen wings).
                3. Risk Mitigation Protocols (Specific technical actions).
                4. Sovereign Verdict (Final Go/No-Go based on SR).
                Tone: Decisive Simplicity, Technical, Minimalist.
                """
                
                final_report = client.chat.completions.create(
                    model=STABLE_MODEL,
                    messages=[{"role": "system", "content": "You are the Architect of Sovereign OS. Convert failures into protective protocols."},
                              {"role": "user", "content": report_prompt}]
                )

                content = final_report.choices[0].message.content

                # عرض النتائج
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
                
                # خيار الطباعة/التحميل
                st.download_button(
                    label="DOWNLOAD ARCHITECTURAL VERDICT",
                    data=content,
                    file_name="Sovereign_OS_Report.txt",
                    mime="text/plain"
                )
                
            except Exception as e:
                st.error(f"Structural Integrity Compromised: {str(e)}")

# التوقيع والختم (الفراشة والترس)
st.markdown("---")
st.markdown(f"""
    <div class="signature-seal">
        <span>Eman El Shafie | Sovereign OS Architect | Eudaimonics Theory Founder</span>
        <span style="font-size: 24px;">🦋⚙️</span>
    </div>
    """, unsafe_allow_html=True)
