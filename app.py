import streamlit as st
from openai import OpenAI
import re

# 1. إعدادات الواجهة السيادية (Sovereign UI v7.0 - Elite)
st.set_page_config(page_title="Sovereign OS | Protocol 07", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0c0c0c; color: #d4af37; font-family: 'Segoe UI', sans-serif; }
    
    /* شعار المحرك الاحترافي - الفراشة والترس */
    .sovereign-header {
        text-align: center;
        padding: 20px;
        background: linear-gradient(180deg, #1a1a1a 0%, #0c0c0c 100%);
        border-bottom: 1px solid #d4af37;
        margin-bottom: 30px;
    }
    .sovereign-logo {
        font-size: 60px;
        filter: drop-shadow(0 0 15px rgba(212, 175, 55, 0.4));
        margin-bottom: 10px;
    }
    
    .stButton>button { 
        background-color: #d4af37; color: #0c0c0c; 
        border-radius: 0px; border: none; font-weight: bold; width: 100%; 
        transition: 0.3s; letter-spacing: 2px;
    }
    .stButton>button:hover {
        background-color: #ffffff; color: #0c0c0c;
        box-shadow: 0 0 20px rgba(212, 175, 55, 0.6);
    }
    .report-box { 
        border-left: 5px solid #d4af37; padding: 35px; 
        background-color: #111; color: #ffffff; 
        line-height: 1.8; font-family: 'Inter', sans-serif;
        box-shadow: inset 0 0 15px rgba(0,0,0,0.5);
    }
    .metric-value { font-size: 3rem; font-weight: bold; color: #d4af37; text-shadow: 0 0 10px rgba(212, 175, 55, 0.3); }
    h1, h2, h3 { color: #d4af37 !important; text-transform: uppercase; letter-spacing: 3px; }
    .stTextArea textarea { background-color: #1a1a1a; color: #ffffff; border: 1px solid #333; }
    
    .signature-seal {
        display: flex; align-items: center; justify-content: flex-end;
        gap: 15px; margin-top: 60px; color: #d4af37; font-size: 1rem;
        border-top: 1px solid #1a1a1a; padding-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# الهيدر السيادي الجديد (🦋⚙️)
st.markdown("""
    <div class="sovereign-header">
        <div class="sovereign-logo">🦋⚙️</div>
        <h1 style="margin:0;">Sovereign Engine v7</h1>
        <p style="color:#888; letter-spacing:5px;">ARCHITECTURAL VALIDATION SYSTEM</p>
    </div>
    """, unsafe_allow_html=True)

# إعداد العميل
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=st.secrets.get("HF_TOKEN")
)

STABLE_MODEL = "meta-llama/Llama-3.3-70B-Instruct"

# المدخلات الاستراتيجية
strategic_context = st.text_area("Input Strategic Context (Expansion, Risk, or Asset):", 
                                 placeholder="Define the structural gap or invisible asset to be validated...",
                                 height=150)

if st.button("EXECUTE SOVEREIGN VERDICT"):
    if not strategic_context:
        st.error("Protocol Error: Strategic Context is required to bridge structural gaps.")
    else:
        with st.spinner("Decoding Invisible Assets & Calculating Sovereign Certainty..."):
            try:
                # المرحلة 1: استخراج القيم الرقمية
                estimation_prompt = f"Analyze: '{strategic_context}'. Return strictly as: IA:value, SRF:value, RE:value. (Scale 1-10)"
                
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
                
                # معادلة السيادة
                SR = (IA * SRF) / RE

                # المرحلة 2: توليد التقرير المعماري
                report_prompt = f"""
                Context: {strategic_context}
                Sovereign Ratio (SR): {SR:.2f}
                Task: Generate a 'Sovereign Certainty Report'. 
                Sections: 
                1. Structural Gap Analysis (Identify the fragile nodes).
                2. Invisible Asset Activation (Unlocking hidden wings).
                3. Risk Mitigation Protocols (Technical protective steps).
                4. Sovereign Verdict (Final Architectural Decision).
                Tone: Decisive Simplicity, Elite, Non-Therapeutic.
                """
                
                final_report = client.chat.completions.create(
                    model=STABLE_MODEL,
                    messages=[{"role": "system", "content": "You are the Architect of Sovereign OS. Convert failures into protective protocols."},
                              {"role": "user", "content": report_prompt}]
                )

                content = final_report.choices[0].message.content

                # عرض النتائج النهائية
                st.markdown("---")
                col1, col2 = st.columns([1, 2])
                with col1:
                    st.markdown("### Sovereign Ratio")
                    st.markdown(f'<p class="metric-value">{SR:.2f}</p>', unsafe_allow_html=True)
                    if SR >= 1.5:
                        st.success("STATUS: SOVEREIGN (GO)")
                    else:
                        st.warning("STATUS: FRAGILE (NO-GO)")

                with col2:
                    st.markdown(f'<div class="report-box">{content}</div>', unsafe_allow_html=True)
                
                st.download_button(
                    label="DOWNLOAD ARCHITECTURAL VERDICT (PDF/TXT)",
                    data=content,
                    file_name="Sovereign_OS_Verdict.txt",
                    mime="text/plain"
                )
                
            except Exception as e:
                st.error(f"Integrity Compromised: {str(e)}")

# التوقيع الختامي (الختم السيادي)
st.markdown(f"""
    <div class="signature-seal">
        <span>Eman El Shafie | Sovereign OS Architect | Eudaimonics Theory Founder</span>
        <span style="font-size: 30px; filter: drop-shadow(0 0 5px #d4af37);">🦋⚙️</span>
    </div>
    """, unsafe_allow_html=True)
