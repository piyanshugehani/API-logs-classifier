import streamlit as st
import pandas as pd
import requests
import io

st.title("Log Classification App")
st.write("Upload a CSV file containing 'source' and 'log_message' columns for classification.")
st.write("The 'source' column should contain the log source, and the 'log_message' column should contain the log message.")


uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()

    # Prepare the file for FastAPI upload
    files = {'file': (uploaded_file.name, bytes_data, 'text/csv')}

    try:
        # Make a POST request to the FastAPI endpoint
        response = requests.post("http://127.0.0.1:8000/classify/", files=files)

        if response.status_code == 200:
            st.success("File classified successfully!")
            # Read the returned CSV content
            classified_df = pd.read_csv(io.BytesIO(response.content))
            st.write("Classified Data:")
            # Display dataframe with increased height and width
            st.dataframe(classified_df, height=600, width=800)

            # Option to download the classified file
            st.download_button(
                label="Download Classified CSV",
                data=response.content,
                file_name="classified_logs.csv",
                mime="text/csv",
            )
        else:
            st.error(f"Error during classification: {response.status_code} - {response.text}")
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the FastAPI server. Please ensure it is running at http://127.0.0.1:8000.")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")