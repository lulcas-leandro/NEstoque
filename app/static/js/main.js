document.addEventListener('DOMContentLoaded', () => {
    const userToggle = document.getElementById('userMenuToggle');
    const userDropdown = document.getElementById('userDropdown');
    
    if (userToggle && userDropdown) {
        userToggle.addEventListener('click', (e) => {
            e.stopPropagation();
            userToggle.classList.toggle('active');
            userDropdown.classList.toggle('show');
        });
        
        document.addEventListener('click', (e) => {
            if (!userToggle.contains(e.target) && !userDropdown.contains(e.target)) {
                userToggle.classList.remove('active');
                userDropdown.classList.remove('show');
            }
        });
        
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                userToggle.classList.remove('active');
                userDropdown.classList.remove('show');
            }
        });
    }

    window.confirmDelete = (url) => {
        if (confirm('Tem certeza que deseja excluir este produto?')) {
            const form = document.createElement('form');
            form.method = 'POST';
            form.action = url;
            document.body.appendChild(form);
            form.submit();
        }
    };

    // busca com loading
    const searchButton = document.getElementById('searchButton');
    const searchInput = document.getElementById('searchInput');
    const searchIcon = document.querySelector('.search-button .icon');
    const searchSpinner = document.querySelector('.search-button .spinner');

    if (searchButton && searchInput && searchIcon && searchSpinner) {
        searchButton.addEventListener('click', (e) => {
            e.stopImmediatePropagation();
            e.preventDefault();

            searchInput.focus();
            searchIcon.classList.add('hidden');
            searchSpinner.classList.add('visible');

            // Simular busca - funcionalidade será implementada futuramente
            setTimeout(() => {
                searchIcon.classList.remove('hidden');
                searchSpinner.classList.remove('visible');
                searchInput.value = '';
                searchInput.blur();
            }, 2000);
        });

        searchInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                searchButton.click();
            }
        });
    }
});
