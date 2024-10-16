import matplotlib.pyplot as plt
import seaborn as sns

def plot_product_distribution(df, hue=None):
    fig, ax = plt.subplots()
    sns.countplot(data=df, x='Product', hue=hue, palette='YlGnBu', ax=ax)
    plt.title(f"Product Distribution by {hue if hue else 'Overall'}")
    return fig

def plot_income_by_product(df):
    fig, ax = plt.subplots()
    sns.boxplot(data=df, x='Product', y='Income', palette='YlGnBu', ax=ax)
    plt.title("Income Distribution by Product")
    return fig

def plot_usage_by_product(df):
    fig, ax = plt.subplots()
    sns.boxplot(data=df, x='Product', y='Usage', palette='YlGnBu', ax=ax)
    plt.title("Usage Distribution by Product")
    return fig

def plot_fitness_by_product(df):
    fig, ax = plt.subplots()
    sns.boxplot(data=df, x='Product', y='Fitness', palette='YlGnBu', ax=ax)
    plt.title("Fitness Distribution by Product")
    return fig