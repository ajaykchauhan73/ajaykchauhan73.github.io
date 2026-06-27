"""Generate a 1200x630 Open Graph link-preview card for the portfolio."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math

W, H = 1200, 630
FONTS = "C:/Windows/Fonts/"

def font(name, size):
    return ImageFont.truetype(FONTS + name, size)

f_name   = font("segoeuib.ttf", 78)   # bold name
f_role   = font("segoeui.ttf", 36)
f_sub    = font("segoeui.ttf", 26)
f_chip   = font("segoeuib.ttf", 22)
f_url    = font("segoeui.ttf", 24)

# ---- base dark background ----
img = Image.new("RGB", (W, H), (6, 9, 18))

# ---- soft gradient blobs (mesh) ----
def blob(cx, cy, r, color):
    layer = Image.new("RGB", (W, H), (6, 9, 18))
    d = ImageDraw.Draw(layer)
    d.ellipse([cx-r, cy-r, cx+r, cy+r], fill=color)
    layer = layer.filter(ImageFilter.GaussianBlur(140))
    return layer

for cx, cy, r, col in [(120, 80, 320, (46, 81, 201)),
                       (1120, 120, 300, (14, 116, 144)),
                       (560, 640, 320, (126, 34, 206))]:
    b = blob(cx, cy, r, col)
    img = Image.blend(img, b, 0.55)

draw = ImageDraw.Draw(img)

# ---- subtle border frame ----
draw.rounded_rectangle([16, 16, W-16, H-16], radius=28, outline=(255, 255, 255), width=2)

# ---- circular photo with gradient ring (right side) ----
PHOTO = "ajay.jpg"
ring_d = 300
cx, cy = 940, H//2          # ring center
try:
    photo = Image.open(PHOTO).convert("RGB")
    # center-crop to square
    s = min(photo.size)
    l = (photo.width - s)//2
    t = (photo.height - s)//2
    photo = photo.crop((l, t, l+s, t+s)).resize((ring_d, ring_d), Image.LANCZOS)

    # gradient ring
    ring = Image.new("RGB", (ring_d+28, ring_d+28), (6, 9, 18))
    rd = ImageDraw.Draw(ring)
    cols = [(109,140,255), (34,211,238), (192,132,252)]
    for i in range(360):
        t_ = i/360
        if t_ < 0.5:
            a, b_, k = cols[0], cols[1], t_/0.5
        else:
            a, b_, k = cols[1], cols[2], (t_-0.5)/0.5
        c = tuple(int(a[j] + (b_[j]-a[j])*k) for j in range(3))
        rd.pieslice([0, 0, ring_d+27, ring_d+27], i, i+2, fill=c)
    rmask = Image.new("L", ring.size, 0)
    ImageDraw.Draw(rmask).ellipse([0, 0, ring_d+27, ring_d+27], fill=255)
    img.paste(ring, (cx-(ring_d+28)//2, cy-(ring_d+28)//2), rmask)

    # photo mask
    pmask = Image.new("L", (ring_d, ring_d), 0)
    ImageDraw.Draw(pmask).ellipse([0, 0, ring_d, ring_d], fill=255)
    img.paste(photo, (cx-ring_d//2, cy-ring_d//2), pmask)
except FileNotFoundError:
    pass

# ---- left text block ----
x = 80
# status badge
badge_y = 120
draw.ellipse([x, badge_y+6, x+14, badge_y+20], fill=(52, 211, 153))
draw.text((x+26, badge_y), "Open to opportunities", font=f_sub, fill=(147, 161, 189))

# name (two lines)
draw.text((x, 175), "Ajay Kumar", font=f_name, fill=(234, 240, 251))
# gradient-ish surname (approximate with accent color)
draw.text((x, 262), "Chauhan", font=f_name, fill=(109, 170, 240))

# role
draw.text((x, 372), "Backend Software Engineer", font=f_role, fill=(234, 240, 251))

# skill chips
chips = ["Java", "Spring Boot", "Microservices", "AWS"]
cy2 = 440
cxp = x
for c in chips:
    tw = draw.textlength(c, font=f_chip)
    pad = 18
    draw.rounded_rectangle([cxp, cy2, cxp+tw+pad*2, cy2+44], radius=12,
                           fill=(20, 28, 48), outline=(60, 80, 130), width=1)
    draw.text((cxp+pad, cy2+9), c, font=f_chip, fill=(179, 198, 255))
    cxp += tw + pad*2 + 14

# url at bottom
draw.text((x, 520), "ajaykchauhan73.github.io", font=f_url, fill=(34, 211, 238))

img.save("og-image.png", "PNG")
img.convert("RGB").save("og-image.jpg", "JPEG", quality=88)
print("Saved og-image.png and og-image.jpg")
