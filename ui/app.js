// Global point list
let points = [];

// Load sample data
fetch("../data/sample_points.json")
  .then(r => r.json())
  .then(data => {
    points = data;
    populateSelectors();
    renderHybrid(points);
  });

function populateSelectors() {
  const selA = document.getElementById("measure-point-a");
  const selB = document.getElementById("measure-point-b");
  const multi = document.getElementById("multi-measure-select");
  points.forEach(p => {
    const optA = new Option(p.label, p.id);
    const optB = new Option(p.label, p.id);
    const optM = new Option(p.label, p.id);
    selA.add(optA);
    selB.add(optB);
    multi.add(optM);
  });
}
