import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load your data 
df = pd.read_csv("data/inputs/cleaned/tableau_data.csv")  

# Display all column names
print(df.columns.tolist())

# List of one-hot encoded skill columns
skill_columns = [
    'Python', 'SQL', 'TensorFlow', 'Kubernetes', 'Scala', 'PyTorch', 'Linux', 'Git',
    'Java', 'GCP', 'Hadoop', 'Tableau', 'R', 'Computer Vision', 'Data Visualization',
    'Deep Learning', 'MLOps', 'Spark', 'NLP', 'Azure', 'AWS', 'Mathematics', 'Docker', 'Statistics'
]

# Sum the values for each skill to get frequency
skill_counts = df[skill_columns].sum().sort_values(ascending=False)

# Convert to dictionary
skill_freq = skill_counts.to_dict()

wordcloud = WordCloud(
    width=800,
    height=400,
    background_color='#222222',  # dark charcoal background
    colormap='cividis'
).generate_from_frequencies(skill_freq)


# Display the word cloud
plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Top In-Demand Skills in AI Jobs')
plt.show()

plt.savefig('skills_wordcloud.png', bbox_inches='tight', dpi=300)