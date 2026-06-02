function getRotation() {
  return {
    yaw: parseFloat(document.getElementById("rot-yaw").value),
    pitch: parseFloat(document.getElementById("rot-pitch").value),
    roll: parseFloat(document.getElementById("rot-roll").value)
  };
}
