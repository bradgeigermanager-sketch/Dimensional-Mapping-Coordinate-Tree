import { renderPoints } from './renderer.js';

export function loadData() {
  fetch('../data/sample.json')
    .then(res => res.json())
    .then(data => renderPoints(data));
}
