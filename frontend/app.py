import streamlit as st
import pandas as pd
from PIL import Image

from styles.theme import inject_custom_styles
from components.stepper import render_stepper
from components.metrics import render_metrics_grid
from components.utils import scroll_to_element
from services.api_client import execute_audit_scan, calculate_file_hash

# 1. Page Config
try:
    img = Image.open("assets/logo.png")
    st.set_page_config(page_title="Audit Sentinel", page_icon=img, layout="wide", initial_sidebar_state="collapsed")
except Exception:
    st.set_page_config(page_title="Audit Sentinel", layout="wide", initial_sidebar_state="collapsed")

inject_custom_styles()

# 2. Hero Banner
try:
    st.image("assets/hero-banner.svg", use_container_width=True)
except Exception:
    st.warning("Hero banner image (`assets/hero-banner.svg`) not found — continuing without it.")

# 3. State Management
uploaded_file_exists = "uploaded_file_data" in st.session_state
results_ready = "audit_results" in st.session_state

current_stage = 0 if not uploaded_file_exists else (1 if not results_ready else 2)

render_stepper(current_stage)

# STAGE 1: INGESTION
st.markdown(
    """
    <div id="stage-0" class="stage-container">
        <div class="stage-title">
            <span class="stage-pill">Ingestion</span>
            <span>Upload your ledger</span>
        </div>
        <p class="helper-text">Drop your financial CSV here, or browse files, to begin automated compliance testing.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

uploaded_file = st.file_uploader(
    label="Upload Financial CSV",
    type=["csv"],
    help="Standard UTF-8 encoded .csv files.",
    label_visibility="collapsed",
)

if uploaded_file and not uploaded_file_exists:
    st.session_state["uploaded_file_data"] = {
        "name": uploaded_file.name,
        "bytes": uploaded_file.getvalue(),
        "size": uploaded_file.size,
    }
    st.toast("File uploaded successfully")
    st.rerun()

# STAGE 2: SCAN
if uploaded_file_exists:
    file_info = st.session_state["uploaded_file_data"]

    st.markdown(
        """
        <div id="stage-1" class="stage-container">
            <div class="stage-title">
                <span class="stage-pill">Sanity Check</span>
                <span class="stage-pill">Anomaly Detection</span>
                <span>Run the audit scan</span>
            </div>
            <p class="helper-text">Sanitizes sensitive data, verifies structure, and flags exceptions against governance rules.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="action-card">', unsafe_allow_html=True)
    st.info(f"**Loaded file:** `{file_info['name']}` ({file_info['size'] / 1024:.1f} KB)")

    if st.button("Run audit scan", type="primary"):
        with st.spinner("Sanitizing data and checking rules..."):
            try:
                file_hash = calculate_file_hash(file_info["bytes"])
                res = execute_audit_scan(file_info["bytes"], file_info["name"], file_hash)
                
                st.session_state["audit_results"] = res
                st.session_state["audit_filename"] = file_info["name"]
                st.toast("Scan complete")
                st.rerun()
            except Exception as e:
                st.error(f"**Scan failed:** {e}")

    st.markdown('</div>', unsafe_allow_html=True)

    if current_stage == 1 and "scrolled_stage_1" not in st.session_state:
        st.session_state["scrolled_stage_1"] = True
        scroll_to_element("stage-1")

# STAGE 3: RESULTS
if "audit_results" in st.session_state:
    data = st.session_state["audit_results"]
    report_filename = st.session_state.get("audit_filename", "report.csv")

    st.divider()
    st.markdown(
        """
        <div id="stage-2" class="stage-container">
            <div class="stage-title">
                <span class="stage-pill">Audit Visuals</span>
                <span>Summary & Exceptions</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    processed = data.get("total_records_processed", 0)
    exceptions = data.get("total_exceptions_found", 0)

    render_metrics_grid(processed, exceptions)

    exceptions_list = data.get("exception_summary", [])
    exceptions_df = pd.DataFrame(exceptions_list)

    if not exceptions_df.empty:
        st.subheader("Flagged outliers and control gaps")
        st.dataframe(exceptions_df, use_container_width=True, hide_index=True)

        csv_report = exceptions_df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="Download exception report (CSV)",
            data=csv_report,
            file_name=f"audit_exceptions_{report_filename}",
            mime="text/csv",
        )
    else:
        st.success("**Zero exceptions flagged.** Every entry passed sanity checks and governance rules.")

    if current_stage == 2 and "scrolled_stage_2" not in st.session_state:
        st.session_state["scrolled_stage_2"] = True
        scroll_to_element("stage-2")