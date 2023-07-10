# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

    pip install <package> -t .

"""
import os.path
import io
import json
import sys



base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'Json' + os.sep + 'libs' + os.sep
sys.path.append(cur_path)

if cur_path not in sys.path:
    sys.path.append(cur_path)


# Globals declared here
import jsonpath_ng
from copy import deepcopy


# Default declared here
        # Initialize settings for the module here

def buscar_(fail_on_empty,json,object):
    data = True
    try:
        obj = "\""+object+"\":"
        element_exist = json.find(obj)
        if fail_on_empty is True and element_exist == -1:
            data = False
            raise Exception("Get Value From Json keyword failed to find a value")

        return data
    except Exception as e:
        PrintException()
        raise e

"""
    Obtengo el modulo que fue invocado
"""

module = GetParams("module")

if module == "read":
    path_ = GetParams('path')
    result = GetParams('var_')
    encoding = None
    try:

        with io.open(path_, mode="r", encoding=encoding) as json_file:
            data = json.load(json_file)
            data = str(data).replace("'", "\"")
        SetVar(result, data)

    except Exception as e:
        PrintException()
        raise e

if module == "create_json_file":
    path_ = GetParams('path')
    jsn = GetParams('jsn')
    result = GetParams('var_')

    try:
        ruta = os.path.join(path_)
        datos_json = json.dumps(jsn, indent=4)
        with io.open(ruta, mode="w") as file:
            file.write(datos_json)
        data = os.path.exists(ruta)


        print('a qui '+str(data))
        SetVar(result, data)
    except Exception as e:
        PrintException()
        raise e

if module == "string_to_json":
    string = GetParams('string')
    result = GetParams('var_')
    try:
        data = json.loads(string)
        SetVar(result,data)
    except Exception as e:
        PrintException()
        raise e

if module == "json_to_string":
    string = GetParams('json_object')
    result = GetParams('var_')
    try:
        data = json.dumps(string)
        SetVar(result,data)
    except Exception as e:
        PrintException()
        raise e

if module == "delete_object_from_json":
    jsn = GetParams('json')
    object = GetParams('json_object')
    result = GetParams('var_')

    try:
        data = ''
        exist = buscar_(True, jsn, object)
        print(exist)
        if exist is True:
            JSON = json.loads(jsn)
            del JSON[object]
            data = json.dumps(JSON)
            data = str(data).replace("'", "\"")
        SetVar(result,data)
    except Exception as e:
        PrintException()
        raise e

if module == "get_value_from_json":
    jsn = GetParams('json')
    object = GetParams('json_object')
    result = GetParams('var_')

    try:
        data = ''
        exist = buscar_(True,jsn,object)
        if exist is True:
            JSON = json.loads(jsn)
            data = JSON[object]
            data = str(data).replace("'", "\"")

        SetVar(result,data)
    except Exception as e:
        PrintException()
        raise e

if module == "contains_value_in_json":
    jsn = GetParams('json')
    object = GetParams('json_object')
    result = GetParams('valor_exist')
    try:
        exist = buscar_(True,jsn,object)

        SetVar(result,exist)
    except Exception as e:
        PrintException()
        raise e

if module == "update_value_from_json":
    jsn = GetParams('json')
    object = GetParams('json_object')
    n_valor = GetParams('n_valor')
    result = GetParams('var_')

    try:

        exist = buscar_(True, jsn, object)
        if exist is True:
            JSON = json.loads(jsn)
            JSON[object] = n_valor
            data = json.dumps(JSON)
            data = str(data).replace("'", "\"")

        SetVar(result, data)
    except Exception as e:
        PrintException()
        raise e

if module == "sort_json":
    jsn = GetParams('json')
    result = GetParams('var_')

    try:
        JSON = json.loads(jsn)
        data = json.dumps(JSON, sort_keys=True)
        SetVar(result, data)

    except Exception as e:
        PrintException()
        raise e
