# 🌿 Plant Disease Detection System for Sustainable Agriculture

A web-based image classification system built with **Streamlit** and **TensorFlow** that identifies plant diseases from leaf images using a pre-trained deep learning model. This tool aims to assist farmers and agricultural researchers in making quicker, informed decisions for sustainable crop management.

🔗 **Live Repo:** [SusanFernandes/Plant-Disease-Detection-System-for-Sustainable-Agriculture](https://github.com/SusanFernandes/Plant-Disease-Detection-System-for-Sustainable-Agriculture)

---

## 📸 Features

- 🖼️ Upload images of diseased or healthy plant leaves
- ⚙️ Powered by a pre-trained deep learning model (`.keras`)
- 🧠 Classifies across **38 plant disease types**
- 🖥️ Simple and intuitive web UI using **Streamlit**
- 💅 Clean and responsive design with custom UI elements

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.10 installed
- Git installed

---

### 🔧 Installation & Setup

Run the following commands **in one terminal session**:

```
# 1. Clone the repository
git clone https://github.com/SusanFernandes/Plant-Disease-Detection-System-for-Sustainable-Agriculture.git
cd Plant-Disease-Detection-System-for-Sustainable-Agriculture

# 2. Create and activate a virtual environment (Python 3.10)
py -3.10 -m venv venv310
.\venv310\Scripts\activate   # For Windows
# source venv310/bin/activate   # (macOS/Linux alternative)

# 3. Upgrade pip (recommended)
python -m pip install --upgrade pip

# 4. Install required Python packages
pip install tensorflow streamlit pillow numpy

# 5. Run the app
streamlit run app.py


🧠 If you encounter slow internet or timeout errors during pip install, retry with:

pip install --default-timeout=100 tensorflow streamlit pillow numpy


🗂️ Project Structure

Plant-Disease-Detection-System-for-Sustainable-Agriculture/
├── app.py                            # Main Streamlit application
├── trained_plant_disease_model.keras # Pre-trained model file (Keras)
├── Diseases.png                      # Home screen image
├── venv310/                          # Python virtual environment
├── .gitignore                        # Git ignore rules
└── README.md                         # You're here!


```
🧠 Model Details
Format: .keras (Keras native model)
Input Shape: 128 x 128 x 3
Number of Classes: 38

🏷️ Sample Classes:

Tomato___Late_blight,
Apple___Black_rot,
Grape___Black_rot,
Corn_(maize)___Northern_Leaf_Blight,
Potato___Early_blight,
Tomato___Tomato_mosaic_virus,
... and many more


✅ Supported Crops & Diseases
🌾 Crops:

🍅 Tomato,
🍏 Apple,
🍇 Grape,
🌽 Corn (Maize),
🥔 Potato,
🍑 Peach,
🫑 Bell Pepper,
🫐 Blueberry,
🍓 Strawberry,
🌱 Soybean,
🍊 Orange,
🍒 Cherry,
🥒 Squash


🦠 Diseases Detected:

Leaf Blight,
Early/Late Blight,
Mosaic Virus,
Rust,
Powdery Mildew,
Bacterial Spots

🔐 License
This project is released under an open-source license.
Use it freely for research, education, and non-commercial purposes.

👩‍💻 Author
Susan Fernandes
🔗 GitHub: @SusanFernandes
