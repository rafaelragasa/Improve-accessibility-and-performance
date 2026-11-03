document.addEventListener('DOMContentLoaded', () => {
  const button = document.getElementById('review-button');

  if (!button) {
    return;
  }

  button.addEventListener('click', () => {
    const originalText = button.textContent;
    button.textContent = 'Review started';
    button.disabled = true;

    window.setTimeout(() => {
      button.textContent = originalText;
      button.disabled = false;
    }, 1200);
  });
});
