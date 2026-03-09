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
    }
    .stButton>button { 
        background-color: #d4af37; color: #0c0c0c; 
        border-radius: 0px; border: none; font-weight: bold; width: 100%; 
    }
    .report-box { 
        border: 1px solid #d4af37; padding: 30px; 
        background-color: #1a1a1a; color: #ffffff; 
        line-height: 1.8; height: auto; overflow: visible; white-space: pre-wrap; 
    }
    h1, h2, h3 { color: #d4af37 !important; }
    .stTextArea textarea { background-color: #1a1a1a; color: #ffffff; border: 1px solid #333; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="sovereign-logo">Σ</div>', unsafe_allow_html=True)
st.title("Sovereign OS | Protocol 07")
st.subheader("Autonomous Risk Architecture & Decision Engine")

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=st.secrets.get("HF_TOKEN")
)

# تحديد مسار النموذج المستقر
STABLE_MODEL = "meta-llama/Llama-3.3-70B-Instruct"

strategic_context = st.text_area("Provide the strategic challenge or invisible asset:", height=150)

if st.button("EXECUTE PROTOCOL 07"):
    if not strategic_context:
        st.error("Strategic Context is required for architectural validation.")
    else:
        with st.spinner("Decoding Structural Failures..."):
            try:
                # المرحلة 1: التقدير التلقائي
                estimation_prompt = f"Analyze: '{strategic_context}'. Return strictly as dictionary: IA (1-10), SRF (1-10), RE (1-10)."
                
                est_response = client.chat.completions.create(
                    model=STABLE_MODEL,
                    messages=[{"role": "system", "content": "Extract values strictly for Protocol 07. No prose."},
                              {"role": "user", "content": estimation_prompt}]
                )
                
                raw_val = est_response.choices[0].message.content
                values = {k: float(v) for k, v in re.findall(r'(\w+)\s*[:=]\s*(\d+\.?\d*)', raw_val)}
                
                IA = values.get('IA', 5.0)
                SRF = values.get('SRF', 1.0)
                RE = values.get('RE', 3.0)
                
                SR = (IA * SRF) / RE

                # المرحلة 2: التقرير النهائي
                report_prompt = f"Context: {strategic_context}. Calculated SR: {SR:.2f}. Generate a Decisive Report: Threat Vector, Risk Clause, Action Protocols, Exit Criteria. Technical English only."
                
                final_report = client.chat.completions.create(
                    model=STABLE_MODEL,
                    messages=[{"role": "system", "content": "Architect of Sovereign OS. Minimalist tone."},
                              {"role": "user", "content": report_prompt}]
                )

                content = final_report.choices[0].message.content

                st.markdown("---")
                st.markdown(f"### Sovereign Decision Result: **{SR:.2f}**")
                st.markdown(f'<div class="report-box">{content}</div>', unsafe_allow_html=True)
                
                st.download_button(
                    label="Download Full Decision Protocol",
                    data=content,
                    file_name="Sovereign_OS_Verdict.txt",
                    mime="text/plain"
                )
                
            except Exception as e:
                st.error(f"Structural Integrity Compromised: {str(e)}")

st.markdown("---")
st.caption("Eman El Shafie | Sovereign OS Architect | Eudaimonics Theory Founder")
