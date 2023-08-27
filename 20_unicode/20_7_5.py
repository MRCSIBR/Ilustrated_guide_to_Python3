import demoji

"""
Para reemplazar emojis old school con las versiones Unicode podemos usar la libreria
demoji. https://pypi.org/project/demoji/

Requerimientos:
    $pip install demoji

"""
import demoji

def replace_emojis(text):
    # Replace the old school emojis with Unicode versions
    text = demoji.replace(text)

    return text


print(replace_emojis("Hello world! :P"))