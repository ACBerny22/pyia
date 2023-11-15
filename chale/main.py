import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize

# Separado por parrafos.
with open("D:\Tareas 8vo Semestre\pyia\chale\input2.txt", "r", encoding="utf8") as f:
    paragraphs = f.readlines()

punc = '''!()—-«»[]{};:'"\,<>/?@#$%^&*_~''' # No "."
dict = {}
df = pd.read_csv('./chale/stopwords.csv')

stopwords_list = df['word'].tolist()  # Reemplaza 'stopword_columna' con el nombre real de la columna de stopwords

def remove_stopwords(input_text):
    words = word_tokenize(input_text)
    filtered_words = [word for word in words if word.lower() not in stopwords_list]
    return ' '.join(filtered_words)


# Limpia el texto y devuelve una matriz con cada linea para cada parrafo.
def clear_text(text):
    clean_paragraphs = []
    for line in text:
        # Remover signos de puntuacion
        for word in line:
            if word in punc:
                line = line.replace(word, "")
                line = remove_stopwords(line)
        
        clean_paragraphs.append(line)
    return clean_paragraphs

def create_dict(paras):
    for para in paras:
        for sentence in para:
            #print(sentence)
            words = word_tokenize(sentence)
            for i in range(len(words)):
                dict[words[i]] = 1 + dict.get(words[i], 0)

    keys = list(dict.keys())
    values = list(dict.values())
    sorted_value_index = np.argsort(values)[::-1]
    sorted_dict = {keys[i]: values[i] for i in sorted_value_index}
    return sorted_dict

def get_sentences(paras):
    line_group = []
    for paragraph in paras:
        lines = paragraph.split(". ")
        line_group.append(lines)
    return line_group


def evaluate_sentences(paras, dict):
    value = 0
    paras = get_sentences(paras)
    sentences_with_rank = []
    for para in paras:
        #print("NEW PARAGRAPH")
        grouped_sentences = []
        for line in para:
            #print(line)
            words = word_tokenize(line)
            for word in words:
                if word in dict:
                    #print(dict[word])
                    value += dict[word]
                else: continue
            grouped_sentences.append([value, line])
            value = 0
        #print(grouped_sentences)
        sentences_with_rank.append(grouped_sentences)
    return sentences_with_rank


def k_largest(iterable, k):
    it = iter(iterable)
    result = [next(it) for _ in range(k)] # O(k) space
    r_min = min(result)
    for elem in it:
        if elem > r_min:
            result.remove(r_min)  # O(n*k) time
            result.append(elem)
            r_min = min(result)
    return result

def select_lines(choices, n):
    collection = []
    for parag in choices:
        if n < len(parag):
            selection = k_largest(parag, n)
        else:
            selection = k_largest(parag, len(parag))
        collection.append(selection)
    return collection

def build_text(choices):
    text = ""
    for parag in choices:
        for line in parag:
            text += line[1]
            
            if line[1][-1] != "\n":
                text += ". "
    print(text)

# Limpiar el texto, quita puntuaciones y stopwords
clean_paragraphs = clear_text(paragraphs)

# Matriz de parrafos separados por enunciados.
grouped_sentences = get_sentences(clean_paragraphs)

# Crea el diccionario con los puntos de cada palabra.
dict = create_dict(grouped_sentences)

# Evaluar cada oracion.
pick_choices = evaluate_sentences(paragraphs, dict)

# Obtener las oraciones que formaran parte del resumen.
resume = select_lines(pick_choices, 2)

# Construir el parrafo completo
build_text(resume)