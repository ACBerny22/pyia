# Generador de Arboles de Decisión.
# Mauricio Beranbe Fortuna Lopez
# IA 7:00 - 8:00

import pandas as pd
import math

df = pd.read_csv("id3/tennis.csv")

collection = []

classes = df.columns.values
class_target = classes[-1]
outcomes = df[class_target].unique().tolist() # Lista con las clases per se, en este caso SI y NO.

# Devuelve un diccionario con las frecuencias SI y NO.
def get_frec_tables(df, class_to_omit):
    dict = {}
    for clas in classes[:-1]:
        if clas == class_to_omit:
            continue
        
        rows = df[clas].unique()

        element = []
        for value in rows:
            count_yes = df[df[class_target] == 'si'][clas].eq(value).sum()
            count_no = df[df[class_target] == 'no'][clas].eq(value).sum()

            row = [value, count_yes, count_no]
            element.append(row)
            #print(row)
        dict.update({clas:element})

    return dict

# Recibe el diccionario y devuelve una matriz con la ganancia para cada clase
def get_gain(df, tables):

    # Para la ganancia, necesitamos acutalizar los valores que recibe para cada dataframe
    global_count_yes = len(df[df[class_target] == 'si'])
    global_count_no = len(df[df[class_target] == 'no'])
    total_jugar = len(df[class_target])

    global_entropy = -(global_count_yes/total_jugar)*math.log2(global_count_yes/total_jugar)-(global_count_no/total_jugar)*math.log2(global_count_no/total_jugar)
    print("Entropia del Conjunto:", global_entropy)

    gains = []
    for element in tables:
        entropy = 0
        for row in tables[element]:
            if row[1] == 0 or row[2] == 0:
                continue
            row_count = row[1]+row[2]
            take = ((row_count)/total_jugar)*(-(row[1]/row_count)*math.log2(row[1]/row_count)-(row[2]/row_count)*math.log2(row[2]/row_count))
            print("Entropia individual:", take)
            entropy += take

        gains.append([global_entropy-entropy, element])
    return gains 

def is_unique(s):
    a = s.to_numpy() # s.values (pandas<0.24)
    return (a[0] == a).all()

def create_dfs(df, gains):
    
    branches_leaf = []
    branches_node = []


    # Encontramos el valor con mayor ganancia
    max_value = max(gains, key=lambda x: x[0]) 
    tag_of_max_value = max_value[1]
    temp_dict = {tag_of_max_value:{}}

    # Creamos la lista para poder dividir el DF
    outcomes = df[tag_of_max_value].unique().tolist()

    print("Root:", tag_of_max_value)
    print("Branches:", outcomes)

    for outcome in outcomes:
        temp_dict[tag_of_max_value].update({outcome:{}})

    # Creamos las tablas, separandolas por el atributo con mas ganancia.
    for outcome in outcomes:
        branch = df.loc[df[tag_of_max_value] == outcome]

        if not is_unique(branch[class_target]):
            branches_node.append(branch)
            print("\nTabla NO terminal:")
            print(branch)
            print(outcome, ":", "{}")
            temp_dict[tag_of_max_value][outcome] = {}

        else:
            branches_leaf.append(branch)
            print("\nTabla terminal, se alcanzo HOMOGENEIDAD:")
            print(branch)
            print(outcome, ":", branch[class_target].unique()[0])
            temp_dict[tag_of_max_value][outcome] = branch[class_target].unique()[0]


    print(temp_dict)
    #collection.append(temp_dict)
    
    return branches_leaf, branches_node, tag_of_max_value, temp_dict


def combinar_diccionarios(dic_principal, *diccionarios):
    for dic in diccionarios:
        for key, value in dic.items():
            if key in dic_principal:
                dic_principal[key] = value
            else:
                dic_principal["lluvioso"]["viento"]["fuerte"] = value
                #dic_principal[key] = dic_principal.get(key, value)

def find_leaf_paths(tree, path=None):
    if path is None:
        path = []

    for key, value in tree.items():
        current_path = path + [key]

        if isinstance(value, dict):
            find_leaf_paths(value, current_path)
        else:
            print(" -> ".join(current_path) + " : " + str(value))


def iter(next_branches, next_omition):
    # Comienzo de las iteraciones
    print("\n--------------------SIGUIENTE NIVEL--------------------:")
    prayer = next_omition
    print("THIS WILL COMEOUT FROM:", prayer)
    while next_branches:
        #omitions = []
        print("\n--------------------SIGUIENTE ROOT PARENT LEVEL--------------------:")
        #print("LOS SLOTS DE ESTAS TABLAS SALEN DEL:", next_omition)
        for branch in next_branches:
            print("\nSiguiente Tabla: ")
            tables = get_frec_tables(branch,next_omition)
            print("Separacion y Cuenta de Tablas:")
            print(tables)
            gains = get_gain(branch, tables)
            end_branches, next_branches, next_omition, temp_dict = create_dfs(branch, gains)
            collection.append((temp_dict, prayer))

            
            if next_branches:
                print("The ones that are not yet resolved:", next_branches[0][next_omition].unique()[0])
                iter(next_branches, next_branches[0][next_omition].unique()[0])

        if len(end_branches) > 0:
            break

def main():
    
    tree = {}

    # Separacion Inicial
    tables = get_frec_tables(df,class_to_omit=[])
    print("Separacion y Cuenta de Tablas:")
    print(tables)
    gains = get_gain(df, tables)

    end_branches, next_branches, next_omition, out_tree = create_dfs(df, gains)
    collection.append((out_tree, None))

    # Comienzo de las iteraciones
    iter(next_branches, next_omition)

    print("AND SO, WE HAVE THIS SHIT:")
    for coll in collection:
        print(coll)
            
if __name__ == '__main__':
    main()
