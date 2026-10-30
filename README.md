# Kristina Gaytandzhieva — portfolio

A plain static website. It has no build step and no dependencies.

## Put it online with Vercel (free, no domain needed)

**Option A: GitHub (recommended, no terminal needed)**
1. Create a free account at github.com, make a new repository, and upload the contents of this folder (index.html must be at the top level). Use "Add file → Upload files" and drag everything in.
2. Sign up at vercel.com with your GitHub account (Hobby plan, free).
3. Click Add New → Project, then import the repo.
   - Framework preset: **Other**.
   - Leave the build settings empty.
   - Click Deploy.
4. Your site is live at `https://<project-name>.vercel.app`. Rename the project in Settings to change that name. After this, every file you change on GitHub redeploys automatically.

**Option B: from a terminal**
Run `npx vercel` in this folder and accept the defaults. Then run `npx vercel --prod` to publish.

## Links
- The CV button downloads `assets/Kristina_Gaytandzhieva_CV_2026.pdf`. To update the CV, replace that file and keep the same name.
- LinkedIn points to linkedin.com/in/kristina-gaitanova.

## Structure
- `index.html`: homepage
- `grow-by-mia.html`, `katalysta.html`, `vitesse-running.html`, `geegee.html`, `ahoy-connect.html`: marketing case studies
- `learnify.html`, `drops-of-emotions.html`, `mymultisport.html`: UX case studies
- `prototypes/`: clickable prototypes (Learnify mobile and desktop, Drops of Emotions)
- `assets/`: images
- `vercel.json`: clean URLs, so `/geegee` works without `.html`
