function computeHybridMeasurements() {
  const idA = document.getElementById("measure-point-a").value;
  const idB = document.getElementById("measure-point-b").value;
  const A = points.find(p => p.id === idA);
  const B = points.find(p => p.id === idB);
  if (!A || !B) {
    document.getElementById("measurement-output").innerHTML = "<em>Select two valid points.</em>";
    return;
  }

  const rA = Math.abs(A.w);
  const rB = Math.abs(B.w);
  const dr = rB - rA;
  const relA = relational3D(A);
  const relB = relational3D(B);
  const dx = relB[0] - relA[0];
  const dy = relB[1] - relA[1];
  const dz = relB[2] - relA[2];
  const relationalDist = Math.sqrt(dx*dx + dy*dy + dz*dz);
  const hybridDist = Math.sqrt(dr*dr + relationalDist*relationalDist);

  document.getElementById("measurement-output").innerHTML = `
    <strong>ΔRadial:</strong> ${dr.toFixed(3)}<br>
    <strong>Relational 3D Distance:</strong> ${relationalDist.toFixed(3)}<br>
    <strong>Hybrid 4D Distance:</strong> ${hybridDist.toFixed(3)}<br>
  `;
}

function computeMultiMeasurements() {
  const sel = document.getElementById("multi-measure-select");
  const chosen = [...sel.options].filter(o => o.selected).map(o => o.value);
  if (chosen.length < 2) {
    document.getElementById("multi-measure-output").innerHTML = "<em>Select at least two points.</em>";
    return;
  }
  let html = "<strong>Chain Measurements:</strong><br><br>";
  for (let i = 0; i < chosen.length - 1; i++) {
    const A = points.find(p => p.id === chosen[i]);
    const B = points.find(p => p.id === chosen[i+1]);
    if (!A || !B) continue;
    const rA = Math.abs(A.w);
    const rB = Math.abs(B.w);
    const dr = rB - rA;
    const relA = relational3D(A);
    const relB = relational3D(B);
    const dx = relB[0] - relA[0];
    const dy = relB[1] - relA[1];
    const dz = relB[2] - relA[2];
    const relationalDist = Math.sqrt(dx*dx + dy*dy + dz*dz);
    const hybridDist = Math.sqrt(dr*dr + relationalDist*relationalDist);
    html += `
      <strong>${A.label} → ${B.label}</strong><br>
      ΔRadial: ${dr.toFixed(3)}<br>
      Relational Distance: ${relationalDist.toFixed(3)}<br>
      Hybrid Distance: ${hybridDist.toFixed(3)}<br><br>
    `;
  }
  document.getElementById("multi-measure-output").innerHTML = html;
}

document.getElementById("compute-measure-btn").addEventListener("click", computeHybridMeasurements);
document.getElementById("compute-multi-btn").addEventListener("click", computeMultiMeasurements);
