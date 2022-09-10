// Reduce the blogs heading by adding ellipses to titles that are too long.
const elements = document.querySelectorAll('.card-title');
elements.forEach(el => {
  el.textContent=el.innerHTML.substring(0,23)+"...";
});