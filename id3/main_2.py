# Generador de Arboles de Decisión.
# Mauricio Beranbe Fortuna Lopez
# IA 7:00 - 8:00

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

    """print(global_count_no)
    print(global_count_yes)
    print(total_jugar)"""

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
    #print("Sera divido por:", tag_of_max_value)

    # Creamos la lista para poder dividir el DF
    outcomes = df[tag_of_max_value].unique().tolist()
    #print(outcomes)

    # Creamos las tablas, separandolas por el atributo con mas ganancia.
    for outcome in outcomes:
        branch = df.loc[df[tag_of_max_value] == outcome]

        if not is_unique(branch["jugar"]):
            branches_node.append(branch)
            print("\nTabla NO terminal:")
            print(branch)
        else:
            branches_leaf.append(branch)
            print("\nTabla terminal, se alcanzo HOMOGENEIDAD:")
            print(branch)

    return branches_leaf, branches_node, tag_of_max_value, outcomes


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

def main():
    
    tree = {}

    # Separacion Inicial
    tables = get_frec_tables(df,class_to_omit=[])
    print("Separacion y Cuenta de Tablas:")
    print(tables)
    gains = get_gain(df, tables)
    #print(gains)

    end_branches, next_branches, next_omition, outcomes = create_dfs(df, gains)

    #print("We separate by:", next_omition)
    #print("The branches are:", outcomes)

    #print("ENDS:\n",end_branches)
    #print("NODE:\n",next_branches)

    tree.update({next_omition:{}})

    # Obtener los nodos que seran hojas.
    for ends in end_branches:
        to_leaf = ends[next_omition].unique()
        value = ends["jugar"].unique()[0]
        print(value)

    # Añadir al arbol.
    for outcome in outcomes:
        if outcome != to_leaf[0]:
            tree[next_omition].update({outcome:{}})
        else:
            tree[next_omition].update({outcome:value})

    print(tree)

    route_travel = ["vista"]
    route = ["vista"]
    # Comienzo de las iteraciones
    while next_branches:
        route.append(next_omition)
        omitions = []
        print("\n--------------------SIGUIENTE NIVEL--------------------:")
        for branch in next_branches:
            print("\nSiguiente Tabla: ")
            #print("Estamos en la tabla que le corresponde a:", omitions)
            tables = get_frec_tables(branch,omitions)
            print("Separacion y Cuenta de Tablas:")
            print(tables)
            gains = get_gain(branch, tables)
            #print(gains)
            end_branches, next_branches, next_omition, outcomes = create_dfs(branch, gains)
            omitions.append(next_omition)

            current_key = branch[route[-1]].unique()[0]

            """
            print("We are working with the branch of:", current_key)
            print("We separate by:", next_omition)
            print("The branches are:", outcomes)"""

            # print("ENDS:\n",end_branches)
            # print("NODE:\n",next_branches)

            final_branches = end_branches + next_branches
            #print("OPTIONS:", final_branches)
            
            chunk = {current_key: {next_omition: outcomes}}
            ramificaciones = chunk[current_key][next_omition]
            
            print("Attribute:", next_omition)

            for branch in final_branches:
                if is_unique(branch["jugar"]):
                    key_of_final_branch = branch[next_omition].unique()[0]
                    values_of_final_branch = []
                    for branch in final_branches:
                        if is_unique(branch["jugar"]):
                            values_of_final_branch.append(branch["jugar"].unique()[0])
                    chunk[current_key][next_omition] = {ramificacion: value for ramificacion, value in zip(ramificaciones, values_of_final_branch)}
                else:
                    key_of_final_branch = branch[next_omition].unique()[0]
                    chunk[current_key][next_omition][key_of_final_branch] = {}

            combinar_diccionarios(tree['vista'], chunk)

    print("\nArbol de Desicion:")
    print(tree)
    print("\nReglas:")
    find_leaf_paths(tree)
            
if __name__ == '__main__':
    main()
