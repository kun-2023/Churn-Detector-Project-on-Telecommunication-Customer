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
    scores=df_metrics.set_index("metrics")["test_scores"].astype(float)
    metric_names=[
        "Accuracy", 
        "Recall",
        "Precision", 
        "F1_score", 
        "ROC_AUC_SCORE"
    ]

    cols=st.columns(5)
    for col, name in zip(cols, metric_names):
        with col:
            st.metric(
                label=name.replace("_", " "),
                value=f"{scores[name]:.3f}"
            )

    st.subheader("Feature Importance")
    importance=df_feature_importance.copy()
    importance.columns=importance.columns.str.lower()
    importance=(
        importance.sort_values(
            "importance", ascending=False
        ).head(15)
    )
    fig, ax=plt.subplots(figsize=(11,7))
    ax.barh(
        importance["feature"],
        importance["importance"]
    )
    ax.invert_yaxis()
    ax.set_xlabel("Importance")
    ax.set_ylabel("")

    ax.tick_params(axis="y", labelsize=9)
    fig.subplots_adjust(left=0.46, 
                        right=0.97, 
                        top=0.50, 
                        bottom=0.19)
    st.pyplot(fig, width="stretch")
    plt.close(fig)

    st.subheader("Testing Data Confusion Matrix")
    fig, ax=plt.subplots(figsize=(4,3))
    sns.heatmap(df_confusion_matrix, annot=True,
                fmt="d", cmap="Blues", cbar=False,
                ax=ax)
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
    st.pyplot(fig)
    plt.close(fig)