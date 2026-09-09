// Vibe Hosting — small progressive-enhancement script
// Builds the hero "vibe meter" equalizer bars and staggers their pulse.

document.addEventListener("DOMContentLoaded", () => {
  const container = document.getElementById("vibeBars");
  if (!container) return;

  const BAR_COUNT = 24;

  for (let i = 0; i < BAR_COUNT; i++) {
    const bar = document.createElement("span");

    // Randomised min/max scale + duration so the bars feel alive,
    // not like a single looping GIF.
    const min = (0.15 + Math.random() * 0.25).toFixed(2);
    const max = (0.6 + Math.random() * 0.4).toFixed(2);
    const duration = (0.9 + Math.random() * 0.9).toFixed(2);
    const delay = (Math.random() * 1.2).toFixed(2);

    bar.style.setProperty("--min", min);
    bar.style.setProperty("--max", max);
    bar.style.animationDuration = `${duration}s`;
    bar.style.animationDelay = `${delay}s`;

    container.appendChild(bar);
  }
});
