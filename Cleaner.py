import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Load your data
df = pd.read_csv('Popular_Baby_Names.csv')

# If you haven't downloaded the nltk stopwords, do so
nltk.download('punkt')
nltk.download('stopwords')

def clean_text(text):
    # Convert text to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    
    # Remove numbers
    text = re.sub(r'\d+', '', text)
    
    # Remove common non-sensical text
    text = re.sub(r'\n', ' ', text)
    
    # Tokenize the text
    text = word_tokenize(text)
    
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    text = [word for word in text if word not in stop_words]
    
    return text

# Apply the function to every feedback
df['cleaned_feedback'] = df['Popular_Baby_Names.csv'].apply(clean_text)