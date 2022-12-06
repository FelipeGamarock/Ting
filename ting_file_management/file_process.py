import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    content_list = txt_importer(path_file)
    dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(content_list),
        "linhas_do_arquivo": content_list
    }

    for index in range(instance.__len__()):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None

    instance.enqueue(dict)
    print(f"{dict}", file=sys.stdout)
    

def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
