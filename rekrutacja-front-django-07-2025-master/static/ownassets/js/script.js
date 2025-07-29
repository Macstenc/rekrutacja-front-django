console.log('✅ JS załadowany');

document.addEventListener('DOMContentLoaded', function() {
    console.log('✅ DOM wczytany');

    const handle = document.getElementById('accessibility-handle');
    const panel = document.getElementById('accessibility-panel');

    if (!handle || !panel) {
        console.error('❌ Panel lub handle nie znaleziony!');
        return;
    }
    handle.addEventListener('click', () => {
        panel.classList.toggle('open');
        console.log('➡ Panel otwarty?', panel.classList.contains('open'));
        panel.setAttribute('aria-hidden', !panel.classList.contains('open'));
    });

    const root = document.documentElement;
    const defaultFontSize = window.getComputedStyle(root).fontSize; 

    let currentFontSize = parseInt(localStorage.getItem('fontSize')) || 100;
    root.style.fontSize = currentFontSize + '%';

    function changeFontSize(delta) {
        currentFontSize = Math.min(200, Math.max(80, currentFontSize + delta));
        root.style.fontSize = currentFontSize + '%';
        localStorage.setItem('fontSize', currentFontSize);
    }

    document.getElementById('text-increase').addEventListener('click', () => changeFontSize(10));
    document.getElementById('text-decrease').addEventListener('click', () => changeFontSize(-10));

    document.getElementById('contrast-toggle').addEventListener('click', () => {
        document.body.classList.toggle('high-contrast');
        localStorage.setItem('contrast', document.body.classList.contains('high-contrast'));
    });

    document.getElementById('disable-animations').addEventListener('click', () => {
        document.body.classList.toggle('no-animations');
        localStorage.setItem('animations', document.body.classList.contains('no-animations'));
    });

 document.getElementById('reset-settings').addEventListener('click', () => {
    currentFontSize = 100;
    root.style.fontSize = defaultFontSize;
    document.body.classList.remove('high-contrast', 'no-animations');
    localStorage.clear();
    setTimeout(() => location.reload(), 300);  
});


    if (localStorage.getItem('contrast') === 'true') {
        document.body.classList.add('high-contrast');
    }
    if (localStorage.getItem('animations') === 'true') {
        document.body.classList.add('no-animations');
    }
});
