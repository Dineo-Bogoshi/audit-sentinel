import streamlit as st

def render_metrics_grid(processed: int, exceptions: int):
    risk_rate = (exceptions / processed * 100) if processed > 0 else 0.0
    status_text = "Requires review" if risk_rate > 0 else "Compliant"
    accent_border = "var(--danger)" if risk_rate > 0 else "var(--success)"

    st.markdown(
        f"""
        <style>
            .metric-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; margin: 0.5rem 0 1.5rem 0; }}
            .metric-card {{
                background: var(--paper); border: 2px solid var(--ink); border-radius: 14px;
                padding: 18px 20px; box-shadow: 3px 3px 0px var(--ink);
            }}
            .metric-card .metric-label {{
                font-family: 'Geist Mono', monospace; font-size: 0.7rem; text-transform: uppercase;
                letter-spacing: 0.08em; color: var(--muted); margin-bottom: 6px; font-weight: 600;
            }}
            .metric-card .metric-value {{ font-size: 1.8rem; font-weight: 700; color: var(--ink); }}
            .metric-card .metric-sub {{ font-size: 0.85rem; margin-top: 4px; font-weight: 600; }}
        </style>
        <div class="metric-grid">
            <div class="metric-card">
                <div class="metric-label">Processed records</div>
                <div class="metric-value mono">{processed:,}</div>
            </div>
            <div class="metric-card" style="border-color: {accent_border};">
                <div class="metric-label">Flagged exceptions</div>
                <div class="metric-value mono">{exceptions:,}</div>
                <div class="metric-sub" style="color: {accent_border};">{risk_rate:.1f}% risk rate</div>
            </div>
            <div class="metric-card" style="border-color: {accent_border};">
                <div class="metric-label">Governance status</div>
                <div class="metric-value">{status_text}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )