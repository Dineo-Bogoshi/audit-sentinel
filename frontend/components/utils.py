import streamlit as st

def scroll_to_element(element_id: str):
    """Injects JavaScript to smoothly scroll to a specific HTML element ID."""
    js = f"""
    <script>
        setTimeout(function() {{
            var element = parent.document.getElementById('{element_id}');
            if (element) {{
                element.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
            }}
        }}, 150);
    </script>
    """
    st.html(js)