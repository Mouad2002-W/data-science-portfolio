# data-science-portfolio
# Housing Price Prediction Project

This repository contains the code and resources for a machine learning project aimed at predicting housing prices using various algorithms. The project includes data preprocessing, model training, API deployment, and a web application for predictions.

## Repository Structure

- **API.ipynb**: Jupyter notebook for testing the API endpoints.
- **HousingF.xls**: Dataset containing housing information used for training and testing.
- **MLR_model.pkl**: Serialized machine learning model (Multiple Linear Regression) for housing price prediction.
- **README.md**: This file, providing an overview of the project.
- **aoriginalhousing-price-prediction-best-ml-algorithms.ipynb**: Jupyter notebook exploring different machine learning algorithms for housing price prediction.
- **app.py**: Python script for running the Flask web application.
- **docker.ipynb**: Jupyter notebook for Docker-related configurations and testing.
- **Dockerfile**: Dockerfile for containerizing the application.
- **index.html**: Homepage for the web application.
- **predict.html**: Web page for making housing price predictions.
- **requirements.txt**: List of Python dependencies required for the project.
- **scaler.pkl**: Serialized scaler used for data preprocessing.
- **testAPI.ipynb**: Jupyter notebook for additional API testing.

## Project Overview

The goal of this project is to predict housing prices based on various features such as location, size, and other attributes. The project involves:

1. **Data Preprocessing**: Cleaning and preparing the dataset for model training.
2. **Model Training**: Training and evaluating multiple machine learning algorithms to find the best-performing model.
3. **API Deployment**: Creating an API endpoint for making predictions.
4. **Web Application**: Building a user-friendly web interface for interacting with the model.
5. **Dockerization**: Containerizing the application for easy deployment.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Scikit-learn
- Pandas
- NumPy
- Docker (optional)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
