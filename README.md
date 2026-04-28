# C*Power v0.1

> **⚠️ WORK IN PROGRESS — Calculations have not been independently validated. Do not use for published research without cross-checking against G*Power or another validated tool.**

A browser-based, mobile-friendly statistical power analysis tool — a clone of [G*Power](https://www.psychologie.hhu.de/arbeitsgruppen/allgemeine-psychologie-und-arbeitspsychologie/gpower) that requires no installation and works on smartphones, tablets, and desktops.

Generated using [Claude](https://claude.ai) (Anthropic) as a demonstration of LLM-assisted scientific tool development.

---

## 🚀 Quick Start

Just open `cpower.html` in any modern browser. No installation, no dependencies, no server needed.

```bash
git clone https://github.com/YOUR_USERNAME/cpower
open cpower.html          # macOS
start cpower.html         # Windows
xdg-open cpower.html      # Linux
```

Or [**use it online →**](https://YOUR_USERNAME.github.io/cpower) *(if hosted via GitHub Pages)*

---

## ✨ Features

### Statistical Tests
| Family | Tests |
|--------|-------|
| **F tests** | One-way ANOVA, ANCOVA, Repeated Measures (within/between), MANOVA, Multiple Regression (R², R² increase) |
| **t tests** | Independent samples, One sample, Paired samples, Correlation (point biserial), Generic |
| **χ² tests** | Goodness-of-fit / contingency tables, Variance |
| **z tests** | Two proportions, Sign test, Two correlations (Pearson r), Generic |
| **Exact tests** | Binomial, Multinomial goodness-of-fit |

### Analysis Types
- **A priori** — Compute required sample size given α, power, and effect size
- **Post hoc** — Compute achieved power given sample size and effect size
- **Criterion** — Compute required α given power, N, and effect size
- **Sensitivity** — Compute minimum detectable effect size given α, power, and N

### Other Features
- 📊 **Distribution plot** — H₀ and H₁ distributions with α, β, and power regions shaded
- 📄 **Report generator** — Copy-paste text for Methods sections and preregistrations
- 📋 **Protocol tab** — Automatic log of all analyses, exportable as CSV
- 📈 **X-Y plot** — Power curves across ranges of effect size, N, or α
- 🎨 **5 themes** — G\*Power Classic, Flat & Teal (2010s), Polished Minimal, Terminal/Hacker, Aged Paper/Sepia
- 📱 **Mobile-first** — Fully responsive layout for phones and tablets
- 💾 **PWA-ready** — Installable as a home-screen app (Add to Home Screen)

---

## 📱 Mobile Use

C*Power is designed to work well on mobile:

- Responsive layout collapses the effect size drawer on small screens
- Touch-friendly controls with appropriate tap targets
- Installable as a Progressive Web App:
  - **iOS Safari**: Share → Add to Home Screen
  - **Android Chrome**: Menu → Add to Home Screen / Install App

---

## ⚠️ Important Disclaimers

### This tool has NOT been validated

The statistical calculations in C*Power were implemented by a large language model (Claude, Anthropic) based on standard textbook formulations and approximations. **They have not been independently validated against G*Power, R, or any other reference implementation.**

Known limitations:
- Some noncentral distribution calculations use approximations rather than exact methods
- Edge cases (very small N, extreme effect sizes, complex ANOVA designs) may produce incorrect results
- Sensitivity and criterion analyses use iterative search with fixed step sizes, which may miss precise solutions

**Always verify results using G*Power before including them in a manuscript or preregistration.**

### Please cite G*Power

If you use power analysis results (after verification), please cite the original G*Power software:

> Faul, F., Erdfelder, E., Lang, A.-G., & Buchner, A. (2007). G\*Power 3: A flexible statistical power analysis program for the social, behavioral, and biomedical sciences. *Behavior Research Methods, 39*(2), 175–191. https://doi.org/10.3758/BF03193146

> Faul, F., Erdfelder, E., Buchner, A., & Lang, A.-G. (2009). Statistical power analyses using G\*Power 3.1: Tests for correlation and regression analyses. *Behavior Research Methods, 41*(4), 1149–1160. https://doi.org/10.3758/BRM.41.4.1149

The G*Power team at Heinrich Heine University Düsseldorf deserves full credit for the original software. C\*Power is not affiliated with them in any way.

---

## 🎨 Themes

| Theme | Description |
|-------|-------------|
| **G\*Power Classic** | Faithful recreation of G\*Power's Windows XP-era appearance |
| **Flat & Teal (2010s)** | Dark teal/navy flat design inspired by the 2010s Material era |
| **Polished Minimal** | Clean white with subtle shadows and purple gradient accents |
| **Terminal / Hacker** | Full black background with green phosphor text |
| **Aged Paper / Sepia** | Warm sepia tones reminiscent of aged academic documents |

---

## 🛠️ Development

C*Power is a single self-contained HTML file with no external dependencies (other than a Google Fonts import for non-default themes). All statistical calculations are implemented in vanilla JavaScript.

### Contributing

Contributions are very welcome, especially:

- **Validation** — Cross-checking outputs against G*Power, R (`pwr` package), or Python (`statsmodels`) for specific tests
- **Bug fixes** — Especially in noncentral distribution calculations
- **New tests** — Additional statistical tests not yet implemented
- **Mobile UX** — Improvements to the mobile layout

### File structure

```
cpower.html     # Everything — HTML, CSS, and JavaScript in one file
README.md       # This file
```

### Running locally

No build step required. Just open `cpower.html` in a browser.

For development with live reload:
```bash
npx live-server --open=cpower.html
```

---

## 📐 Statistical Methods

C*Power uses the following approximation approaches:

| Distribution | Method |
|-------------|--------|
| Normal | Abramowitz & Stegun rational approximation for CDF; Beasley-Springer-Moro for inverse |
| t | Regularized incomplete beta function via Lentz continued fraction |
| F | Regularized incomplete beta function |
| χ² | Regularized incomplete gamma function (series + continued fraction) |
| Noncentral F | Poisson-weighted mixture of central F distributions (up to j=60 terms) |
| Noncentral t | Normal approximation to the noncentral t distribution |
| Noncentral χ² | Poisson-weighted mixture of central χ² distributions |

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

This project is not affiliated with the G*Power team at Heinrich Heine University Düsseldorf.

---

## 🙏 Acknowledgements

- **Franz Faul, Edgar Erdfelder, Albert-Georg Lang, Axel Buchner** — creators of G*Power
- **Anthropic / Claude** — LLM used to generate this tool
- Cohen, J. (1988). *Statistical Power Analysis for the Behavioral Sciences* (2nd ed.) — foundational reference for effect size conventions
