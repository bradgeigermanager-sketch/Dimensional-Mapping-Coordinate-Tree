function renderTree(points) {
  const canvas = document.getElementById("hybrid-viewport");
  const ctx = canvas.getContext("2d");
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  for (const p of points) {
    const height = Math.abs(p.w);
    const [xr, yr, zr] = relational3D(p);
    const X = xr * 40;
    const Y = -height * 40;
    const Z = zr * 40;
    const scale = 200 / (Z + 300);
    const x2d = 400 + X * scale;
    const y2d = 550 + Y * scale;

    // trunk
    ctx.beginPath();
    ctx.moveTo(400, 550);
    ctx.lineTo(400, y2d);
    ctx.strokeStyle = "#6c7086";
    ctx.stroke();

    // branch
    ctx.beginPath();
    ctx.moveTo(400, y2d);
    ctx.lineTo(x2d, y2d);
    ctx.strokeStyle = "#89b4fa";
    ctx.stroke();

    // leaf / node
    ctx.beginPath();
    ctx.arc(x2d, y2d, 6, 0, Math.PI * 2);
    ctx.fillStyle = "#a6e3a1";
    ctx.fill();
  }
}

document.getElementById("tree-visualization-toggle")
  .addEventListener("change", e => {
    if (e.target.checked) renderTree(points);
    else renderHybrid(points);
  });
