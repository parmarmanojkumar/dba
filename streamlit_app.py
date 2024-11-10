import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Dummy Data
# Dummy Data
total_agents = 3
total_queries = 2450
queries_flagged = 15
compliance_score = 98
total_agents_fw= 4
most_used_fw="CrewAI"

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
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Agents", total_agents, "+200%")
col2.metric("Total Queries", f"{total_queries / 1000:.2f}K", "+53.1%")
col3.metric("Total Queries Flagged", f"{queries_flagged}%", "-59%")
col4.metric("Compliance Score", f"{compliance_score}%", "+19%")

# Additional Information Row (Dark Mode Friendly)
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Additional Information</div>', unsafe_allow_html=True)
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("No. of Agent Framework", total_agents_fw, "+100%")
col2.metric("Most Used Agent Framework", most_used_fw, "-Langchain")
col3.metric("Risky Agent", "Sales", "-Chat")
col4.metric("Most violated Policy", "PII", "-Prompt Injection")
col5.metric("OWASP TOP10", "SID", "-PI")

# Divider
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Guardian Overview Section (Donut Chart Only)
st.markdown('<div class="subheader">Guardian Overview</div>', unsafe_allow_html=True)
st.subheader("Guardrail Overview")
fig_donut = go.Figure(data=[go.Pie(labels=['Total Query', 'Policy Violation - Action', 'Policy Violation - Flag'], values=[2090, 160, 200], hole=.4)])
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
        'Policy Violation - Action': np.random.randint(30, 90, 6),
        'Policy Violation - Flag': np.random.randint(10, 40, 6)
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
    'Policy Violation - Action': np.random.randint(30, 100, 6),
    'Policy Violation - Flag': np.random.randint(20, 80, 6)
})
fig_policy = go.Figure()
fig_policy.add_trace(go.Bar(x=policy_violations_data['Action'], y=policy_violations_data['Policy'], name='Policy Violation - Action', orientation='h'))
fig_policy.add_trace(go.Bar(x=policy_violations_data['Anomaly'], y=policy_violations_data['Policy'], name='Policy Violation - Flag', orientation='h'))
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
