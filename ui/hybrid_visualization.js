// Note: this file assumes helper functions relational3D and rotationMatrix are available
function projectHybridPoint(point) {
  const [xr, yr, zr] = relational3D(point);
  const r = Math.abs(point.w);
  const { yaw, pitch, roll } = getRotation();
  const R = rotationMatrix(yaw * Math.PI/180, pitch * Math.PI/180, roll * Math.PI/180);

  // Apply rotation matrix R to [xr, yr, zr]
  const X = R[0][0] * xr + R[0][1] * yr + R[0][2] * zr;
  const Y = R[1][0] * xr + R[1][1] * yr + R[1][2] * zr;
  const Z = R[2][0] * xr + R[2][1] * yr + R[2][2] * zr;

  const zoom = getZoom();
  const scale = zoom * (200 / (Z + 6));
  return {
    x2d: 400 + X * scale,
    y2d: 300 + Y * scale,
    radius: Math.max(2, Math.pow(r, 0.5) * zoom)
  };
}

function renderHybrid(points) {
  const canvas = document.getElementById("hybrid-viewport");
  const ctx = canvas.getContext("2d");
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  for (const p of points) {
    const { x2d, y2d, radius } = projectHybridPoint(p);
    ctx.beginPath();
    ctx.arc(x2d, y2d, radius, 0, Math.PI * 2);
    ctx.fillStyle = "rgba(163,113,247,0.8)";
    ctx.fill();
  }
}
