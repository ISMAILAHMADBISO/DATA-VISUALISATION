import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def load_dataset():
    """
    Prompts the user to enter the file path of the dataset and loads it as a DataFrame.
    """
    file_path = input("Enter the path to your dataset (CSV file): ")
    try:
        df = pd.read_csv(file_path)
        print("\nDataset loaded successfully!")
        print(f"Columns in the dataset: {', '.join(df.columns)}")
        return df
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return None

def static_plot(df):
    """
    Creates static visualizations using Matplotlib and Seaborn.
    """
    print("\nSelect a column for static visualization:")
    column = input(f"Choose from {', '.join(df.columns)}: ")
    if column in df.columns:
        plt.figure(figsize=(10, 6))
        sns.histplot(df[column], kde=True, color='blue')
        plt.title(f"Distribution of {column}")
        plt.xlabel(column)
        plt.ylabel("Frequency")
        plt.grid()
        plt.show()
    else:
        print("Invalid column name. Please try again.")

def interactive_plot(df):
    """
    Creates interactive visualizations using Plotly.
    """
    print("\nSelect columns for interactive visualization:")
    x_col = input(f"Choose X-axis column from {', '.join(df.columns)}: ")
    y_col = input(f"Choose Y-axis column from {', '.join(df.columns)}: ")
    if x_col in df.columns and y_col in df.columns:
        fig = px.scatter(df, x=x_col, y=y_col, title=f"Scatter Plot of {x_col} vs {y_col}", height=600, width=800)
        fig.show()
    else:
        print("Invalid column names. Please try again.")

def main():
    """
    Main function to drive the tool.
    """
    print("Welcome to the Data Visualization Tool!")
    df = load_dataset()
    if df is not None:
        while True:
            print("\nChoose an option:")
            print("1. Static Plot (Matplotlib & Seaborn)")
            print("2. Interactive Plot (Plotly)")
            print("3. Exit")
            choice = input("Enter your choice (1/2/3): ")
            
            if choice == '1':
                static_plot(df)
            elif choice == '2':
                interactive_plot(df)
            elif choice == '3':
                print("Thank you for using the Data Visualization Tool!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
