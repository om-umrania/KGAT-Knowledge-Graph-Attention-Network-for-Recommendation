import numpy as np
import pandas as pd
import random

# Parameters for synthetic data generation
num_users = 1000  # Number of users
num_codes = 200   # Number of code items
num_images = 200  # Number of image items
num_videos = 100  # Number of video items
num_documents = 150  # Number of document items
num_links = 150  # Number of link items
num_attributes = 50  # Number of item attributes
interaction_probability = 0.1  # Probability of a user interacting with an item

# Define item categories
item_categories = ['code', 'image', 'video', 'document', 'link']

# Generate user-item interactions
user_ids = np.arange(1, num_users + 1)
item_ids = np.arange(1, sum([num_codes, num_images, num_videos, num_documents, num_links]) + 1)

# Create an empty list to store interactions
interactions = []

for user in user_ids:
    for item in item_ids:
        if random.random() < interaction_probability:
            interactions.append((user, item))

# Convert interactions to a DataFrame
interactions_df = pd.DataFrame(interactions, columns=['user_id', 'item_id'])

# Generate item attributes based on content type
attributes = np.arange(1, num_attributes + 1)
item_attributes = []
item_count = 1

# Assign attributes to each content type
for category, count in zip(item_categories, [num_codes, num_images, num_videos, num_documents, num_links]):
    for _ in range(count):
        num_item_attributes = random.randint(1, 3)
        selected_attributes = random.sample(list(attributes), num_item_attributes)
        for attr in selected_attributes:
            item_attributes.append((item_count, category, attr))
        item_count += 1

# Convert item-attribute relationships to a DataFrame
item_attributes_df = pd.DataFrame(item_attributes, columns=['item_id', 'category', 'attribute_id'])

# Create a knowledge graph based on item-attribute relationships
kg_relations = []

for item, category, attr in item_attributes:
    # Each attribute can be related to 1 to 3 other items across categories
    num_related_items = random.randint(1, 3)
    related_items = random.sample(list(item_ids), num_related_items)
    for related_item in related_items:
        kg_relations.append((item, category, attr, related_item))

# Convert knowledge graph relations to a DataFrame
kg_relations_df = pd.DataFrame(kg_relations, columns=['item_id', 'category', 'attribute_id', 'related_item_id'])

# Display the generated data
print("User-Item Interactions:")
print(interactions_df.head())

print("\nItem-Attribute Relationships:")
print(item_attributes_df.head())

print("\nKnowledge Graph Relations:")
print(kg_relations_df.head())

# Save the data to CSV files for further use
interactions_df.to_csv('synthetic_user_item_interactions_multimedia.csv', index=False)
item_attributes_df.to_csv('synthetic_item_attributes_multimedia.csv', index=False)
kg_relations_df.to_csv('synthetic_knowledge_graph_relations_multimedia.csv', index=False)
