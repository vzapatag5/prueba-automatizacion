from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # para ver qué pasa
        page = browser.new_page()

        # Página de prueba directa
        page.goto("https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv")

        # Guardar contenido directamente
        content = page.content()

        with open("archivo_prueba.csv", "w", encoding="utf-8") as f:
            f.write(content)

        print("Archivo guardado correctamente")
        browser.close()

run()