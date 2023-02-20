import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for index in instance._data: # lista inicial queue
        if index["nome_do_arquivo"] == path_file:
            return None

    arquive = txt_importer(path_file)

    dict_file = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(arquive),
        "linhas_do_arquivo": arquive
    }
    instance.enqueue(dict_file)
    print(dict_file, file=sys.stdout)
    # Para garantir mostrar via stdout os dados processados


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
