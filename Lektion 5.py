from wordcloud import WordCloud,  STOPWORDS
import matplotlib.pyplot as plt
import numpy as np

with open("Alice.txt", encoding="utf8") as f:
    text = f.read()

x, y = np.ogrid[:1000, :1000]


mask = (x-500)**2 + (y-500) ** 2 > 400**2
mask = 255 * mask.astype(int)
wordcloud = WordCloud(width=1920, height=1080, mask=mask)

STOPWORDS.add('said')
STOPWORDS.add('she')

wordcloud.generate(text)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
