import streamlit as st
from langchain.llms import HuggingFaceHub


# Apply custom CSS
st.markdown(
    """
    <style>
        /* Set background to black */
        .stApp {
            background-color: black;
        }

        /* Change title color to white and add background color only for the title */
        h1 {
            color: white;
            background-color:#53C5C5FF;
            text-align: center;
            border-radius: 15px;  /* Rounded corners */
            padding: 10px;
        }

        /* Center the button */
        .stButton>button {
            display: block;
            margin-left: auto;
            margin-right: auto;
            background-color: #EEF5F5FF;  /* Optional: Set button background color */
            color: black;  /* Optional: Set button text color */
            border-radius: 10px;  /* Optional: Round button corners */
        }

        /* Optional: Change text input background and text color */
        .stTextInput, .stTextArea {
            background-color: #000000FF;  /* Light Orange */
            color: white;
            border-radius: 5px;
        }

        /* Change the AI response text color to white */
        .stMarkdown {
            color: white;  /* White color for the AI response */
        }

        /* Set sidebar text color to white */
        .css-1d391kg { 
            color: white;
        }


        /* Avoid background repetition on subheader */
        .stSubheader {
            background: none;  /* Reset background for the subheader */
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize the LLM model
llm = HuggingFaceHub(
    repo_id="mistralai/Mistral-7B-Instruct-v0.1",
    huggingfacehub_api_token="your key"
)

# Streamlit UI
st.title("Byte & Spice-Indian flavors🍽️")


# User input
theme = st.text_input("Describe your restaurant's theme:", "Authentic Indian flavors with modern dining.")

if st.button("Generate Details"):
    prompt = f"""
    You are an AI assistant specializing in restaurant branding. 
    Provide structured details for an Indian restaurant based on the theme: {theme}.
    
    **Do NOT include personal recommendations. Just provide structured details.**  
    **Format the response as follows:**
    
    1️⃣ **Restaurant Name** – A unique and creative name for the restaurant.  
    2️⃣ **Concept & Theme** – A brief explanation of the restaurant's theme and ambiance.  
    3️⃣ **Signature Dishes** – Three must-try dishes from the menu.  
    4️⃣ **Ideal Location** – Suggested locations based on the restaurant's concept.  
    5️⃣ **Target Audience** – The type of customers this restaurant will attract.  
    """

    # Get AI response
    response = llm(theme)

    # Display results
    st.subheader("Here’s your restaurant concept:")
    st.write(response)
