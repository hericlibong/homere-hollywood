const DATA_URL = "./data/viz_timeline_degre_fidelite.json";

const state = {
  scenes: [],
  activeScene: null,
  degreeFilters: new Set([1, 2, 3, 4]),
  sourceFilters: new Set(),
  character: "",
};

const degreeLabels = new Map([
  [1, "Reprise fidèle"],
  [2, "Déplacement"],
  [3, "Invention sur fond emprunté"],
  [4, "Invention contradictoire"],
]);

const sourceLabels = [
  "L'Iliade",
  "Le Cycle Troyen",
  "Héritage Gréco-Romain",
  "Adaptation Cinéma",
];

const fallbackColors = new Map([
  [1, "#D6A84F"],
  [2, "#C7743A"],
  [3, "#6E7F80"],
  [4, "#B33A3A"],
]);

const els = {
  timeline: d3.select("#timeline"),
  timelineWrap: document.querySelector("#timelineWrap"),
  tooltip: document.querySelector("#tooltip"),
  degreeFilters: document.querySelector("#degreeFilters"),
  sourceFilters: document.querySelector("#sourceFilters"),
  characterFilter: document.querySelector("#characterFilter"),
  resetFilters: document.querySelector("#resetFilters"),
  legend: document.querySelector("#legend"),
  sceneCount: document.querySelector("#sceneCount"),
  visibleCount: document.querySelector("#visibleCount"),
  activeLabel: document.querySelector("#activeLabel"),
  prevScene: document.querySelector("#prevScene"),
  nextScene: document.querySelector("#nextScene"),
  mediaPanel: document.querySelector("#mediaPanel"),
  mediaScene: document.querySelector("#mediaScene"),
  mediaTitle: document.querySelector("#mediaTitle"),
  detailNumber: document.querySelector("#detailNumber"),
  detailTitle: document.querySelector("#detailTitle"),
  detailTags: document.querySelector("#detailTags"),
  detailCharacters: document.querySelector("#detailCharacters"),
  detailReference: document.querySelector("#detailReference"),
  detailAction: document.querySelector("#detailAction"),
  detailExplanation: document.querySelector("#detailExplanation"),
};

async function init() {
  const payload = await fetch(DATA_URL).then((response) => {
    if (!response.ok) {
      throw new Error(`Impossible de charger ${DATA_URL}`);
    }
    return response.json();
  });

  const normalizedPayload = Array.isArray(payload)
    ? { scenes: payload, color_scale: null }
    : payload;

  state.scenes = normalizedPayload.scenes || [];
  state.sourceFilters = new Set(sourceLabels);
  state.activeScene = state.scenes[0];

  buildControls();
  renderLegend(normalizedPayload.color_scale);
  renderTimeline();
  renderDetail(state.activeScene);
  bindEvents();
}

function getColor(scene) {
  return scene.color || fallbackColors.get(Number(scene.degre_fidelite)) || "#999";
}

function filteredScenes() {
  return state.scenes.filter((scene) => {
    const degreeOk = state.degreeFilters.has(Number(scene.degre_fidelite));
    const sourceOk = state.sourceFilters.has(scene.source_principale);
    const characterOk = !state.character || scene.characters.includes(state.character);
    return degreeOk && sourceOk && characterOk;
  });
}

function buildControls() {
  els.sceneCount.textContent = `${state.scenes.length} scènes`;

  for (const [degree, label] of degreeLabels) {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "filter-button";
    button.dataset.degree = String(degree);
    button.style.borderLeftColor = fallbackColors.get(degree);
    button.setAttribute("aria-pressed", "true");
    button.textContent = label;
    els.degreeFilters.appendChild(button);
  }

  for (const source of sourceLabels) {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "filter-button";
    button.dataset.source = source;
    button.style.borderLeftColor = "#1f5f66";
    button.setAttribute("aria-pressed", "true");
    button.textContent = source;
    els.sourceFilters.appendChild(button);
  }

  const characters = Array.from(
    new Set(state.scenes.flatMap((scene) => scene.characters).filter(Boolean))
  ).sort((a, b) => a.localeCompare(b, "fr"));

  for (const character of characters) {
    const option = document.createElement("option");
    option.value = character;
    option.textContent = character;
    els.characterFilter.appendChild(option);
  }
}

function renderLegend(colorScale) {
  els.legend.innerHTML = "";
  for (const [degree, label] of degreeLabels) {
    const key = `degre_${degree}`;
    const color = colorScale?.[key]?.color || fallbackColors.get(degree);
    const item = document.createElement("span");
    item.className = "legend-item";
    item.innerHTML = `<span class="legend-swatch" style="background:${color}"></span>${label}`;
    els.legend.appendChild(item);
  }
}

function renderTimeline() {
  const width = Math.max(980, els.timelineWrap.clientWidth);
  const height = 112;
  const margin = { top: 18, right: 16, bottom: 28, left: 16 };
  const innerWidth = width - margin.left - margin.right;
  const innerHeight = height - margin.top - margin.bottom;
  const visible = filteredScenes();
  const visibleIds = new Set(visible.map((scene) => scene.scene_number));

  els.visibleCount.textContent = `${visible.length} visibles`;
  els.timeline.attr("viewBox", `0 0 ${width} ${height}`).attr("width", "100%");

  const x = d3
    .scaleBand()
    .domain(state.scenes.map((scene) => scene.scene_number))
    .range([margin.left, margin.left + innerWidth])
    .paddingInner(0.08);

  const rectHeight = innerHeight;
  const rectY = margin.top;

  const rects = els.timeline
    .selectAll("rect.scene-rect")
    .data(state.scenes, (scene) => scene.scene_number);

  rects
    .join("rect")
    .attr("class", (scene) => {
      const classes = ["scene-rect"];
      if (!visibleIds.has(scene.scene_number)) classes.push("is-muted");
      if (state.activeScene?.scene_number === scene.scene_number) classes.push("is-active");
      return classes.join(" ");
    })
    .attr("x", (scene) => x(scene.scene_number))
    .attr("y", rectY)
    .attr("width", Math.max(2, x.bandwidth()))
    .attr("height", rectHeight)
    .attr("fill", getColor)
    .attr("tabindex", 0)
    .attr("role", "button")
    .attr("aria-label", (scene) => `Scène ${scene.scene_number}, ${scene.libelle_degre}`)
    .on("mouseenter focus", (event, scene) => showTooltip(event, scene))
    .on("mousemove", moveTooltip)
    .on("mouseleave blur", hideTooltip)
    .on("click", (event, scene) => selectScene(scene))
    .on("keydown", (event, scene) => {
      if (event.key === "Enter" || event.key === " ") {
        event.preventDefault();
        selectScene(scene);
      }
    });

  const axisScale = d3
    .scaleLinear()
    .domain([0, state.scenes.length - 1])
    .range([margin.left, margin.left + innerWidth]);

  const axis = d3
    .axisBottom(axisScale)
    .ticks(6)
    .tickFormat((index) => {
      const scene = state.scenes[Math.round(index)];
      return scene ? `Sc. ${scene.scene_number}` : "";
    });

  els.timeline
    .selectAll("g.timeline-axis")
    .data([null])
    .join("g")
    .attr("class", "timeline-axis")
    .attr("transform", `translate(0, ${height - margin.bottom + 12})`)
    .call(axis)
    .call((g) => g.select(".domain").remove())
    .call((g) => g.selectAll("line").attr("stroke", "#bfb4a5"))
    .call((g) => g.selectAll("text").attr("fill", "#706960").attr("font-weight", 700));
}

function showTooltip(event, scene) {
  els.activeLabel.textContent = `Scène ${scene.scene_number} · ${scene.scene_heading || "Sans intitulé"}`;
  els.tooltip.hidden = false;
  els.tooltip.innerHTML = `
    <strong>Scène ${scene.scene_number}</strong>
    <span>${scene.scene_heading || "Sans intitulé"}</span>
    <span>${scene.libelle_degre}</span>
    <span>${scene.source_principale}</span>
  `;
  moveTooltip(event);
}

function moveTooltip(event) {
  const padding = 16;
  const rect = els.tooltip.getBoundingClientRect();
  const x = Math.min(window.innerWidth - rect.width - padding, event.clientX + 14);
  const y = Math.min(window.innerHeight - rect.height - padding, event.clientY + 14);
  els.tooltip.style.left = `${Math.max(padding, x)}px`;
  els.tooltip.style.top = `${Math.max(padding, y)}px`;
}

function hideTooltip() {
  els.tooltip.hidden = true;
  if (state.activeScene) {
    els.activeLabel.textContent = `Scène ${state.activeScene.scene_number} · ${
      state.activeScene.scene_heading || "Sans intitulé"
    }`;
  }
}

function selectScene(scene) {
  state.activeScene = scene;
  renderDetail(scene);
  renderTimeline();
}

function renderDetail(scene) {
  els.activeLabel.textContent = `Scène ${scene.scene_number} · ${scene.scene_heading || "Sans intitulé"}`;
  renderMedia(scene);
  els.detailNumber.textContent = `Scène ${scene.scene_number}`;
  els.detailTitle.textContent = scene.scene_heading || "Sans intitulé";
  els.detailCharacters.textContent = scene.characters.length ? scene.characters.join(", ") : "-";
  els.detailReference.textContent = scene.reference_iliade || "-";
  els.detailAction.textContent = scene.action_film || "-";
  els.detailExplanation.textContent = scene.explication_litteraire || "-";

  els.detailTags.innerHTML = "";
  const degreeTag = document.createElement("span");
  degreeTag.className = "tag degree";
  degreeTag.style.borderLeftColor = getColor(scene);
  degreeTag.textContent = scene.libelle_degre;
  els.detailTags.appendChild(degreeTag);

  const sourceTag = document.createElement("span");
  sourceTag.className = "tag";
  sourceTag.textContent = scene.source_principale;
  els.detailTags.appendChild(sourceTag);
}

function renderMedia(scene) {
  els.mediaPanel.innerHTML = "";
  if (scene.image_src) {
    const image = document.createElement("img");
    image.className = "scene-image";
    image.src = scene.image_src;
    image.alt = scene.image_alt || `Scène ${scene.scene_number} de Troy`;
    els.mediaPanel.appendChild(image);
    return;
  }

  const placeholder = document.createElement("div");
  placeholder.className = "media-placeholder";
  placeholder.innerHTML = `
    <span>Scène ${scene.scene_number}</span>
    <strong>${scene.scene_heading || "Image à ajouter"}</strong>
  `;
  els.mediaPanel.appendChild(placeholder);
}

function bindEvents() {
  els.degreeFilters.addEventListener("click", (event) => {
    const button = event.target.closest("[data-degree]");
    if (!button) return;
    const degree = Number(button.dataset.degree);
    toggleSetValue(state.degreeFilters, degree, [1, 2, 3, 4]);
    button.setAttribute("aria-pressed", String(state.degreeFilters.has(degree)));
    renderTimeline();
  });

  els.sourceFilters.addEventListener("click", (event) => {
    const button = event.target.closest("[data-source]");
    if (!button) return;
    const source = button.dataset.source;
    toggleSetValue(state.sourceFilters, source, sourceLabels);
    button.setAttribute("aria-pressed", String(state.sourceFilters.has(source)));
    renderTimeline();
  });

  els.characterFilter.addEventListener("change", () => {
    state.character = els.characterFilter.value;
    renderTimeline();
  });

  els.resetFilters.addEventListener("click", () => {
    state.degreeFilters = new Set([1, 2, 3, 4]);
    state.sourceFilters = new Set(sourceLabels);
    state.character = "";
    els.characterFilter.value = "";
    document.querySelectorAll(".filter-button").forEach((button) => {
      button.setAttribute("aria-pressed", "true");
    });
    renderTimeline();
  });

  els.prevScene.addEventListener("click", () => stepScene(-1));
  els.nextScene.addEventListener("click", () => stepScene(1));
  window.addEventListener("resize", debounce(renderTimeline, 120));
}

function toggleSetValue(set, value, allValues) {
  if (set.has(value) && set.size > 1) {
    set.delete(value);
  } else if (!set.has(value)) {
    set.add(value);
  } else if (set.size === 1) {
    for (const item of allValues) set.add(item);
  }
}

function stepScene(direction) {
  const visible = filteredScenes();
  if (!visible.length) return;
  const currentIndex = visible.findIndex(
    (scene) => scene.scene_number === state.activeScene?.scene_number
  );
  const baseIndex = currentIndex === -1 ? 0 : currentIndex;
  const nextIndex = (baseIndex + direction + visible.length) % visible.length;
  selectScene(visible[nextIndex]);
}

function debounce(fn, delay) {
  let timer = null;
  return (...args) => {
    window.clearTimeout(timer);
    timer = window.setTimeout(() => fn(...args), delay);
  };
}

init().catch((error) => {
  console.error(error);
  els.activeLabel.textContent = "Erreur de chargement des données.";
});
