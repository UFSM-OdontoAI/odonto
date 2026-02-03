from django.http import FileResponse, Http404
from django.conf import settings
from pathlib import Path

def serve_image(request, split, filename):
    img_dir = settings.COCO_DATASETS[split]['images']
    path = Path(img_dir) / filename
    if not path.exists():
        raise Http404
    return FileResponse(open(path, 'rb'), content_type='image/jpeg')
