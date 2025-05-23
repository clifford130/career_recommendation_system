# advisor/knowledge/ai_analysis.py
from transformers import pipeline
from .frames import career_frames # Added import

# Create a text classification pipeline using a pre-trained model.
# (This is a simple example; in a real-world scenario, you might train your own model.)
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def analyze_career_fit(text): # candidate_labels parameter removed
    """
    Analyzes the free-text input (e.g., career goals or experiences) and
    returns scores for a list of candidate career labels.
    """
    candidate_labels = list(career_frames.keys()) # Dynamically set

    # The classifier by default sorts labels by score in descending order.
    # multi_label=False is the default, meaning scores are for single best fit.
    result = classifier(text, candidate_labels) 
    
    # Return all labels and their corresponding scores, sorted by score by the pipeline
    return result["labels"], result["scores"]
