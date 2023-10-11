import pandas as pd

archivo_csv = './naive_bayes/nb.csv'  # Reemplaza con la ruta de tu archivo CSV
df = pd.read_csv(archivo_csv)

all_matrix = []

# Atributos individuales (Headers).
attributes = list(df.columns.values)

# Obtengamos constantes...
class_target = attributes[len(attributes) - 1] # Nombre del atributo TARGET.
classes = df[class_target].unique().tolist() # Lista con las clases per se, en este caso SI y NO.

#Construimos la tupla de frecuencias
def build_tuple(element, array_of_frec):

    probs = []

    # Basado en el elemento que toque, sacamos la probabilidad de SI.


    # Basado en el elemento que toque, sacamos la probabilidad de NO.

    # Eso, o se puede hacer con un for, dependiendo de las clases que haya, pero pos
    # primero hay que ver que pedo con el dataframe que me regreso JAJA.


    #Armarmos la tupla.
    tup = (element, probs[0], probs[1])
    print(element)


def get_frequencies_df(classes, attribute):
    
    list_of_df = []

    # En este caso, es SI y NO
    for single in classes:
        frequencies = df[df[class_target] == single][attribute].value_counts()
        frequencies = frequencies.reindex(df[attribute].unique(), fill_value=0)

        list_of_df.append((frequencies, single))

    # Yes, this is cursed, i know, but holy fuck man, give me a break .-.
    return list_of_df
    


# Armar la matriz de probabilidades.
def get_prob_matrix(attributes):
    for i in range(len(attributes)):
        # Extraemos los elementos unicos de cada atributo.
        principle = df[attributes[i]].unique().tolist()

        # Array con los df que contienen las frecuencias.
        frec_by_element = get_frequencies_df(classes, attributes[i])

        #print(frec_by_element)

        # Iteramos entre cada elemento para hacer la lista de tuplas
        # que contendra las probabilidades.
        all_matrix_row = []

        for element in principle:
            # (elemento, prob_class_1, prob_class_2)
            tupla = build_tuple(element, frec_by_element)
            all_matrix_row.append(tupla)
        
        # Añadimos la lista de tuplas generada anteriormente.
        all_matrix.append(all_matrix_row)



def main():
    get_prob_matrix(attributes)


if __name__ == '__main__':
    main()
