import streamlit as st

def render_stepper(current_stage: int):
    steps = [
        ("1", "Ingestion"),
        ("2", "Sanity Check + Anomaly"),
        ("3", "Audit Visuals"),
    ]

    html = """
    <style>
        .stepper { display: flex; align-items: center; justify-content: space-between; margin: 1.5rem 0; width: 100%; }
        .step { display: flex; flex-direction: column; align-items: center; gap: 6px; flex: 1; }
        .step .dot {
            width: 34px; height: 34px; border-radius: 50%; display: flex; align-items: center; justify-content: center;
            font-family: 'Geist Mono', monospace; font-size: 0.85rem; font-weight: 700;
            border: 2px solid var(--ink); color: var(--ink); background: #ffffff;
        }
        .step.active .dot { background: var(--paper); border-color: var(--ink); }
        .step.done .dot { background: var(--ink); color: #ffffff; }
        .step .label { font-size: 0.78rem; color: var(--muted); text-align: center; font-weight: 500; }
        .step.active .label, .step.done .label { color: var(--ink); font-weight: 700; }
        .connector { flex: 1; height: 2px; background: var(--ink); margin: 0 4px 22px 4px; }
    </style>
    <div class="stepper">
    """
    
    for i, (num, label) in enumerate(steps):
        if i < current_stage:
            cls, glyph = "done", "✓"
        elif i == current_stage:
            cls, glyph = "active", num
        else:
            cls, glyph = "", num
            
        html += f'<div class="step {cls}"><div class="dot">{glyph}</div><div class="label">{label}</div></div>'
        if i < len(steps) - 1:
            html += '<div class="connector"></div>'
            
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)