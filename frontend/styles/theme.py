import streamlit as st

def inject_custom_styles():
    st.markdown(
        """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=Geist+Mono:wght@400;500;600&display=swap');

            :root {
                --ink: #000000;
                --paper: #fbec8c;
                --canvas: #cff1fa;
                --muted: #4a4a4a;
                --line: #000000;
                --danger: #c23934;
                --success: #1f9254;
            }

            html, body, [class*="css"] {
                font-family: 'Poppins', sans-serif !important;
                color: var(--ink) !important;
            }

            .mono { font-family: 'Geist Mono', monospace !important; }

            /* Hide Sidebar */
            [data-testid="stSidebar"], [data-testid="collapsedControl"] { display: none; }

            /* Container Settings */
            .block-container,
            [data-testid="stAppViewContainer"] .main .block-container {
                background: #ffffff;
                border: 2px solid var(--ink);
                border-radius: 20px;
                padding: 2rem 2.5rem 3rem 2.5rem !important;
                margin-top: 1rem;
                margin-bottom: 2rem;
                max-width: 1050px;
                box-shadow: 6px 6px 0px var(--ink);
            }

            /* Section headers */
            .stage-container {
                scroll-margin-top: 2rem;
                padding-top: 0.5rem;
            }
            .stage-title {
                font-size: 1.35rem;
                font-weight: 700;
                letter-spacing: -0.01em;
                color: var(--ink);
                margin-top: 1rem;
                margin-bottom: 0.5rem;
                display: flex;
                align-items: center;
                gap: 10px;
            }
            .stage-pill {
                display: inline-block;
                font-size: 0.72rem;
                font-weight: 700;
                text-transform: uppercase;
                letter-spacing: 0.06em;
                padding: 4px 12px;
                border: 1.5px solid var(--ink);
                border-radius: 999px;
                background-color: var(--paper);
                color: var(--ink);
            }
            .helper-text {
                color: var(--muted);
                font-size: 0.92rem;
                margin-top: -0.25rem;
                margin-bottom: 1rem;
            }

            /* Active Stage Card Focus */
            .action-card {
                background: var(--paper);
                border: 2px solid var(--ink);
                border-radius: 16px;
                padding: 1.5rem;
                margin: 1rem 0;
                box-shadow: 4px 4px 0px var(--ink);
            }

            /* Buttons */
            .stButton > button[kind="primary"], .stButton > button {
                background: var(--ink) !important;
                color: #ffffff !important;
                border: 2px solid var(--ink) !important;
                border-radius: 999px !important;
                padding: 0.6rem 2rem !important;
                font-weight: 600 !important;
                width: 100% !important;
                max-width: 320px !important;
                box-shadow: 3px 3px 0px var(--paper);
            }
            .stButton > button:hover {
                transform: translate(-1px, -1px);
                box-shadow: 4px 4px 0px var(--paper);
            }

            /* File uploader dropzone */
            [data-testid="stFileUploaderDropzone"] {
                border: 2px dashed var(--ink) !important;
                border-radius: 16px !important;
                background: var(--paper) !important;
            }

            /* Dataframe styling */
            [data-testid="stDataFrame"] {
                border-radius: 12px;
                border: 2px solid var(--ink);
            }
        </style>
        """,
        unsafe_allow_html=True,
    )