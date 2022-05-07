import os
from google.cloud import language_v1
from google.cloud.language_v1 import enums

from google.cloud import language
from google.cloud.language import types

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "path_to_json_credentials_file"


# Identify Entities
text_content = open('combined.txt', 'r')
text_content = text_content[0:1000]

client = language_v1.LanguageServiceClient()

type_ = enums.Document.Type.PLAIN_TEXT

language = "en"
document = {"content": text_content, "type": type_, "language": language}

encoding_type = enums.EncodingType.UTF8

response = client.analyze_entities(document, encoding_type=encoding_type)

for entity in response.entities:
    print(u"Entity Name: {}".format(entity.name))

    print(u"Entity type: {}".format(enums.Entity.Type(entity.type).name))

    print(u"Salience score: {}".format(round(entity.salience,3)))

    for metadata_name, metadata_value in entity.metadata.items():
        print(u"{}: {}".format(metadata_name, metadata_value))

    print('\n')


# Calculate Sentiment Score
document = types.Document(
    content=text_content,
    type=enums.Document.Type.PLAIN_TEXT)

sentiment = client.analyze_sentiment(document=document).document_sentiment
sscore = round(sentiment.score,4)
smag = round(sentiment.magnitude,4)

if sscore < 1 and sscore < -0.5:
  sent_label = "Very Negative"
elif sscore < 0 and sscore > -0.5:
  sent_label = "Negative"
elif sscore == 0:
  sent_label = "Neutral"
elif sscore > 0.5:
  sent_label = "Very Positive"
elif sscore > 0 and sscore < 0.5:
  sent_label = "Positive"

print('Sentiment Score: {} is {}'.format(sscore,sent_label))

predictedY =[sscore] 
UnlabelledY=[0,1,0]

if sscore < 0:
    plotcolor = 'red'
else:
    plotcolor = 'green'

plt.scatter(predictedY, np.zeros_like(predictedY),color=plotcolor,s=100)

plt.yticks([])
plt.subplots_adjust(top=0.9,bottom=0.8)
plt.xlim(-1,1)
plt.xlabel('Negative                                                            Positive')
plt.title("Sentiment Attitude Analysis")
plt.show()


# Calculate Sentiment Magnitude
if smag > 0 and smag < 1:
  sent_m_label = "No Emotion"
elif smag > 2:
  sent_m_label = "High Emotion"
elif smag > 1 and smag < 2:
  sent_m_label = "Low Emotion"

print('Sentiment Magnitude: {} is {}'.format(smag,sent_m_label))

predictedY =[smag] 
UnlabelledY=[0,1,0]

if smag > 0 and smag < 2:
    plotcolor = 'red'
else:
    plotcolor = 'green'

plt.scatter(predictedY, np.zeros_like(predictedY),color=plotcolor,s=100)

plt.yticks([])
plt.subplots_adjust(top=0.9,bottom=0.8)
plt.xlim(0,5)
plt.xlabel('Low Emotion                                                          High Emotion')
plt.title("Sentiment Magnitiude Analysis")
plt.show()


# Calculate Categorization
response = client.classify_text(document)

for category in response.categories:
    print(u"Category name: {}".format(category.name))
    print(u"Confidence: {}%".format(int(round(category.confidence,3)*100)))
    