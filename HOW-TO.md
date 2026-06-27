# Portfolio — How To Update

Your portfolio is a single self-contained website. This file explains how to update it yourself.

- **Live site:** https://ajaykchauhan73.github.io
- **GitHub repo:** https://github.com/ajaykchauhan73/ajaykchauhan73.github.io
- **Local folder:** `C:\Claude\ajaykchauhan73.github.io\`
- **Main files:**
  - `index.html` — the entire website (text, design, everything)
  - `ajay.jpg` — your profile photo (used in the hero)
  - `og-image.jpg` — the link-preview share card (shown when you share your link)
  - `make_og.py` — script that regenerates the share card

> After any change, the live site updates automatically in about **1 minute**.
> Then hard-refresh your browser with **Ctrl + Shift + R** to see it (clears the cache).

---

## 1. Change your profile photo

The website always loads a file named **`ajay.jpg`**. To change your picture, just replace that file.

1. Rename your new photo to **`ajay.jpg`** (the name must match exactly).
2. Copy it into `C:\Claude\ajaykchauhan73.github.io\`, replacing the old one.
3. Open **PowerShell** and run:
   ```powershell
   cd C:\Claude\ajaykchauhan73.github.io
   git add ajay.jpg
   git commit -m "Update profile photo"
   git push
   ```
4. Wait ~1 minute, then hard-refresh the site (Ctrl + Shift + R).

**Tip:** A square-ish photo looks best (it's cropped into a circle). Keep it under ~1 MB if possible.

---

## 1b. Update the link-preview share card

The **share card** (`og-image.jpg`) is the thumbnail people see when you paste your
portfolio link on LinkedIn, WhatsApp, Slack, etc. It shows your name, title, photo,
and skills on a branded background.

It is generated automatically by `make_og.py` (it uses your current `ajay.jpg`).
**Regenerate it whenever you change your photo, title, or name:**

1. Make sure `ajay.jpg` is up to date (see section 1).
2. Run the generator and publish:
   ```powershell
   cd C:\Claude\ajaykchauhan73.github.io
   python make_og.py
   git add -A
   git commit -m "Update share card"
   git push
   ```

**First-time setup only** (if `python make_og.py` errors with "No module named PIL"):
```powershell
python -m pip install Pillow
```

### Make social sites show the NEW card
Social platforms cache link previews. After updating, force a refresh:
- **LinkedIn:** https://www.linkedin.com/post-inspector/ -> paste your URL -> Inspect
- **Facebook / WhatsApp:** https://developers.facebook.com/tools/debug/ -> paste URL -> Scrape Again

To tweak the text/skills on the card, edit `make_og.py` (the chips, name, and role
are near the bottom), then re-run the steps above.

---

## 2. Publish ANY change (photo, text, design)

Whenever you edit `index.html` or swap the photo, publish with these commands:

```powershell
cd C:\Claude\ajaykchauhan73.github.io
git add -A
git commit -m "Describe what you changed"
git push
```

That's it — the live site rebuilds automatically.

---

## 3. Change text content (name, summary, experience, skills…)

All the words on the site live inside `index.html`.

1. Open `C:\Claude\ajaykchauhan73.github.io\index.html` in any text editor (Notepad, VS Code, etc.).
2. Use **Ctrl + F** to find the text you want to change, edit it, and save.
3. Publish using the commands in section 2.

> Not comfortable editing HTML? Just ask Claude — give it the new resume or the change, and it will do it for you.

---

## 4. Easiest option — ask Claude

For any update (new photo, new resume, design tweak, new project), simply tell Claude:
- *"Change my portfolio photo to [filename]"*
- *"Update my portfolio from this new resume: [path]"*
- *"Add a new project / change the colors / etc."*

Claude will edit, commit, and push it for you.

---

## 5. Good to know

- **No certificate errors:** the site uses GitHub's `*.github.io` domain, which has a free, valid, auto-renewing SSL certificate. HTTPS is enforced.
- **One filename rule:** the photo must stay named `ajay.jpg`, or update the reference inside `index.html` (`<img src="ajay.jpg">` and the `og:image` meta tag).
- **Resume:** the site is a JD-agnostic "master" profile. Update it whenever a new resume version adds something. Latest source used: `C:\Users\DELL\Documents\Ajay-Resume.pdf`.
- **Backup copy:** a duplicate of `index.html` also lives at `C:\Claude\index.html` (not required for the live site, just a local copy).

---

## Quick command reference

```powershell
# Go to the project
cd C:\Claude\ajaykchauhan73.github.io

# See what changed
git status

# Publish changes
git add -A
git commit -m "your message"
git push
```
