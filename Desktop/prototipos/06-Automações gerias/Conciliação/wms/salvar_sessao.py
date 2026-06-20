from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    contexto = navegador.new_context()
    pagina = contexto.new_page()
    pagina.goto("https://wms-revendas.ambevtech.com.br/wmsnew/login")