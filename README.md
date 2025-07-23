Google Scraper

Jednoduchá Flask aplikace pro získávání organických výsledků z první stránky Googlu na základě zadaného klíčového slova. Výsledky lze stáhnout ve formátu JSON.

🔍 Funkce
Webová stránka s formulářem pro zadání klíčového slova

Vyhledání výsledků z první stránky Google (organické výsledky)

Zobrazení výsledků v přehledném seznamu

Možnost stáhnout výsledky ve formátu JSON

Unit test pro ověření funkce scraperu

🖥️ Online verze
Aplikace je nasazená na Render:
https://google-scraper-151u.onrender.com/


✅ Lokální spuštění

1. Naklonuj repozitář, je uložen v ZIP v e-mailu:

bash
git clone https://github.com/kubahradil/google-scraper.git

cd google-scraper

2. Vytvoř virtuální prostředí a aktivuj:

bash
python -m venv venv

venv\Scripts\activate      # Windows

source venv/bin/activate   # Linux/Mac

3. Nainstaluj závislosti:

bash
pip install -r requirements.txt

4. Spusť aplikaci:

bash
flask run

5. Otevři v prohlížeči:
http://127.0.0.1:5000


✅ Spuštění testů

Pro ověření funkčnosti scraperu:

bash
python -m unittest discover tests


⚙️ Použité technologie

Python 3

Flask (webový framework)

Requests + BeautifulSoup (scraping)

Gunicorn (produkční server pro Render)

