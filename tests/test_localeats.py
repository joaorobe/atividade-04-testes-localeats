import pytest
from playwright.sync_api import Page, sync_playwright


BASE_URL = "https://local-eats-unisenac.vercel.app"
LOGIN_URL = f"{BASE_URL}/static/login.html"


@pytest.fixture
def page() -> Page:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()
        yield page
        browser.close()


def test_aba_criar_conta_apresenta_campos_de_cadastro(page: Page):
    page.goto(LOGIN_URL)
    assert page.title() == "Entrar | Local Eats"
    assert page.get_by_text("Bem-vindo ao app de Qualidade de Software").is_visible()

    page.get_by_role("button", name="Criar Conta").click()

    assert page.get_by_placeholder("Seu nome").is_visible()
    assert page.get_by_role("button", name="Registrar").is_visible()


def test_login_vazio_bloqueia_envio_por_campo_obrigatorio(page: Page):
    page.goto(LOGIN_URL)
    email = page.get_by_placeholder("teste@teste.com")
    assert email.is_visible()
    assert page.get_by_placeholder("Sua senha secreta").is_visible()

    page.get_by_role("button", name="Entrar").nth(1).click()

    assert page.url == LOGIN_URL
    assert email.evaluate("(element) => element.validity.valueMissing") is True
