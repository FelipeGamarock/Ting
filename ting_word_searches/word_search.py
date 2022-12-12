def exists_word(word, instance):
    files_with_word = list()
    for index in range(instance.__len__()):
        content = instance.search(index)
        content_lines = content["linhas_do_arquivo"]
        ocurrences = list()
        for i in range(content_lines.__len__()):
            if word.lower() in content_lines[i].lower():
                ocurrences.append(i + 1)

        if len(ocurrences):
            files_with_word.append(
                {
                    "palavra": word,
                    "arquivo": content["nome_do_arquivo"],
                    "ocorrencias": [{"linha": row} for row in ocurrences],
                }
            )

    return files_with_word


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
