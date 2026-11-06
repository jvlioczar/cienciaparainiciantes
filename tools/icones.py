"""Gera os PNG do site (ícones e imagem de compartilhamento) com Pillow. Uso: python tools/icones.py. Não faz parte do build."""
import math, os
from PIL import Image, ImageDraw, ImageFont
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = os.path.join(ROOT, 'assets')
NOITE = (75, 42, 130)
def grad(w, h, c1, c2):
    im = Image.new('RGB', (w, h)); d = ImageDraw.Draw(im)
    for i in range(w):
        t = i / max(1, w - 1); d.line([(i, 0), (i, h)], fill=tuple(round(c1[k] + (c2[k] - c1[k]) * t) for k in range(3)))
    return im
def orbita(im, cx, cy, rx, ry, rot, w, c1, c2, s=4):
    """Elipse vazada com gradiente, girada, desenhada em alta resolução e reduzida."""
    W, H = im.size
    m = Image.new('L', (W * s, H * s), 0); d = ImageDraw.Draw(m)
    pts_out, pts_in = [], []
    for k in range(360):
        a = math.radians(k); r = math.radians(rot)
        for (ex, ey, lst) in ((rx, ry, pts_out), (rx - w, ry - w, pts_in)):
            x, y = ex * math.cos(a), ey * math.sin(a)
            lst.append(((cx + x * math.cos(r) - y * math.sin(r)) * s, (cy + x * math.sin(r) + y * math.cos(r)) * s))
    d.polygon(pts_out, fill=255); d.polygon(pts_in, fill=0)
    m = m.resize((W, H), Image.LANCZOS)
    im.paste(grad(W, H, c1, c2), (0, 0), m)
def ponto(im, cx, cy, r, c1, c2, s=4):
    W, H = im.size
    m = Image.new('L', (W * s, H * s), 0); ImageDraw.Draw(m).ellipse([(cx - r) * s, (cy - r) * s, (cx + r) * s, (cy + r) * s], fill=255)
    im.paste(grad(W, H, c1, c2), (0, 0), m.resize((W, H), Image.LANCZOS))
def logo(im, cx, cy, R):
    w = R * .13
    orbita(im, cx, cy, R, R * .38, 0, w, (142, 197, 240), (90, 72, 208))
    orbita(im, cx, cy, R, R * .38, 60, w, (201, 182, 255), (123, 82, 224))
    orbita(im, cx, cy, R, R * .38, -60, w, (243, 165, 200), (177, 79, 201))
    ponto(im, cx, cy, R * .22, (243, 165, 200), (177, 79, 201))
def icone(n):
    im = Image.new('RGB', (n, n), NOITE); logo(im, n / 2, n / 2, n * .42); return im
for n in (180, 192, 512): icone(n).save(os.path.join(A, f'icon-{n}.png'), optimize=True)
im = Image.new('RGB', (1200, 630), NOITE); d = ImageDraw.Draw(im)
logo(im, 960, 315, 200)
def fonte(nomes, tam):
    for n in nomes:
        p = os.path.join('C:/Windows/Fonts', n)
        if os.path.exists(p): return ImageFont.truetype(p, tam)
    return ImageFont.load_default()
f1 = fonte(['georgiab.ttf', 'georgia.ttf', 'times.ttf'], 86); f2 = fonte(['segoeui.ttf', 'arial.ttf'], 32); f3 = fonte(['segoeuib.ttf', 'arialbd.ttf'], 24)
d.text((80, 170), 'Ciência', font=f1, fill=(255, 255, 255)); d.text((80, 270), 'Para Iniciantes', font=f1, fill=(255, 255, 255))
d.text((80, 400), 'Método, evidência, epistemologia e pseudociência,', font=f2, fill=(220, 207, 242)); d.text((80, 442), 'do básico ao avançado, com fontes.', font=f2, fill=(220, 207, 242))
d.text((80, 540), 'cienciaparainiciantes.biblioverse.org  ·  BiblioVerse', font=f3, fill=(201, 182, 255))
im.save(os.path.join(A, 'share.png'), optimize=True)
print('ok')
