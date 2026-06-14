# Personal Portfolio

A sleek, responsive personal portfolio website with a floating water dark/light theme, built using static HTML templates and Python for compilation.

## Features

- **Dynamic Theme:** Responsive dark and light theme designed around a modern floating water aesthetic.
- **Glassmorphism Design:** Beautiful, premium UI cards with smooth hover micro-animations.
- **Fully Responsive:** Mobile-first layout styling optimized for all device sizes.
- **SEO & Accessibility:** Implemented Semantic HTML, skip links, unique IDs, and proper meta descriptions.

## Structure

- `Task-1/` - The project source directory.
  - `templates/partials/` - Reusable layout components (`header.html` and `footer.html`).
  - `templates/pages/` - Core page templates containing placeholders (`{{HEADER}}`, `{{FOOTER}}`).
  - `build.py` - A Python build script to compile the pages.
  - `styles.css` - Custom styling for the site.
  - `avatar.png` - Profile image.
- `netlify.toml` - Netlify deployment configuration.
- `.github/workflows/deploy.yml` - GitHub Actions workflow for automatic deployment to GitHub Pages.

## How to Build Locally

To compile the page templates and output the final HTML files:

1. Ensure you have Python 3 installed.
2. Run the build script from the root directory:
   ```bash
   python Task-1/build.py
   ```
3. The generated HTML pages (`index.html`, `about.html`, etc.) will be written to the `Task-1/` folder.

## Deployment

### Netlify (Configured)

This project contains a `netlify.toml` file. When connected to Netlify, it automatically runs:
- **Build Command:** `python Task-1/build.py`
- **Publish Directory:** `Task-1`

### GitHub Pages

A GitHub Actions workflow is set up in `.github/workflows/deploy.yml` that automatically builds and deploys the portfolio to the `gh-pages` branch on every push to the `main` branch.
