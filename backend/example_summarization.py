# Use a pipeline as a high-level helper
from transformers import pipeline


def summarize(text):
  pipe = pipeline("summarization", model="Falconsai/text_summarization")

  ARTICLE = text
  print(pipe(ARTICLE, max_length=1200, min_length=500, do_sample=False))