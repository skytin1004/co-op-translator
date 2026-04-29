window.tailwind = window.tailwind || {};
window.tailwind.config = {
  prefix: "tw-",
  darkMode: ["selector", '[data-md-color-scheme="slate"]'],
  corePlugins: {
    preflight: false,
  },
  theme: {
    extend: {
      colors: {
        coop: {
          ink: "#172033",
          blue: "#2563eb",
          cyan: "#0891b2",
          mint: "#10b981",
          soft: "#f4f8fb",
        },
      },
      boxShadow: {
        coop: "0 24px 70px rgba(15, 23, 42, 0.12)",
      },
      fontFamily: {
        display: ["Inter", "ui-sans-serif", "system-ui", "sans-serif"],
      },
    },
  },
};
