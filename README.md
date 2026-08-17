# C*Power v0.2

> **⚠️ WORK IN PROGRESS — Calculations have not been independently validated. Do not use for published research without cross-checking against G*Power or another validated tool.**

A browser-based, mobile-friendly statistical power analysis tool — a clone of [G*Power](https://www.psychologie.hhu.de/arbeitsgruppen/allgemeine-psychologie-und-arbeitspsychologie/gpower) that requires no installation and works on smartphones, tablets, and desktops.

Generated using [Claude](https://claude.ai) (Anthropic) as a demonstration of LLM-assisted scientific tool development.

---

## 🚀 Quick Start

**Live:** [lukasroeseler.github.io/c-power](https://lukasroeseler.github.io/c-power/)

Or run it locally — it's a single self-contained `index.html`, no installation, no dependencies, no server needed:

```bash
git clone https://github.com/lukasroeseler/c-power
cd c-power
open index.html          # macOS
start index.html         # Windows
xdg-open index.html      # Linux
```

---

## ✨ Features

### Statistical Tests
| Family | Tests |
|--------|-------|
| **F tests** | One-way ANOVA, ANCOVA, Repeated Measures (within/between), MANOVA, Multiple Regression (R², R² increase) |
| **t tests** | Independent samples, One sample, Paired samples, Correlation (point-biserial, exact), Generic |
| **χ² tests** | Goodness-of-fit / contingency tables, Variance |
| **z tests** | Two proportions, Sign test, Generic |
| **Exact tests** | Binomial, Multinomial goodness-of-fit |
| **Correlations** | One sample (H₀: ρ=ρ₀), Difference between two independent r's (Fisher, 1925), Difference between two dependent/overlapping r's (Steiger, 1980) |

### Analysis Types
- **A priori** — Compute required sample size given α, power, and effect size
- **Post hoc** — Compute achieved power given sample size and effect size
- **Criterion** — Compute required α given power, N, and effect size
- **Sensitivity** — Compute minimum detectable effect size given α, power, and N

### Other Features
- 📊 **Distribution plot** — H₀ and H₁ distributions with α, β, and power regions shaded; hover for explanations, export as PNG
- 📄 **Report generator** — Copy-paste text for Methods sections and preregistrations, shown inline below the parameters (auto-refreshes on every Calculate)
- 🇷 **R code export** — Per-test method description (plain-language + formula) plus copy-pasteable R code that reproduces the exact same number, using the `pwr` package where available and base-R noncentral distribution functions otherwise — shown inline below the parameters, alongside the report
- 🧮 **Effect Size Calculator** — its own tab with ~11 conversion recipes across mean differences (d/g/dz/Glass's Δ), correlations, variance-explained (η²/ω²/f/f²/R²), proportions/categorical (h/OR/RR/w/Cramér's V/φ), and odds ratios; every conversion shows its formula, applicable warnings, and the literature/R packages it's based on, plus a one-click "Send" into the main calculator's matching input when relevant
- 📋 **Protocol tab** — Automatic log of all analyses, exportable as CSV
- 📈 **X-Y plot** — Power curves across ranges of effect size, N, α, or power, with hover readout and PNG/CSV export
- ⓘ **Parameter tooltips** — Effect-size conventions and empirical benchmarks from Cohen (1988), Gignac & Szodorai (2016), and others
- 🎨 **5 themes** — G\*Power Classic, Flat & Teal (2010s), Polished Minimal, Terminal/Hacker, Aged Paper/Sepia
- 📱 **Mobile-first** — Fully responsive layout for phones and tablets
- 🔍 **Screen-size preview** — Pick Desktop/Tablet/Mobile/Custom from the menu bar to check the responsive layout at a given width without resizing your actual browser window
- 💾 **PWA-ready** — Installable as a home-screen app (Add to Home Screen)

---

## 📱 Mobile Use

C*Power is designed to work well on mobile:

- Responsive layout (params, tabs, and the Effect Size Calculator's two-column layout all collapse to a single column on narrow screens)
- The in-app "Screen size" selector (top menu bar) lets you preview Mobile/Tablet widths from a desktop browser before testing on an actual device
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
index.html      # Everything — HTML, CSS, and JavaScript in one file
README.md       # This file
```

### Running locally

No build step required. Just open `index.html` in a browser.

For development with live reload:
```bash
npx live-server --open=index.html
```

### Deployment (GitHub Pages)

The live site is served from the repository root via GitHub Pages, so the app file **must be named `index.html`** at the repo root (not `cpower.html`). Pushing to the default branch redeploys automatically within ~1 minute; GitHub Pages caches for up to 10 minutes (`Cache-Control: max-age=600`), so hard-refresh (or wait) after deploying if you don't see changes immediately.

```bash
git add index.html README.md
git commit -m "Add correlation tests, R code export, method descriptions"
git push origin main
```

---

## 📐 Statistical Methods

C*Power uses the following methods:

| Distribution | Method |
|-------------|--------|
| Normal | Abramowitz & Stegun (1964) rational approximation for CDF; Beasley-Springer-Moro for inverse |
| t (central) | Regularized incomplete beta with Pike-Hill symmetry |
| F (central) | Regularized incomplete beta with Pike-Hill symmetry |
| χ² (central) | Regularized incomplete gamma (series + continued fraction) |
| Noncentral F | Exact Poisson-weighted mixture: P(F'≤f) = Σⱼ Pois(j; λ/2)·I_y(d₁/2+j, d₂/2) where y = d₁f/(d₁f+d₂) |
| Noncentral t | NC-F transformation for two-tailed; normal approximation for df ≥ 30 |
| Noncentral χ² | Exact Poisson-weighted mixture of central χ² distributions |
| Sample-size search | Stepwise integer search starting from minimum valid N (df ≥ 1) |
| Sensitivity / criterion | Bisection on bracketed monotone power function |

### Validation

The following test cases have been validated against G*Power 3.1 and/or R (`pwr`, `cocor`):

| Test | Inputs | Expected | C*Power |
|------|--------|-----------|-----------|
| ANOVA | k=4, f=0.25, α=0.05, 1−β=0.95 | N=280 | N=279 |
| ANOVA | k=3, f=0.40, α=0.05, 1−β=0.80 | N=66  | N=64  |
| Multiple regression (R²) | u=3, f²=0.15, α=0.05, 1−β=0.95 | N=119 | N=119 |
| t two-sample | d=0.50, α=0.05, 1−β=0.80 | N=128 | N=128 |
| t paired | dz=0.50, α=0.05, 1−β=0.80 | N=34  | N=34  |
| Correlation (one sample) | r=0.30, α=0.05, 1−β=0.95 | N=137.76 (`pwr.r.test`) | N=138 |
| Correlation (two independent) | r₁=0.5, r₂=0.2, n₁=n₂=100 | z=2.4136 (`cocor::fisher1925`) | z=2.4136 |
| Correlation (two dependent/overlapping) | r_jk=0.5, r_jh=0.3, r_kh=0.4, n=100 | z=2.0349 (`cocor::steiger1980`) | z=2.0349 |

Differences of ±2 in required N are from rounding (G*Power/pwr report a real number; C*Power rounds up to the next integer). The correlation tests were validated by installing R packages `pwr` and `cocor` and comparing test statistics directly — see `/tests/validate_correlations.R` if included, or the R code export feature within the app itself.

### Known issues

- Sensitivity/criterion analyses for tests without a closed-form solution use bisection with a fixed iteration count (60) — should converge to machine precision, but hasn't been stress-tested at extreme parameter values (e.g. α → 0, N → 2).
- Several Effect Size Calculator conversions (ω² from η², d↔OR via the logit method, d→f for more than two groups) are documented approximations rather than exact identities — see the warning shown with each conversion.

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

This project is not affiliated with the G*Power team at Heinrich Heine University Düsseldorf.

---

## 🙏 Acknowledgements

- **Franz Faul, Edgar Erdfelder, Albert-Georg Lang, Axel Buchner** — creators of G*Power
- **Anthropic / Claude** — LLM used to generate this tool
- Cohen, J. (1988). *Statistical Power Analysis for the Behavioral Sciences* (2nd ed.) — foundational reference for effect size conventions
