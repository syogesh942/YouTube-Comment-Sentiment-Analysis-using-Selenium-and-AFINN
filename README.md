# YouTube-Comment-Sentiment-Analysis-using-Selenium-and-AFINN

This Python script conducts sentiment analysis on comments from a YouTube video using the AFINN lexicon. It utilizes Selenium to scrape the comments from the video's page, processes the comments, detects the language of each comment, and then performs sentiment analysis using the AFINN lexicon.

Here's a breakdown of the script:

Importing Libraries:

re: Regular expression operations.
string: String operations.
time.sleep: Pauses the script execution for a specified number of seconds.
langdetect: Language detection library.
selenium: Web scraping library for automating web browsers.
afinn: AFINN-based sentiment analysis library.
Selenium Setup:

Configures Chrome options for the Selenium WebDriver, maximizing the browser window and allowing it to be detached.
Creates a Chrome WebDriver instance.
Opens a specified YouTube video URL.
Waits for the page to load.
Skipping Ads:

Attempts to find and click the "Skip Ads" button using XPath.
Scrolling and Comment Retrieval:

Scrolls the webpage to load more comments, collecting them in a list.
Stemming and Preprocessing:

Processes comments by stemming, removing non-alphabetic characters, URLs, digits, and punctuation, and converting to lowercase.
Language Filtering:

Detects the language of each comment and filters out non-English comments.
Sentiment Analysis using AFINN:

Utilizes the AFINN lexicon to analyze the sentiment of each English comment.
Defines a function to determine sentiment based on the AFINN score.
Prints each sentence and its sentiment label (Positive, Negative, Neutral) based on the AFINN score.
