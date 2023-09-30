import re
import string
from time import sleep
from langdetect import detect
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Configure Chrome options
opt = Options()
opt.add_argument("start-maximized")  # Maximize the browser window when it opens
opt.add_experimental_option("detach", True)  # Allow the browser window to be detached

# Create a Chrome WebDriver instance with the specified options
driver = webdriver.Chrome(options=opt)

# Open the specified URL in the Chrome browser
driver.get("https://youtu.be/gngPnSIE1h4?si=aMt1vVf90w_VcISO")

# Pause the script execution for 2 seconds to allow the page to load
sleep(5)

try:
    skip_button = driver.find_element(By.xpath('//button[@aria-label="Skip Ads"]'))
    skip_button.click()
except:
    pass  # Skip button might not always be present

# Set up variables for scrolling
scroll_increment = 500  # Scroll down by 1000 pixels each time
total_scrolls = 11  # Scroll a total of 22 times

words = []

# Perform scrolling to load more content on the page
for _ in range(total_scrolls):
    # Scroll down by the specified increment using JavaScript
    driver.execute_script(f"window.scrollBy(0, {scroll_increment});")
    comments = driver.find_elements(By.XPATH, '//*[@id="content-text"]')
    for i in comments:
        words.append(i.text)

    # Add a delay of 2 seconds to simulate human-like scrolling behavior
    sleep(2)

driver.quit()

comments = set(words)


def stemming(comment_set):
    stemmed_sentences = set()
    for comment in comment_set:
        # Split into sentences
        sentences = re.split(r'[.!?]', comment)
        for sentence in sentences:
            # Process each sentence
            stemmed_content = re.sub('[^a-zA-Z]', " ", sentence)
            stemmed_content = re.sub('https?://\S+|www\.\S+', '', stemmed_content)
            stemmed_content = re.sub(r'\b\d+\b|\b\d+[.,]?\d+\b', '', stemmed_content)
            stemmed_content = stemmed_content.translate(str.maketrans('', '', string.punctuation))
            stemmed_content = stemmed_content.lower()
            stemmed_sentences.add(stemmed_content)
    return stemmed_sentences


stemmed_sentences_set = stemming(comments)


def get_english_texts(text_set):
    english_texts = set()
    for text in text_set:
        try:
            if detect(text) == 'en':
                english_texts.add(text)
        except:
            # Error occurred during language detection, handle it based on your requirements
            pass
    return english_texts



english_texts_set = get_english_texts(stemmed_sentences_set)

from afinn import Afinn

# Initialize the Afinn object
afinn = Afinn()


# Define a function to get sentiment label
def get_sentiment_label_afinn(score):
    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"


# Analyze sentiment using AFINN
for sentence in english_texts_set:
    # Get the sentiment score using AFINN
    afinn_score = afinn.score(sentence)

    # Print the sentence and its sentiment using AFINN
    print("Sentence:", sentence)
    print("Sentiment (AFINN):", get_sentiment_label_afinn(afinn_score))
    print()
