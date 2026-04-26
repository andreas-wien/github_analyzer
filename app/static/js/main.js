async function loadLanguages(force = false) {
  const status = document.getElementById("status");
  const value = document.getElementById("value");

  value.innerHTML = "";

  const cached = localStorage.getItem("languages");
  const cachedTime = localStorage.getItem("languages_time");

  const ONE_HOUR = 1000 * 60 * 60;

  const cacheValid = cached && cachedTime && Date.now() - cachedTime < ONE_HOUR;

  if (cacheValid && !force) {
    status.innerText = "Loaded from cache";
    renderLanguages(JSON.parse(cached));
    return;
  }

  status.innerText = cached ? "Refreshing..." : "Loading...";

  try {
    const response = await fetch("/languages/load");

    if (!response.ok) {
      throw new Error("HTTP error " + response.status);
    }

    const data = await response.json();

    localStorage.setItem("languages", JSON.stringify(data));
    localStorage.setItem("languages_time", Date.now());

    status.innerText = cached ? "Cache refreshed" : "Languages loaded";

    renderLanguages(data);
  } catch (err) {
    status.innerText = "Error occurred";
    console.error(err);
  }
}

function renderLanguages(data) {
  const value = document.getElementById("value");
  const empty = document.getElementById("empty-state");

  // hide empty state when data arrives
  if (empty) {
    empty.style.display = "none";
  }

  const sorted = Object.entries(data).sort((a, b) => b[1] - a[1]);

  if (sorted.length === 0) {
    value.innerHTML = "<p>No data available</p>";
    return;
  }

  const max = sorted[0][1];

  value.innerHTML = sorted
    .map(([lang, count]) => {
      const percent = Math.round((count / max) * 100);

      return `
      <div class="col-md-6">
        <div class="card shadow-sm mb-2">
          <div class="card-body">

            <div class="d-flex justify-content-between">
              <strong>${lang}</strong>
              <span>${count.toLocaleString()}</span>
            </div>

            <div class="progress mt-2">
              <div class="progress-bar" style="width:${percent}%"></div>
            </div>

          </div>
        </div>
      </div>
    `;
    })
    .join("");
}

document.addEventListener("DOMContentLoaded", () => {
  loadLanguages();
});
