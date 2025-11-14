document.addEventListener('DOMContentLoaded', () => {
    if (!document.startViewTransition) {
        return;
    }

    const authLinks = document.querySelectorAll('a[href*="auth"]');
    
    authLinks.forEach(link => {
        link.addEventListener('click', async (e) => {
            e.preventDefault();
            const targetUrl = link.href;
            const isGoingToRegister = targetUrl.includes('register');
            
            sessionStorage.setItem('authTransition', isGoingToRegister ? 'toRegister' : 'toLogin');
            
            const transition = document.startViewTransition(async () => {
                await new Promise(resolve => {
                    window.addEventListener('beforeunload', resolve, { once: true });
                    window.location.href = targetUrl;
                });
            });
            
            try {
                await transition.finished;
            } catch (e) {
                console.log('Transition interrupted');
            }
        });
    });
    
    const transitionType = sessionStorage.getItem('authTransition');
    if (transitionType) {
        sessionStorage.removeItem('authTransition');
        
        const authSplit = document.querySelector('.auth-split');
        if (transitionType === 'toRegister') {
            authSplit.classList.add('reversed');
        }
    }
});
