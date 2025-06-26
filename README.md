# 📊 Software Effort Estimation using CNN, LSTM, RBFN, and MLP Optimized by PSO

This project presents a comparative study of four machine learning models — **CNN**, **LSTM**, **RBFN**, and **MLP** — for **Software Effort Estimation (SEE)**. All models are fine-tuned using **Particle Swarm Optimization (PSO)** to improve predictive performance.

## 📌 Objective

The goal is to build an accurate model that can estimate software development effort based on historical project features using various neural network architectures, enhanced by PSO-based hyperparameter tuning.

## 🧠 Implemented Models

| Model | Description |
|-------|-------------|
| **CNN** | 1D Convolutional Neural Network for extracting local patterns |
| **LSTM** | Long Short-Term Memory for handling sequential dependencies |
| **RBFN** | Radial Basis Function Network using Gaussian activations |
| **MLP** | Multilayer Perceptron, a classic feedforward ANN |

Each model is trained and evaluated on standardized datasets.

## ⚙️ PSO - Particle Swarm Optimization

- **PSO** is used to optimize:
  - Learning rate
  - Number of hidden layers/neurons
  - Batch size
  - Activation functions
- PSO improves convergence and avoids manual tuning.

## 📁 Dataset

Datasets commonly used in SEE tasks, such as:
- `Desharnais`
- `China`
- `Albrecht`
- `COCOMO81`
- Custom CSV datasets with cleaned and normalized features

**Preprocessing includes:**
- One-hot encoding (if categorical)
- Min-max normalization
- Splitting into training, validation, and test sets

---

## 📏 Evaluation Metrics

| Metric | Meaning |
|--------|---------|
| **MAE** | Mean Absolute Error |
| **MSE** | Mean Squared Error |
| **RMSE** | Root Mean Squared Error |
| **R² Score** | Coefficient of Determination |
| **MMRE** | Mean Magnitude of Relative Error |
| **MdMRE** | Median of MRE |
| **PRED(25)** | Percentage of predictions within 25% of actual effort |

## 🛠️ Technologies Used

- Python 3.10+
- TensorFlow / Keras
- Scikit-learn
- Matplotlib & Seaborn
- NumPy & Pandas
- Custom PSO implementation or `pyswarms`

---

## 📚 References

- Boehm, B. W. (1981). *Software Engineering Economics.*
- Kitchenham, B. et al. (2001). *Evaluation of software cost estimation models.*
- Kennedy, J., & Eberhart, R. (1995). *Particle Swarm Optimiza*
