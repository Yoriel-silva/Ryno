from sqlalchemy.orm import (declarative_base, 
                            Mapped, 
                            mapped_column)

# Modelos de dados
Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    senha: Mapped[str] = mapped_column(nullable=False)
    
    tipo: Mapped[str] = mapped_column(nullable=True)

    telefone: Mapped[str] = mapped_column(nullable=True)
    horario: Mapped[str] = mapped_column(nullable=True)
    modalidade: Mapped[str] = mapped_column(nullable=True)
    preco: Mapped[str] = mapped_column(nullable=True)