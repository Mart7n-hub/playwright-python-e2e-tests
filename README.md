# Playwright Python E2E Tests
Automatizované end-to-end testy webu Engeto vytvořené pomocí Python, Pytest a Playwright.

## Použité technologie
- Python 3.x
- Pytest
- Playwright
- python-dotenv

## Testované scénáře
### 1. Odmítnutí cookies
Test ověřuje, že po kliknutí na tlačítko pro odmítnutí cookies zmizí cookie banner.

### 2. Navigace na stránku kurzu
Test ověřuje:
- přechod na stránku Testing Akademie
- otevření seznamu termínů kurzu
- zobrazení nadpisu Termíny

### 3. Přihlášení do výukového portálu
Test ověřuje:
- přihlášení pomocí e-mailu a hesla
- úspěšné přesměrování do studijní sekce
- dostupnost tlačítka Záznamy lekcí

## Konfigurace
V kořenovém adresáři projektu vytvořte soubor .env:

```env
USERNAME=vas_email
PASSWORD=vase_heslo
```
## Spuštění testů

```bash
pytest -vv -s
