import streamlit as st
from streamlit_option_menu import option_menu
import pickle
import string
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))


# Function to display navigation menu
def streamlit_menu():
    example = 3  # Example number for horizontal menu
    selected = option_menu(
        menu_title=None,
        options=["Home", "About", "Regulations"],
        icons=["house", "book", "envelope"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#FFFFF"},  # Set background color
            "icon": {"color": "#FFD700", "font-size": "20px"},  # Set icon color and size
            "nav-link": {
                "font-size": "25px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            # "nav-link-selected": {"background-color": ""},  # Set selected menu color
        },
    )
    return selected

# Display navigation menu
selected_tab = streamlit_menu()


# Main content based on selected tab
if selected_tab == "Home":
    st.markdown("<h1 style='font-size: 27px;'>SpamSleuth  - Your Ultimate Email and SMS Guardian</h1>", unsafe_allow_html=True)


    input_sms = st.text_area("Enter the message")
    
    if st.button('Predict'):
        # 1. preprocess
        transformed_sms = transform_text(input_sms)
        # 2. vectorize
        vector_input = tfidf.transform([transformed_sms])
        # 3. predict
        result = model.predict(vector_input)[0]
        # 4. Display
        if result == 1:
            st.header("Spam")
        else:
            st.header("Not Spam")
elif selected_tab == "About":
    st.title("About")
    st.write("This is an email/sms spam classifier application.")
    st.write("It predicts whether a given message is spam or not spam.")
    st.write("Simply enter your spam messages/SMS content and click on predict to know your result!")
    st.write("The classification is based on a machine learning model trained on text data.")
    st.write("Feel free to use the application to classify your messages ")
elif selected_tab == "Regulations":
    st.title("Regulations")
    st.write("Here are some regulations to follow while using this application:")
    st.write("1. Use the application responsibly and do not abuse it for malicious purposes.")
    st.write("2. If you encounter any issues or have feedback, please reach out to the developer team.")
