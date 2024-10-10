from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session as Session_n
from Models.models import Usuario

# Conexão com Base de dados
db = create_engine("sqlite:///base.db", echo=True)

# Criar sessão para realizar operações de CRUD

Session = sessionmaker(bind=db)


# Operação de Escrita
def create(modelos):
    # Verifica se 'modelos' é iterável; se não for, transforma em uma lista
    if not isinstance(modelos, list):
        modelos = [modelos]

    with Session() as s:
        for modelo in modelos:
            s.add(modelo)
        s.commit()

# Operação de Leitura
def read(user_email):
    with Session() as s:
        usuario = s.query(Usuario).filter(Usuario.email == f'{user_email}').first()
    return usuario

def update(nome: str, email: str, senha: str):
    with Session() as s:
        usuario = s.query(Usuario).filter(Usuario.email == email).first()
        if usuario:
            usuario.nome = nome
            usuario.email = email
            usuario.senha = senha
            s.commit()
            s.refresh(usuario)
            return usuario
        return None

def delete(user_email: str):
    with Session() as s:
        usuario = s.query(Usuario).filter(Usuario.email == user_email).first()
        if usuario:
            s.delete(usuario)
            s.commit()
            return None

#Operação de Atualização de usario especifico usando o e-mail - opção1
def update_aluno(nome: str, email: str, telefone: str, endereco: str, session_email: str):
    with Session() as s:
        usuario  = s.query(Usuario).filter(Usuario.email == f'{session_email}').first()
        if usuario:
            usuario.nome = nome
            usuario.email = email
            usuario.telefone = telefone
            usuario.endereco = endereco

            s.commit()
            s.refresh(usuario)
            return usuario
        return None

#Operação de Atualização de usario especifico usando o e-mail - opção1
def update_prof(nome: str, email: str, telefone: str, endereco: str, modalidade: str, horario: str, preco: str,session_email: str):
    with Session() as s:
        usuario  = s.query(Usuario).filter(Usuario.email == f'{session_email}').first()
        if usuario:
            usuario.nome = nome
            usuario.email = email
            usuario.telefone = telefone
            usuario.endereco = endereco

            usuario.modalidade = modalidade
            usuario.horario = horario
            usuario.preco = preco

            s.commit()
            s.refresh(usuario)
            return usuario
        return None
    
# Função para buscar profissionais da modalidade basquete
def get_profissionais_modalidade(session: Session_n,modalidade_profissional):
    # Faz a consulta para buscar todos os usuários do tipo 'profissional' e modalidade 'basquete'
    profissionais_modalidade = session.query(Usuario).filter(
        Usuario.tipo == 'profissional',  # Verifica se o tipo é 'professor'
        Usuario.modalidade == modalidade_profissional  # Verifica se a modalidade é 'basquete'
    ).all()  # Pega todos os resultados que satisfazem a condição

    return profissionais_modalidade