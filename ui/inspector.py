export function showPointInfo(point) {
  document.getElementById("info").innerText =
    JSON.stringify(point, null, 2);
}
