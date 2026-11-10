# Kristina Gaytandzhieva — portfolio: project notes

Read this first in any new session. It is the handover between chats.

## What this is
Kristina's personal portfolio: a senior growth marketer with hands-on UX training. Hero line: "Growth marketing with a designer's touch." Plain static HTML: no build step, no dependencies, no framework. Since Nov 2026 the hero reads "Growth marketing with a designer's touch, built with AI." with a "New · AI-built work" link to `#ai`.

- Repo: `kristinastivanova-sudo/portfolio`. Hosted on **Vercel** (Hobby, free), connected to this repo: every push to `main` redeploys automatically in under a minute. Kristina decided to keep it on Vercel (moving to Cloudflare is possible later if it becomes commercial or she wants one dashboard with the shop).
- `vercel.json` sets clean URLs: `/geegee` serves `geegee.html`.
- Origin: designed in a Claude Design canvas ("Portfolio Redesign"), then exported to these static pages. **The HTML in this repo is now the source of truth.** The export tool is not kept; edits made here do not flow back to the canvas.

## Structure
- `index.html`: homepage. Sections by id: `#top` (hero; the portrait is hidden on mobile), `#work` (marketing case-study cards), `#services`, `#design` (UX case-study cards), `#ai` ("AI-built" showcase near the bottom: Homefans and Drops of Emotions side by side, sand background; these two also keep their normal cards in `#work` and `#design`, each with a purple "Built with Claude" chip). Footer has the CV download and LinkedIn.
- Navigation: desktop "Work" dropdown (`.nav-dd-menu`) with Marketing → `index.html#work`, AI-built → `index.html#ai` and Design → `index.html#design`; on mobile a `<details class="nav-mobile">` burger menu with the same links as sub-items. Keep both in sync when adding nav items.
- Marketing case studies: `homefans.html` (current role, first card, also in `#ai`), `grow-by-mia.html`, `katalysta.html`, `vitesse-running.html`, `geegee.html`, `ahoy-connect.html`.
- UX case studies: `learnify.html`, `drops-of-emotions.html` (also in `#ai`), `mymultisport.html`.
- Table of contents: the long case studies (`homefans`, `learnify`, `drops-of-emotions`, `mymultisport`) have a sticky "On this page" pill bar (`<nav class="toc">`) right after the hero. It sticks under the header (top 81px desktop, 83px mobile), has 48px space below it, scrolls sideways on mobile, and a small script highlights the current section. Each linked `<section>` has an `id`. When adding or renaming a section on these pages, update the bar's links too. Other case studies are short enough without one.
- `prototypes/`: clickable prototypes linked from the UX case studies (`learnify/`, `learnify-desktop/`, `drops/`).
- `assets/`: images (webp/jpg/png, already compressed) and `Kristina_Gaytandzhieva_CV_2026.pdf`. To update the CV, replace the PDF and keep the file name.
- `404.html`, `favicon.svg`.
- Styles are inline on each page (a `<style>` block plus inline `style=""` attributes from the export). There is no shared stylesheet, so a global style change means editing every page.

## The "next project" chain
Each case study ends with a link to the next one, forming a loop:
homefans → grow-by-mia → katalysta → vitesse-running → geegee → ahoy-connect → learnify → drops-of-emotions → mymultisport → homefans.

## Adding a case study
1. Copy the closest existing page (marketing or UX) to `new-name.html`; replace title, meta description, hero, sections, images and results. Put images in `assets/` (compress: max ~1600px wide, webp or jpg).
2. Add a card on `index.html`: copy an existing `<a class="card" href="...">` in `#work` (marketing) or `#design` (UX) and change link, image, tags and text.
3. Splice it into the next-project chain: the page before it links to it, and it links to the page that came next.

## Removing a case study
1. Delete its card from `index.html`.
2. Fix the chain: the page that linked to it now links to the one after it.
3. Delete the HTML file (and its images/prototype folder if nothing else uses them). Check with `grep -rn "old-name" .` that no link is left.

## Design
Fonts: **Schibsted Grotesk** (headings, weights 500–800; replaced Bricolage Grotesque in Nov 2026 because it was too distracting) + **Figtree** (text), from Google Fonts. Colors: ink `#040005`, text grey `#5C5762`, background `#FFFDFA`, sand `#F5EFE6`, line `#E9E2D6`, yellow accent `#FFC94C`, deep purple `#300045`.

## Facts that appear on the site
- Homefans (since Aug 2026): leads the social media and PPC teams; owns Meta Ads and email (Klaviyo); works with host onboarding (supply), sales and devs; runs the team on monday.com; Claude connected to Meta Ads and Klaviyo; built a design system, landing pages and the blog in Claude Design. The page shows her club landing page design (Boca Juniors, `assets/homefans-club-page.jpg`, from her Claude Design file): built for Google Ads ticket-search traffic, experiences grouped by home fixture, reuses backend data so it can be generated in bulk for popular clubs, green trust bar based on her OTA research. Next (in progress): destination/city pages for Meta with fixtures and things to do. Waiting on more landing page screenshots. Numbers on the page come from Homefans' booking export, Sep–Oct 2026 vs Sep–Oct 2025, cancelled/refunded excluded: revenue +34%, bookings +15%, AOV +17%, coupon share 44% → 16%, cities with bookings 28 → 51, Rio share 50% → 34%. Brand search 9× return is one week (2–8 Nov 2026). Shown as percentages only, never euro totals.
- Drops of Emotions: v1 and v2 designed in Figma, then redesigned in Claude Design and built by Kristina with Claude on Cloudflare (replaced Shopify): custom checkout with Stripe Checkout, Speedy courier API, custom admin. Live at https://dropsofemotions.bg (linked from the case study hero and the "Version 3 · live" section). Waiting on a screenshot of the live site.
- 10+ years in marketing; engagements: Grow by Mia 18 months, Katalysta 12 months, Vitesse Running 12 months, GeeGee 5 months; social content for AhoyConnect.
- LinkedIn: linkedin.com/in/kristina-gaitanova. CV: `assets/Kristina_Gaytandzhieva_CV_2026.pdf`.

## How to work on it
1. `git clone`, then serve locally: `python3 -m http.server 8080` in the repo folder (open `/index.html`; clean URLs only work on Vercel).
2. Check every changed page with Playwright at 1440 and 390 wide: no sideways scroll (`document.documentElement.scrollWidth` equals the viewport), images load, mobile menu opens.
3. Check links: `grep -o 'href="[^"#]*\.html"' *.html` and make sure every target exists.
4. Commit and push to `main`; Vercel deploys. Tell Kristina what changed.
