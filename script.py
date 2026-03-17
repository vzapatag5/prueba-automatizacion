from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv")

        content = page.content()

        # 👇 ruta absoluta segura
        file_path = os.path.join(os.getcwd(), "archivo_prueba.csv")

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

        print("Archivo guardado en:", file_path)

        browser.close()

run()