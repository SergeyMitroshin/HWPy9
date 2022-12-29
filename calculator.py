import numexpr as ne

def calc(arg_str):
    return str(ne.evaluate(arg_str))

# Функцию calc можно выписать вручную, но мне очень понравилась библиотека numexpr
# своим функционалом. Также она защищена от атаки выполнения кода (инъекци)
