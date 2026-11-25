"""Convert source photos into responsive WebP files for the website.

Usage:
    python3 tools/optimize_images.py /path/to/source-images

Every .png/.jpg in the source folder becomes assets/img/<name>-<width>.webp
in several widths, and assets/img/manifest.json records the sizes so the
page builder can write correct srcset/width/height attributes.
Source originals are NOT committed (they are large); keep them safe elsewhere.
"""
import json
import sys
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "img"
WIDTHS = (480, 960, 1600)
QUALITY = 80


def widths_for(src_w):
    ws = [w for w in WIDTHS if w < src_w]
    ws.append(min(src_w, WIDTHS[-1]))
    return sorted(set(ws))


def main(src_dir):
    OUT.mkdir(parents=True, exist_ok=True)
    manifest = {}
    for path in sorted(Path(src_dir).iterdir()):
        if path.suffix.lower() not in {".png", ".jpg", ".jpeg"}:
            continue
        name = path.stem
        im = ImageOps.exif_transpose(Image.open(path)).convert("RGB")
        sizes = []
        for w in widths_for(im.width):
            h = round(im.height * w / im.width)
            im.resize((w, h), Image.LANCZOS).save(
                OUT / f"{name}-{w}.webp", "WEBP", quality=QUALITY, method=6
            )
            sizes.append([w, h])
        manifest[name] = sizes
        print(f"{name}: {sizes}")
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=1))


if __name__ == "__main__":
    main(sys.argv[1])
