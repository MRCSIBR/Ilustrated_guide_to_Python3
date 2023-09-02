import re

def convert_case(cadena, separator='_'):
    # Convertir camel case a snake case
    snake_case = re.sub('([A-Z])', r'_\1', cadena).lower().lstrip('_')

    # Convertir snake case a kebab case
    kebab_case = snake_case.replace('_', separator)

    return kebab_case

cadena = 'estoEsUnEjemplo'
snake_case = convert_case(cadena)
kebab_case = convert_case(cadena, separator='-')

print(snake_case)  # 'esto_es_un_ejemplo'
print(kebab_case)  # 'esto-es-un-ejemplo'
