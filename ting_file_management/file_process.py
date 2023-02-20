import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for index in instance._data:  # lista inicial queue
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
    if len(instance) == 0:
        return print("Não há elementos", file=sys.stdout)

    arquive_removed = instance.dequeue()
    path_file = arquive_removed["nome_do_arquivo"]

    print(f"Arquivo {path_file} removido com sucesso\n", file=sys.stdout)


def file_metadata(instance, position):
    try:
        result = instance.search(position)
        print(f"{result}", file=sys.stdout)
    except IndexError:
        print("Posição inválida", file= sys.stderr)
