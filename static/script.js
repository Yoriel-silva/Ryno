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