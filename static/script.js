//Informações adicionais na hora do cadastro profissionais
function toggleInformacoes() {
    const checkbox = document.getElementById("tipo");
    const informacoesAdicionais = document.getElementById("informacoesAdicionais");

    if (checkbox.checked) {
        informacoesAdicionais.style.display = "block";  // Mostrar campos adicionais
    } else {
        informacoesAdicionais.style.display = "none";   // Esconder campos adicionais
    }
}


//Obter se é profissional ou aluno no cadastro
function atualizarValorSwitch() {
    const checkbox = document.getElementById("tipo");
    const valorSwitch = document.getElementById("valorSwitch");

    // Atualiza o valor do campo oculto baseado na posição do switch
    if (checkbox.checked) {
        valorSwitch.value = "profissional";
    } else {
        valorSwitch.value = "aluno";
    }
}


//Atualizar dados no perfil
function toggleEdit() {
    var displayElement = document.getElementById("perfil");
    var editElement = document.getElementById("edit");
    if (displayElement.style.display === "none") {
        displayElement.style.display = "block";
        editElement.style.display = "none";
    } else {
        displayElement.style.display = "none";
        editElement.style.display = "block";
    }
}

function toggleBoth() {
    var displayElement1 = document.getElementById("perfil");
    var editElement1 = document.getElementById("edit");
    var displayElement2 = document.getElementById("contato-p");
    var editElement2 = document.getElementById("edit-p");
    
    // Verifica o estado do primeiro conjunto
    if (displayElement1.style.display === "none" && displayElement2.style.display === "none") {
        // Exibe ambos os elementos de visualização e oculta os de edição
        displayElement1.style.display = "block";
        editElement1.style.display = "none";
        displayElement2.style.display = "block";
        editElement2.style.display = "none";
    } else {
        // Oculta os elementos de visualização e exibe os de edição
        displayElement1.style.display = "none";
        editElement1.style.display = "block";
        displayElement2.style.display = "none";
        editElement2.style.display = "block";
    }
}

function submitCombinedForm() {
    // Seleciona os dois formulários
    var form1 = document.getElementById("editForm");
    var form2 = document.getElementById("editForm-p");

    // Itera sobre os campos do segundo formulário e os adiciona ao primeiro formulário
    var form2Elements = form2.elements;
    for (var i = 0; i < form2Elements.length; i++) {
        var input = form2Elements[i].cloneNode(true); // Clona o campo
        form1.appendChild(input); // Adiciona o campo ao primeiro formulário
    }

    // Submete o formulário combinado (form1)
    form1.submit();
}


// Função para confirmar e deletar conta
// Função para abrir o modal
function abrirModal() {
    document.getElementById("confirmModal").style.display = "block";
}

// Função para fechar o modal
function fecharModal() {
    document.getElementById("confirmModal").style.display = "none";
}

function confirmarDelecao() {
    // Fecha o modal
    fecharModal();

    // Chamada à API para deletar a conta
    fetch(`http://127.0.0.1:7777/perfil/delete`, {
        method: 'GET',
    })
    .then(response => {
        if (response.ok) {
            // Redirecionar ou atualizar a página após a exclusão
            window.location.href = "perfil/logout";
        } else {
            alert("Erro ao deletar a conta.");
        }
    })
    .catch(error => {
        alert("Ocorreu um erro ao tentar deletar a conta.");
        console.error(error);
    });
}

//menu
const selectSelected = document.querySelector('.select-selected');
const selectItems = document.querySelector('.select-items');
const hiddenInput = document.getElementById('modalidade');

// Abre ou fecha a lista de opções
selectSelected.addEventListener('click', function() {
    selectItems.style.display = selectItems.style.display === 'block' ? 'none' : 'block';
});

// Atualiza a seleção
selectItems.addEventListener('click', function(event) {
    if (event.target.matches('div')) {
        selectSelected.textContent = event.target.textContent; // Atualiza o texto do botão
        hiddenInput.value = event.target.getAttribute('data-value'); // Atualiza o valor do input oculto
        selectItems.style.display = 'none'; // Fecha a lista de opções

        // Restaura a cor do texto após uma seleção
        selectSelected.style.color = '#ffffff'; // Cor do texto normal
    }
});

// Fecha a lista de opções se clicar fora
document.addEventListener('click', function(event) {
    if (!selectSelected.contains(event.target)) {
        selectItems.style.display = 'none';
    }
});