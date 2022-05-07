pip install scattertext
pip install wordcloud matplotlib



import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS 
# stopwords is a collection of words that dont convey meaning. mostly pronouns such as he she etc.

#generate word cloud
text = read.csv(r, 'C:/Users/david/Desktop/CHI Research Project/Combined.csv')
#text = "copy_text_from_job_description_in_link_provided_above" # the input of the wordcloud generator
#generate the wordcloud object, set the height and width, set the random_state parameter to ensure
reproducibility of results and set the stopwords parameter so that the irrelevant words such as pronouns are discarded.
wordcloud = WordCloud(width = 3000, height = 2000, random_state=1, background_color='blue', collocations=False, stopwords = STOPWORDS).generate(text)
# text is the input to the generate() method
#draw the figure
#Set figure size
plt.figure(figsize=(40, 30))
# Display image
plt.imshow(wordcloud) 
# No axis 
plt.axis("off")
plt.show()