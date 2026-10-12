import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import seaborn as sns
from src.config import NUM_COLS, CAT_COLS


PROJECT_ROOT=Path(__file__).resolve().parent[1]

df=pd.read_csv(PROJECT_ROOT/"outputs/clean_data/clean_data.csv")
# Partner churn, 
def plot_Partner(ax):
    sns.barplot(data=df, x="Partner", 
                y="Churn_Label", estimator="mean", 
                errorbar=None, ax=ax)
    ax.set_title("Churn Rate by Partner")

# Dependents
def plot_Dependents(ax):
    sns.barplot(data=df, x="Dependents", 
                y="Churn_Label", estimator="mean", 
                errorbar=None, ax=ax)
    ax.set_title("Churn Rate by Dependents")

# InternetService
def plot_InternetService(ax):
    sns.barplot(data=df, x="InternetService", 
                y="Churn_Label", estimator="mean", 
                errorbar=None, ax=ax)
    ax.set_title("Churn Rate by InternetService")


# OnlineSecurity
def plot_OnlineSecurity(ax):
    sns.barplot(data=df, x="OnlineSecurity", 
                y="Churn_Label", estimator="mean", 
                errorbar=None, ax=ax)
    ax.set_title("Churn Rate by OnlineSecurity")


# OnlineBackup 
def plot_OnlineBackup(ax):
    sns.barplot(data=df, x="OnlineBackup", 
                y="Churn_Label", estimator="mean", 
                errorbar=None, ax=ax)
    ax.set_title("Churn Rate by OnlineBackup")


# DeviceProtection
def plot_DeviceProtection(ax):
    sns.barplot(data=df, x="DeviceProtection", 
                y="Churn_Label", estimator="mean", 
                errorbar=None, ax=ax)
    ax.set_title("Churn Rate by DeviceProtection")



# TechSupport 
def plot_TechSupport(ax):
    sns.barplot(data=df, x="TechSupport", 
                y="Churn_Label", estimator="mean", 
                errorbar=None, ax=ax)
    ax.set_title("Churn Rate by TechSupport")

# Contract
def plot_Contract(ax):
    sns.barplot(data=df, x="Contract", 
                y="Churn_Label", estimator="mean", 
                errorbar=None, ax=ax)
    ax.set_title("Churn Rate by Contract")


# PaperlessBill
def plot_PaperlessBill(ax):
    sns.barplot(data=df, x="PaperlessBill", 
                y="Churn_Label", estimator="mean", 
                errorbar=None, ax=ax)
    ax.set_title("Churn Rate by PaperlessBill")


# PaymentMethod
def plot_PaymentMethod(ax):
    sns.barplot(data=df, x="PaymentMethod", 
                y="Churn_Label", estimator="mean", 
                errorbar=None, ax=ax)
    ax.set_title("Churn Rate by PaymentMethod")




# correlation
df_encoded=pd.get_dummies(df[CAT_COLS], drop_first=True, dtype=int)
df_encoded=pd.concat([df_encoded, df[NUM_COLS]], axis=1)
corr=df_encoded.corr()

def show_eda():
    st.title("Customers Churn EDA")
    st.subheader("Churn Distribution")

    plt.figure(figsize=(5,5))
    sns.countplot(data=df, x="Churn_Label")
    plt.xticklabels([0,1],["Not Churn", "Churn"])
    plt.xticks(rotation=45)
    plt.show()

    st.subheader("Churn Rate by Category")
    plot_functions=[plot_Partner, plot_Dependents, plot_InternetService, 
                    plot_OnlineBackup, plot_OnlineSecurity, plot_DeviceProtection, 
                    plot_TechSupport, plot_Contract, plot_PaperlessBill,
                    plot_PaymentMethod]
    fig, axes=plt.sunplots(nrow=4, ncols=3, figsize=(18,20))
    axes=axes.flatten()
    for ax, plot_function in zip(axes, plot_functions):
        plot_function(ax)

    for ax in axes[len(plot_functions):]:
        ax.set_visible(False)
    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)



    
    st.subheader("Correlation of all categories")
    
    plt.figure(figsize=(30,30))
    sns.heatmap(corr, annot=True, cmap="coolwarm", center=0)
    plt.show()