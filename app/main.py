from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
import uvicorn
from Models.models import Usuario
from CRUD.crud import create, read
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from starlette.middleware.sessions import SessionMiddleware
from typing import Optional
import os #Import para debug

# Conexão com DB
db = create_engine("sqlite:///base.db", echo=True)
Session = sessionmaker(bind=db)

# Variável para rodar o FastAPI
app = FastAPI()

# Senha
SECRET_KEY = "12345"
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)

# Montar pasta STATIC, lá ficam o css e as imagens
app.mount("/static", StaticFiles(directory="../Ryno/static"), name="static")

# Pasta HTML
templates = Jinja2Templates(directory="app/templates")

# Redireciona para pagina home
@app.get("/", response_class=HTMLResponse)
def read_home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

# Redireciona para pagina do aluno
@app.get("/perfil_aluno", response_class=HTMLResponse)
def read_aluno(request: Request):
    return templates.TemplateResponse("perfil_aluno.html", {"request": request})

# Redireciona para pagina do profissional
@app.get("/profissional", response_class=HTMLResponse)
def read_profissional(request: Request):
    return templates.TemplateResponse("profissional.html", {"request": request})

# Redireciona para pagina de castro
@app.get("/cadastro", response_class=HTMLResponse)
def read_cadastro(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})

# Post de Cadastro
@app.post('/cadastro/enviar', response_class=HTMLResponse)
def cadastro(
    nome: str = Form(...), 
    email: str = Form(...), 
    senha: str = Form(...), 
    tipo: Optional[str] = Form('aluno'),  # Switch pode ser None ou "on"
    telefone: Optional[str] = Form(None),  # Campos opcionais
    horario: Optional[str] = Form(None), 
    modalidade: Optional[str] = Form(None), 
    preco: Optional[str] = Form(None)
):
    tipo_final = tipo if tipo == "profissional" else "aluno"

    if tipo_final == "profissional":
        if not telefone or not horario or not modalidade or not preco:
            return HTMLResponse(content="Preencha todos os campos adicionais.", status_code=400)
        usuario = Usuario(
            nome=nome,
            email=email,
            senha=senha,
            tipo=tipo_final,
            telefone=telefone,
            horario=horario,
            modalidade=modalidade,
            preco=preco
        )
    else:
        usuario = Usuario(
            nome=nome,
            email=email,
            senha=senha,
            tipo=tipo_final
            # Não inclui os campos opcionais se o switch estiver "off"
        )
    create(usuario)
    return RedirectResponse(url=f"/login", status_code=303)

# Redireciona para pagina de login
@app.get("/login", response_class=HTMLResponse)
def read_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# Perfil Professor
@app.get("/perfil_professor", response_class=HTMLResponse)
def read_professor(request: Request):
    return templates.TemplateResponse("perfil_professor.html", {"request": request})

# Login
@app.post("/login/enviar", response_class=HTMLResponse)
def login(request: Request, email: str = Form(...), senha: str = Form(...)):
    # Obter a sessão
    session = request.session

    # Ler o usuário do banco de dados
    user = read(email)
    
    # Verificar se o usuário foi encontrado e se a senha está correta
    if not user or user.senha != senha:
        raise HTTPException(status_code=400, detail="Credenciais inválidas")
    
    # Armazenar o email do usuário na sessão
    session['user_email'] = user.email
    
    # Redirecionar para a página do perfil do aluno
    return RedirectResponse(url="/perfil_aluno", status_code=303)


# Redireciona para pagina do instagram
@app.get("/redirect-to-instagram")
def redirect_to_instagram():
    instagram_url = "https://www.instagram.com//"
    return RedirectResponse(url=instagram_url)

# Redireciona para pagina do X
@app.get("redirect-to-x")
def redirect_to_x():
    x_url = "https://www.x.com/"
    return RedirectResponse(url=x_url)

# Redireciona para pagina do Facebook
@app.get("redirect-to-facebook")
def redirect_to_facebook():
    facebook_url = "https://www.facebook.com/"
    return RedirectResponse(url=facebook_url)

# Redireciona para o Whatsapp
@app.get("redirect-to-wpp")
def redirect_to_wpp():
    wpp_url = "https://wa.me/seu_numero" # Substituir seu_numero pelo numero do sistema desse modo: 55619xxxxxxxx
    return RedirectResponse(url=wpp_url)

# Roda o programa
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=7777)