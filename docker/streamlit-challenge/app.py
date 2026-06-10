import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import os
import glob

st.set_page_config(
    page_title="CSV Explorer",
    page_icon="📊",
    layout="wide",
)

# ── Sidebar ──────────────────────────────────────────────────────────────────
st.sidebar.title("📂 Load Data")
st.sidebar.markdown("---")

source = st.sidebar.radio(
    "Data source",
    ["Upload a CSV file", "Use file from /data folder"],
    index=0,
)

df = None

if source == "Upload a CSV file":
    uploaded = st.sidebar.file_uploader("Choose a CSV", type=["csv"])
    if uploaded:
        df = pd.read_csv(uploaded)
        st.sidebar.success(f"Loaded: {uploaded.name}")
else:
    data_dir = "/data"
    csv_files = glob.glob(os.path.join(data_dir, "*.csv"))
    if not csv_files:
        st.sidebar.warning("No CSV files found in /data. Mount a local folder with `-v`.")
    else:
        chosen = st.sidebar.selectbox(
            "Select a file",
            [os.path.basename(f) for f in csv_files],
        )
        df = pd.read_csv(os.path.join(data_dir, chosen))
        st.sidebar.success(f"Loaded: {chosen}")

# ── Main area ─────────────────────────────────────────────────────────────────
st.title("📊 CSV Explorer")
st.caption("Upload any CSV and instantly explore its structure, quality, and distributions.")

if df is None:
    st.info("👈 Load a CSV file using the sidebar to get started.")
    st.stop()

# ── Section 1: Data Preview ───────────────────────────────────────────────────
st.header("1 · Data Preview")
col_rows, col_cols, col_mem = st.columns(3)
col_rows.metric("Rows", f"{len(df):,}")
col_cols.metric("Columns", len(df.columns))
col_mem.metric("Memory", f"{df.memory_usage(deep=True).sum() / 1024:.1f} KB")

rows_to_show = st.slider("Rows to preview", min_value=5, max_value=min(200, len(df)), value=10)
st.dataframe(df.head(rows_to_show), use_container_width=True)

# ── Section 2: Column Types ───────────────────────────────────────────────────
st.header("2 · Column Types")
type_df = pd.DataFrame({
    "Column": df.columns,
    "Dtype": [str(df[c].dtype) for c in df.columns],
    "Unique Values": [df[c].nunique() for c in df.columns],
    "Sample Value": [str(df[c].dropna().iloc[0]) if df[c].notna().any() else "—" for c in df.columns],
})
st.dataframe(type_df, use_container_width=True, hide_index=True)

# ── Section 3: Missing Value Summary ─────────────────────────────────────────
st.header("3 · Missing Value Summary")
missing = df.isnull().sum()
missing_pct = (missing / len(df) * 100).round(2)
missing_df = pd.DataFrame({
    "Column": missing.index,
    "Missing Count": missing.values,
    "Missing %": missing_pct.values,
}).query("`Missing Count` > 0").reset_index(drop=True)

if missing_df.empty:
    st.success("✅ No missing values found in this dataset!")
else:
    st.warning(f"Found missing values in {len(missing_df)} column(s).")
    st.dataframe(missing_df, use_container_width=True, hide_index=True)

    fig, ax = plt.subplots(figsize=(8, max(2, len(missing_df) * 0.45)))
    bars = ax.barh(missing_df["Column"], missing_df["Missing %"], color="#e05c5c", edgecolor="white")
    ax.set_xlabel("Missing %")
    ax.set_xlim(0, 100)
    ax.xaxis.set_major_formatter(mticker.FormatStrFormatter("%.0f%%"))
    ax.invert_yaxis()
    ax.set_title("Missing Values by Column", fontweight="bold", pad=10)
    ax.spines[["top", "right"]].set_visible(False)
    for bar, val in zip(bars, missing_df["Missing %"]):
        ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height() / 2,
                f"{val:.1f}%", va="center", fontsize=9)
    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

# ── Section 4: Simple Charts ──────────────────────────────────────────────────
st.header("4 · Distribution Charts")

numeric_cols = df.select_dtypes(include="number").columns.tolist()
categorical_cols = df.select_dtypes(include=["object", "category", "bool"]).columns.tolist()

chart_tabs = st.tabs(["Numeric Distributions", "Categorical Counts"])

with chart_tabs[0]:
    if not numeric_cols:
        st.info("No numeric columns detected.")
    else:
        selected_num = st.selectbox("Choose a numeric column", numeric_cols, key="num_col")
        col_data = df[selected_num].dropna()

        fig, axes = plt.subplots(1, 2, figsize=(11, 3.5))

        axes[0].hist(col_data, bins=30, color="#4c7be8", edgecolor="white", linewidth=0.6)
        axes[0].set_title(f"Histogram — {selected_num}", fontweight="bold")
        axes[0].set_xlabel(selected_num)
        axes[0].set_ylabel("Count")
        axes[0].spines[["top", "right"]].set_visible(False)

        axes[1].boxplot(col_data, vert=True, patch_artist=True,
                        boxprops=dict(facecolor="#4c7be8", color="#1a3a8a"),
                        medianprops=dict(color="white", linewidth=2),
                        whiskerprops=dict(color="#1a3a8a"),
                        capprops=dict(color="#1a3a8a"),
                        flierprops=dict(marker="o", color="#e05c5c", markersize=4))
        axes[1].set_title(f"Box Plot — {selected_num}", fontweight="bold")
        axes[1].set_ylabel(selected_num)
        axes[1].spines[["top", "right"]].set_visible(False)

        fig.tight_layout()
        st.pyplot(fig)
        plt.close(fig)

        st.markdown("**Descriptive Statistics**")
        st.dataframe(col_data.describe().rename("value").to_frame().T, use_container_width=True)

with chart_tabs[1]:
    if not categorical_cols:
        st.info("No categorical columns detected.")
    else:
        selected_cat = st.selectbox("Choose a categorical column", categorical_cols, key="cat_col")
        top_n = st.slider("Top N categories", 5, 30, 10)
        counts = df[selected_cat].value_counts().head(top_n)

        fig, ax = plt.subplots(figsize=(9, max(3, len(counts) * 0.45)))
        bars = ax.barh(counts.index.astype(str)[::-1], counts.values[::-1],
                       color="#4c7be8", edgecolor="white")
        ax.set_xlabel("Count")
        ax.set_title(f"Top {top_n} values — {selected_cat}", fontweight="bold", pad=10)
        ax.spines[["top", "right"]].set_visible(False)
        for bar, val in zip(bars, counts.values[::-1]):
            ax.text(bar.get_width() + counts.values.max() * 0.01,
                    bar.get_y() + bar.get_height() / 2,
                    str(val), va="center", fontsize=9)
        fig.tight_layout()
        st.pyplot(fig)
        plt.close(fig)

# ── Section 5: Filter & Export ────────────────────────────────────────────────
st.header("5 · Filter by Column")

filter_col = st.selectbox("Column to filter on", df.columns.tolist(), key="filter_col")
col_dtype = df[filter_col].dtype

if pd.api.types.is_numeric_dtype(col_dtype):
    col_min, col_max = float(df[filter_col].min()), float(df[filter_col].max())
    low, high = st.slider(
        f"Range for {filter_col}",
        min_value=col_min, max_value=col_max,
        value=(col_min, col_max),
    )
    filtered = df[(df[filter_col] >= low) & (df[filter_col] <= high)]
else:
    unique_vals = df[filter_col].dropna().unique().tolist()
    chosen_vals = st.multiselect(
        f"Select values for {filter_col}",
        options=unique_vals,
        default=unique_vals[:min(5, len(unique_vals))],
    )
    filtered = df[df[filter_col].isin(chosen_vals)] if chosen_vals else df.iloc[0:0]

st.caption(f"Showing {len(filtered):,} of {len(df):,} rows after filter.")
st.dataframe(filtered, use_container_width=True)

csv_bytes = filtered.to_csv(index=False).encode("utf-8")
st.download_button(
    label="⬇ Download filtered data as CSV",
    data=csv_bytes,
    file_name="filtered_export.csv",
    mime="text/csv",
)
