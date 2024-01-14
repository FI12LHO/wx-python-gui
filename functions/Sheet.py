from pathlib import Path

import gspread


def append_row(content: list) -> None:
    # apontando caminho ao arquivo service
    service = Path("./service_account.json")

    # instanciando classe e apontando ao arquivo service com as credenciais
    gc = gspread.service_account(filename=service)

    # ID da planilha
    wk_sheet = gc.open_by_key("1JqveM0s_g0v6HAVO23xrfKJQTW3Xhb6PWZ4rKFL0sAk")

    # obtendo a primeira pagina da planilha
    sh1 = wk_sheet.sheet1

    # adicionando linha ao final da planilha
    sh1.append_row(content)

    pass
