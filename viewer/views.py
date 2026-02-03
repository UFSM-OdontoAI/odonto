from django.conf import settings
from django.shortcuts import render
from .services.coco import CocoDataset

DATASETS = {
 split: CocoDataset(cfg['annotations'])
 for split, cfg in settings.COCO_DATASETS.items()
}

def home(request):
 return render(request,'viewer/home.html')

def image_list(request, split):
 coco = DATASETS[split]
 return render(request,'viewer/image_list.html',{
  'split': split,
  'images': coco.images.values()
 })

def image_detail(request, split, image_id):
 coco = DATASETS[split]
 image = coco.images[image_id]
 anns = coco.annotations_by_image.get(image_id, [])
 out = []
 for a in anns:
  out.append({
   'bbox': a['bbox'],
   'segmentation': a.get('segmentation', []),
   'category': coco.categories[a['category_id']]['name'],
   'category_id': a['category_id']
  })
 return render(request,'viewer/image_detail.html',{
  'split': split,
  'image': image,
  'annotations': out
 })
