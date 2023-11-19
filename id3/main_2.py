import pandas as pd
import math

df = pd.read_csv("id3/nb.csv")

classes = df.columns.values
class_target = classes[-1]
outcomes = df[class_target].unique().tolist() # Lista con las clases per se, en este caso SI y NO.

# Devuelve un diccionario con las frecuencias SI y NO.
def get_frec_tables(df, class_to_omit):
    dict = {}

    for clas in classes[:-1]:

        if clas in class_to_omit:
            continue
        
        rows = df[clas].unique()
        #print(df[clas].unique())

        element = []
        for value in rows:
            count_yes = df[df['jugar'] == 'si'][clas].eq(value).sum()
            count_no = df[df['jugar'] == 'no'][clas].eq(value).sum()

            row = [value, count_yes, count_no]
            element.append(row)
            #print(row)

        dict.update({clas:element})

    return dict

# Recibe el diccionario y devuelve una matriz con la ganancia para cada clase
def get_gain(df, tables):

    # Para la ganancia, necesitamos acutalizar los valores que recibe para cada dataframe
    global_count_yes = len(df[df['jugar'] == 'si'])
    global_count_no = len(df[df['jugar'] == 'no'])
    total_jugar = len(df['jugar'])

    print(global_count_no)
    print(global_count_yes)
    print(total_jugar)


    global_entropy = -(global_count_yes/total_jugar)*math.log2(global_count_yes/total_jugar)-(global_count_no/total_jugar)*math.log2(global_count_no/total_jugar)
    print(global_entropy)

    gains = []
    for element in tables:
        entropy = 0
        for row in tables[element]:
            if row[1] == 0 or row[2] == 0:
                continue
            row_count = row[1]+row[2]
            take = ((row_count)/total_jugar)*(-(row[1]/row_count)*math.log2(row[1]/row_count)-(row[2]/row_count)*math.log2(row[2]/row_count))
            entropy += take

        gains.append([global_entropy-entropy, element])
    return gains 

def is_unique(s):
    a = s.to_numpy() # s.values (pandas<0.24)
    return (a[0] == a).all()

def create_dfs(df, gains):
    
    branches = []

    # Encontramos el valor con mayor ganancia
    max_value = max(gains, key=lambda x: x[0]) 
    tag_of_max_value = max_value[1]  
    print("Sera divido por:", tag_of_max_value)

    # Creamos la lista para poder dividir el DF
    outcomes = df[tag_of_max_value].unique().tolist()
    print(outcomes)

    # Creamos las tablas, separandolas por el atributo con mas ganancia.
    for outcome in outcomes:
        branch = df.loc[df[tag_of_max_value] == outcome]

        if not is_unique(branch["jugar"]):
            branches.append(branch)
            print("WE SHALL CONTINUE")
            print(branch)
        else:
            print("NEW RULE HAS BEEN CREATED!!")
            print(branch)

    return branches, tag_of_max_value


def main():
    
    # Separacion Inicial
    tables = get_frec_tables(df,class_to_omit=[])
    print(tables)
    gains = get_gain(df, tables)
    next_branches, next_omition = create_dfs(df, gains)

    # Comienzo de las iteraciones
    while next_branches:
        omitions = []
        for branch in next_branches:
            tables = get_frec_tables(branch,omitions)
            print(tables)
            gains = get_gain(branch, tables)
            print(gains)
            next_branches, next_omition = create_dfs(branch, gains)
            omitions.append(next_omition)


if __name__ == '__main__':
    main()