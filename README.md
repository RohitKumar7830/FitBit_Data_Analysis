# Predictive Modeling of Physical Activity Trends Using Fitbit Data

## Overview

This project leverages machine learning techniques to analyze Fitbit data, aiming to uncover patterns in user physical activity and provide predictive insights. By focusing on metrics such as steps, heart rate, physical activity intensity, and sleep patterns, the analysis demonstrates the potential of wearable technology in personalized health monitoring and fitness management.

## Key Features

* **Data Collection**: Aggregates data from Fitbit devices, including daily steps, distances, activity intensity, and more
* **Data Preprocessing**: Uses standardized scaling for consistent analysis across metrics
* **Clustering**: Implements K-Means clustering to categorize users into distinct activity profiles
* **Feature Importance Analysis**: Uses Random Forest Regression to identify key activity metrics influencing physical health
* **Predictive Modeling**: Predicts step counts using machine learning models
* **Interactive App**: Built with Streamlit for real-time predictions based on user inputs

## Getting Started

### Prerequisites

* Python 3.8 or higher
* pip (Python package installer)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/username/fitbit-predictive-modeling.git
   cd fitbit-predictive-modeling
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Dataset Preparation

* Place your Fitbit data CSV file in the `data/` directory
* Ensure the dataset includes relevant columns such as:
  * `TotalSteps`
  * `TotalDistance`
  * `VeryActiveMinutes`
  * `SedentaryMinutes`, etc.

### Running the Project

#### Preprocessing Data
Run the preprocessing script to clean and prepare your data:
```bash
python scripts/data_preprocessing.py
```

#### Clustering Analysis
Perform K-Means clustering to identify user activity profiles:
```bash
python scripts/clustering_analysis.py
```

#### Feature Importance Analysis
Analyze the importance of different activity metrics:
```bash
python scripts/feature_importance.py
```

#### Streamlit App
Launch the interactive prediction app:
```bash
streamlit run app/streamlit_app.py
```

## Results

* Identified distinct user activity clusters (e.g., low, moderate, high activity)
* Determined key metrics influencing total steps, highlighting the importance of very active minutes
* Developed a predictive model to estimate daily step counts based on activity inputs

## Future Enhancements

* Extend the dataset to include diverse demographics
* Integrate additional health metrics like calorie burn and sleep quality
* Enhance the Streamlit app with data visualization and customization features

## Authors

* **Rohit Kumar Bandi Ravikumar**
* **Raghavendra Yadav Golla**
* **Samah Senbel**

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

* Sacred Heart University
* Advisors and contributors for their invaluable guidance
