from PyPDF2 import PdfReader
import os


def get_splitted_text(text: str) -> str:
    first_paragraphs: [str] = ["I. INTRODUCTION", "1 Introduction", "1. Introduction", "1.1 Introduction", "1.1. Introduction",
                               "Introduction"]
    for paragraph in first_paragraphs:
        if paragraph in text:
            return text.split(paragraph)[1]
    return text


def split_first_page(page: str) -> (str, str):
    x = page.split("Abstract")
    abstract: str = ""
    text: str = ""
    if len(x) == 2:
        abstract = x[0]
        text = get_splitted_text(x[1])
    else:
        x = page.split("abstract")
        if len(x) == 2:
            abstract = x[0]
            text = get_splitted_text(x[1])

    return abstract, text


def get_abstract_and_text(filename: str) -> (str, str):
    # read the pdf file
    reader = PdfReader(filename)
    abstract: str = ""
    text: str = ""
    i = 0
    for page in reader.pages:
        if i == 0:
            first_page = page.extractText()
            abstract, text = split_first_page(first_page)
        else:
            text += page.extractText()
        i += 1
    return abstract, text


def get_similarity_index(abstract, generated_abstract) -> float:
    # calculate the jaccard index
    abstract_words = set(abstract.split())
    generated_abstract_words = set(generated_abstract.split())
    intersection = abstract_words.intersection(generated_abstract_words)
    union = abstract_words.union(generated_abstract_words)
    return float(len(intersection) / len(union))
