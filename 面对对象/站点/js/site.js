(() => {
  const frame = document.getElementById('contentFrame');
  const themeToggle = document.getElementById('themeToggle');
  // Navigation handling
  document.querySelectorAll('.site-nav a[data-target]').forEach(a => {
    a.addEventListener('click', (e) => {
      e.preventDefault();
      const target = a.getAttribute('data-target');
      frame.src = `../文档/${target}.html`;
    });
  });
  // Theme handling
  const applyTheme = (theme) => {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
  };
  const stored = localStorage.getItem('theme');
  if (stored === 'dark' || (stored === null && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    applyTheme('dark');
  } else {
    applyTheme('light');
  }
  themeToggle.addEventListener('click', () => {
    const current = document.documentElement.getAttribute('data-theme');
    const next = current === 'dark' ? 'light' : 'dark';
    applyTheme(next);
  });
})();
