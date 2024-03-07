# META-Gen Visualization Tool

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10794898.svg)](https://doi.org/10.5281/zenodo.10794898)

This tool is designed to visualize dataset from the study of the effect of straw treatments on the microbial community in the soil. It is built using Streamlit, pandas, numpy, plotly, and matplotlib. Clustering and data transformation are done using pandas, numpy and k-prototypes algorithm.

The application is divided into sections:

1. Bacteria Data View
2. Bacteria Data Visualization charts
3. Fungi Data View
4. Fungi Data Visualization charts
5. Experimental visualization chart to visualize binary data

## Running the App Locally

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    - On Unix or MacOS:
        ```bash
        source venv/bin/activate
        ```
5. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
6. Run the Streamlit app:
    ```bash
    streamlit run Home.py
    ```

## Deployed Version

You can access the deployed version of the app at: [Deployed App URL](https://ds--metagtool-dmwcqyuhbd3kaikvk5me8j.streamlit.app/)