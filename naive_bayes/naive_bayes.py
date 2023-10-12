import pandas as pd

archivo_csv = './naive_bayes/nb.csv'  # Reemplaza con la ruta de tu archivo CSV
df = pd.read_csv(archivo_csv)

all_matrix = []

# Atributos individuales (Headers).
attributes = list(df.columns.values)

# Obtengamos constantes...
class_target = attributes[len(attributes) - 1] # Nombre del atributo TARGET.
classes = df[class_target].unique().tolist() # Lista con las clases per se, en este caso SI y NO.


# Im sooo incompetent!.
def get_totals(df):
    sum = 0
    for elemento, ocurrencias in df.items():
        sum += ocurrencias
    return sum

#Construimos la tupla de frecuencias
def build_tuple(element, array_of_frec, target_class):

    df_n = array_of_frec[0][0]
    df_s = array_of_frec[1][0]

    #Armarmos la tupla.
    tup = (element, df_s[element]/(get_totals(df_s)), df_n[element]/(get_totals(df_n)))

    if target_class == class_target:
        total = get_totals(df_n) + get_totals(df_s)
        tup = (element, df_s[element]/total, df_n[element]/total)


    return tup


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
            tupla = build_tuple(element, frec_by_element, attributes[i])
            all_matrix_row.append(tupla)
        
        # Añadimos la lista de tuplas generada anteriormente.
        all_matrix.append(all_matrix_row)


def get_prob_value(attribute, to_target):
    pass

def main():
    get_prob_matrix(attributes)

    print(attributes)

    for row in all_matrix:
        print(' ', row)


if __name__ == '__main__':
    main()
