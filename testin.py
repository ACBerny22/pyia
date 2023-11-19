import json

x =  { 
    "estado":{
        "lluvia":{
            "viento":{
                "leve":"SI",
                "fuerte":{
                    "humedad":{
                        "alta":"SI",
                        "normal":"NO"
                    }
                }
            }
        },
        "nublado":"SI",
        "soleado":{
            "humedad":{
                "alta":"NO",
                "normal":"SI"
            }
        },
        }
    }

def find_leaf_paths(tree, path=None):
    if path is None:
        path = []

    for key, value in tree.items():
        current_path = path + [key]

        if isinstance(value, dict):
            find_leaf_paths(value, current_path)
        else:
            print(" -> ".join(current_path) + " : " + str(value))

print(x) 