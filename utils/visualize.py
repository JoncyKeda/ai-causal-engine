import matplotlib.pyplot as plt
import streamlit as st

def plot_distribution(df, cause, effect):
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))

    ax[0].hist(df[cause], bins=10)
    ax[0].set_title(f"{cause} Distribution")

    ax[1].hist(df[effect], bins=10)
    ax[1].set_title(f"{effect} Distribution")

    st.pyplot(fig)
