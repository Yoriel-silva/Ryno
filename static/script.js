function toggleInformacoes() {
    const checkbox = document.getElementById("tipo");
    const informacoesAdicionais = document.getElementById("informacoesAdicionais");

    if (checkbox.checked) {
        informacoesAdicionais.style.display = "block";  // Mostrar campos adicionais
    } else {
        informacoesAdicionais.style.display = "none";   // Esconder campos adicionais
    }
}

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
