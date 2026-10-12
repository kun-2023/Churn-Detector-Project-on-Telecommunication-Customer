from pathlib import Path
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

PROJECT_ROOT=Path(__file__).resolve().parents[1]
FRONTEND_DATA_DIR=PROJECT_ROOT/"outputs/frontend_data"
metrics_path=FRONTEND_DATA_DIR/"metrics.csv"
feature_importance_path=FRONTEND_DATA_DIR/"feature_importance.csv"
confusion_matrix_path=FRONTEND_DATA_DIR/"confusion_matrix.csv"

df_metrics=pd.read_csv(metrics_path)
df_feature_importance=pd.read_csv(feature_importance_path)
df_confusion_matrix=pd.read_csv(confusion_matrix_path, index_col=0)

def show_metrics():
    st.title("Model Performance Metrics")
    st.subheader("Metrics")
    st.dataframe(df_metrics, use_container_width=True)

    st.subheader("Feature Importance")
    st.bar_chart(
        df_feature_importance,
        x="feature",
        y="importance",
        horizontal=True
    )

    st.subheader("Testing Data Confusion Matrix")
    fig, ax=plt.subplots(figsize=(6,4))
    sns.heatmap(df_confusion_matrix, annot=True,
                fmt="d", cmap="Blues", cbar=False,
                ax=ax)
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
    st.pyplot(fig)
    plt.close(fig)