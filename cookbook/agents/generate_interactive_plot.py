import plotly.express as px
from sklearn.datasets import load_iris
import pandas as pd

# Load the iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Create the interactive plot
fig = px.scatter(df, x='sepal length (cm)', y='sepal width (cm)', 
                 color='species', title='Iris Dataset', 
                 labels={'sepal length (cm)': 'Sepal Length', 'sepal width (cm)': 'Sepal Width'})

# Save the plot as an HTML file
file_path = 'interactive_iris_plot.html'
fig.write_html(file_path)
file_path