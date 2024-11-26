document.querySelectorAll('.scroll-container').forEach(container => {

    const scrollAmount = 200; // A quantidade de rolagem

    container.querySelectorAll('.scroll-button').forEach(button => {
        button.addEventListener('click', () => {
            const maxScrollLeft = container.scrollWidth - container.clientWidth;

            if (button.classList.contains('right')) {
                if (container.scrollLeft + scrollAmount >= maxScrollLeft) {
                    // Para um efeito mais fluido, rola suavemente ao início
                    container.scrollTo({ left: 0, behavior: 'smooth' });
                } else {
                    container.scrollBy({ left: scrollAmount, behavior: 'smooth' });
                }
            } else {
                if (container.scrollLeft - scrollAmount <= 0) {
                    // Para um efeito mais fluido, rola suavemente ao final
                    container.scrollTo({ left: maxScrollLeft, behavior: 'smooth' });
                } else {
                    container.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
                }
            }
        });
    });
});
