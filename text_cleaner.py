import re


def clean_resume_text(text):

    # lowercase
    text = text.lower()

    # preserve technical words
    text = text.replace("c++", "cplusplus")
    text = text.replace("c#", "csharp")
    text = text.replace(".net", "dotnet")

    # remove unwanted characters
    text = re.sub(r"[^a-z0-9\s]", " ", text)

    # remove multiple spaces
    text = re.sub(r"\s+", " ", text).strip()

    # restore keywords
    text = text.replace("cplusplus", "c++")
    text = text.replace("csharp", "c#")
    text = text.replace("dotnet", ".net")

    return text