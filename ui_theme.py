# """
# Streamlit UI theme: dark-first fintech styling, top bar, sidebar navigation.
# Logic in app.py is unchanged; this module only handles presentation helpers.
# """

# from __future__ import annotations

# from datetime import datetime
# from html import escape

# # Product branding (shown in browser tab, top bar, and sidebar)
# APP_BRAND_FULL = "Financial Analysis and Stock Trading Analysis"
# APP_BRAND_TAGLINE = "Real-time market insights"

# # (internal_page_key, icon, short_label) — internal keys must match app.py branches
# NAV_DEFINITION = [
#     ("About the Project", "🏠", "Overview"),
#     ("Live News Sentiment", "📰", "News & sentiment"),
#     ("Company Basic Details", "📋", "Company profile"),
#     ("Company Advanced Details", "📊", "Technicals"),
#     ("Google Trends with Forecast", "🔎", "Search trends"),
#     ("Twitter Trends", "𝕏", "Social trends"),
#     ("Meeting Summarization", "🎙️", "Meeting notes"),
# ]


# def _nav_display(internal: str, icon: str, short: str) -> str:
#     return f"{icon}  {short}"


# def init_theme_state(st) -> None:
#     if "ui_theme_is_light" not in st.session_state:
#         st.session_state["ui_theme_is_light"] = False


# def inject_global_css(st) -> None:
#     theme = "light" if st.session_state.get("ui_theme_is_light", False) else "dark"
#     if theme == "light":
#         bg = "#F6F8FA"
#         panel = "#FFFFFF"
#         panel2 = "#EAEEF2"
#         text = "#1F2328"
#         muted = "#656D76"
#         border = "rgba(31,35,40,0.12)"
#         shadow = "0 8px 24px rgba(31,35,40,0.08)"
#     else:
#         bg = "#0E1117"
#         panel = "#161B22"
#         panel2 = "#1C2128"
#         text = "#F0F6FC"
#         muted = "#8B949E"
#         border = "rgba(240,246,252,0.08)"
#         shadow = "0 8px 32px rgba(0,0,0,0.45)"

#     pos = "#00C853"
#     neg = "#FF1744"
#     accent = "#3FB950"

#     st.markdown(
#         f"""
#         <style>
#         @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

#         html, body, .stApp, [data-testid="stAppViewContainer"] {{
#             font-family: 'Inter', 'Segoe UI', system-ui, sans-serif !important;
#             color: {text};
#         }}
#         .stApp {{
#             background-color: {bg} !important;
#         }}
#         /* Streamlit default chrome — without this, a light/white band hides the top of the app */
#         header[data-testid="stHeader"] {{
#             background-color: {bg} !important;
#             background-image: none !important;
#         }}
#         div[data-testid="stToolbar"] {{
#             background-color: {bg} !important;
#         }}
#         div[data-testid="stDecoration"] {{
#             background-image: none !important;
#             background-color: {bg} !important;
#         }}
#         [data-testid="collapsedControl"] {{
#             color: {text} !important;
#         }}
#         /* Main content blocks inherit app background (fixes white strips in column layouts) */
#         .main .block-container {{
#             background-color: transparent !important;
#         }}
#         div[data-testid="column"] {{
#             background-color: transparent !important;
#         }}
#         section.main > div,
#         [data-testid="stAppViewContainer"] > .main {{
#             background-color: {bg} !important;
#         }}
#         /* Text inputs — default Streamlit/BaseWeb is bright white */
#         .stTextInput input,
#         .stTextInput > div > div > input,
#         [data-baseweb="input"] {{
#             background-color: {panel2} !important;
#             color: {text} !important;
#             border-color: {border} !important;
#             border-radius: 10px !important;
#         }}
#         .stTextInput label {{
#             color: {muted} !important;
#         }}
#         section[data-testid="stSidebar"] > div {{
#             background-color: {panel} !important;
#             border-right: 1px solid {border} !important;
#         }}
#         section[data-testid="stSidebar"] * {{
#             color: {text} !important;
#         }}
#         section[data-testid="stSidebar"] .stMarkdown, section[data-testid="stSidebar"] p, section[data-testid="stSidebar"] label {{
#             color: {muted} !important;
#         }}
#         section[data-testid="stSidebar"] h1, section[data-testid="stSidebar"] h2, section[data-testid="stSidebar"] h3 {{
#             color: {text} !important;
#         }}
#         div[data-testid="stVerticalBlock"] > div:has(> label) {{
#             color: {text};
#         }}
#         .block-container {{
#             padding-top: 1.25rem !important;
#             padding-bottom: 3rem !important;
#             max-width: 1200px;
#         }}
#         h1, h2, h3 {{
#             font-weight: 600 !important;
#             letter-spacing: -0.02em;
#         }}
#         .stButton > button {{
#             border-radius: 10px !important;
#             font-weight: 600 !important;
#             border: 1px solid {border} !important;
#             background: {panel2} !important;
#             color: {text} !important;
#             transition: transform 0.15s ease, box-shadow 0.15s ease;
#         }}
#         .stButton > button:hover {{
#             transform: translateY(-1px);
#             box-shadow: {shadow};
#             border-color: {accent} !important;
#         }}
#         div[data-testid="stMetric"] {{
#             background: {panel};
#             border: 1px solid {border};
#             border-radius: 12px;
#             padding: 0.75rem 1rem;
#             box-shadow: {shadow};
#         }}
#         div[data-testid="stMetric"]:hover {{
#             border-color: {accent};
#         }}
#         .topbar-wrap {{
#             background: linear-gradient(180deg, {panel} 0%, {bg} 100%);
#             border: 1px solid {border};
#             border-radius: 14px;
#             padding: 0.65rem 1.1rem;
#             margin-bottom: 1rem;
#             box-shadow: {shadow};
#         }}
#         .topbar-inner {{
#             display: flex;
#             align-items: center;
#             justify-content: space-between;
#             gap: 1rem;
#             flex-wrap: wrap;
#         }}
#         .topbar-brand {{
#             font-size: 1.35rem;
#             font-weight: 700;
#             letter-spacing: -0.03em;
#             color: {text};
#             margin: 0;
#         }}
#         .topbar-brand span {{
#             color: {accent};
#         }}
#         .topbar-brand-long {{
#             font-size: clamp(0.72rem, 1.65vw, 0.92rem);
#             line-height: 1.3;
#             max-width: min(440px, 58vw);
#             flex: 1 1 auto;
#         }}
#         .topbar-meta {{
#             font-size: 0.8rem;
#             color: {muted};
#             white-space: nowrap;
#         }}
#         .sidebar-brand {{
#             display: flex;
#             align-items: center;
#             gap: 0.65rem;
#             margin-bottom: 0.5rem;
#         }}
#         .sb-logo {{
#             width: 40px;
#             height: 40px;
#             border-radius: 10px;
#             background: linear-gradient(135deg, {accent}, #238636);
#             color: #fff;
#             display: flex;
#             align-items: center;
#             justify-content: center;
#             font-weight: 800;
#             font-size: 1.1rem;
#         }}
#         .sb-title {{ font-weight: 700; font-size: 1rem; color: {text}; }}
#         .sb-title-long {{
#             font-weight: 600;
#             font-size: 0.74rem;
#             line-height: 1.35;
#             max-width: 188px;
#         }}
#         .sb-sub {{ font-size: 0.72rem; color: {muted}; margin-top: 2px; }}
#         .page-card {{
#             background: {panel};
#             border: 1px solid {border};
#             border-radius: 14px;
#             padding: 1.1rem 1.25rem;
#             margin-bottom: 1rem;
#             box-shadow: {shadow};
#         }}
#         .hero-header {{
#             background: linear-gradient(135deg, {panel2} 0%, {panel} 100%);
#             border: 1px solid {border};
#             border-radius: 16px;
#             padding: 1.25rem 1.5rem;
#             margin-bottom: 1.25rem;
#             box-shadow: {shadow};
#         }}
#         .hero-ticker {{ font-size: 2rem; font-weight: 800; letter-spacing: -0.04em; color: {text}; }}
#         .hero-name {{ font-size: 1rem; color: {muted}; margin-top: 0.25rem; }}
#         .hero-price {{ font-size: 1.75rem; font-weight: 700; margin-top: 0.5rem; color: {text}; }}
#         .hero-chg-pos {{ color: {pos}; font-weight: 600; }}
#         .hero-chg-neg {{ color: {neg}; font-weight: 600; }}
#         .rail-card {{
#             background: {panel};
#             border: 1px solid {border};
#             border-radius: 12px;
#             padding: 0.85rem 1rem;
#             margin-bottom: 0.65rem;
#             font-size: 0.82rem;
#             color: {muted};
#         }}
#         .rail-title {{ font-weight: 600; color: {text}; margin-bottom: 0.35rem; font-size: 0.88rem; }}
#         .stRadio > div {{ gap: 0.35rem; }}
#         .stRadio label {{
#             border-radius: 10px !important;
#             padding: 0.4rem 0.5rem !important;
#             border: 1px solid transparent;
#         }}
#         .stRadio label:hover {{
#             background: {panel2} !important;
#             border-color: {border} !important;
#         }}
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )


# def render_theme_toggle(st) -> None:
#     init_theme_state(st)
#     st.sidebar.toggle("Light mode", key="ui_theme_is_light")


# def render_top_bar(st) -> None:
#     now = datetime.now().strftime("%Y-%m-%d · %H:%M")
#     first, _, rest = APP_BRAND_FULL.partition(" ")
#     brand_html = (
#         f'<p class="topbar-brand topbar-brand-long">'
#         f'<span>{escape(first)}</span> {escape(rest)}</p>'
#     )
#     st.markdown(
#         f"""
#         <div class="topbar-wrap">
#           <div class="topbar-inner">
#             {brand_html}
#             <p class="topbar-meta">{now}</p>
#           </div>
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )
#     # Avoid an empty leading column (can render as a large light block in some Streamlit versions)
#     c_search, c_meta = st.columns([3.2, 1])
#     with c_search:
#         st.text_input(
#             "Ticker lookup",
#             placeholder="Quick search ticker (e.g. MSFT)",
#             key="global_ticker_search",
#             label_visibility="collapsed",
#         )
#     with c_meta:
#         st.caption("Notifications · —")


# def render_sidebar_navigation(st) -> str:
#     logo_letter = escape(APP_BRAND_FULL.strip()[0].upper())
#     st.sidebar.markdown(
#         f"""
#         <div class="sidebar-brand">
#           <div class="sb-logo">{logo_letter}</div>
#           <div>
#             <div class="sb-title sb-title-long">{escape(APP_BRAND_FULL)}</div>
#             <div class="sb-sub">{escape(APP_BRAND_TAGLINE)}</div>
#           </div>
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )
#     render_theme_toggle(st)
#     st.sidebar.markdown("##### Navigate")
#     options_display = [_nav_display(*row) for row in NAV_DEFINITION]
#     internal_by_display = {_nav_display(*row): row[0] for row in NAV_DEFINITION}
#     choice = st.sidebar.radio(
#         "nav",
#         options_display,
#         label_visibility="collapsed",
#         key="sidebar_nav_radio",
#     )
#     st.sidebar.markdown("---")
#     st.sidebar.caption("Roadmap")
#     st.sidebar.caption("Portfolio · Alerts · Screener (coming soon)")
#     return internal_by_display[choice]


# def render_company_hero(st, ticker: str, info: dict) -> None:
#     name = info.get("longName") or info.get("shortName") or ticker
#     price = info.get("regularMarketPrice") or info.get("currentPrice")
#     prev = info.get("previousClose")
#     cur = info.get("currency") or "USD"
#     chg_pct = None
#     if price is not None and prev not in (None, 0):
#         try:
#             chg_pct = (float(price) - float(prev)) / float(prev) * 100.0
#         except (TypeError, ValueError):
#             chg_pct = None
#     chg_cls = "hero-chg-pos" if (chg_pct is not None and chg_pct >= 0) else "hero-chg-neg"
#     chg_txt = ""
#     if chg_pct is not None:
#         sign = "+" if chg_pct >= 0 else ""
#         chg_txt = f'<span class="{chg_cls}">{sign}{chg_pct:.2f}%</span> vs prior close'
#     price_txt = f"{price:,.2f}" if isinstance(price, (int, float)) else (str(price) if price else "—")

#     st.markdown(
#         f"""
#         <div class="hero-header">
#           <div class="hero-ticker">{ticker}</div>
#           <div class="hero-name">{name}</div>
#           <div class="hero-price">{price_txt} <span style="font-size:0.95rem;font-weight:500;">{cur}</span></div>
#           <div style="margin-top:0.35rem;font-size:0.9rem;">{chg_txt}</div>
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )
#     b1, b2, _ = st.columns([1, 1, 2])
#     with b1:
#         st.button("Add to watchlist", key="watchlist_btn", disabled=True, help="Coming soon")
#     with b2:
#         st.button("Export snapshot", key="export_btn", disabled=True, help="Coming soon")


# def _fmt_metric(v) -> str:
#     if v is None or v == "N/A":
#         return "—"
#     try:
#         if isinstance(v, (int, float)):
#             if abs(v) >= 1e12:
#                 return f"{v / 1e12:.2f}T"
#             if abs(v) >= 1e9:
#                 return f"{v / 1e9:.2f}B"
#             if abs(v) >= 1e6:
#                 return f"{v / 1e6:.2f}M"
#             if abs(v) >= 1000:
#                 return f"{v:,.0f}"
#             return f"{v:,.4g}".rstrip("0").rstrip(".")
#     except (TypeError, ValueError):
#         pass
#     return str(v)


# def render_metric_strip(st, info: dict) -> None:
#     mcap = info.get("marketCap")
#     pe = info.get("forwardPE") or info.get("trailingPE")
#     divy = info.get("dividendYield")
#     if isinstance(divy, float) and 0 < divy < 1:
#         divy_disp = f"{divy * 100:.2f}%"
#     else:
#         divy_disp = _fmt_metric(divy) if divy not in (None, "N/A") else "—"

#     c1, c2, c3, c4 = st.columns(4)
#     with c1:
#         st.metric("Market cap", _fmt_metric(mcap))
#     with c2:
#         st.metric("P/E (fwd/trail)", _fmt_metric(pe))
#     with c3:
#         st.metric("Dividend yield", divy_disp)
#     with c4:
#         st.metric("Beta", _fmt_metric(info.get("beta")))

#     c5, c6, c7, c8 = st.columns(4)
#     with c5:
#         st.metric("52W high", _fmt_metric(info.get("fiftyTwoWeekHigh")))
#     with c6:
#         st.metric("52W low", _fmt_metric(info.get("fiftyTwoWeekLow")))
#     with c7:
#         st.metric("EPS (fwd)", _fmt_metric(info.get("forwardEps")))
#     with c8:
#         st.metric("Volume", _fmt_metric(info.get("volume")))


# def render_right_rail_placeholder(st) -> None:
#     st.markdown('<div class="rail-title">Market pulse</div>', unsafe_allow_html=True)
#     st.markdown(
#         '<div class="rail-card">Top movers, heatmap, and headline feed can plug in here.</div>',
#         unsafe_allow_html=True,
#     )
#     st.markdown(
#         '<div class="rail-card">Use your data providers or cache to populate gainers/losers.</div>',
#         unsafe_allow_html=True,
#     )


# def page_title(st, title: str, subtitle: str | None = None) -> None:
#     st.markdown(f'<div class="page-card"><h2 style="margin:0;">{title}</h2>', unsafe_allow_html=True)
#     if subtitle:
#         st.markdown(
#             f'<p style="margin:0.35rem 0 0 0;opacity:0.75;font-size:0.95rem;">{subtitle}</p>',
#             unsafe_allow_html=True,
#         )
#     st.markdown("</div>", unsafe_allow_html=True)

"""
Modern Streamlit UI theme for FAST dashboard.
Compatible version for Streamlit deployments.
"""

from __future__ import annotations

from datetime import datetime
from html import escape
from typing import Optional

APP_BRAND_FULL = "Financial Analysis and Stock Trading Analysis"
APP_BRAND_TAGLINE = "Real-time market insights"

NAV_DEFINITION = [
    ("Dashboard", "✨", "Dashboard"),
    ("About the Project", "🏠", "Overview"),
    ("Live News Sentiment", "📰", "News & sentiment"),
    ("Company Basic Details", "📋", "Company profile"),
    ("Company Advanced Details", "📊", "Technicals"),
    ("Google Trends with Forecast", "🔎", "Search trends"),
    ("Twitter Trends", "𝕏", "Social trends"),
    ("Meeting Summarization", "🎙️", "Meeting notes"),
    ("Stock Future Prediction", "🔮", "Forecast"),
]


def _nav_display(internal, icon, short):
    return f"{icon}  {short}"


def init_theme_state(st):
    if "ui_theme_is_light" not in st.session_state:
        st.session_state["ui_theme_is_light"] = False

    if "global_ticker_search" not in st.session_state:
        st.session_state["global_ticker_search"] = "AAPL"


def inject_global_css(st):
    theme = "light" if st.session_state.get("ui_theme_is_light", False) else "dark"

    if theme == "light":
        bg = "#F5F7FB"
        panel = "#FFFFFF"
        text = "#101828"
        muted = "#667085"
        border = "rgba(16,24,40,0.08)"
        shadow = "0 10px 30px rgba(16,24,40,0.08)"
        accent = "#2563EB"
        accent_2 = "#10B981"
    else:
        bg = "#07111F"
        panel = "#0F172A"
        text = "#E5EEF9"
        muted = "#94A3B8"
        border = "rgba(148,163,184,0.14)"
        shadow = "0 18px 40px rgba(0,0,0,0.35)"
        accent = "#38BDF8"
        accent_2 = "#22C55E"

    pos = "#22C55E"
    neg = "#EF4444"
    warn = "#F59E0B"

    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

        html, body, .stApp, [data-testid="stAppViewContainer"] {{
            font-family: 'Inter', system-ui, sans-serif !important;
            color: {text};
        }}

        .stApp {{
            background:
                radial-gradient(circle at top left, rgba(56,189,248,0.10), transparent 30%),
                radial-gradient(circle at top right, rgba(34,197,94,0.08), transparent 28%),
                linear-gradient(180deg, {bg} 0%, {bg} 100%) !important;
        }}

        header[data-testid="stHeader"],
        div[data-testid="stToolbar"],
        div[data-testid="stDecoration"],
        section.main > div,
        [data-testid="stAppViewContainer"] > .main {{
            background: transparent !important;
            background-image: none !important;
        }}

        [data-testid="collapsedControl"] {{
            color: {text} !important;
        }}

        .block-container {{
            max-width: 1320px;
            padding-top: 1.2rem !important;
            padding-bottom: 3rem !important;
        }}

        h1, h2, h3 {{
            letter-spacing: -0.03em;
            font-weight: 700 !important;
            color: {text} !important;
        }}

        p, label, .stMarkdown, .stCaption {{
            color: {muted};
        }}

        section[data-testid="stSidebar"] > div {{
            background: rgba(15, 23, 42, 0.78) !important;
            backdrop-filter: blur(16px);
            border-right: 1px solid {border} !important;
        }}

        section[data-testid="stSidebar"] * {{
            color: {text} !important;
        }}

        .sidebar-brand {{
            display: flex;
            align-items: center;
            gap: 0.75rem;
            margin-bottom: 1rem;
            padding: 0.75rem;
            border: 1px solid {border};
            border-radius: 18px;
            background: linear-gradient(135deg, rgba(56,189,248,0.10), rgba(34,197,94,0.08));
            box-shadow: {shadow};
        }}

        .sb-logo {{
            width: 46px;
            height: 46px;
            border-radius: 14px;
            background: linear-gradient(135deg, {accent}, {accent_2});
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 800;
            font-size: 1.1rem;
            box-shadow: 0 8px 24px rgba(0,0,0,0.20);
        }}

        .sb-title {{
            font-weight: 800;
            font-size: 0.95rem;
            color: {text};
            line-height: 1.2;
        }}

        .sb-sub {{
            font-size: 0.75rem;
            color: {muted};
            margin-top: 0.2rem;
        }}

        .stRadio > div {{
            gap: 0.45rem;
        }}

        .stRadio label {{
            border-radius: 14px !important;
            padding: 0.52rem 0.7rem !important;
            border: 1px solid transparent !important;
            background: transparent !important;
            transition: all 0.18s ease;
        }}

        .stRadio label:hover {{
            background: rgba(255,255,255,0.04) !important;
            border-color: {border} !important;
        }}

        .stTextInput input,
        .stNumberInput input,
        .stDateInput input,
        .stSelectbox div[data-baseweb="select"],
        [data-baseweb="input"] {{
            background: rgba(255,255,255,0.03) !important;
            color: {text} !important;
            border: 1px solid {border} !important;
            border-radius: 14px !important;
        }}

        .stButton > button {{
            border-radius: 14px !important;
            border: 1px solid {border} !important;
            background: linear-gradient(135deg, rgba(56,189,248,0.12), rgba(34,197,94,0.10)) !important;
            color: {text} !important;
            font-weight: 700 !important;
            padding: 0.55rem 1rem !important;
            transition: all 0.18s ease;
            box-shadow: {shadow};
        }}

        .stButton > button:hover {{
            transform: translateY(-1px);
            border-color: rgba(56,189,248,0.40) !important;
        }}

        div[data-testid="stMetric"] {{
            background: linear-gradient(180deg, rgba(255,255,255,0.04), rgba(255,255,255,0.02));
            border: 1px solid {border};
            border-radius: 18px;
            padding: 1rem 1rem;
            box-shadow: {shadow};
        }}

        div[data-testid="stMetricLabel"] {{
            color: {muted} !important;
        }}

        div[data-testid="stMetricValue"] {{
            color: {text} !important;
            font-weight: 800 !important;
        }}

        .topbar-wrap {{
            border: 1px solid {border};
            border-radius: 22px;
            padding: 1rem 1.2rem;
            margin-bottom: 1.2rem;
            background:
                linear-gradient(135deg, rgba(56,189,248,0.10), rgba(34,197,94,0.08)),
                rgba(15,23,42,0.72);
            backdrop-filter: blur(16px);
            box-shadow: {shadow};
        }}

        .topbar-inner {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 1rem;
            flex-wrap: wrap;
        }}

        .topbar-brand {{
            font-size: clamp(1.1rem, 2vw, 1.5rem);
            font-weight: 800;
            color: {text};
            margin: 0;
            letter-spacing: -0.03em;
        }}

        .topbar-brand span {{
            color: {accent};
        }}

        .topbar-meta {{
            font-size: 0.82rem;
            color: {muted};
            margin: 0;
        }}

        .hero-card {{
            border: 1px solid {border};
            border-radius: 24px;
            padding: 1.4rem 1.45rem;
            margin-bottom: 1.1rem;
            background:
                radial-gradient(circle at top right, rgba(56,189,248,0.10), transparent 32%),
                linear-gradient(180deg, rgba(255,255,255,0.05), rgba(255,255,255,0.02));
            box-shadow: {shadow};
        }}

        .hero-kicker {{
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.15em;
            color: {accent};
            font-weight: 700;
            margin-bottom: 0.55rem;
        }}

        .hero-title {{
            font-size: clamp(1.8rem, 4vw, 3rem);
            font-weight: 800;
            color: {text};
            line-height: 1.05;
            margin-bottom: 0.45rem;
        }}

        .hero-subtitle {{
            font-size: 1rem;
            color: {muted};
            line-height: 1.6;
            max-width: 780px;
        }}

        .page-card {{
            background: linear-gradient(180deg, rgba(255,255,255,0.04), rgba(255,255,255,0.02));
            border: 1px solid {border};
            border-radius: 20px;
            padding: 1rem 1.1rem;
            margin-bottom: 1rem;
            box-shadow: {shadow};
        }}

        .section-card {{
            background: linear-gradient(180deg, rgba(255,255,255,0.04), rgba(255,255,255,0.02));
            border: 1px solid {border};
            border-radius: 20px;
            padding: 1rem 1rem 0.6rem 1rem;
            margin-bottom: 1rem;
            box-shadow: {shadow};
        }}

        .section-title {{
            font-size: 1rem;
            font-weight: 700;
            color: {text};
            margin-bottom: 0.3rem;
        }}

        .section-subtitle {{
            font-size: 0.86rem;
            color: {muted};
            margin-bottom: 0.9rem;
        }}

        .insight-card {{
            border: 1px solid {border};
            border-radius: 18px;
            padding: 1rem;
            margin-bottom: 0.8rem;
            background: rgba(255,255,255,0.03);
            box-shadow: {shadow};
        }}

        .insight-label {{
            font-size: 0.78rem;
            text-transform: uppercase;
            letter-spacing: 0.14em;
            color: {muted};
            margin-bottom: 0.35rem;
            font-weight: 700;
        }}

        .insight-value {{
            font-size: 1.35rem;
            font-weight: 800;
            color: {text};
            margin-bottom: 0.2rem;
        }}

        .insight-help {{
            font-size: 0.88rem;
            color: {muted};
            line-height: 1.5;
        }}

        .badge {{
            display: inline-block;
            padding: 0.28rem 0.65rem;
            border-radius: 999px;
            font-size: 0.75rem;
            font-weight: 700;
            margin-right: 0.35rem;
            border: 1px solid {border};
        }}

        .badge-pos {{
            background: rgba(34,197,94,0.15);
            color: {pos};
        }}

        .badge-neg {{
            background: rgba(239,68,68,0.14);
            color: {neg};
        }}

        .badge-neutral {{
            background: rgba(245,158,11,0.13);
            color: {warn};
        }}

        .hero-header {{
            background:
                radial-gradient(circle at top right, rgba(56,189,248,0.14), transparent 30%),
                linear-gradient(135deg, rgba(255,255,255,0.05), rgba(255,255,255,0.02));
            border: 1px solid {border};
            border-radius: 22px;
            padding: 1.3rem 1.35rem;
            margin-bottom: 1rem;
            box-shadow: {shadow};
        }}

        .hero-ticker {{
            font-size: 2rem;
            font-weight: 800;
            letter-spacing: -0.04em;
            color: {text};
        }}

        .hero-name {{
            font-size: 0.95rem;
            color: {muted};
            margin-top: 0.2rem;
        }}

        .hero-price {{
            font-size: 1.9rem;
            font-weight: 800;
            margin-top: 0.55rem;
            color: {text};
        }}

        .hero-chg-pos {{
            color: {pos};
            font-weight: 700;
        }}

        .hero-chg-neg {{
            color: {neg};
            font-weight: 700;
        }}

        .rail-card {{
            background: rgba(255,255,255,0.03);
            border: 1px solid {border};
            border-radius: 18px;
            padding: 1rem;
            margin-bottom: 0.8rem;
            color: {muted};
            box-shadow: {shadow};
        }}

        .rail-title {{
            font-weight: 700;
            color: {text};
            margin-bottom: 0.45rem;
            font-size: 0.95rem;
        }}

        .news-item {{
            padding: 0.8rem 0;
            border-bottom: 1px solid {border};
        }}

        .news-item:last-child {{
            border-bottom: none;
        }}

        .news-headline {{
            font-size: 0.92rem;
            color: {text};
            font-weight: 600;
            line-height: 1.5;
        }}

        .news-meta {{
            font-size: 0.78rem;
            color: {muted};
            margin-top: 0.2rem;
        }}

        [data-testid="stDataFrame"] {{
            border-radius: 16px;
            overflow: hidden;
            border: 1px solid {border};
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_theme_toggle(st):
    init_theme_state(st)
    st.sidebar.toggle("Light mode", key="ui_theme_is_light")


def render_top_bar(st):
    now = datetime.now().strftime("%Y-%m-%d · %H:%M")
    first, _, rest = APP_BRAND_FULL.partition(" ")
    brand_html = '<p class="topbar-brand"><span>{}</span> {}</p>'.format(
        escape(first), escape(rest)
    )

    st.markdown(
        """
        <div class="topbar-wrap">
          <div class="topbar-inner">
            {brand}
            <p class="topbar-meta">Live dashboard · {now}</p>
          </div>
        </div>
        """.format(brand=brand_html, now=now),
        unsafe_allow_html=True,
    )


def render_sidebar_navigation(st):
    logo_letter = escape(APP_BRAND_FULL.strip()[0].upper())
    st.sidebar.markdown(
        """
        <div class="sidebar-brand">
          <div class="sb-logo">{logo}</div>
          <div>
            <div class="sb-title">{title}</div>
            <div class="sb-sub">{subtitle}</div>
          </div>
        </div>
        """.format(
            logo=logo_letter,
            title=escape(APP_BRAND_FULL),
            subtitle=escape(APP_BRAND_TAGLINE),
        ),
        unsafe_allow_html=True,
    )

    render_theme_toggle(st)

    st.sidebar.markdown("##### Navigation")
    options_display = [_nav_display(*row) for row in NAV_DEFINITION]
    internal_by_display = {_nav_display(*row): row[0] for row in NAV_DEFINITION}

    choice = st.sidebar.radio(
        "nav",
        options_display,
        label_visibility="collapsed",
        key="sidebar_nav_radio",
    )

    st.sidebar.markdown("---")
    st.sidebar.caption("Smart market workspace")
    st.sidebar.caption("News · Forecast · Technicals · Fundamentals")

    return internal_by_display[choice]


def render_dashboard_hero(st):
    st.markdown(
        """
        <div class="hero-card">
            <div class="hero-kicker">AI Finance Dashboard</div>
            <div class="hero-title">Track markets, sentiment, and forecast trends in one place.</div>
            <div class="hero-subtitle">
                A modern stock intelligence dashboard combining price movement, technical indicators,
                live news sentiment, and predictive analytics in a clean institutional-style interface.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_section_card_start(st, title, subtitle=""):
    st.markdown(
        """
        <div class="section-card">
            <div class="section-title">{title}</div>
            <div class="section-subtitle">{subtitle}</div>
        """.format(
            title=escape(str(title)),
            subtitle=escape(str(subtitle)),
        ),
        unsafe_allow_html=True,
    )


def render_section_card_end(st):
    st.markdown("</div>", unsafe_allow_html=True)


def render_insight_card(st, label, value, help_text):
    st.markdown(
        """
        <div class="insight-card">
            <div class="insight-label">{label}</div>
            <div class="insight-value">{value}</div>
            <div class="insight-help">{help_text}</div>
        </div>
        """.format(
            label=escape(str(label)),
            value=escape(str(value)),
            help_text=escape(str(help_text)),
        ),
        unsafe_allow_html=True,
    )


def render_sentiment_badge(sentiment):
    s = str(sentiment or "").strip().lower()
    if s == "positive":
        return '<span class="badge badge-pos">Positive</span>'
    if s == "negative":
        return '<span class="badge badge-neg">Negative</span>'
    return '<span class="badge badge-neutral">Neutral</span>'


def render_company_hero(st, ticker, info):
    name = info.get("longName") or info.get("shortName") or ticker
    price = info.get("regularMarketPrice") or info.get("currentPrice")
    prev = info.get("previousClose")
    cur = info.get("currency") or "USD"

    chg_pct = None
    if price is not None and prev not in (None, 0):
        try:
            chg_pct = (float(price) - float(prev)) / float(prev) * 100.0
        except Exception:
            chg_pct = None

    chg_cls = "hero-chg-pos" if (chg_pct is not None and chg_pct >= 0) else "hero-chg-neg"
    chg_txt = ""
    if chg_pct is not None:
        sign = "+" if chg_pct >= 0 else ""
        chg_txt = '<span class="{cls}">{sign}{pct:.2f}%</span> vs prior close'.format(
            cls=chg_cls, sign=sign, pct=chg_pct
        )

    if isinstance(price, (int, float)):
        price_txt = "{:,.2f}".format(price)
    else:
        price_txt = str(price) if price else "—"

    st.markdown(
        """
        <div class="hero-header">
          <div class="hero-ticker">{ticker}</div>
          <div class="hero-name">{name}</div>
          <div class="hero-price">{price} <span style="font-size:0.95rem;font-weight:500;">{currency}</span></div>
          <div style="margin-top:0.35rem;font-size:0.92rem;">{chg}</div>
        </div>
        """.format(
            ticker=escape(str(ticker)),
            name=escape(str(name)),
            price=escape(str(price_txt)),
            currency=escape(str(cur)),
            chg=chg_txt,
        ),
        unsafe_allow_html=True,
    )


def _fmt_metric(v):
    if v is None or v == "N/A":
        return "—"
    try:
        if isinstance(v, (int, float)):
            if abs(v) >= 1e12:
                return "{:.2f}T".format(v / 1e12)
            if abs(v) >= 1e9:
                return "{:.2f}B".format(v / 1e9)
            if abs(v) >= 1e6:
                return "{:.2f}M".format(v / 1e6)
            if abs(v) >= 1000:
                return "{:,.0f}".format(v)
            return "{:,.4g}".format(v).rstrip("0").rstrip(".")
    except Exception:
        pass
    return str(v)


def render_metric_strip(st, info):
    mcap = info.get("marketCap")
    pe = info.get("forwardPE") or info.get("trailingPE")
    divy = info.get("dividendYield")

    if isinstance(divy, float) and 0 < divy < 1:
        divy_disp = "{:.2f}%".format(divy * 100)
    else:
        divy_disp = _fmt_metric(divy) if divy not in (None, "N/A") else "—"

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("Market cap", _fmt_metric(mcap))
    with c2:
        st.metric("P/E", _fmt_metric(pe))
    with c3:
        st.metric("Dividend yield", divy_disp)
    with c4:
        st.metric("Beta", _fmt_metric(info.get("beta")))


def render_right_rail_placeholder(st):
    st.markdown('<div class="rail-title">Market pulse</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="rail-card">Add top gainers, watchlist alerts, or sector heatmaps here.</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="rail-card">This side rail works best for summaries, signals, and quick stats.</div>',
        unsafe_allow_html=True,
    )


def page_title(st, title, subtitle=None):
    st.markdown(
        '<div class="page-card"><h2 style="margin:0;">{}</h2>'.format(escape(str(title))),
        unsafe_allow_html=True,
    )
    if subtitle:
        st.markdown(
            '<p style="margin:0.35rem 0 0 0;opacity:0.82;font-size:0.95rem;">{}</p>'.format(
                escape(str(subtitle))
            ),
            unsafe_allow_html=True,
        )
    st.markdown("</div>", unsafe_allow_html=True)
