# Titanium Shop — website

Bilingual (English + Arabic) static website for **Titanium Shop**, Amman — *Unlimited Luxury*.

- English pages: repository root (`index.html`, `cars.html`, …)
- Arabic pages: `/ar/` (same file names, right-to-left)
- No server, no database, no secret keys. The request form is delivered by email through [FormSubmit](https://formsubmit.co).

## Structure

```
index.html … 404.html      English pages (generated)
ar/                        Arabic pages (generated)
assets/css/style.css       Design system (black & titanium silver)
assets/js/main.js          Menu, scroll reveal, fleet filter, request form
assets/img/                Responsive WebP photos (generated) + manifest.json
assets/brand/              Logo, emblem, wordmark, favicons, social image
tools/content.py           ALL text, phone numbers, prices, fleet — edit here
tools/build.py             Generates every page from content.py
tools/optimize_images.py   Converts source photos into WebP sizes
netlify.toml               Security headers, caching, 404s (Netlify)
```

## Editing content

1. Change text, a price or a phone number in `tools/content.py`.
2. Run `python3 tools/build.py`.
3. Commit and push the regenerated `.html` files.

**Prices:** each service uses `PRICE_ON_REQUEST` until a real price is added, e.g.
`"price": L("يبدأ من 150 دينار يومياً", "From 150 JOD per day")` inside that service.

**Adding a car:** add the photo to the source-images folder, run
`python3 tools/optimize_images.py <source-images-folder>`, then add a line to `FLEET` in `content.py` and rebuild.

## Request form (FormSubmit)

- Submissions go to `titaniumshopjo@gmail.com` (`FORM_ACTION` in `content.py`).
- **First submission only:** FormSubmit emails a confirmation link to that inbox. Click it once, or no requests will arrive.
- After confirming, FormSubmit can give a random alias for the address; replace the email in `FORM_ACTION` with it to hide the address from bots.
- Spam protection: FormSubmit reCAPTCHA (on by default) + a hidden honeypot field.
- Check the Spam folder for the first few emails and mark them "Not spam".

## Hosting

- **During development:** GitHub Pages from `main` (`/` root).
- **Launch on Netlify:** Project configuration → Developer settings → Continuous deployment → Build settings → *Active builds*. No build command is needed (`publish = "."`). Security headers in `netlify.toml` only apply on Netlify.
- **At launch:** `SITE_URL` in `content.py` currently points to GitHub Pages (so link previews work now). Change it to the Netlify URL or the domain, update the sitemap line in `robots.txt`, rebuild.
- **Domain:** when bought, update `SITE_URL` in `content.py` and the sitemap line in `robots.txt`, rebuild, and add the domain in Netlify (Domain management).

## Still needed from the client

- Real prices per service (currently "A quote within 5 minutes").
- Company story and figures (clients served, years, countries) if they want them shown.
- Logo source file (AI/SVG/PDF) for print use.
- Domain name.
