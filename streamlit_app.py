import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Custom CSS styling for dark mode compatibility and improved layout
st.markdown("""
    <style>
    .header {
        font-size:22px !important;
        color: white;
        background-color: #3E288C;
        padding: 15px;
        text-align: center;
        border-radius: 8px;
        margin-bottom: 10px;
    }
    .subheader {
        font-size:18px;
        font-weight: bold;
        color: #3E288C;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .kpi, .info-block {
        background-color: #3E288C;
        color: white;
        padding: 10px;
        border-radius: 8px;
        text-align: center;
    }
    .divider {
        height: 2px;
        background-color: #e0e0e0;
        margin: 30px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="header">AIShield | GuArdIan | Agentic AI Security Posture</div>', unsafe_allow_html=True)

# Dropdowns for Organization and Agent
st.sidebar.selectbox("Organisation", ["ACME", "Other"])
st.sidebar.selectbox("Agent", ["All", "Agent 1", "Agent 2"])

# KPIs Section
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Key Metrics</div>', unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)
col1.markdown('<div class="kpi"><h3>Total Agents</h3><p>3 (+200%)</p></div>', unsafe_allow_html=True)
col2.markdown('<div class="kpi"><h3>Total Queries</h3><p>2.45K (+53.1%)</p></div>', unsafe_allow_html=True)
col3.markdown('<div class="kpi"><h3>Total Queries Flagged</h3><p>15% (-59%)</p></div>', unsafe_allow_html=True)
col4.markdown('<div class="kpi"><h3>Compliance Score</h3><p>98% (+19%)</p></div>', unsafe_allow_html=True)

# Additional Information Row (Dark Mode Friendly)
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Additional Information</div>', unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)
col1.markdown('<div class="info-block"><strong>No. of Agent Framework</strong><p>4</p></div>', unsafe_allow_html=True)
col2.markdown('<div class="info-block"><strong>Most Used Framework</strong><p>CrewAI</p></div>', unsafe_allow_html=True)
col3.markdown('<div class="info-block"><strong>At Risk Agent</strong><p>Sales</p></div>', unsafe_allow_html=True)
col4.markdown('<div class="info-block"><strong>At Risk Issue</strong><p>LLM06: SID</p></div>', unsafe_allow_html=True)

# Divider
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Guardian Overview Section (Donut Chart Only)
st.markdown('<div class="subheader">Guardian Overview</div>', unsafe_allow_html=True)
st.subheader("Guardrail Overview")
fig_donut = go.Figure(data=[go.Pie(labels=['Total Query', 'Action', 'Anomalous'], values=[2090, 160, 200], hole=.4)])
fig_donut.update_layout(showlegend=False)
st.plotly_chart(fig_donut, use_container_width=True)

# Divider
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Daily Agent Activity and Guardrail Activity Section
st.markdown('<div class="subheader">Activity Monitoring</div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)

# Daily Agent Activity
with col1:
    st.subheader("Daily Agent Activity")
    activity_data = pd.DataFrame({
        'Date': pd.date_range(start='2022-10-10', periods=6, freq='D').strftime('%d %b'),
        'Sales': np.random.randint(20, 40, 6),
        'Chat': np.random.randint(30, 60, 6),
        'Finance': np.random.randint(10, 30, 6)
    })
    activity_data.set_index('Date', inplace=True)
    st.bar_chart(activity_data)

# Guardrail Activity
with col2:
    st.subheader("Guardrail Activity")
    guardrail_data = pd.DataFrame({
        'Date': pd.date_range(start='2022-10-10', periods=6, freq='D').strftime('%d %b'),
        'Action': np.random.randint(30, 90, 6),
        'Anomaly': np.random.randint(10, 40, 6)
    })
    guardrail_data.set_index('Date', inplace=True)
    st.bar_chart(guardrail_data)

# Divider
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Policy Violations and OWASP Top 10 Sections
st.markdown('<div class="subheader">Policy Violations & OWASP Top 10</div>', unsafe_allow_html=True)


# Policy Violations Chart
st.subheader("Policy Violations")
policy_violations_data = pd.DataFrame({
    'Policy': ['PII', 'Ban Topic', 'Prompt Injection', 'NSFW', 'Bias', 'Malicious URL'],
    'Action': np.random.randint(30, 100, 6),
    'Anomaly': np.random.randint(20, 80, 6)
})
fig_policy = go.Figure()
fig_policy.add_trace(go.Bar(x=policy_violations_data['Action'], y=policy_violations_data['Policy'], name='Action', orientation='h'))
fig_policy.add_trace(go.Bar(x=policy_violations_data['Anomaly'], y=policy_violations_data['Policy'], name='Anomaly', orientation='h'))
fig_policy.update_layout(barmode='stack')
st.plotly_chart(fig_policy, use_container_width=True)

# OWASP Top 10 Heatmap

# Divider and Geographic Spread Section
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Geographic Spread of Agents</div>', unsafe_allow_html=True)
map_data = pd.DataFrame({
    'lat': np.random.uniform(-90, 90, 10),
    'lon': np.random.uniform(-180, 180, 10),
})
fig_map = px.scatter_geo(map_data, lat='lat', lon='lon', scope='world')
st.plotly_chart(fig_map, use_container_width=True)
