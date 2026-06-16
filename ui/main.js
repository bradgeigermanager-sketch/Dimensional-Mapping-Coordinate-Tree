import { renderPoints } from './renderer.js';

export function loadData() {
  fetch('../data/sample.json')
    .then(res => res.json())
    .then(data => renderPoints(data));
}
function run() {
  const mode = document.getElementById("mode").value;

  fetch('../data/sample.json')
    .then(res => res.json())
    .then(data => {
      console.log("Mode:", mode);
      renderPoints(data, mode);
    });
}
