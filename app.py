import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# --- Model Training ---
# We train the model directly in the app for simplicity.
# For larger models, you would load a pre-trained .pkl file.
@st.cache_resource
def train_model():
    iris = load_iris()
    X = pd.DataFrame(iris.data, columns=iris.feature_names)
    y = pd.Series(iris.target)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model, iris.target_names

model, target_names = train_model()

# --- Streamlit App Interface ---
st.set_page_config(page_title="Iris Species Predictor", layout="centered")

st.title("🌸 Iris Species Predictor")
st.write("""
This app uses a Random Forest model to predict the species of an Iris flower 
based on its sepal and petal measurements. Adjust the sliders on the left to see the prediction.
""")

# --- Sidebar for User Input ---
st.sidebar.header("Input Features")

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length (cm)', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width (cm)', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length (cm)', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width (cm)', 0.1, 2.5, 0.2)
    data = {'sepal length (cm)': sepal_length,
            'sepal width (cm)': sepal_width,
            'petal length (cm)': petal_length,
            'petal width (cm)': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

# --- Main Panel for Displaying Info ---
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Your Input:")
    st.write(df)

# --- Prediction and Output ---
prediction = model.predict(df)
prediction_proba = model.predict_proba(df)
predicted_species = target_names[prediction[0]]

with col2:
    st.subheader("Prediction")
    st.metric(label="Predicted Species", value=predicted_species)

    st.subheader("Prediction Probability")
    st.bar_chart(pd.DataFrame(prediction_proba, columns=target_names).T)

# Display an image based on prediction
if predicted_species == 'setosa':
    st.image('https://upload.wikimedia.org/wikipedia/commons/5/56/Kosaciec_syberyjski_Iris_sibirica.jpg', caption='Iris Setosa')
elif predicted_species == 'versicolor':
    st.image('https://upload.wikimedia.org/wikipedia/commons/4/41/Iris_versicolor_3.jpg', caption='Iris Versicolor')
else:
    st.image('https://upload.wikimedia.org/wikipedia/commons/9/9f/Iris_virginica.jpg', caption='Iris Virginica')