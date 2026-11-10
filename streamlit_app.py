
import streamlit as st
import pickle
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Iris Flower Classifier",
    page_icon="🌸",
    layout="centered"
)

# Load trained model
with open("models/iris_model.pkl", "rb") as file:
    model = pickle.load(file)

# Load cleaned training dataset
df = pd.read_csv("data/iris_cleaned.csv")

# Get the exact feature names used by the model
feature_names = list(model.feature_names_in_)

# Calculate actual training-data ranges
feature_min = df[feature_names].min()
feature_max = df[feature_names].max()

# Application title
st.title("🌸 Iris Flower Classification")

st.write(
    "Predict the species of an Iris flower using "
    "a trained Random Forest Machine Learning model."
)


st.subheader("Enter Flower Measurements")

st.caption(
    "All measurements must fall within the ranges "
    "observed in the training dataset."
)

# Display actual training ranges
with st.expander("View valid measurement ranges"):
    for feature in feature_names:
        st.write(
            f"**{feature}:** "
            f"{feature_min[feature]:.1f} – "
            f"{feature_max[feature]:.1f} cm"
        )

# Empty input fields
sepal_length = st.number_input(
    "Sepal Length (cm)",
    min_value=0.0,
    max_value=10.0,
    value=None,
    placeholder="Enter sepal length"
)

sepal_width = st.number_input(
    "Sepal Width (cm)",
    min_value=0.0,
    max_value=10.0,
    value=None,
    placeholder="Enter sepal width"
)

petal_length = st.number_input(
    "Petal Length (cm)",
    min_value=0.0,
    max_value=10.0,
    value=None,
    placeholder="Enter petal length"
)

petal_width = st.number_input(
    "Petal Width (cm)",
    min_value=0.0,
    max_value=10.0,
    value=None,
    placeholder="Enter petal width"
)

# Prediction button
if st.button("Predict Iris Species"):

    # Collect user inputs
    input_values = [
        sepal_length,
        sepal_width,
        petal_length,
        petal_width
    ]

    # Check for missing values
    if any(value is None for value in input_values):

        st.warning(
            "Please enter all four flower measurements."
        )

    else:

        # Prepare input as a DataFrame
        measurements = pd.DataFrame(
            [input_values],
            columns=feature_names
        )

        # Validate against actual training-data ranges
        invalid_features = []

        for feature in feature_names:

            value = measurements[feature].iloc[0]
            minimum = feature_min[feature]
            maximum = feature_max[feature]

            if value < minimum or value > maximum:

                invalid_features.append(
                    f"{feature}: entered {value:.2f} cm "
                    f"(valid range: {minimum:.2f}–"
                    f"{maximum:.2f} cm)"
                )

        # Reject out-of-range inputs
        if invalid_features:

            st.error(
                "Input measurements are outside the "
                "training dataset's ranges."
            )

            for feature in invalid_features:
                st.write(f"- {feature}")

            st.warning(
                "Prediction cancelled. This model is trained "
                "only on the classic three-species Iris dataset. "
                "It cannot reliably identify unfamiliar species "
                "or measurements outside its training ranges."
            )

        else:

            # Generate prediction
            prediction = model.predict(measurements)[0]

            # Display prediction
            st.success(
                f"Predicted Species: Iris-{prediction.capitalize()}"
            )

            st.info(
                "Prediction generated using the trained "
                "Random Forest model."
            )

            st.caption(
                "Note: Passing range validation does not "
                "guarantee that the prediction is correct."
            )
