"""Generate simple 'Featured' thumbnails for the portfolio link."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1200, 630
FONTS = "C:/Windows/Fonts/"
def font(n, s): return ImageFont.truetype(FONTS + n, s)

def grad_bg(c1, c2):
    base = Image.new("RGB", (W, H), c1)
    top = Image.new("RGB", (W, H), c2)
    mask = Image.new("L", (W, H))
    md = mask.load()
    for y in range(H):
        v = int(255 * (y / H))
        for x in range(W):
            md[x, y] = v
    return Image.composite(top, base, mask)

def blob(img, cx, cy, r, color, a=0.5):
    layer = Image.new("RGB", (W, H), (0,0,0))
    ImageDraw.Draw(layer).ellipse([cx-r,cy-r,cx+r,cy+r], fill=color)
    layer = layer.filter(ImageFilter.GaussianBlur(150))
    return Image.blend(img, layer, a)

def center_text(d, y, text, fnt, fill):
    w = d.textlength(text, font=fnt)
    d.text(((W-w)//2, y), text, font=fnt, fill=fill)
    return w

# ---------- Variant A: minimal centered ----------
def variant_a():
    img = grad_bg((8, 12, 24), (12, 20, 40))
    img = blob(img, 300, 120, 280, (46, 81, 201), 0.45)
    img = blob(img, 950, 560, 280, (34, 120, 160), 0.40)
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([18,18,W-18,H-18], radius=30, outline=(255,255,255), width=2)

    center_text(d, 150, "A J A Y   K U M A R   C H A U H A N", font("segoeui.ttf", 30), (147,161,189))
    center_text(d, 215, "Portfolio", font("segoeuib.ttf", 130), (234,240,251))
    center_text(d, 380, "Backend Software Engineer", font("segoeui.ttf", 40), (109,170,240))

    # URL pill
    url = "ajaykchauhan73.github.io"
    fu = font("segoeuib.ttf", 30)
    uw = d.textlength(url, font=fu)
    pw = uw + 70
    px = (W - pw)//2
    d.rounded_rectangle([px, 480, px+pw, 548], radius=34, fill=(34,211,238))
    d.text((px+35, 494), url, font=fu, fill=(6,12,22))
    img.save("feature-a.png")

# ---------- Variant B: left-aligned modern ----------
def variant_b():
    img = grad_bg((10, 14, 26), (16, 22, 44))
    img = blob(img, 1050, 120, 320, (126, 34, 206), 0.40)
    img = blob(img, 120, 540, 300, (46, 81, 201), 0.42)
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([18,18,W-18,H-18], radius=30, outline=(255,255,255), width=2)

    x = 90
    # accent bar
    d.rounded_rectangle([x, 175, x+8, 430], radius=4, fill=(34,211,238))
    xx = x + 40
    d.text((xx, 150), "PORTFOLIO", font=font("segoeuib.ttf", 34), fill=(34,211,238))
    d.text((xx, 210), "Ajay Kumar", font=font("segoeuib.ttf", 92), fill=(234,240,251))
    d.text((xx, 305), "Chauhan", font=font("segoeuib.ttf", 92), fill=(109,170,240))
    d.text((xx, 420), "Backend Software Engineer  -  Java | Spring Boot", font=font("segoeui.ttf", 34), fill=(147,161,189))

    # url with arrow
    d.text((xx, 500), "ajaykchauhan73.github.io", font=font("segoeuib.ttf", 36), fill=(255,255,255))
    aw = d.textlength("ajaykchauhan73.github.io", font=font("segoeuib.ttf", 36))
    d.text((xx+aw+20, 498), "->", font=font("segoeuib.ttf", 40), fill=(34,211,238))
    img.save("feature-b.png")

variant_a()
variant_b()
print("Saved feature-a.png and feature-b.png")
