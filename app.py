import streamlit as st
from data_loader import load_data
from visualizations import (
    plot_product_distribution,
    plot_income_by_product,
    plot_usage_by_product,
    plot_fitness_by_product
)
from analysis import (
    get_summary_statistics,
    calculate_product_probabilities,
    calculate_gender_product_probabilities
)

def main():
    st.title('Aerofit Treadmill Analysis Dashboard')

    # Load data
    df = load_data()

    # Sidebar for navigation
    page = st.sidebar.selectbox("Choose a page", ["Overview", "Product Analysis", "Customer Segments", "Probability Analysis"])

    if page == "Overview":
        show_overview(df)
    elif page == "Product Analysis":
        show_product_analysis(df)
    elif page == "Customer Segments":
        show_customer_segments(df)
    elif page == "Probability Analysis":
        show_probability_analysis(df)

def show_overview(df):
    st.header("Dataset Overview")
    st.write(df.head())
    st.write(f"Total number of records: {len(df)}")

    st.subheader("Summary Statistics")
    st.write(get_summary_statistics(df))

    st.subheader("Product Distribution")
    fig = plot_product_distribution(df)
    st.pyplot(fig)

def show_product_analysis(df):
    st.header("Product Analysis")

    st.subheader("Average Income by Product")
    fig = plot_income_by_product(df)
    st.pyplot(fig)

    st.subheader("Average Usage by Product")
    fig = plot_usage_by_product(df)
    st.pyplot(fig)

    st.subheader("Average Fitness by Product")
    fig = plot_fitness_by_product(df)
    st.pyplot(fig)

def show_customer_segments(df):
    st.header("Customer Segments")

    segment = st.selectbox("Select a segment", ["Gender", "Marital Status", "Age Group"])

    if segment == "Gender":
        fig = plot_product_distribution(df, hue='Gender')
        st.pyplot(fig)
    elif segment == "Marital Status":
        fig = plot_product_distribution(df, hue='MaritalStatus')
        st.pyplot(fig)
    elif segment == "Age Group":
        df['AgeGroup'] = pd.cut(df['Age'], bins=[0, 25, 35, 45, 100], labels=['18-25', '26-35', '36-45', '45+'])
        fig = plot_product_distribution(df, hue='AgeGroup')
        st.pyplot(fig)

def show_probability_analysis(df):
    st.header("Probability Analysis")

    st.subheader("Product Probabilities")
    product_probs = calculate_product_probabilities(df)
    st.write(product_probs)

    st.subheader("Gender-Product Probabilities")
    gender_product_probs = calculate_gender_product_probabilities(df)
    st.write(gender_product_probs)

if __name__ == "__main__":
    main()