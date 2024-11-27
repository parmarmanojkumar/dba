import streamlit as st
import pandas as pd
from datetime import datetime

verbose = False

# App title
st.title("Organisation Policy Management")

# Section 1: Scan Supression
st.markdown("## 1. Scan Suppression")
# Data for file formats
scan_formats = ["SAST", "SBOM/SCA",]
scan_format_df = pd.DataFrame({"Scan Format": scan_formats, "Suppress": [False] * len(scan_formats)})
# Display table headers
col1, col2, col3 = st.columns([3, 1, 1.5])
col1.markdown("**Scan Format**")
col2.markdown("**Suppress**")
col3.markdown("**Status**")

# Interactive table with toggles and status
for i, row in scan_format_df.iterrows():
    col1, col2, col3 = st.columns([3, 1, 1.5])
    with col1:
        st.text(row["Scan Format"])
    with col2:
        toggle = st.checkbox("", key=f"suppress_scan_format_{i}")
        scan_format_df.at[i, "Suppress"] = toggle
    with col3:
        if toggle:
            st.markdown(f"🔴 Suppressed")
        else:
            st.markdown(f"🟢 Not Suppressed")

if verbose:
    # Display suppressed file formats
    st.markdown("### Suppressed Scan Formats")
    suppressed_scan_formats = scan_format_df[scan_format_df["Suppress"]]
    if not suppressed_scan_formats.empty:
        st.write(suppressed_scan_formats[["File Format"]])
    else:
        st.info("No scan formats are currently suppressed.")

# Section 1: File Format Suppression
st.markdown("## 2. File Format Suppression")

# Data for file formats
file_formats = [".pb", ".h5", ".onnx", ".tflite", ".joblib", ".pkl", ".ckpt", ".keras", ".pt", ".pth", ".bin", ".zip", ".safetensors", ".ipynb", "requirement.txt", ".YAML"]
file_format_df = pd.DataFrame({"File Format": file_formats, "Suppress": [False] * len(file_formats)})

# Display table headers
col1, col2, col3 = st.columns([3, 1, 1.5])
col1.markdown("**File Format**")
col2.markdown("**Suppress**")
col3.markdown("**Status**")

# Interactive table with toggles and status
for i, row in file_format_df.iterrows():
    col1, col2, col3 = st.columns([3, 1, 1.5])
    with col1:
        st.text(row["File Format"])
    with col2:
        toggle = st.checkbox("", key=f"suppress_file_format_{i}")
        file_format_df.at[i, "Suppress"] = toggle
    with col3:
        if toggle:
            st.markdown(f"🔴 Suppressed")
        else:
            st.markdown(f"🟢 Not Suppressed")

if verbose:
    # Display suppressed file formats
    st.markdown("### Suppressed File Formats")
    suppressed_file_formats = file_format_df[file_format_df["Suppress"]]
    if not suppressed_file_formats.empty:
        st.write(suppressed_file_formats[["File Format"]])
    else:
        st.info("No file formats are currently suppressed.")

# Section 3: Vulnerability Suppression
st.markdown("## 3. Vulnerability Suppression")

# Data for vulnerabilities
vulnerability_data = {
    "Framework": [
        "Tensorflow", "Tensorflow", "Tensorflow", "Tensorflow", "Checkpoint(TF,PT)",
        "Keras", "Keras", "Keras", "Keras", "PyTorch", "PyTorch", "PyTorch",
        "ONNX", "ONNX", "GGUF", "Scikit-Learn", "Misc", "SafeTensors", "SafeTensors"
    ],
    "File Format": [
        ".pb", ".pb", ".h5", ".h5", ".ckpt", ".keras", ".keras", ".h5", ".h5",
        ".pt", ".pth", ".bin", ".onnx", ".onnx", ".gguf", ".pkl", ".zip", ".safetensors", ".safetensors"
    ],
    "Vulnerability ID": [
        "AIS-TF-D-01: Protobuf Deserialization",
        "AIS-TF-B-01: TensorFlow PB Backdoor",
        "AIS-TF-D-02: TensorFlow/Keras H5 Deserialization",
        "AIS-TF-B-02: TensorFlow/Keras H5 Backdoor with malicious layers",
        "AIS-CP-D-01: TensorFlow/PyTorch Checkpoint (saved intermediate model) Deserialization",
        "AIS-KR-D-01: Keras Deserialization",
        "AIS-TF-B-02: TensorFlow/Keras H5 Backdoor with malicious layers",
        "AIS-TF-D-02: TensorFlow/Keras H5 Deserialization",
        "AIS-TF-B-02: TensorFlow/Keras H5 Backdoor with malicious layers",
        "AIS-PT-D-01: Pickle Serialization in PyTorch Models",
        "AIS-PT-D-01: Pickle Serialization in PyTorch Models",
        "AIS-PT-D-02: Serialization in PyTorch Models",
        "AIS-ON-B-01: ONNX Architecture Backdoor",
        "AIS-ON-R-01: Corrupted or Manipulated File Format",
        "AIS-GU-R-01: GGUF Runtime Threat",
        "AIS-PK-D-01: Pickle Serialization",
        "AIS-MI-D-01: Zip File Trojan or file corruption",
        "AIS-ST-D-01: Improper file Format",
        "AIS-ST-D-02: File shards – path traversal"
    ]
}

# Convert data to a DataFrame
vulnerability_df = pd.DataFrame(vulnerability_data)

# Add a column for toggles
vulnerability_df["Suppress"] = [False] * len(vulnerability_df)

# Display table headers
col1, col2, col3, col4, col5 = st.columns([1.5, 1.5, 3, 1, 1.5])
col1.markdown("**Framework**")
col2.markdown("**File Format**")
col3.markdown("**Vulnerability ID**")
col4.markdown("**Suppress**")
col5.markdown("**Status**")

# Interactive table with toggles and status
for i, row in vulnerability_df.iterrows():
    col1, col2, col3, col4, col5 = st.columns([1.5, 1.5, 3, 1, 1.5])
    with col1:
        st.text(row["Framework"])
    with col2:
        st.text(row["File Format"])
    with col3:
        st.text(row["Vulnerability ID"])
    with col4:
        toggle = st.checkbox("", key=f"suppress_vulnerability_{i}")
        vulnerability_df.at[i, "Suppress"] = toggle
    with col5:
        if toggle:
            st.markdown(f"🔴 Suppressed")
        else:
            st.markdown(f"🟢 Not Suppressed")

if verbose:
    # Display suppressed vulnerabilities
    st.markdown("### Suppressed Vulnerabilities")
    suppressed_vulnerabilities = vulnerability_df[vulnerability_df["Suppress"]]
    if not suppressed_vulnerabilities.empty:
        st.write(suppressed_vulnerabilities[["Framework", "File Format", "Vulnerability ID"]])
    else:
        st.info("No vulnerabilities are currently suppressed.")
        
# Section 4: Add Rule
st.markdown("## 4. Add Suppression Rule")

# Global list to store rules
# Initialize session state for rules
if "rules" not in st.session_state:
    st.session_state["rules"] = []
file_path = st.text_input("File Path", "")

# Filter unassigned vulnerabilities for this file
# Filter unassigned vulnerabilities for this file
assigned_vulnerabilities = [
    rule["Vulnerability ID"] for rule in st.session_state["rules"] if rule["File Path"] == file_path
]
available_vulnerabilities = vulnerability_df[~vulnerability_df["Vulnerability ID"].isin(assigned_vulnerabilities)]

# Filter vulnerabilities for the current rule
available_vulnerabilities = vulnerability_df["Vulnerability ID"].tolist()
selected_vulnerability = st.selectbox(
    "Select Vulnerability",
    options=available_vulnerabilities,
)

# Input for created/modified by
created_by = st.text_input("Created/Modified By", "")

# Add a new rule
if st.button("Add Mapping"):
    if file_path and selected_vulnerability and created_by:
        # Add the new rule
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.session_state["rules"].append({
            "Serial Number": len(st.session_state["rules"]) + 1,
            "File Path": file_path,
            "Vulnerability ID": selected_vulnerability,
            "Created By": created_by,
            "Modified By": "",
            "Modified Timestamp": "",
            "Status": "Created",
        })
        st.success(f"Mapping added: {file_path} -> {selected_vulnerability}")
    else:
        st.error("Please fill in all fields.")

# Show all rules
#st.markdown("### Current Mappings")
if st.session_state["rules"]:
    rules_df = pd.DataFrame(st.session_state["rules"])
    #st.dataframe(rules_df.style.hide(axis="index"), use_container_width=True)

    # Modify or delete rules
    st.markdown("### 4.1 Modify or Delete Existing Rules")
    rule_to_modify = st.selectbox(
        "Select Rule to Modify or Delete",
        options=rules_df["Serial Number"].tolist(),
        format_func=lambda x: f"Rule {x}",
    )

    selected_rule = rules_df[rules_df["Serial Number"] == rule_to_modify].iloc[0]
    action = st.radio("Action", ["Modify", "Delete"])

    if action == "Modify":
        # Input fields for modification
        modified_vulnerability = st.selectbox(
            "Modify Vulnerability",
            options=available_vulnerabilities,
            index=available_vulnerabilities.index(selected_rule["Vulnerability ID"]),
        )
        modified_by = st.text_input("Modified By", "")
        if st.button("Apply Modification"):
            if modified_by:
                # Update the rule
                idx = st.session_state["rules"].index(
                    next(r for r in st.session_state["rules"] if r["Serial Number"] == rule_to_modify)
                )
                st.session_state["rules"][idx].update({
                    "Vulnerability ID": modified_vulnerability,
                    "Modified By": modified_by,
                    "Modified Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "Status": "Modified",
                })
                st.success(f"Rule {rule_to_modify} modified successfully.")
            else:
                st.error("Please provide a name for 'Modified By'.")

    elif action == "Delete":
        deleted_by = st.text_input("Deleted By", "")
        if st.button("Confirm Deletion"):
            if deleted_by:
                # Mark the rule as deleted
                idx = st.session_state["rules"].index(
                    next(r for r in st.session_state["rules"] if r["Serial Number"] == rule_to_modify)
                )
                st.session_state["rules"][idx].update({
                    "Modified By": deleted_by,
                    "Modified Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "Status": "Deleted",
                })
                st.success(f"Rule {rule_to_modify} marked as deleted.")
            else:
                st.error("Please provide a name for 'Deleted By'.")

    # Display updated rules table
    #st.markdown("### Updated Rules")
    updated_rules_df = pd.DataFrame(st.session_state["rules"])
    st.dataframe(updated_rules_df.style.hide(axis="index"), use_container_width=True)
else:
    st.info("No mappings have been added yet.")