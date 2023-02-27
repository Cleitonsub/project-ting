from ting_file_management.queue import Queue


def exists_word(word: str, instance: Queue):
    results = []
    occurrences = []
    
    for index, line in enumerate(instance.search(0)["linhas_do_arquivo"]):
        if word.lower() in line.lower():
            occurrences.append({"linha": index + 1})

    if occurrences:
        results.append({
            "palavra": word,
            "arquivo": instance.search(0)["nome_do_arquivo"],
            "ocorrencias": occurrences
        })

    return results


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
