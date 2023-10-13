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

# Obtiene de manera individual.
def get_prob_value(content, clas, attribute_index):

    class_index = 1
    if clas == 'si': class_index = 0 

    # Obtiene la fila de probabilidades, segun el atributo.
    selected_line = all_matrix[attribute_index]
    # Segun la clase que sea, selecciona la tupla.
    selected_tuple = next((tupla for tupla in selected_line if tupla[0] == content), None)

    # Selecciona la probabilidad dependiendo de la clase que se esta buscando (si o no)
    selected_prob = selected_tuple[(1+class_index)]

    print(selected_prob)
    return selected_prob


def get_class_by_args(args):
    max_index = args.index(max(args))
    return classes[max_index]


def main():
    get_prob_matrix(attributes)

    print(attributes)

    """
    for row in all_matrix:
        print(' ', row)
    """

    test_case = ["soleado", "baja", "normal", "no"] #No incluimos jugar.

    args = []
    for clas in classes:
        print("for: ", clas)
        prob = 1 
        for i in range(len(test_case)):
            prob = prob * get_prob_value(test_case[i], clas, i)
        
        # La ultima fila de tuplas es la de jugar.
        clas_line = all_matrix[len(all_matrix) - 1]
        selected_tuple = next((tupla for tupla in clas_line if tupla[0] == clas), None)

        class_index = 1
        if clas == 'si': class_index = 0 

        prob = prob * (selected_tuple[1+class_index])
        args.append(prob)

    print(args)
    
    final_class = get_class_by_args(args)
    print("La clasificacion final es: ", final_class)

    
    

if __name__ == '__main__':
    main()
