# Restaurant Concept Generator using LangChain, Streamlit, and Hugging Face API
![image](https://github.com/user-attachments/assets/2f350c3f-65ed-43eb-bc0b-6dfff12bb12b)


This project leverages **LangChain**, **Streamlit**, and the **Hugging Face API** to generate unique and detailed restaurant concepts based on the user's input. The application is designed to help entrepreneurs or food enthusiasts create restaurant concepts with ease, offering suggestions on restaurant names, themes, signature dishes, ideal locations, and target audiences.

## 🚀 Project Overview

The application generates restaurant details based on the theme provided by the user. By utilizing the power of **LangChain** and Hugging Face's large language models, this tool produces structured, professional, and actionable insights that can help inspire new restaurant ideas.

## 🧠 Key Features
- **Restaurant Name**: Unique and creative name ideas for the restaurant.
- **Concept & Theme**: A brief explanation of the restaurant's ambiance and style.
- **Signature Dishes**: Three must-try dishes from the menu.
- **Ideal Location**: Suggested locations based on the restaurant's concept.
- **Target Audience**: The type of customers the restaurant will attract.

## 🛠️ Technologies Used
- **LangChain**: A framework for building applications with LLMs (Large Language Models).
- **Streamlit**: A framework to create web apps directly from Python scripts.
- **Hugging Face API**: Used to connect to a pre-trained language model to generate text-based insights.

## ⚙️ Setup Instructions

### Prerequisites
- Python 3.6+
- Streamlit
- LangChain
- Hugging Face API key (You can get it by creating an account on [Hugging Face](https://huggingface.co/)).

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/restaurant-concept-generator.git
   cd restaurant-concept-generator


2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   
3. Obtain a Hugging Face API key:

        * Sign up at Hugging Face.
        * Get your API key from this page.
        * Add your Hugging Face API key in the script. You can set it directly in the code or use environment variables.

4. Running the App
To run the Streamlit app locally:
   ```bash
   streamlit run app.py
   
This will open the app in your default browser, where you can input your restaurant's theme and receive the generated details.

##💡How It Works

    User Input: The user provides a restaurant theme through an input box on the Streamlit app.
    LLM Model: The theme is passed to the Hugging Face language model via LangChain to generate creative and structured restaurant details.
    AI Response: The generated details, including restaurant name, concept, signature dishes, location, and target audience, are displayed in a well-structured format on the web page.
## 📝 Example

### Input:
    Theme: "Modern Indian cuisine with a fusion twist."
    
### Output:
        1️⃣ Restaurant Name: "Fusion Spice"
        2️⃣ Concept & Theme: A contemporary fusion restaurant that combines classic Indian spices with modern techniques and ingredients, offering a sophisticated yet casual dining experience.
        3️⃣ Signature Dishes:
          * Tandoori Salmon: Marinated salmon grilled in the tandoor, served with mint chutney.
          * Butter Chicken Lasagna: A fusion of Italian lasagna with Indian butter chicken sauce.
          * Mango Lassi Cheesecake: A creamy cheesecake infused with mango lassi flavors. 
        4️⃣ Ideal Location: Upscale urban areas, preferably near cultural hubs or trendy neighborhoods. 
        5️⃣ Target Audience: Foodies, young professionals, and families looking for a unique blend of Indian and international cuisines.
## 📄 License
This project is open source and available under the MIT License.
